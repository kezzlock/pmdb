import re

from django.db.models import CharField, ForeignKey, Q, TextField
from django.utils import timezone
from django.utils.html import escape
from django_datatables_view.base_datatable_view import BaseDatatableView
from rest_framework import generics

from projects.models import Project
from projects.serializers import ProjectDetailSerializer, ProjectSerializer


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    """Split query string.

    Splits the query string in invidual keywords, getting rid of unecessary
    spaces and grouping quoted words together.

    Example:

        >>> normalize_query('some random  words "with   quotes  " and  spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    """
    return [normspace(' ', (t[0] or t[1]).strip())
            for t in findterms(query_string)]


class ProjectListJson(BaseDatatableView):
    model = Project
    columns = ['id', 'name', 'molecule', 'manager', 'pharmaceutical_form',
               'product_category', 'strength', 'market', 'moq']
    # 'description', 'project_type', 'manager', 'contract_type',
    # 'status', 'therapeutic_area',
    # 'priority', 'atc_class', 'pack_size', 'pact_type', 'shelf_life',]
    order_columns = ['', 'name', 'molecule.name', 'manager.username',
                     'pharmaceutical_form', 'product_category.type',
                     'strength', 'market.name', 'moq']

    def get_initial_queryset(self):
        # return all objects ordered reversed
        return self.model.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = self.get_columns()
        return context

    def render_column(self, row, column):
        """Render a column on a row.

        Column can be given in a module notation eg. document.invoice.type
        """
        # try to find rightmost object
        obj = row
        parts = column.split('.')
        for part in parts[:-1]:
            if obj is None:
                break
            obj = getattr(obj, part)

        # try using get_OBJECT_display for choice fields
        if hasattr(obj, 'get_%s_display' % parts[-1]):
            value = getattr(obj, 'get_%s_display' % parts[-1])()
        else:
            value = getattr(obj, parts[-1], None)

        if value is None:
            value = self.none_string

        if self.escape_values:
            value = escape(value)

        # return link to absolute url
        if value and column == 'name':
            # return '<a href="%s" class="table__name-link">%s</a>' % (obj.get_absolute_url(), value)
            return f'<a href="#" class="table__name-link" onclick="showDetails({obj.pk})">{value}</a>'
        return value

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset
        try:
            search = self.request.GET.get('search[value]', None).strip()
        except Exception:
            search = ""
        if search:
            # normalize query string and get the list of words
            terms = normalize_query(search)
            # get list of text fields
            fields = [f for f in self.model._meta.fields if isinstance(
                f, (CharField, TextField))]
            # get the list of foreig fields
            foreign_fields = [
                f for f in self.model._meta.fields if isinstance(f, ForeignKey)]
            # get dict with ForeigKey field as key and list of Char/Text fields
            # that are in related model as a argument
            foreign_models_fields = {}
            for foreign_field in foreign_fields:
                try:
                    fmodel = self.model._meta.get_field(
                        '%s' % foreign_field.name).remote_field.model
                except Exception:
                    # for older version of django
                    fmodel = self.model._meta.get_field(
                        '%s' % foreign_field.name).rel.to

                foreign_models_fields[foreign_field] = [
                    f for f in fmodel._meta.fields if isinstance(f, (CharField, TextField))]
            # define empty Q object
            qobjects = Q()
            for term in terms:
                # get queries for Char/Text fields
                queries = [Q(**{'%s__icontains' % f.name: term})
                           for f in fields]
                # exted queries by foreign fields
                if foreign_models_fields:
                    for foreign_field, model_fields in foreign_models_fields.items():
                        queries += [Q(**{'%s__%s__icontains' % (foreign_field.name, f.name): term})
                                    for f in model_fields]

                # crete OR statement for Q objects
                for query in queries:
                    qobjects = qobjects | query
            # return filtered querystring
            return qs.filter(qobjects)
        return qs


class ProjectDetailJson(generics.RetrieveAPIView):
    """Retrieve a project instance."""

    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer


class ProjectCreateJson(generics.CreateAPIView):
    """Create a project instance."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        """Add default data when project is created."""
        now = timezone.now()
        user = self.request.user
        serializer.save(created_by=user, create_date=now)


class ProjectUpdateJson(generics.RetrieveUpdateAPIView):
    """Update a Project Instance using JSON."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_update(self, serializer):
        """Add default data when project is updated."""
        now = timezone.now()
        user = self.request.user
        serializer.save(modify_by=user, modify_date=now)

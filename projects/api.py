from django.utils.html import escape
from django_datatables_view.base_datatable_view import BaseDatatableView
from rest_framework import generics

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectListJson(BaseDatatableView):
    model = Project
    columns = ['id', 'name', 'molecule', 'form',
               'strength', 'brand_name', 'market', 'moq']
    # 'description', 'project_type', 'manager', 'contract_type',
    # 'status', 'prescription_category', 'therapeutic_area',
    # 'priority', 'atc_class', 'pack_size', 'pact_type', 'shelf_life',]
    order_columns = ['name', 'molecule', 'form',
                     'strength', 'brand_name', 'market']

    def render_column(self, row, column):
        """ Renders a column on a row.
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


class ProjectDetailJson(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a project instance.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

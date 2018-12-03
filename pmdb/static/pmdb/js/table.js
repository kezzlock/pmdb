let datatableApiUrl = '/api/project/datatable/';

/* Table script */
    var table = $('._table').DataTable({
        //data: JSON_duza_tabela.data,
        //columns: JSON_duza_tabela.columns,
        searching: true,
        processing: true,
        serverSide: true,
        serverSave: true,
        ajax: datatableApiUrl,
        columnDefs: [
            {
                targets: 0,
                render: function (data) {
                    return '<div class="table__select-container"><input class="table__select table__select-one ' + data + '" type="checkbox"></div>';
                },
                title: '<div class="table__select-container"><input type="checkbox" class="table__select table__select-all"></div>',
                width: '25px',
                orderable: false
            },
            {
                targets: '_all',
                className: 'table__cell'

            },
            {
                targets: '_all',
                render: function (data) {
                    if (data === [] || data === '' || data === {}) {
                        return '&mdash;';
                    }
                    return data;
                }
            },
        ],
        order: [],
        paging: false,
        info: false,
        dom: 't',
        autoWidth: false,
        createdRow: function (row) {
            $(row).addClass('table__row table__body-row');
        },
        initComplete: function () {
            $('.table__thead > tr').addClass('table__row table__header-row');
            $('th').addClass('table__cell--header');
            $('.table__cell--header.sorting').append('<img class="table__sort-icon" src="/static/pmdb/img/arrows.svg">');
            $('.table__cell--header:not(:first-child)').addClass('table__cell--header-no-checkbox');

            $('.table__name-link').click(function () {
              $('menu-container').hide();
              // update details menu
              // require of ObjID attribute on table__name-link
              var objID = $(this).attr('objID');
              if (objID === undefined) {
                  objID = 1;
              }
              $.ajax({
                url: '/api/project/1/'.replace(/1/, objID.toString()),
                dataType: 'json',
                success: function(data) {
                  Object.keys(data).forEach(function(key) {
                      if ( data[key] !== null && data[key] !== '' ){
                        $('#details__'+key).text(data[key]);
                      }
                  });
                }
              });
              // child will show after parent
              $('.menu').show(0, function () {
                  $('.details').show();
              });

            });

            $('.table__select-one').change(function (event) {
                event.stopPropagation();
                showHideManipulationIcons();

                if($(this).is(':checked')) {
                    $(this).prop('checked', false);
                    $(this).closest('.table__row').removeClass('table__row--selected');
                } else {
                    $(this).prop('checked', true);
                    $(this).closest('.table__row').addClass('table__row--selected');
                }
              });
            $('.table__body-row').click(function () {
                $(this).find('.table__select-one').change();
            })
        }
    });

    $(table.table().container()).addClass('sheet__table-wrapper');

    $('.sheet__search').keyup(function () {
        table.search(this.value).draw();
    });

    $('.sorting.table__cell--header.table__cell--header-no-checkbox').click(function () {
        $('.table__sort-icon-sorted')
            .replaceWith('<img class="table__sort-icon" src="/static/pmdb/img/arrows.svg">');

        if ($(this).hasClass('sorting_asc')) {
            $(this)
                .children('.table__sort-icon')
                .replaceWith('<img class="table__sort-icon table__sort-icon-sorted" src="/static/pmdb/img/sort_asc.svg">');
        }

        if ($(this).hasClass('sorting_desc')) {
            $(this)
                .children('.table__sort-icon')
                .replaceWith('<img class="table__sort-icon table__sort-icon-sorted" src="/static/pmdb/img/sort_desc.svg">');
        }
    });

    $('.table__select-all').click(function () {
        var all_checked = $(this).prop('checked');

        if (all_checked) {
            $('.table__select-one').prop('checked', false).change();
        } else {
            $('.table__select-one').prop('checked', true).change();
        }
        showHideManipulationIcons();
    });

    $('.sheet__delete-icon')
        .mouseenter(function () {
        $('.table__row--selected').addClass('table__row--selected-to-delete');
    })
        .mouseleave(function () {
        $('.table__row--selected').removeClass('table__row--selected-to-delete');
    });

    $('.sheet__export-icon')
        .mouseenter(function () {
            $('.table__row--selected').addClass('table__row--selected-to-export');
    })
        .mouseleave(function () {
            $('.table__row--selected').removeClass('table__row--selected-to-export');
    });

    /**
     * Decide whether show or hide table rows manipulation icons (edit, delete, import) basing on number of selected rows
     */
    function showHideManipulationIcons() {
        let numberOfSelectedRows = $('.table__select:checked').length;

        if (numberOfSelectedRows === 0) {
            $('.sheet__manipulation-icon').css('visibility', 'hidden');
        }
        if (numberOfSelectedRows === 1) {
            $('.sheet__manipulation-icon').css('visibility', 'visible');

        }
        if (numberOfSelectedRows > 1) {
          $('.sheet__manipulation-icon:not(:first-child)').css('visibility', 'visible');
          $('.sheet__manipulation-icon:first-child').css('visibility', 'hidden');
        }
    }

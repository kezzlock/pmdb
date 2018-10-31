/* Side menus script */

let filterApiUrl = '/api/project/datatable/';

$('.menu__exit-icon').click(function () {
    // child will be hide after container
    $('.menu').hide(0, function () {
        $('.menu-container').hide();
    });
});

$('.sheet__show-column-control-menu').click(function () {
    $('.menu-container').hide();
    // child will show after parent
    $('.menu').show(0, function () {
        $('.columns-control').show();
    });
});

$('.sheet__show-manipulation-menu').click(function () {
    $('.menu-container').hide();
    // child will show after parent
    $('.menu').show(0, function () {
        $('.menu-manipulate').show();
    });
});

$('.sheet__show-filter-menu').click(function () {
    $('.menu-container').hide();
    // child will show after parent
    $('.menu').show(0, function () {
        $('.menu-filter').show();
    });
});

$('.sheet__show-choices-menu').click(function () {
    $('.menu-container').hide();
    // child will show after parent
    $('.menu').show(0, function () {
        $('.menu-choices').show();
    });
});

$('.menu-header__clear-icon').click(function () {
    $('.menu-filter .form-control').val(null).trigger('change');
});

$('.manipulate-form').submit(function (event) {
    $.ajax({
        'url': '',
        'type': 'post',
        'contentType': 'json',
        'data': $(this).serializeArray(),
        'success': function (result, status, xhr) {

        },
        'error': function (xhr, status, error) {

        }
    });
});

$('.filter-form').submit(function (event) {
    $.ajax({
        'url': filterApiUrl,
        'type': 'post',
        'contentType': 'json',
        'data': $(this).serializeArray(),
        'success': function (result, status, xhr) {
            table.clear();
            table.rows.add(result);
            table.draw();
        },
    });
});

$('.custom-select').select2({
    width: '100%',
    theme: 'bootstrap4'
});

// handlers for date inputs (workaround to keep html5 datepicker and input placeholder)
$('.date-control').on('focus', function () {
    this.type = 'date';
});

$('.date-control').on('blur', function () {
    this.type = 'text';
});

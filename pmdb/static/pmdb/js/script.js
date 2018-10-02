/* Side menu script*/

$(function () {
    $('.menu__exit-icon').click(function () {
        // child will be hide after container
        $('.menu').hide(0, function () {
            $('.menu__content').hide();
        });
    });

    $('.sheet__show-column-control-menu').click(function () {
        $('.menu__content').hide();
        // child will show after parent
        $('.menu').show(0, function () {
            $('.columns-control').show();
        });
    });
});
/* Sidebar script */

/**
 * Bit of explanation:
 * -tabs are elements inside sidebar
 * -tab has its owm header and eventualy vertically toggleable menu
 */

$(function () {
    var isSidebarExpanded = false;
    var countOpenMenus = 0;

    var sidebarMouseenterHandler = function (event, delay = 100) {
        timer = setTimeout(function () {
            if (isSidebarExpanded === false) {
                $('.sidebar__tab-icon-wrapper--special').addClass('sidebar__tab-icon-wrapper--special-hover')
                $('.sidebar__tab-header-title').animate({width: 'show'});
                isSidebarExpanded = true;
            }
        }, delay);
    };

    var sidebarMouseleaveHandler = function () {
        clearTimeout(timer);
        if (countOpenMenus === 0) {
            $.when(
                $('.sidebar__tab-header-title').animate({width: 'hide'})
            ).done(function () {
                $('.sidebar__tab-icon-wrapper--special').removeClass('sidebar__tab-icon-wrapper--special-hover');
                $('.sidebar').addClass('sidebar--hoverable');
            });
            isSidebarExpanded = false;
        }
    };

    $('.sidebar').mouseenter(sidebarMouseenterHandler);

    $('.sidebar').mouseleave(sidebarMouseleaveHandler);

    $('.sidebar__tab-menu').on('customSlideUp', function (e) {
        $(this).slideUp(function () {
            countOpenMenus--;

            // check if mouse is not over sidebar
            if (!$('.sidebar:hover').length) {
                $('.sidebar').trigger('mouseleave');
            }
        });
    });

    $('.sidebar__tab-menu').on('customSlideDown', function (e) {
        $(this).slideDown();
    });

    $('.sidebar__tab-header').click(function () {
        $(this).find('.sidebar__tab-arrow').toggleClass('sidebar__tab-arrow--rotated')

        if (!$(this).hasClass('sidebar__tab-header--special')) {
            $('.tab-selected').toggleClass('tab-selected');
            $(this).addClass('tab-selected');
        }

        var tabMenu = $(this).siblings('.sidebar__tab-menu');
        if (isSidebarExpanded) {
            if (tabMenu.is(':hidden')) {
                tabMenu.trigger('customSlideDown');
                countOpenMenus++;
            }
            else {
                tabMenu.trigger('customSlideUp');
            }
        }
    });

    $('.nav-bar__toggle-sidebar').click(function () {
        var sidebar = $('.sidebar');

        // expand sidebar
        if (sidebar.hasClass('hover-on') && !isSidebarExpanded) {
            sidebar.trigger('mouseenter', 0);
            sidebar.off('mouseenter mouseleave');
            sidebar.toggleClass('hover-on hover-off sidebar--hoverable');

        }

        // hide sidebar
        else if (sidebar.hasClass('hover-off')) {
            sidebar.on('mouseenter', sidebarMouseenterHandler);
            sidebar.on('mouseleave', sidebarMouseleaveHandler);
            sidebar.trigger('mouseleave');
            sidebar.toggleClass('hover-on hover-off');
        }
    });
});

$(function(){
    var $carSound = $('#car-sound');
    $('#footer-car').click(function(){
        var $car = $(this),
            pathLength = $(window).width();
        $carSound[0].play();
        setTimeout(function(){
            $car.addClass('starts');
            setTimeout(function(){
                $car.removeClass('starts')
            }, 29000)
        }, 1660)
    })
});
(function() {
  $(function() {});

}).call(this);

$(function(){

var app = {
    $body: $('body'),
    $fixedHead: $('#fixed-head'),
    $showCatalogMenu: $('#show-catalog-menu'),
    $showCatalogMenuMobile: $('#show-catalog-menu-mobile'),
    $catalogMenu: $('#catalog-menu'),
    catalogMenuHeight: 0,
    catalogMenuThreshold: 0,

    Popup: function(e){
        e.preventDefault();
        $.fancybox({
            href: $(this).attr('href'),
            padding: 20,
            wrapCSS: 'fancybox-form',
            fitToView: false,
            type: 'ajax',
            helpers: {
                overlay : {
                    css : {
                        'background' : 'rgba(0, 0, 0, .21)'
                    },
                    locked: false
                }
            }
        })
    },

    OnScroll: function(){
        var scrollTop = $(window).scrollTop();
        if (scrollTop > app.catalogMenuThreshold) {
            app.$body.addClass('over-page');
            app.$showCatalogMenu.fadeIn(200);
        } else {
            app.$body
                .removeClass('display-catalog-menu')
                .removeClass('over-page');
            app.$showCatalogMenu.fadeOut(200);
        }
    },

    Scroll2Section: function(sectionCode) {
        var $section = $('#section-' + sectionCode);
        if ($section) {
            var topExtra = app.$fixedHead.outerHeight();
            if($('html').hasClass('cms-toolbar-expanded')) {
                topExtra += 30;
            }
            if(app.$body.hasClass('display-catalog-menu')) {
                topExtra += app.catalogMenuHeight;
            }
            $('html,body').animate({
                scrollTop: $section.offset().top - topExtra
            });
            window.location.hash = sectionCode;
        }
    },
    HashNavigate: function(e){
        var href = $(this).attr('href'),
            hrefParts = href.split('#'),
            path = hrefParts[0],
            hash = hrefParts[1];
        if(window.location.pathname == path) {
            e.preventDefault();
            app.Scroll2Section(hash);
        }
    },

    ToggleCatalogMenu: function(e){
        e.preventDefault();
        if (app.$body.hasClass('display-catalog-menu')) {
            app.$body.removeClass('display-catalog-menu');
            app.catalogMenuThreshold = app.catalogMenuHeight;
        } else {
            app.$body.addClass('display-catalog-menu');
            app.catalogMenuThreshold = 0;
        }
    },
    ToggleCatalogMenuMobile: function(e) {
        e.preventDefault();
        app.$body.toggleClass('display-catalog-menu-mobile');
    },

    Init: function(){
        var app = this,
            hash = window.location.hash.replace('#', '');

        if(hash) {
            app.Scroll2Section(hash);
        }

//        $('select').selectBox();
        $('select').select2();
        $('input').iCheck({
            checkboxClass: 'icheckbox_fs',
            radioClass: 'iradio_fs'
        });
        $('.maskedinput').mask("+7(999) 999-99-99");
        $('.superbanner_slider').iosSlider({
            desktopClickDrag: true,
            snapToChildren: true,
            navPrevSelector: '.superbanner_arrow.prev',
            navNextSelector: '.superbanner_arrow.next',
            infiniteSlider: true,
            autoSlide: true,
            navSlideSelector: '.superbanner_nav_item',
            onSlideChange: function(args) {
                $('.superbanner_nav_item').removeClass('selected');
				$('.superbanner_nav_item:eq(' + (args.currentSlideNumber - 1) + ')').addClass('selected');
            }
        });

        app.catalogMenuHeight = app.$catalogMenu.outerHeight(true);
        app.catalogMenuThreshold = app.catalogMenuHeight;
        app.$showCatalogMenu.click(app.ToggleCatalogMenu);
        app.$showCatalogMenuMobile.click(app.ToggleCatalogMenuMobile);
        $(window).scroll(app.OnScroll);

        app.$body
            .on('click','.open-popup', app.Popup)
            .on('click','a[href*=#]', app.HashNavigate);
        if($("#cms_toolbar").size() == 1) {
            setTimeout(function(){
                app.$fixedHead.addClass('a')
            }, 100);
        }
    }
};

app.Init();

});
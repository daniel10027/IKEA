(function($){

    //1. Data Background Set
    $('[data-background]').each(function () {
        $(this).css('background-image', 'url(' + $(this).attr('data-background') + ')');
    });


    //2. Mobile Menu
    $(".mobile-menu-toggle").on("click", function () {
        $(".mobile-menu").addClass("active");
        $("body").addClass("overflow-hidden");
    });

    $(".mobile-menu .close").on("click", function () {
        $(".mobile-menu").removeClass("active");
        $("body").removeClass("overflow-hidden");
    });

    $(".mobile-menu ul li.has-submenu i").each(function () {
        $(this).on("click", function () {
        $(this).siblings('ul').slideToggle();
        $(this).toggleClass("icon-rotate");
        });
    });

    $(document).on("mouseup", function (e) {
        var offCanvusMenu = $(".mobile-menu");

        if (!offCanvusMenu.is(e.target) && offCanvusMenu.has(e.target).length === 0) {
            $(".mobile-menu").removeClass("active");
            $("body").removeClass("overflow-hidden");
        }
    });

    //3. Category Menu
    $(".vr6-category-dropdown").on("click", function () {
        $(".vr6-category-sidebar").addClass("active");
        $("body").addClass("overflow-hidden");
    });

    $(".vr6-category-sidebar .close-ct-menu").on("click", function () {
        $(".vr6-category-sidebar").removeClass("active");
        $("body").removeClass("overflow-hidden");
    });

    $(".vr6-category-sidebar ul li.has-submenu i").each(function () {
        $(this).on("click", function () {
        $(this).siblings('ul').slideToggle();
        $(this).toggleClass("icon-rotate");
        });
    });

    $(document).on("mouseup", function (e) {
        var offCanvusMenu = $(".vr6-category-sidebar");

        if (!offCanvusMenu.is(e.target) && offCanvusMenu.has(e.target).length === 0) {
            $(".vr6-category-sidebar").removeClass("active");
            $("body").removeClass("overflow-hidden");
        }
    });

    //4.Theme Slider Funtions 
    $(".hero-main-slider").slick({
        slidesToShow: 1,
        autoplay: false,
        arrows: false,
        fade: true,
        asNavFor: '.hero-vertical-slider',
    });

    $(".hero-vertical-slider").slick({
        slidesToShow: 2,
        autoplay: false,
        vertical: true,
        verticalSwiping: true,
        arrows: false,
        asNavFor: '.hero-main-slider',
        focusOnSelect: true,
    });

    $(".vr-thumbnail-slider").each(function(){

        var ControlSlider = $(this).parents(".vr-product-card").find(".vr-thumbnail-control-slider");

        var ThumbnailSlider = $(this);

        ThumbnailSlider.slick({
            slidesToShow: 1,
            arrows: false, 
            autoplay: false,
            asNavFor: ControlSlider,
            loop: true,
        });

        ControlSlider.slick({
            slidesToShow: 3,
            arrows: false,
            autoplay: false,
            vertical: true,
            verticalSwiping: true,
            focusOnSelect: true,
            asNavFor: ThumbnailSlider,
            loop: true,
        });
    }); 

    //arival slider
    $(".arrival-slider").slick({
        slidesToShow: 4,
        autoplay: true,
        loop: true,
        prevArrow: '<button class="prev-arrow"><i class="fas fa-arrow-left"></i>Prev</button>', 
        nextArrow: '<button class="next-arrow">Next<i class="fas fa-arrow-right"></i></button>', 
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 3,
                }
            }, 
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 2,
                }
            }, 
            {
                breakpoint: 575,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });

    //hero slider 
    $(".hm2-hero-slider").slick({
        slidesToShow: 1,
        autoplay: true,
        arrows: false,
        dots: true,
        fade: true,
    });

    //brand slider 
    $(".hm2-brand-slider").slick({
        slidesToShow: 5,
        autoplay: true,
        arrows: false, 
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 4,
                }
            },
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 3,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                }
            },
            {
                breakpoint: 400,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });

    //gallery slider
    $(".hm2-gallery-slide-1").slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 0,
        speed: 6000,
        pauseOnHover: true,
        cssEase: 'linear',
        loop: true,
        responsive: [
            {
                breakpoint: 1400,
                settings: {
                    slidesToShow: 4,
                }
            },
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 3,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                }
            },
            {
                breakpoint: 500,
                settings: {
                    slidesToShow: 1,
                }
            },
        ]
    });

    $(".hm2-gallery-slide-2").slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 0,
        speed: 6000,
        pauseOnHover: true,
        cssEase: 'linear',
        loop: true,
        rtl: true,
        responsive: [
            {
                breakpoint: 1400,
                settings: {
                    slidesToShow: 4,
                }
            },
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 3,
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                }
            },
            {
                breakpoint: 500,
                settings: {
                    slidesToShow: 1,
                }
            },
        ]
    });

    $(".hm3-hero-slider").slick({
        slidesToShow: 3,
        arrows: false,
        autoplay: true,
        speed: 700,
        autoplaySpeed: 3000,
        dots: true,
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 2,
                }
            }, 
            {
                breakpoint: 768, 
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    }); 

    $(".hm3-brand-slider").slick({
        slidesToShow: 6,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 0, 
        speed: 5000,
        cssEase: 'linear',
        responsive: [
            {
                breakpoint: 1400, 
                setttings: {
                    slidesToShow: 5,
                }
            },
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 4,
                }
            }, 
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 3,
                }
            },
            {
                breakpoint: 768, 
                settings: {
                    slidesToShow: 2,
                }
            }, 
            {
                breakpoint: 500, 
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });

    $(".hm3-blog-slider").slick({
        slidesToShow: 3,
        autoplay: true,
        speed: 600,
        prevArrow: '<button class="prev-arrow"><i class="me-3 fas fa-arrow-left"></i>Prev</button>', 
        nextArrow: '<button class="next-arrow">Next<i class="ms-3 fas fa-arrow-right"></i></button>',
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 2,
                }
            }, 
            {
                breakpoint: 670,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]  
    }); 

    //vr product slider
    $(".vr-poroduct-single-slider").slick({
        slidesToShow: 1, 
        asNavFor: '.vr-product-thumb-control',
        prevArrow: '<button class="prev-arrow"><i class="fas fa-angle-left"></i></button>',
        nextArrow: '<button class="next-arrow"><i class="fas fa-angle-right"></i></button>',
    
    });

    $(".vr-product-thumb-control").slick({
        slidesToShow: 3,
        arrows: false,
        asNavFor: '.vr-poroduct-single-slider',
        focusOnSelect: true,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                }
            }
        ]
    });

    $(".vr-poroduct-single-slider2").slick({
        slidesToShow: 1,
        asNavFor: '.pd-vertical-product-slider',
        prevArrow: '<button class="prev-arrow"><i class="fas fa-angle-left"></i></button>',
        nextArrow: '<button class="next-arrow"><i class="fas fa-angle-right"></i></button>',
    
    });

    $(".pd-vertical-product-slider").slick({
        slidesToShow: 2,
        arrows: false,
        vertical: true,
        verticalSwiping: true,
        asNavFor: '.vr-poroduct-single-slider2',
        focusOnSelect: true,
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 2,
                    vertical: false,
                    verticalSwiping: false,
                }
            }
            
        ]
    });

    $(".vr4-hero-slider").slick({
        slidesToShow: 1,
        prevArrow: '<button type="button" class="prev-btn"><i class="fas fa-arrow-left"></i></button>',
        nextArrow: '<button type="button" class="next-btn"><i class="fas fa-arrow-right"></i></button>',
        speed: 1000,
        autoplay: true,
        fade: true,
    });

    $(".vr4-feedback-slider").slick({
        slidesToShow: 2,
        arrows: false,
        dots: true,
        responsive: [
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });

    $(".cmd-slider").slick({
        slidesToShow: 1,
        arrows: false,
        dots: true,
    });

    $(".vr4-product-card").each(function(){
        var feature_slider = $(this).find(".vr4-feature-image-slider");
        var feature_control_slider = $(this).find(".vr4-ft-control-slider");
        
        feature_slider.slick({
            slidesToShow: 1,
            arrows: false,
            asNavFor: feature_control_slider,
        });

        feature_control_slider.slick({
            slidesToShow: 9, 
            arrows: false,
            asNavFor: feature_slider,
            focusOnSelect: true,
            responsive: [
                {
                    breakpoint: 1600, 
                    settings: {
                        slidesToShow: 7,
                    }
                },
                {
                    breakpoint: 1500, 
                    settings: {
                        slidesToShow: 6,
                    }
                },
                {
                    breakpoint: 1400, 
                    settings: {
                        slidesToShow: 5,
                    }
                },
            ]
        });
    });

    $(".vr5-hero-content-slider").slick({
        slidestoShow: 1,
        arrows: false,
        autoplay: true,
        dots: true,
    });

    $(".vr5-filter-slider").slick({
        slidesToShow: 3,
        arrows: false,
        dots: true,
        responsive: [
            {
                breakpoint: 1100, 
                settings: {
                    slidesToShow: 2,
                }
            }, 
            {
                breakpoint: 768, 
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });

    $(".vr5-collection-slider").slick({
        slidesToShow: 4,
        arrows: false,
        dots: true,
        responsive: [
            {
                breakpoint: 1400, 
                settings: {
                    slidesToShow: 3,
                }
            },
            {
                breakpoint: 992, 
                settings: {
                    slidesToShow: 2,
                }
            },
            {
                breakpoint: 768, 
                settings: {
                    slidesToShow: 1,
                }
            },
        ]
    });

    //vr5 collection slider progress 
    var vr5_slide_length = $(".vr5-collection-slider .vr5-product-card").length;
    var vr5_total_slide = (vr5_slide_length - 1) / 2;

    var slide_per_width = 100 / vr5_total_slide + '%';

    $(".vr5-collection-progress").css({
        width: slide_per_width,
    });




    $(".vr6-hero-slider").slick({
        slidesToShow: 1,
        arrows: false,
        autoplay: true,
        dots: true,
    });

    //5 header functions
    $(".header-search-btn").on("click", function(){
        $(".header-search-box").addClass("active");
    });

    $(".header-search-box .search-close").on("click", function(){
        $(".header-search-box").removeClass("active");
    });

    $(".header-cart").on("click", function(){
        $(".cart-drawer").addClass("active");
    });

    $(".drawer-close").on("click", function(){
        $(".cart-drawer").removeClass("active");
    }); 

    $(document).on("mouseup", function (e) {
        var offCanvusMenu = $(".cart-drawer");

        if (!offCanvusMenu.is(e.target) && offCanvusMenu.has(e.target).length === 0) {
            $(".cart-drawer").removeClass("active");
            $("body").removeClass("overflow-hidden")
        }
    });


    $(".offcanvus-toggle").on("click", function () {
        $(".offcanvus-box").addClass("active");
        $("body").addClass("overflow-hidden")
    });

    $(".offcanvus-close").on("click", function(){
        $(".offcanvus-box").removeClass("active");
        $("body").removeClass("overflow-hidden");
    });

    $(document).on("mouseup", function (e) {
        var offCanvusMenu = $(".offcanvus-box");
  
        if (!offCanvusMenu.is(e.target) && offCanvusMenu.has(e.target).length === 0) {
          $(".offcanvus-box").removeClass("active");
        }
    });

    //vr5 product tooltip
    $(".vr5-product-tooltip").each(function(){
        $(this).hover(function(){
            $(this).parents(".vr5-action-area").find(".vr5-tooltip-product.active").removeClass("active");
            $(this).find(".vr5-tooltip-product").addClass("active");
        });
    });

    //6 checkout toggle
    $(".checkout-toggle-form").each(function() {
        var toggleBtn = $(this).find(".form-toggle-btn");

        toggleBtn.on("click", function(){
            $(this).parents(".checkout-toggle-form").find(".toggle-form").slideToggle(); 
            return false;
        });
    }); 


    //7 price range slider
    $( ".ur-pricing-range" ).slider({
        range: true,
        min: 0,
        max: 500,
        values: [ 75, 300 ],
        slide: function( event, ui ) {
          $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
        }
    });
    $( "#amount" ).val( "$" + $( ".ur-pricing-range" ).slider( "values", 0 ) + " - $" + $( ".ur-pricing-range" ).slider( "values", 1 ) );

    $(document).ready(function(){
        //8. preloader
        $(".preloader").fadeOut();

        //9. init Isotope
        var $grid_1 = $('.grid_1').isotope({
            masonry: {
                columnWidth: 1
            }
        });

        //10. filter items on button click
        $('.vr-filter-btns').on( 'click', 'button', function() {
            var filterValue_1 = $(this).attr('data-filter');
            $grid_1.isotope({ filter: filterValue_1 });
        });

        $(".vr-filter-btns button").each(function(){
            $(this).on("click", function(){
                $(this).parents(".vr-filter-btns").find("button.active").removeClass("active");
                $(this).addClass("active");
            });
        });


        //11. Isotop Grid 2
        var $grid = $('.hm2-grid').isotope({
            
        });

        // filter items on button click
        $('.hm2-filter-btn-group').on( 'click', 'button', function() {
            var filterValue = $(this).attr('data-filter');
            $grid.isotope({ filter: filterValue });
        });

        $(".hm2-filter-btn-group button").each(function(){
            $(this).on("click", function(){
                $(this).parents(".hm2-filter-btn-group").find("button.active").removeClass("active");
                $(this).addClass("active");
            });
        });

        var $grid3 = $('.grid_3').isotope({
            masonry: {
                columnWidth: 1
            }
        });

        // filter items on button click
        $('.vr6-filter-btns').on( 'click', 'button', function() {
            var filterValue3 = $(this).attr('data-filter');
            $grid3.isotope({ filter: filterValue3 });
        });

        $(".vr6-filter-btns button").each(function(){
            $(this).on("click", function(){
                $(this).parents(".vr6-filter-btns").find("button.active").removeClass("active");
                $(this).addClass("active");
            });
        });

        var $grid4 = $('.vr4_grid').isotope({
            masonry: {
                columnWidth: 1
            }
        });

        // filter items on button click
        $('.vr4-filter-nav').on( 'click', 'button', function() {
            var filterValue4 = $(this).attr('data-filter');
            $grid4.isotope({ filter: filterValue4 });
        });

        $(".vr4-filter-nav button").each(function(){
            $(this).on("click", function(){
                $(this).parents(".vr6-filter-btns").find("button.active").removeClass("active");
                $(this).addClass("active");
            });
        });


        //12. video popup 
        Fancybox.bind("[data-fancybox]", {
            
        });

        //13. zoom on hover 
        $('.zoom-on-hover').zoom({
            magnify: 1.2

        });


    });

    //14. header sticky
    $(window).on("scroll", function(){
        var scrollBarPosition = $(this).scrollTop();
        if ( scrollBarPosition > 250 ) {    
            $(".sticky-header").addClass("sticky-on");
        } else {
            $(".sticky-header").removeClass("sticky-on");
        }
    });

    //15. vr4 filter tab
    var tab_pane_height = $(".vr4-filter-section .tab-pane").height();
    $(".vr4-filter-section .tab-content").css({
        "height" : tab_pane_height + "px",
    });

    $(window).resize(function(){
        var tab_pane_height = $(".vr4-filter-section .tab-pane").height();
        $(".vr4-filter-section .tab-content").css({
            "height" : tab_pane_height + "px",
        });
    });

    //16. vr5 filter tab
    var vr5_tab_pane_height = $(".vr5-filter .tab-pane").height();
    $(".vr5-filter .tab-content").css({
        "height" : vr5_tab_pane_height + "px",
    });

    $(window).resize(function(){
        var vr5_tab_pane_height = $(".vr5-filter .tab-pane").height();
        $(".vr5-filter .tab-content").css({
            "height" : vr5_tab_pane_height + "px",
        });
    });


    //17. footer accordion
    var window_width = $(window).width(); 

    if(window_width < 576) {
        $(".footer-nav-widget").each(function(){
            var widget_title = $(this).find(".widget-title");
            var widget_menu = $(this).find("ul.footer-links");

            widget_title.on("click", function(){

                $(this).parents(".footer-mobile-accordion").find("ul.footer-links").slideUp();
                $(this).siblings("ul.footer-links").slideDown();
            });

        });
    }

    $(window).resize(function(){
        var window_width = $(window).width(); 
        if(window_width < 576) {
            $(".footer-nav-widget").each(function(){
                var widget_title = $(this).find(".widget-title");

                widget_title.on("click", function(){
                    $(this).parents(".footer-mobile-accordion").find("ul.footer-links").slideUp();
                    $(this).siblings("ul.footer-links").slideDown();
                });

            });
        }
    });

    //wow js
    new WOW().init();




   

})(jQuery)
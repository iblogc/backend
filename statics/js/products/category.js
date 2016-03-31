/**
 * Created by hxhuang on 15-11-3.
 */


var categoryApp = function () {
    var first_category = 0;
    var second_category = 0;
    var third_category = 0;
    var step = 1;
    var company = 0;
    var brand = 0;

    var first_category_onclick = function () {
        first_category = $(this).attr('data-id');
        $('.js-first-category').each(function () {
            if ($(this).attr('data-id') == first_category) {
                if (!$(this).hasClass('active'))
                    $(this).addClass('active');
            } else {
                if ($(this).hasClass('active'))
                    $(this).removeClass('active');
            }
        });
        $.get(
            "/products/sub_category/" + first_category + "/",
            {},
            function (data) {
                $('.js-second-category-div').empty();
                $('.js-third-category-div').empty();
                $('.js-company-div').empty();
                $('.js-brand-div').empty();
                $('.js-series-div').empty();
                for (var index in data) {
                    var category = data[index];
                    $('.js-second-category-div').append('<div class="row">' +
                        '<div class="header js-second-category" data-id="' + category.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox" name="second-category-id" class="hide" value="'+category.id+'"></div><div class="center-line">' + category.name + '</div></h5></a></div>' +
                        '</div>');
                }
                $('.js-second-category').bind('click', second_category_onclick);
            },
            "json"
        );
        second_category = 0;
        third_category = 0;
        company = 0;
        brand = 0;
    };

    var second_category_onclick = function () {
        second_category = $(this).attr('data-id');
        $('.js-second-category').each(function () {
            if ($(this).attr('data-id') == second_category) {
                if (!$(this).hasClass('active'))
                    $(this).addClass('active');
            } else {
                if ($(this).hasClass('active'))
                    $(this).removeClass('active');
            }
        });
        $.get(
            "/products/sub_category/" + second_category + "/",
            {},
            function (data) {
                $('.js-third-category-div').empty();
                $('.js-company-div').empty();
                $('.js-brand-div').empty();
                $('.js-series-div').empty();
                for (var index in data) {
                    var category = data[index];
                    $('.js-third-category-div').append('<div class="row">' +
                        '<div class="header js-third-category" data-id="' + category.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox"></div><div class="center-line">' + category.name + '</div></h5></a></div>' +
                        '</div>');
                }
                $('.js-third-category').bind('click', third_category_onclick);
            },
            "json"
        );
        third_category = 0;
        company = 0;
        brand = 0;
    };

    var third_category_onclick = function () {
        third_category = $(this).attr('data-id');
        $('.js-third-category').each(function () {
            if ($(this).attr('data-id') == third_category) {
                if (!$(this).hasClass('active'))
                    $(this).addClass('active');
            } else {
                if ($(this).hasClass('active'))
                    $(this).removeClass('active');
            }
        });
        $.get(
            "/products/sub_category/" + third_category + "/companies/",
            {},
            function (data) {
                $('.js-company-div').empty();
                $('.js-brand-div').empty();
                $('.js-series-div').empty();
                for (var index in data) {
                    var category = data[index];
                    $('.js-company-div').append('<div class="row">' +
                        '<div class="header js-company" data-id="' + category.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox"></div><div class="center-line">' + category.name + '</div></h5></a></div>' +
                        '</div>');
                }
                $('.js-company').bind('click', company_onclick);
            },
            "json"
        );
        company = 0;
        brand = 0;
    };

    var company_onclick = function () {
        company = $(this).attr('data-id');
        $('.js-company').each(function () {
            if ($(this).attr('data-id') == company) {
                if (!$(this).hasClass('active'))
                    $(this).addClass('active');
            } else {
                if ($(this).hasClass('active'))
                    $(this).removeClass('active');
            }
        });
        $.get(
            "/products/company/" + third_category + "/" + company + "/brands/",
            {},
            function (data) {
                $('.js-brand-div').empty();
                $('.js-series-div').empty();
                for (var index in data) {
                    var category = data[index];
                    $('.js-brand-div').append('<div class="row">' +
                        '<div class="header js-brand" data-id="' + category.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox"></div><div class="center-line">' + category.name + '</div></h5></a></div>' +
                        '</div>');
                }
                $('.js-brand').bind('click', brand_onclick);
            },
            "json"
        );
        brand = 0;
    };

    var brand_onclick = function () {
        brand = $(this).attr('data-id');
        $('.js-brand').each(function () {
            if ($(this).attr('data-id') == brand) {
                if (!$(this).hasClass('active'))
                    $(this).addClass('active');
            } else {
                if ($(this).hasClass('active'))
                    $(this).removeClass('active');
            }
        });
        $.get(
            "/products/brand/" + brand + "/series/",
            {},
            function (data) {
                $('.js-series-div').empty();
                for (var index in data) {
                    var category = data[index];
                    $('.js-series-div').append('<div class="row">' +
                        '<div class="header js-series" data-id="' + category.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox"></div><div class="center-line">' + category.name + '</div></h5></a></div>' +
                        '</div>');
                }
            },
            "json"
        );
    };

    var add_second_category = function () {
        console.log(first_category);
        if (first_category != 0) {
            step = 2;
            $('.js-modal-save-button').bind('click', save_second_category);
            $('#addCategoryForm').modal('show');
        }
    };

    var add_third_category = function () {
        console.log(second_category);
        if (second_category != 0) {
            step = 3;
            $('.js-modal-save-button').bind('click', save_third_category);
            $('#addCategoryForm').modal('show');
        }
    };

    var add_company = function () {
        if (third_category != 0) {
            $('.js-modal-save-button').bind('click', save_company);
            $('#addCategoryForm').modal('show');
        }
    };

    var add_brand = function () {
        if (company != 0) {
            $('.js-modal-save-button').bind('click', save_brand);
            $('#addCategoryForm').modal('show');
        }
    };

    var add_series = function () {
        if (brand != 0) {
            $('.js-modal-save-button').bind('click', save_series);
            $('#addCategoryForm').modal('show');
        }
    }

    var save_second_category = function () {
        var category_name = $('.js-modal-category-name').val();
        if (second_category == 0 && first_category != 0) {
            $.post(
                "/products/sub_category/" + first_category + "/create/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name': category_name,
                    'step': step
                },
                function (data) {
                    $('.js-second-category-div').append('<div class="row">' +
                        '<div class="header js-second-category" data-id="' + data.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox"></div><div class="center-line">' + data.name + '</div></h5></a></div>' +
                        '</div>');
                    $('div.js-second-category[data-id="' + data.id + '"]').on('click', second_category_onclick);
                },
                "json"
            );
        }
        $('.js-modal-save-button').unbind('click');
        $('#addCategoryForm').modal('hide');
    };

    var save_third_category = function () {
        var category_name = $('.js-modal-category-name').val();
        if (second_category != 0) {
            $.post(
                "/products/sub_category/" + second_category + "/create/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name': category_name,
                    'step': step
                },
                function (data) {
                    $('.js-third-category-div').append('<div class="row">' +
                        '<div class="header js-third-category" data-id="' + data.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox"></div><div class="center-line">' + data.name + '</div></h5></a></div>' +
                        '</div>');
                    $('div.js-third-category[data-id="' + data.id + '"]').on('click', third_category_onclick);
                },
                "json"
            );
        }
        $('.js-modal-save-button').unbind('click');
        $('#addCategoryForm').modal('hide');
    };

    var save_company = function () {
        var company_name = $('.js-modal-category-name').val();
        if (third_category != 0) {
            $.post(
                "/products/sub_category/" + third_category + "/company/create/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name': company_name,
                },
                function (data) {
                    $('.js-company-div').append('<div class="row">' +
                        '<div class="header js-company" data-id="' + data.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox"></div><div class="center-line">' + data.name + '</div></h5></a></div>' +
                        '</div>');
                    $('div.js-company[data-id="' + data.id + '"]').on('click', company_onclick);
                },
                "json"
            );
        }
        $('.js-modal-save-button').unbind('click');
        $('#addCategoryForm').modal('hide');
    };

    var save_brand = function () {
        var brand_name = $('.js-modal-category-name').val();
        if (company != 0 && third_category != 0) {
            $.post(
                "/products/company/" + third_category + "/" + company + "/brand/create/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name': brand_name,
                },
                function (data) {
                    $('.js-brand-div').append('<div class="row">' +
                        '<div class="header js-brand" data-id="' + data.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox"></div><div class="center-line">' + data.name + '</div></h5></a></div>' +
                        '</div>');
                    $('div.js-brand[data-id="' + data.id + '"]').on('click', brand_onclick);
                },
                "json"
            );
        }
        $('.js-modal-save-button').unbind('click');
        $('#addCategoryForm').modal('hide');
    };

    var save_series = function () {
        var series_name = $('.js-modal-category-name').val();
        if (brand != 0) {
            $.post(
                "/products/brand/" + brand + "/series/create/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name': series_name,
                },
                function (data) {
                    $('.js-series-div').append('<div class="row">' +
                        '<div class="header js-series" data-id="' + data.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox"></div><div class="center-line">' + data.name + '</div></h5></a></div>' +
                        '</div>');
                },
                "json"
            );
        }
        $('.js-modal-save-button').unbind('click');
        $('#addCategoryForm').modal('hide');
    }

    return {

        init: function () {
            $('.js-first-category').on('click', first_category_onclick);
            $('.js-first-category').mouseover(function(){
                if(!$(this).hasClass('active')){
                    $(this).css('background-color','#009DD9');
                }
            });
            $('.js-first-category').mouseout(function(){
                if(!$(this).hasClass('active')){
                    $(this).css('background-color', '#7f8995');
                }
            });
            $('.js-add-second-category').on('click', add_second_category);
            $('.js-add-third-category').on('click', add_third_category);
            $('.js-add-comnapy').on('click', add_company);
            $('.js-add-brand').on('click', add_brand);
            $('.js-add-series').on('click', add_series);
        }
    }
}();



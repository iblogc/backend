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
                        '<div class="header js-second-category" data-id="' + category.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox" name="second-category-id" value="' + category.id + '"></div><div class="center-line js-second-category-name">' + category.name + '</div></h5></a></div>' +
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
                        '<div class="header js-third-category" data-id="' + category.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox" name="third-category-id" value="' + category.id + '"></div><div class="center-line js-third-category-name">' + category.name + '</div></h5></a></div>' +
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
                        '<div class="header js-company" data-id="' + category.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox" name="company-id" value="' + category.id + '"></div><div class="center-line js-company-name">' + category.name + '</div></h5></a></div>' +
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
                        '<div class="header js-brand" data-id="' + category.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox" name="brand-id" value="' + category.id + '"></div><div class="center-line js-brand-name">' + category.name + '</div></h5></a></div>' +
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
                        '<div class="header js-series" data-id="' + category.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox"  name="series-id" value="' + category.id + '"></div><div class="center-line  js-series-name">' + category.name + '</div></h5></a></div>' +
                        '</div>');
                }
                $('.js-series').bind('click', series_onclick);
            },
            "json"
        );
    };

    var series_onclick = function () {
        series = $(this).attr('data-id');
        $('.js-series').each(function () {
            if ($(this).attr('data-id') == series) {
                if (!$(this).hasClass('active'))
                    $(this).addClass('active');
            } else {
                if ($(this).hasClass('active'))
                    $(this).removeClass('active');
            }
        });
    }

    var add_second_category = function () {
        console.log(first_category);
        if (first_category != 0) {
            step = 2;
            $('.js-modal-save-button').bind('click', save_second_category);
            $('#addCategoryForm').modal('show');
            $('#addCategoryFormLabel').html('添加二级分类');
            $('.js-modal-category-label').html('二级分类名称');
            $('.js-modal-category-name').val('');
        }
    };

    var add_third_category = function () {
        console.log(second_category);
        if (second_category != 0) {
            step = 3;
            $('.js-modal-save-button').bind('click', save_third_category);
            $('#addCategoryForm').modal('show');
            $('#addCategoryFormLabel').html('添加三级分类');
            $('.js-modal-category-label').html('三级分类名称');
            $('.js-modal-category-name').val('');
        }
    };

    var add_company = function () {
        if (third_category != 0) {
            $('.js-modal-save-button').bind('click', save_company);
            $('#addCategoryForm').modal('show');
            $('#addCategoryFormLabel').html('添加厂家');
            $('.js-modal-category-label').html('厂家名称');
            $('.js-modal-category-name').val('');
        }
    };

    var add_brand = function () {
        if (company != 0) {
            $('.js-modal-save-button').bind('click', save_brand);
            $('#addCategoryForm').modal('show');
            $('#addCategoryFormLabel').html('添加品牌');
            $('.js-modal-category-label').html('品牌名称');
            $('.js-modal-category-name').val('');
        }
    };

    var add_series = function () {
        if (brand != 0) {
            $('.js-modal-save-button').bind('click', save_series);
            $('#addCategoryForm').modal('show');
            $('#addCategoryFormLabel').html('添加系列');
            $('.js-modal-category-label').html('系列名称');
            $('.js-modal-category-name').val('');
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
                        '<div class="header js-second-category" data-id="' + data.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox" name="second-category-id" value="' + data.id + '"></div><div class="center-line  js-second-category-name">' + data.name + '</div></h5></a></div>' +
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
                        '<div class="header js-third-category" data-id="' + data.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox" name="third-category-id" value="' + data.id + '"></div><div class="center-line  js-third-category-name">' + data.name + '</div></h5></a></div>' +
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
                        '<div class="header js-company" data-id="' + data.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox" name="company-id" value="' + data.id + '"></div><div class="center-line js-company-name">' + data.name + '</div></h5></a></div>' +
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
                        '<div class="header js-brand" data-id="' + data.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox" name="brand-id" value="' + data.id + '"></div><div class="center-line js-brand-name">' + data.name + '</div></h5></a></div>' +
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
                        '<div class="header js-series" data-id="' + data.id + '"><a href="javascript:void(0);"><h5><div><input type="checkbox" name="series-id" value="' + data.id + '"></div><div class="center-line js-series-name">' + data.name + '</div></h5></a></div>' +
                        '</div>');
                    $('div.js-series[data-id="' + data.id + '"]').on('click', series_onclick);
                },
                "json"
            );
        }
        $('.js-modal-save-button').unbind('click');
        $('#addCategoryForm').modal('hide');
    };

    var delete_second_category = function () {
        if (second_category != 0) {
            $('#deleteCategoryForm').modal('show');
            $('.js-modal-confirm-button').bind('click', delete_second_category_confirm);
        }

    };

    var delete_third_category = function () {
        if (third_category != 0) {
            $('#deleteCategoryForm').modal('show');
            $('.js-modal-confirm-button').bind('click', delete_third_category_confirm);
        }
    };

    var delete_company = function () {
        if (third_category != 0 && company != 0) {
            $('#deleteCategoryForm').modal('show');
            $('.js-modal-confirm-button').bind('click', delete_company_confirm);
        }
    };

    var delete_brand = function () {
        if (third_category != 0 && company != 0 && brand != 0) {
            $('#deleteCategoryForm').modal('show');
            $('.js-modal-confirm-button').bind('click', delete_brand_confirm);
        }
    };

    var delete_series = function () {
        if (series != 0) {
            $('#deleteCategoryForm').modal('show');
            $('.js-modal-confirm-button').bind('click', delete_series_confirm);
        }
    }

    var delete_second_category_confirm = function () {
        if (second_category != 0) {
            $.post(
                "/products/sub_category/" + second_category + "/delete/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                },
                function (data) {
                    if (data.success == 1) {
                        $('div.js-second-category[data-id="' + second_category + '"]').remove();
                        second_category = 0;
                        $('.js-third-category-div').empty();
                        $('.js-company-div').empty();
                        $('.js-brand-div').empty();
                        $('.js-series-div').empty();
                    }
                },
                "json"
            );
        }
        $('#deleteCategoryForm').modal('hide');
        $('.js-modal-confirm-button').unbind('click');
    };

    var delete_third_category_confirm = function () {
        if (third_category != 0) {
            $.post(
                "/products/sub_category/" + third_category + "/delete/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                },
                function (data) {
                    if (data.success == 1) {
                        $('div.js-third-category[data-id="' + third_category + '"]').remove();
                        third_category = 0;
                        $('.js-company-div').empty();
                        $('.js-brand-div').empty();
                        $('.js-series-div').empty();
                    }
                },
                "json"
            );
        }
        $('#deleteCategoryForm').modal('hide');
        $('.js-modal-confirm-button').unbind('click');
    };

    var delete_company_confirm = function () {
        if (third_category != 0 && company != 0) {
            $.post(
                "/products/company/" + third_category + "/" + company + "/delete/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                },
                function (data) {
                    if (data.success == 1) {
                        $('div.js-company[data-id="' + company + '"]').remove();
                        company = 0;
                        $('.js-brand-div').empty();
                        $('.js-series-div').empty();
                    }
                },
                "json"
            );
        }
        $('#deleteCategoryForm').modal('hide');
        $('.js-modal-confirm-button').unbind('click');
    };

    var delete_brand_confirm = function () {
        if (third_category != 0 && company != 0 && brand != 0) {
            $.post(
                "/products/brand/" + third_category + "/" + company + "/" + brand + "/delete/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                },
                function (data) {
                    if (data.success == 1) {
                        $('div.js-brand[data-id="' + brand + '"]').remove();
                        brand = 0;
                        $('.js-series-div').empty();
                    }
                },
                "json"
            );
        }
        $('#deleteCategoryForm').modal('hide');
        $('.js-modal-confirm-button').unbind('click');
    };

    var delete_series_confirm = function () {
        if (series != 0) {
            $.post(
                "/products/series/" + series + "/delete/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                },
                function (data) {
                    if (data.success == 1) {
                        $('div.js-series[data-id="' + series + '"]').remove();
                        brand = 0;
                        $('.js-series-div').empty();
                    }
                },
                "json"
            );
        }
        $('#deleteCategoryForm').modal('hide');
        $('.js-modal-confirm-button').unbind('click');
    };

    var edit_second_category = function () {
        if (second_category != 0) {
            $('.js-modal-save-button').bind('click', save_second_category_edit);
            $('#addCategoryForm').modal('show');
            $('#addCategoryFormLabel').html('编辑二级分类');
            $('.js-modal-category-label').html('二级分类名称');
            $('.js-modal-category-name').val($('.js-second-category[data-id="' + second_category + '"]').find('.js-second-category-name').html());
        }
    };

    var edit_third_category = function () {
        if (third_category != 0) {
            $('.js-modal-save-button').bind('click', save_third_category_edit);
            $('#addCategoryForm').modal('show');
            $('#addCategoryFormLabel').html('编辑三级分类');
            $('.js-modal-category-label').html('三级分类名称');
            $('.js-modal-category-name').val($('.js-third-category[data-id="' + third_category + '"]').find('.js-third-category-name').html());
        }
    };

    var edit_company = function () {
        if (company != 0) {
            $('.js-modal-save-button').bind('click', save_company_edit);
            $('#addCategoryForm').modal('show');
            $('#addCategoryFormLabel').html('编辑厂家');
            $('.js-modal-category-label').html('厂家名称');
            $('.js-modal-category-name').val($('.js-company[data-id="' + company + '"]').find('.js-company-name').html());
        }
    };

    var edit_brand = function () {
        if (brand != 0) {
            $('.js-modal-save-button').bind('click', save_brand_edit);
            $('#addCategoryForm').modal('show');
            $('#addCategoryFormLabel').html('编辑品牌');
            $('.js-modal-category-label').html('品牌名称');
            $('.js-modal-category-name').val($('.js-brand[data-id="' + brand + '"]').find('.js-brand-name').html());
        }
    };

    var edit_series = function () {
        if (series != 0) {
            $('.js-modal-save-button').bind('click', save_series_edit);
            $('#addCategoryForm').modal('show');
            $('#addCategoryFormLabel').html('编辑系列');
            $('.js-modal-category-label').html('系列名称');
            $('.js-modal-category-name').val($('.js-series[data-id="' + series + '"]').find('.js-series-name').html());
        }
    };

    var save_second_category_edit = function () {
        var category_name = $('.js-modal-category-name').val();
        if (second_category != 0) {
            $.post(
                "/products/sub_category/" + second_category + "/update/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name': category_name,
                },
                function (data) {
                    if (data.success == 1) {
                        $('.js-second-category[data-id="' + second_category + '"]').find('.js-second-category-name').html(category_name);
                    }
                },
                "json"
            );
        }
        $('.js-modal-save-button').unbind('click');
        $('#addCategoryForm').modal('hide');
    };

    var save_third_category_edit = function () {
        var category_name = $('.js-modal-category-name').val();
        if (third_category != 0) {
            $.post(
                "/products/sub_category/" + third_category + "/update/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name': category_name,
                },
                function (data) {
                    if (data.success == 1) {
                        $('.js-third-category[data-id="' + third_category + '"]').find('.js-third-category-name').html(category_name);
                    }
                },
                "json"
            );
        }
        $('.js-modal-save-button').unbind('click');
        $('#addCategoryForm').modal('hide');
    };

    var save_company_edit = function () {
        var category_name = $('.js-modal-category-name').val();
        if (company != 0) {
            $.post(
                "/products/company/" + company + "/update/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name': category_name,
                },
                function (data) {
                    if (data.success == 1) {
                        $('.js-company[data-id="' + company + '"]').find('.js-company-name').html(category_name);
                    }
                },
                "json"
            );
        }
        $('.js-modal-save-button').unbind('click');
        $('#addCategoryForm').modal('hide');
    };

    var save_brand_edit = function () {
        var category_name = $('.js-modal-category-name').val();
        if (brand != 0) {
            $.post(
                "/products/brand/" + brand + "/update/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name': category_name,
                },
                function (data) {
                    if (data.success == 1) {
                        $('.js-brand[data-id="' + brand + '"]').find('.js-brand-name').html(category_name);
                    }
                },
                "json"
            );
        }
        $('.js-modal-save-button').unbind('click');
        $('#addCategoryForm').modal('hide');
    };

    var save_series_edit = function () {
        var category_name = $('.js-modal-category-name').val();
        if (series != 0) {
            $.post(
                "/products/series/" + series + "/update/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name': category_name,
                },
                function (data) {
                    if (data.success == 1) {
                        $('.js-series[data-id="' + series + '"]').find('.js-series-name').html(category_name);
                    }
                },
                "json"
            );
        }
        $('.js-modal-save-button').unbind('click');
        $('#addCategoryForm').modal('hide');
    };

    var upload_file = function () {
        var data = new FormData();
        data.append('file', document.getElementById('file').files[0]);
        data.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
        $.ajax({
            type: "POST",
            url: "/products/import/",
            data: data,
            cache: false,
            dataType: 'json',
            processData: false, // Don't process the files
            contentType: false, // Set content type to false as jQuery will tell the server its a query string request

            success: function () {
                alert("Data Uploaded: ");
            }
        });
    }

    return {

        init: function () {
            $('.js-first-category').on('click', first_category_onclick);
            // $('.js-first-category').mouseover(function(){
            //     if(!$(this).hasClass('active')){
            //         $(this).css('background-color','#009DD9');
            //     }
            // });
            // $('.js-first-category').mouseout(function(){
            //     if(!$(this).hasClass('active')){
            //         $(this).css('background-color', '#7f8995');
            //     }
            // });
            $('.js-add-second-category').on('click', add_second_category);
            $('.js-add-third-category').on('click', add_third_category);
            $('.js-add-comnapy').on('click', add_company);
            $('.js-add-brand').on('click', add_brand);
            $('.js-add-series').on('click', add_series);
            $('.js-delete-second-category').on('click', delete_second_category);
            $('.js-delete-third-category').on('click', delete_third_category);
            $('.js-delete-company').on('click', delete_company);
            $('.js-delete-brand').on('click', delete_brand);
            $('.js-delete-series').on('click', delete_series);
            $('.js-edit-second-category').on('click', edit_second_category);
            $('.js-edit-third-category').on('click', edit_third_category);
            $('.js-edit-company').on('click', edit_company);
            $('.js-edit-brand').on('click', edit_brand);
            $('.js-edit-series').on('click', edit_series);
            $('.js-batch-delete-button').on('click', function () {
                $('input[type="checkbox"]').show();
            });
            $('.js-modal-cancel-button').on('click', function () {
                $('#deleteCategoryForm').modal('hide');
            });
            $('.js-upload-button').on('click', upload_file);

        }
    }
}();



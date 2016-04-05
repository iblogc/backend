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
    var series = 0;
    var settings_series = 0;
    var checkboxFlag = false;

    var changeClass = function (obj) {
        $(obj).addClass('selected').siblings().removeClass('selected');
    };

    var checkboxHide = function () {
        $('input[type=checkbox]').hide();
        checkboxFlag = false;
    };

    var batchDelete = function () {
        checkboxHide();
        $('button[data-type=normal]').show();
        $('button[data-for=batch-delete]').hide();
        var selected_ids = new Array();
        $('input[type="checkbox"]:checked').each(function () {
            selected_ids.push($(this).val());
        });
        var ids = selected_ids.join(',');
        if ($(this).attr('data-type') == 1) {
            console.log('confirm');
            if (brand != 0) {
                $.post(
                    encodeURI("/products/series/batch_delete/"),
                    {
                        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                        'ids': ids,
                    },
                    function (data) {
                        if (data.success == 1) {
                            for (var index in selected_ids) {
                                $('div.js-series[data-id="' + selected_ids[index] + '"]').remove();
                            }

                        }
                    },
                    "json"
                );
            } else if (company != 0) {
                $.post(
                    encodeURI('/products/brand/' + third_category + '/' + company + '/batch_delete/'),
                    {
                        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                        'ids': ids,
                    },
                    function (data) {
                        if (data.success == 1) {
                            for (var index in selected_ids) {
                                $('div.js-brand[data-id="' + selected_ids[index] + '"]').remove();
                            }

                        }
                    },
                    "json"
                );
            } else if (third_category != 0) {
                $.post(
                    encodeURI('/products/company/' + third_category + '/batch_delete/'),
                    {
                        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                        'ids': ids,
                    },
                    function (data) {
                        if (data.success == 1) {
                            for (var index in selected_ids) {
                                $('div.js-company[data-id="' + selected_ids[index] + '"]').remove();
                            }

                        }
                    },
                    "json"
                );
            } else if (second_category != 0) {
                $.post(
                    encodeURI('/products/sub_category/batch_delete/'),
                    {
                        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                        'ids': ids,
                    },
                    function (data) {
                        if (data.success == 1) {
                            for (var index in selected_ids) {
                                $('div.js-third-category[data-id="' + selected_ids[index] + '"]').remove();
                            }

                        }
                    },
                    "json"
                );
            } else if (first_category != 0) {
                $.post(
                    encodeURI('/products/sub_category/batch_delete/'),
                    {
                        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                        'ids': ids,
                    },
                    function (data) {
                        if (data.success == 1) {
                            for (var index in selected_ids) {
                                $('div.js-second-category[data-id="' + selected_ids[index] + '"]').remove();
                            }

                        }
                    },
                    "json"
                );
            }
        } else if ($(this).attr('data-type') == 0) {
            console.log('cancel');
        }
        $('input[type=checkbox]').removeAttr("checked");
    };

    var first_category_onclick = function () {
        $('.js-second-category-div').empty();
        $('.js-third-category-div').empty();
        $('.js-company-div').empty();
        $('.js-brand-div').empty();
        $('.js-series-div').empty();
        first_category = 0;
        if (checkboxFlag) return;
        first_category = $(this).attr('data-id');
        changeClass(this);
        $.get(
            "/products/sub_category/" + first_category + "/",
            {},
            function (data) {
                for (var index in data) {
                    var category = data[index];
                    $('.js-second-category-div').append('<div class="header js-second-category" data-id="' + category.id + '"><input type="checkbox" name="second-category-id" value="' + category.id + '"><div class="center-line js-second-category-name">' + category.name + '</div></div>');
                }
                $('.js-second-category').bind('click', second_category_onclick);
                checkboxHide();
            },
            "json"
        );
        second_category = 0;
        third_category = 0;
        company = 0;
        brand = 0;
    };

    var second_category_onclick = function () {
        $('.js-third-category-div').empty();
        $('.js-company-div').empty();
        $('.js-brand-div').empty();
        $('.js-series-div').empty();
        second_category = 0;
        if (checkboxFlag) return;
        second_category = $(this).attr('data-id');
        changeClass(this);
        $.get(
            "/products/sub_category/" + second_category + "/",
            {},
            function (data) {
                for (var index in data) {
                    var category = data[index];
                    $('.js-third-category-div').append('<div class="header js-third-category" data-id="' + category.id + '"><input type="checkbox" name="third-category-id" value="' + category.id + '"><div class="center-line js-third-category-name">' + category.name + '</div></div>');
                }
                $('.js-third-category').bind('click', third_category_onclick);
                checkboxHide();
            },
            "json"
        );
        third_category = 0;
        company = 0;
        brand = 0;
    };

    var third_category_onclick = function () {
        $('.js-company-div').empty();
        $('.js-brand-div').empty();
        $('.js-series-div').empty();
        third_category = 0;
        if (checkboxFlag) return;
        third_category = $(this).attr('data-id');
        changeClass(this);
        $.get(
            "/products/sub_category/" + third_category + "/companies/",
            {},
            function (data) {
                for (var index in data) {
                    var category = data[index];
                    $('.js-company-div').append('<div class="header js-company" data-id="' + category.id + '"><input type="checkbox" name="company-id" value="' + category.id + '"><div class="center-line js-company-name">' + category.name + '</div></div>');
                }
                $('.js-company').bind('click', company_onclick);
                checkboxHide();
            },
            "json"
        );
        company = 0;
        brand = 0;
    };

    var company_onclick = function () {
        $('.js-brand-div').empty();
        $('.js-series-div').empty();
        company = 0;
        if (checkboxFlag) return;
        company = $(this).attr('data-id');
        changeClass(this);
        $.get(
            "/products/company/" + third_category + "/" + company + "/brands/",
            {},
            function (data) {

                for (var index in data) {
                    var category = data[index];
                    $('.js-brand-div').append('<div class="header js-brand" data-id="' + category.id + '"><input type="checkbox" name="brand-id" value="' + category.id + '"><div class="center-line js-brand-name">' + category.name + '</div></div>');
                }
                $('.js-brand').bind('click', brand_onclick);
                checkboxHide();
            },
            "json"
        );
        brand = 0;
    };

    var brand_onclick = function () {
        $('.js-series-div').empty();
        brand = 0;
        if (checkboxFlag)  return;
        brand = $(this).attr('data-id');
        changeClass(this);
        $.get(
            "/products/brand/" + brand + "/series/",
            {},
            function (data) {
                for (var index in data) {
                    var category = data[index];
                    $('.js-series-div').append('<div class="header js-series" data-id="' + category.id + '"><input type="checkbox"  name="series-id" value="' + category.id + '"><div class="center-line js-series-name">' + category.name + '</div></div>');
                }
                $('.js-series').bind('click', series_onclick);
                checkboxHide();
            },
            "json"
        );
    };

    var series_onclick = function () {
        brand = 0;
        if (checkboxFlag)  return;
        series = $(this).attr('data-id');
        changeClass(this);
        $('.fa-cog').attr('category-id', third_category);
        $('.fa-cog').attr('series-id', series);
    };

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
    };

    var save_second_category = function () {
        var category_name = $('.js-modal-category-name').val();
        if (first_category != 0) {
            $.post(
                "/products/sub_category/" + first_category + "/create/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'name': category_name,
                    'step': step
                },
                function (data) {
                    $('.js-second-category-div').append('<div class="header js-second-category" data-id="' + data.id + '"><input type="checkbox" name="second-category-id" value="' + data.id + '"><div class="center-line js-second-category-name">' + data.name + '</div></div>');
                    $('div.js-second-category[data-id="' + data.id + '"]').on('click', second_category_onclick);
                    checkboxHide();
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
                    $('.js-third-category-div').append('<div class="header js-third-category" data-id="' + data.id + '"><input type="checkbox" name="third-category-id" value="' + data.id + '"><div class="center-line js-third-category-name">' + data.name + '</div></div>');
                    $('div.js-third-category[data-id="' + data.id + '"]').on('click', third_category_onclick);
                    checkboxHide();
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
                    $('.js-company-div').append('<div class="header js-company" data-id="' + data.id + '"><input type="checkbox" name="company-id" value="' + data.id + '"><div class="center-line js-company-name">' + data.name + '</div></div>');
                    $('div.js-company[data-id="' + data.id + '"]').on('click', company_onclick);
                    checkboxHide();
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
                    $('.js-brand-div').append('<div class="header js-brand" data-id="' + data.id + '"><input type="checkbox" name="brand-id" value="' + data.id + '"><div class="center-line js-brand-name">' + data.name + '</div></div>');
                    $('div.js-brand[data-id="' + data.id + '"]').on('click', brand_onclick);
                    checkboxHide();
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
                    $('.js-series-div').append('<div class="header js-series" data-id="' + data.id + '"><input type="checkbox" name="series-id" value="' + data.id + '"><div class="center-line js-series-name">' + data.name + '</div></div>');
                    $('div.js-series[data-id="' + data.id + '"]').on('click', series_onclick);
                    checkboxHide();
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
                $('#importForm').modal('hide');
                location.reload();
            }
        });
    };


    var setting = function () {
        $('#settingForm').modal('show');
        var category_id = $(this).attr('category-id');
        var series_id = $(this).attr('series-id');
        settings_series = series_id;
        $.get(
            "category/attribute/values/" + category_id + "/" + series_id + "/",
            {},
            function (data) {
                $('.js-modal-attribute-row').remove();
                for (var index in data) {
                    var attribute = data[index];
                    var row_html = '<div class="modal-row js-modal-attribute-row" data-id="' + attribute.id + '">' +
                        '<div>' + attribute.name + '</div>' +
                        '<div>' +
                        '<select name="value" class="form-control">';
                    for (value_index in attribute.values) {
                        row_html += '<option value="' + attribute.values[value_index] + '">' + attribute.values[value_index] + '</option>';
                    }
                    row_html +=
                        '</select>' +
                        '</div>' +
                        '<div>' +
                        '<select name="searchable" class="form-control">' +
                        '<option value="1">yes</option>' +
                        '<option value="0">no</option>' +
                        '</select>' +
                        '</div>' +
                        '<div class="modal-span"><span class="fa fa-cog"></span>&nbsp;&nbsp;&nbsp;&nbsp;<span' +
                        'class="fa fa-close"></span></div>' +
                        '</div>'
                    $('.modal-body-4').append(row_html);
                    $('.modal-body-4').find('div[data-id="' + attribute.id + '"]').find('select[name="value"]').val(attribute.value);
                    $('.modal-body-4').find('div[data-id="' + attribute.id + '"]').find('select[name="searchable"]').val(attribute.searchable);
                }
            },
            "json"
        );
        //$('#settingForm .modal-body-5').hide();
        //$('#settingForm .modal-body-6').hide();
        $('#settingForm button[data-for]').hide();
    };

    var settingAction = function () {
        if ($(this).attr('data-action') == 'save') {
            var attr_ids = new Array();
            var attr_values = new Array();
            var attr_searchables = new Array();
            $('.js-modal-attribute-row').each(function(){
                attr_ids.push($(this).attr('data-id'));
                attr_values.push($(this).find('select[name="value"]').val());
                attr_searchables.push($(this).find('select[name="searchable"]').val());
            });
            console.log(attr_ids);
            console.log(attr_values);
            console.log(attr_searchables);
            $.post(
                "/products/category/attribute/value/update/" + settings_series + "/",
                {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'ids': attr_ids,
                    'values': attr_values,
                    'searchables': attr_searchables
                },
                function (data) {
                    if (data.success == 1) {
                    }
                },
                "json"
            );
            console.log('save');
        }
        $('#settingForm').modal('hide');
    };

    var modalEdit = function () {
        if (!eval($(this).attr('data-status'))) {
            $(this).prev().removeAttr('readonly');
            $(this).html('save');
        } else {
            $(this).prev().attr('readonly', 'readonly');
            $(this).html('edit');
        }
        $(this).attr('data-status', !eval($(this).attr('data-status')));
    };

    var export_xls = function () {
        window.open('/products/export/');
    };

    var search_kw = function () {
        var kw = $('.js-kw').val();
        $.get(
            "/products/category/search/",
            {
                'kw': kw,
            },
            function (data) {
                $('.js-search-result').find('.js-search-detail').remove();
                for (var result in data.data) {
                    $('.js-search-result').append(
                        '<div class="search-detail-row js-search-detail">' +
                        '<div>' + data.data[result].first_category + '</div>' +
                        '<div>' + data.data[result].second_category + '</div>' +
                        '<div>' + data.data[result].third_category + '</div>' +
                        '<div>' + data.data[result].company + '</div>' +
                        '<div>' + data.data[result].brand + '</div>' +
                        '<div>' + data.data[result].series + '</div>' +
                        '<div><span class="fa fa-cog" category-id="' + data.data[result].category_id + '" series-id="' + data.data[result].series_id + '"></span></div>' +
                        '</div>'
                    );
                }
                $('.js-search-result').find('.fa-cog').on('click', setting);
            },
            "json"
        );
    }


    return {

        init: function () {
            $('.js-first-category').on('click', first_category_onclick);
            $('.js-add-second-category').on('click', add_second_category);
            $('.js-add-third-category').on('click', add_third_category);
            $('.js-add-company').on('click', add_company);
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
                $('button[data-for=batch-delete]').show();
                $('button[data-type=normal]').hide();
                checkboxFlag = true;
            });
            $('.js-modal-cancel-button').on('click', function () {
                $('#deleteCategoryForm').modal('hide');
            });
            $('.js-upload-button').on('click', upload_file);
            $('.modal-body-3 input[type=text]').on('click', function () {
                $('input[name=file]').click();
            });

            $('input[name=file]').on('change', function () {
                $('.modal-body-3 input[type=text]').val(this.files[0].name);
            });
            $('.js-export-button').on('click', export_xls);
            $('button[data-for=batch-delete]').on('click', batchDelete);

            $('button[data-for=batch-delete]').hide();

            $('.fa-cog').on('click', setting);
            $('button[data-action]').on('click', settingAction);

            $('.modal-body-5 span[data-status]').on('click', modalEdit);

            $('.js-search-button').on('click', search_kw);
        }
    }
}();



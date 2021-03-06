/**
 * Created by yunxia on 2015/12/12.
 */
var type = 0;
var s1_val;
var brand_id;
var searchUrl;
var kw = '';
var pn = '';
var c1 = '';
var c2 = '';
var c3 = '';
var com = '';
var brand = '';
var series = '';
var date_from = '';
var date_to = '';
var order = '';
var desc = false;
var product_id = 0;
var modalTmp;

var previewImgId = -1;

//产品分类 绑定
$('select[name=product1]').bind('change', function () {
    $('select[name=product2]').html('<option value="0">请选择</option>');
    $('select[name=product3]').html('<option value="0">请选择</option>');
    changeSearchLink();
    if ($(this).val() == '0')
        return;
    s1_val = $('select[name=product1] :selected').attr('name');
    for (var i = 0; i < category[s1_val].second.length; i++) {
        $('select[name=product2]').append('<option name="' + i + '" value="' + category[s1_val].second[i].id + '">' + category[s1_val].second[i].name + '</option>');
    }
});

$('select[name=product2]').bind('change', function () {
    $('select[name=product3]').html('<option value="0">请选择</option>');
    changeSearchLink();
    if ($(this).val() == '0')
        return;
    var s2_val = $('select[name=product2] :selected').attr('name');
    for (var i = 0; i < category[s1_val].second[s2_val].third.length; i++) {
        $('select[name=product3]').append('<option name="' + i + '" value="' + category[s1_val].second[s2_val].third[i].id + '">' + category[s1_val].second[s2_val].third[i].name + '</option>');
    }
});

$('select[name=product3]').bind('change', function () {
    changeSearchLink();
});

//品牌系列 绑定
$('select[name=brand]').bind('change', function () {
    $('select[name=series]').html('<option value="0">请选择</option>');
    changeSearchLink();
    brand_id = $('select[name=brand] :selected').attr('name');
    for (var i = 0; i < brand_series[brand_id].series.length; i++) {
        $('select[name=series]').append('<option name="' + i + '" value="' + brand_series[brand_id].series[i].id + '">' + brand_series[brand_id].series[i].name + '</option>')
    }
});

$('select[name=series]').bind('change', function () {
    changeSearchLink();
});

//创建时间 绑定事件
$(document).on('change', 'input[sid=Date-created]', function () {
    changeSearchLink();
});


//更新时间 绑定
$('input[sid=Date-update]').bind('change', function () {
    changeSearchLink();
});

//$('input[sid=Date-update]').on('keydown', function (event) {
//    if (event.keyCode == 8) {
//        $(this).val('');
//    }
//});

$('#product-Search').bind('change', function () {
    changeSearchLink();
});

$('#select-Search').bind('click', function () {
    changeSearchLink();
    localStorage.setItem('url_temp', type + ',' + kw + ',' + pn + ',' + c1 + ',' + c2 + ',' + c3 + ',' + com + ',' + brand + ',' + series + ',' + date_from + ',' + date_to + ',' + order + ',' + desc);
    location.href = searchUrl;
});

var changeSearchLink = function () {
    kw = $('.js-kw').val();
    pn = $('.js-pn').val();
    c1 = $('.js-c1').val();
    c2 = $('.js-c2').val();
    c3 = $('.js-c3').val();
    com = $('.js-manufactor').val();
    brand = $('.js-brand').val();
    series = $('.js-series').val();
    date_from = $('.js-df').val();
    date_to = $('.js-dt').val();
    var url = '//' + location.host + location.pathname + '?type=' + type + '&kw=' + kw + '&pn=' + pn + '&c1=' + c1 + '&c2=' + c2 + '&c3=' + c3 + '&c=' + com + '&b=' + brand + '&s=' + series + '&df=' + date_from + '&dt=' + date_to + '&order=' + order + '&desc=' + (desc ? 1 : 0);

    localStorage.setItem('lastUrl', 'type=' + type + '&kw=' + kw + '&pn=' + pn + '&c1=' + c1 + '&c2=' + c2 + '&c3=' + c3 + '&c=' + com + '&b=' + brand + '&s=' + series + '&df=' + date_from + '&dt=' + date_to + '&order=' + order + '&desc=' + (desc ? 1 : 0));
    searchUrl = '/product/pdt?type=' + type + '&kw=' + kw + '&pn=' + pn + '&c1=' + c1 + '&c2=' + c2 + '&c3=' + c3 + '&c=' + com + '&b=' + brand + '&s=' + series + '&df=' + date_from + '&dt=' + date_to + '&order=' + order + '&desc=' + (desc ? 1 : 0);
    $('#search-link').attr('href', searchUrl);

};

$('#product-Search').keyup(function (e) {
    if (e.keyCode == 13 && $(this).val() != '') {
        console.log($(this).val());
        $('#select-Search').click();
        $(this).val('');
    }
});

$('.js-header').on('click', function () {
    if(order==$(this).attr('name'))
        desc = !desc;
    order = $(this).attr('name');

    changeSearchLink();
    localStorage.setItem('url_temp', type + ',' + kw + ',' + pn + ',' + c1 + ',' + c2 + ',' + c3 + ',' + com + ',' + brand + ',' + series + ',' + date_from + ',' + date_to + ',' + order + ',' + desc);
    location.href = searchUrl;
});

$('.js-product-detail').on('click', function () {
    var id = $(this).attr('data-id');
    product_id = id;
    $.get('/sdk/product/' + id + '/', {}, function (data) {
        console.log(data);
        $('.js-modal-product-no').html(data.product_no);
        $('.js-modal-product-name').html(data.product_name);
        $('.js-modal-product-category').html(data.category_name);
        $('.js-modal-product-manufactor').html(data.manufactor_name);
        $('.js-modal-product-brand').html(data.brand);
        $('.js-modal-product-series').html(data.series);
        $('.js-modal-model-no').html(data.norm_no);
        $('.js-modal-model-version').html(data.version);
        $('.js-modal-model-size').html('长-' + data.length + ' 宽-' + data.width + ' 高-' + data.height);
        $('.js-modal-model-material').html(data.material);
        $('.js-modal-model-color').html(data.color);
        $('.js-modal-product-img').attr('src',data.chartlet);
        $('.js-modal-args').empty();
        $('.js-file-list').empty();
        $('.js-preview-list').empty();
        for(var key in data.args){
            $('.js-modal-args').append('<li><span>'+key+':</span><span>'+data.args[key]+'</span></li>');
        }
        for(var index in data.files){
            var file = data.files[index];
            $('.js-file-list').append('<div data-id="'+file.id+'">'+file.name+'</div>');
        }
        var tmp = 0;
        for(var index in data.previews){
            tmp++;
            var preview = data.previews[index];
            $('.js-preview-list').append('<div data-id="'+preview.id+'" data-url="'+preview.url+'"><img class="inline-table product-info-box-img" src="'+preview.url+'"/></div>');
            //$('.js-preview-list').append('<div data-id="'+preview.id+'"><a href="'+preview.url+'" target="_blank"><img class="inline-table product-info-box-img" src="'+preview.url+'"/></a></div>');
        }
        $('.js-preview-list').css('width', tmp * 110);
        $('.js-modal-product-remarks').html(data.remarks);
    }, 'JSON');
});

$('.js-active').on('click', function () {
    var id = $(this).attr('data-id');
    $.post('/sdk/product/' + id + '/active/', {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()}, function (data) {
        $('.js-status-text-' + id).html('启用');
    }, 'JSON');
    $(this).parent().find('.js-active').hide();
    $(this).parent().find('.js-void').show();
});

$('.js-void').on('click', function () {
    var id = $(this).attr('data-id');
    $.post('/sdk/product/' + id + '/void/', {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()}, function (data) {
        $('.js-status-text-' + id).html('禁用');
    }, 'JSON');
    $(this).parent().find('.js-active').show();
    $(this).parent().find('.js-void').hide();
});

//var upload_model_file = function() {
//    var data = new FormData();
//    data.append('file', document.getElementById('model-file').files[0]);
//    data.append('product_id', product_id);
//    data.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
//    $.ajax({
//        type: "POST",
//        url: "/products/product/file/upload/",
//        data: data,
//        cache: false,
//        dataType: 'json',
//        processData: false, // Don't process the files
//        contentType: false, // Set content type to false as jQuery will tell the server its a query string request
//        success: function (data) {
//            $('.js-file-list').append('<div data-id="'+data.id+'">'+data.name+'</div>');
//        }
//    });
//};
//
//var upload_model_preview = function() {
//    var data = new FormData();
//    data.append('file', document.getElementById('model-preview').files[0]);
//    data.append('product_id', product_id);
//    data.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
//    $.ajax({
//        type: "POST",
//        url: "/products/product/preview/upload/",
//        data: data,
//        cache: false,
//        dataType: 'json',
//        processData: false, // Don't process the files
//        contentType: false, // Set content type to false as jQuery will tell the server its a query string request
//        success: function (data) {
//            $('.js-preview-list').append('<div data-id="'+data.id+'"><a href="'+data.url+'" target="_blank"><img class="inline-table product-info-box-img" src="'+data.url+'"/></a></div>');
//            $('img[data-id="'+product_id+'"]').attr('src',data.url);
//        }
//    });
//};

var loadPreviewImg = function(){
    var tmp = $(this).attr('data-url');
    $('div[data-name=previewImg] img').attr('src', tmp);
    $('div[data-name=previewImg]').show();
    previewImgId = eval($(this).attr('data-id'));
    console.log(previewImgId + '-----')
};

var changePreviewImg = function(){
    if($(this).attr('data-name') == 'previewImgLeft'){
        if(previewImgId == $('div[data-name=preview-box] .js-preview-list div[data-id]').length) {
            previewImgId = 1;
        } else {
            previewImgId++;
        }
    } else if ($(this).attr('data-name') == 'previewImgRight'){
        if(previewImgId == 1) {
            previewImgId = $('div[data-name=preview-box] .js-preview-list div[data-id]').length;
        } else {
            previewImgId--;
        }
    }
    var tmp = $('.js-preview-list div[data-id=' + previewImgId + ']').attr('data-url');
    $('div[data-name=previewImg] img').attr('src', tmp);
};

var datePickerActive = function(){

    $("#startDate-update").datetimepicker({
        format: "yyyy-mm-dd",
        autoclose: true,
        minView: "month",
        maxView: "decade",
        todayBtn: true,
        language: 'zh-CN'
    }).on("click", function (ev) {
        $("#startDate-update").datetimepicker("setEndDate", $("#endDate-update").val());
    }).on('change', function(){
        if($("#endDate-update").val() == '') $("#endDate-update").val($("#startDate-update").val()).change();;
    });
    $("#endDate-update").datetimepicker({
        format: "yyyy-mm-dd",
        autoclose: true,
        minView: "month",
        maxView: "decade",
        todayBtn: true,
        language: 'zh-CN'
    }).on("click", function (ev) {
        $("#endDate-update").datetimepicker("setStartDate", $("#startDate-update").val());
    }).on('change', function(){
        if($("#startDate-update").val() == '') $("#startDate-update").val($("#endDate-update").val()).change();
    });


    $('.input-group-addon').hide();
    $('.input-group-addon').on('click',function(){
        $(this).prev().val('');
        $(this).hide();
    });

    $('.select-update-time').mouseenter(function () {
        if($(this).val() != '') $(this).next().show();
    });
    $('.select-update-time').mouseleave(function () {
        $(this).next().hide();
    });
    $('.input-group-addon').mouseenter(function () {
        if($(this).prev().val() != '') $(this).show();
    });
    $('.input-group-addon').mouseleave(function () {
        $(this).hide();
    });


};

var productApp = function () {
    return {
        init: function () {
            type = $('input[name="page_type"]').val();
            $('#product-Search').val('');
            for (var i = 0; i < category.length; i++) {
                $('select[name=product1]').append('<option name="' + i + '" value="' + category[i].id + '">' + category[i].name + '</option>');
            }
            console.log(localStorage.getItem("url_temp"));
            if (url == localStorage.getItem("lastUrl")) {
                var temp = localStorage.getItem("url_temp").split(',');
                $('.js-kw').val(temp[1]);
                $('.js-pn').val(temp[2]);
                $('.js-c1').val(temp[3]);
                if (temp[3] != '0') {
                    $('select[name=product1]').change();
                }
                $('.js-c2').val(temp[4]);
                if (temp[4] != '0') {
                    $('select[name=product2]').change();
                }
                $('.js-c3').val(temp[5]);
                $('.js-manufactor').val(temp[6]);
                $('.js-brand').val(temp[7]);
                $('.js-series').val(temp[8]);
                $('.js-df').val(temp[9]);
                $('.js-dt').val(temp[10]);
                type = temp[0];
                order = temp[11];
                desc = temp[12] == 'true';
            }
            $('.js-modal-upload-file').on('click', function () {
                $('input[name="model-file"]').click();
            });
            //$('input[name="model-file"]').on('change', upload_model_file);
            $('.js-modal-upload-preview').on('click', function () {
                $('input[name="model-preview"]').click();
                console.log($('input[name="model-preview"]'))
            });
            //$('input[name="model-preview"]').on('change', upload_model_preview);

            $(document).on('dblclick', '.modal-body .js-preview-list>div', loadPreviewImg);
            $('div[data-name=previewImg]').on('click', function(){$(this).hide()});
            $('div[data-name=previewImg]>div').hover(function(){
                $('div[data-name=previewImg]').off('click');
                $(document).on('click', 'div[data-name=previewImg]>div', changePreviewImg);
            },function(){
                $('div[data-name=previewImg]').on('click', function(){$(this).hide()});
                $(document).off('click', 'div[data-name=previewImg]>div', changePreviewImg);
            });

            datePickerActive();



            $('.modal').on('show.bs.modal', function(){
                modalTmp = this;
                baseApp.dialogShow(this);
            });

            window.top.$('.tabs-main > div').scroll(function(){
                baseApp.dialogShow(modalTmp);
            })
        }
    }
}();
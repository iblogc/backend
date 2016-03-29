/**
 * Created by yunxia on 2015/12/12.
 */
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
//产品分类 绑定
$('select[name=product1]').bind('change', function () {
    $('select[name=product2]').html('<option value="0">请选择</option>');
    $('select[name=product3]').html('<option value="0">请选择</option>');
    changeSearchLink();
    if($(this).val() == '0')
        return;
    s1_val = $('select[name=product1] :selected').attr('name');
    for (var i = 0; i < category[s1_val].second.length; i++) {
        $('select[name=product2]').append('<option name="' + i + '" value="' + category[s1_val].second[i].id + '">' + category[s1_val].second[i].name + '</option>');
    }
});

$('select[name=product2]').bind('change', function () {
    $('select[name=product3]').html('<option value="0">请选择</option>');
    changeSearchLink();
    if($(this).val() == '0')
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
$('input[sid=Date-created]').bind('change', function () {
    changeSearchLink();
    baseApp.compareDate(document.getElementById('startDate-created'), document.getElementById('endDate-created'));
});

//更新时间 绑定
$('input[sid=Date-update]').bind('change', function () {
    changeSearchLink();
    baseApp.compareDate(document.getElementById('startDate-update'), document.getElementById('endDate-update'));
});

$('#product-Search').bind('change', function () {
    changeSearchLink();
});

$('#select-Search').bind('click', function () {
    changeSearchLink();
    localStorage.setItem('url_temp', kw + ',' + pn + ',' + c1 + ',' + c2 + ',' + c3 + ',' + com + ',' + brand + ',' + series + ',' + date_from + ',' + date_to + ',' + order + ',' + desc);
    location.href = searchUrl;
});

var changeSearchLink = function () {
    kw = $('.js-kw').val();
    pn = $('.js-pn').val();
    c1 = $('.js-c1').val();
    c2 = $('.js-c2').val();
    c3 = $('.js-c3').val();
    com = $('.js-company').val();
    brand = $('.js-brand').val();
    series = $('.js-series').val();
    date_from = $('.js-df').val();
    date_to = $('.js-dt').val();
    var url = '//' + location.host + location.pathname + '?kw=' + kw + '&pn=' + pn + '&c1=' + c1 + '&c2=' + c2 + '&c3=' + c3 + '&c=' + com + '&b=' + brand + '&s=' + series + '&df=' + date_from + '&dt=' + date_to + '&order=' + order + '&desc=' + (desc?1:0);

    localStorage.setItem('lastUrl', 'kw=' + kw + '&pn=' + pn + '&c1=' + c1 + '&c2=' + c2 + '&c3=' + c3 + '&c=' + com + '&b=' + brand + '&s=' + series + '&df=' + date_from + '&dt=' + date_to + '&order=' + order + '&desc=' + (desc?1:0));
    searchUrl = '/product/pdt?kw=' + kw + '&pn=' + pn + '&c1=' + c1 + '&c2=' + c2 + '&c3=' + c3 + '&c=' + com + '&b=' + brand + '&s=' + series + '&df=' + date_from + '&dt=' + date_to + '&order=' + order + '&desc=' + (desc?1:0);
    $('#search-link').attr('href', searchUrl);

};

$('#product-Search').keyup(function (e) {
    if (e.keyCode == 13 && $(this).val() != '') {
        console.log($(this).val());
        $('#select-Search').click();
        $(this).val('');
    }
});

$('.js-header').on('click', function(){
    var order = $(this).attr('name');
    desc = !desc;
    changeSearchLink();
    localStorage.setItem('url_temp', kw + ',' + pn + ',' + c1 + ',' + c2 + ',' + c3 + ',' + com + ',' + brand + ',' + series + ',' + date_from + ',' + date_to + ',' + order + ',' + desc);
    location.href = searchUrl;
});

$('.js-product-detail').on('click', function(){
});

$('.js-active').on('click', function(){
    var id=$(this).attr('data-id');
    $.post('/products/', $this.serialize(), function(data){
                    console.log(typeof data);
                    if(data.result==0){
                        $("button[type=submit]").attr('disabled', true).html('登录成功，正在等跳转...');
                        setTimeout(function(){
                            location.href = '/';
                        }, 2000);
                    }else{
                        sweetAlert("登录失败", "用户名和密码错误，请重新登录", "error");
                    }
                }, 'JSON');
});

var productApp = function () {
    return {
        init: function () {
            $('#product-Search').val('');
            for (var i = 0; i < category.length; i++) {
                $('select[name=product1]').append('<option name="' + i + '" value="' + category[i].id + '">' + category[i].name + '</option>');
            }
            ;
            console.log(localStorage.getItem("url_temp"));
            if (url == localStorage.getItem("lastUrl")) {
                var temp = localStorage.getItem("url_temp").split(',');
                $('.js-kw').val(temp[0]);
                $('.js-pn').val(temp[1]);
                $('.js-c1').val(temp[2]);
                if(temp[2]!='0') {
                    $('select[name=product1]').change();
                }
                $('.js-c2').val(temp[3]);
                if(temp[3]!='0') {
                    $('select[name=product2]').change();
                }
                $('.js-c3').val(temp[4]);
                $('.js-company').val(temp[5]);
                $('.js-brand').val(temp[6]);
                $('.js-series').val(temp[7]);
                $('.js-df').val(temp[8]);
                $('.js-dt').val(temp[9]);
                order = temp[10];
                desc = temp[11] == 'true';
            }
            ;

        },
    }
}();
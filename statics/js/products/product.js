/**
 * Created by yunxia on 2015/12/12.
 */
var s1_val;
var brand_id;
var searchUrl;
var pdt1='';
var pdt2='';
var pdt3='';
var brand='';
var series='';
var sdc='';
var edc='';
var sdu='';
var edu='';
var Search_Key='';
var KeyWord='';

//产品分类 绑定
$('select[name=product1]').bind('change', function () {
    $('select[name=product2]').html('<option>请选择</option>');
    $('select[name=product3]').html('<option>请选择</option>');
    changeSearchLink();
    s1_val = $('select[name=product1] :selected').attr('name');
    for(var i = 0; i < category[s1_val].second.length; i++){
        $('select[name=product2]').append('<option name="'+ i +'" value="' + category[s1_val].second[i].id + '">' + category[s1_val].second[i].name + '</option>');
    }
});

$('select[name=product2]').bind('change', function () {
    $('select[name=product3]').html('<option>请选择</option>');
    changeSearchLink();
    var s2_val = $('select[name=product2] :selected').attr('name');
    for(var i = 0; i < category[s1_val].second[s2_val].third.length; i++){
        $('select[name=product3]').append('<option name="'+ i +'" value="' + category[s1_val].second[s2_val].third[i].id + '">' + category[s1_val].second[s2_val].third[i].name + '</option>');
    }
});

$('select[name=product3]').bind('change', function () {
    changeSearchLink();
});

//品牌系列 绑定
$('select[name=brand]').bind('change', function () {
    $('select[name=series]').html('<option>请选择</option>');
    changeSearchLink();
    brand_id = $('select[name=brand] :selected').attr('name');
    for(var i = 0; i < brand_series[brand_id].series.length; i++){
        $('select[name=series]').append('<option name="'+ i +'" value="' + brand_series[brand_id].series[i].id + '">' + brand_series[brand_id].series[i].name + '</option>')
    }
});

$('select[name=series]').bind('change', function () {
    changeSearchLink();
});

//创建时间 绑定事件
$('input[sid=Date-created]').bind('change',function(){
    changeSearchLink();
    baseApp.compareDate(document.getElementById('startDate-created'),document.getElementById('endDate-created'));
});

//更新时间 绑定
$('input[sid=Date-update]').bind('change',function(){
    changeSearchLink();
    baseApp.compareDate(document.getElementById('startDate-update'),document.getElementById('endDate-update'));
});

$('#product-Search').bind('change',function(){
    changeSearchLink();
});

$('#select-Search').bind('click',function(){
    changeSearchLink();
});

var changeSearchLink = function(){
    pdt1 = $('select[name=product1]').val();
    if(pdt1=="请选择") pdt1='';
    pdt2 = $('select[name=product2]').val();
    if(pdt2=="请选择") pdt2='';
    pdt3 = $('select[name=product3]').val();
    if(pdt3=="请选择") pdt3='';
    brand = $('select[name=brand]').val();
    if(brand=="请选择") brand='';
    series = $('select[name=series]').val();
    if(series=="请选择") series='';
    sdc = $('#startDate-created').val();
    edc = $('#endDate-created').val();
    sdu = $('#startDate-update').val();
    edu = $('#endDate-update').val();
    Search_Key = $('#product-Search').val().trim().split(' ').join(',');
    KeyWord = $('#product-Search').val();
    localStorage.setItem('lastUrl', 'c='+pdt1+','+pdt2+','+pdt3+'&bs='+brand+','+series+'&ct='+sdc+','+edc+'&ut='+sdu+','+edu+'&kw='+Search_Key);
    searchUrl = '/product/pdt?c='+pdt1+','+pdt2+','+pdt3+'&bs='+brand+','+series+'&ct='+sdc+','+edc+'&ut='+sdu+','+edu+'&kw='+Search_Key;
    $('#search-link').attr('href',searchUrl);
};

$('#product-Search').keyup(function(e){
    if(e.keyCode == 13 && $(this).val() != ''){
        console.log($(this).val());
        $('#select-Search').click();
        $(this).val('');
    }
});

$('#select-Search').on('click',function(){
    localStorage.setItem('url_temp',pdt1 + ',' + pdt2 + ',' + pdt3 + ',' +  brand + ',' +  series + ',' +  sdc + ',' +  edc + ',' +  sdu + ',' +  edu + ',' + KeyWord);
})

var productApp = function () {
    return {
        init: function () {
            $('#product-Search').val('');
            for (var i = 0; i < category.length; i++) {
                $('select[name=product1]').append('<option name="'+ i +'" value="' + category[i].id + '">' + category[i].name + '</option>');
            };
            for (var i = 0; i < brand_series.length; i++) {
                $('select[name=brand]').append('<option name="'+ i +'" value="' + brand_series[i].id + '">' + brand_series[i].brand + '</option>');
            };
            if(url == localStorage.getItem("lastUrl")){
                var temp = localStorage.getItem("url_temp").split(',');
                if(temp[0]){
                    $('select[name=product1]').val(temp[0]);
                    $('select[name=product1]').change();
                }
                if(temp[1]){
                    $('select[name=product2]').val(temp[1]);
                    $('select[name=product2]').change();
                }
                if(temp[2]){
                    $('select[name=product3]').val(temp[2]);
                }
                if(temp[3]){
                    $('select[name=brand]').val(temp[3]);
                    $('select[name=brand]').change();
                }
                if(temp[4]){
                    $('select[name=series]').val(temp[4]);
                }
                if(temp[5]){
                    $('#startDate-created').val(temp[5]);
                }
                if(temp[6]){
                    $('#endDate-created').val(temp[6]);
                }
                if(temp[7]){
                    $('#startDate-update').val(temp[7]);
                }
                if(temp[8]){
                    $('#endDate-update').val(temp[8]);
                }
                if(temp[9]){
                    $('#product-Search').val(temp[9]);
                }
            };
        },
    }
}();
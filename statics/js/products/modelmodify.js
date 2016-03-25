/**
 * Created by yunxia on 2015/12/30.
 */

var index = 0;
var imgIndex = 0;
var files = [];
var imgFiles = [];
var viewFile;

//模型文件
$('#addModel').bind('click',function(){
    $('#addModelInput').click();
});

$('#addModelInput').bind('change',function(){
    var f = document.querySelector("#addModelInput").files;
    for(var i = 0; i < f.length; i++){
        var filesName = f[i].name;
        var num = f[i].size/1024;
        var filesSize = '&nbsp;&nbsp;&nbsp;&nbsp;('+ num.toFixed(2) + 'K)';
        var html = '<li sid=' + index + '>'+ filesName + filesSize +'<span class="deleteModel_span">&nbsp;&nbsp;&nbsp;<img src="/statics/imgs/icon/delete.png"></span></li>';
        $('#addModelUl').append(html);
        files.push(f[i]);
        index++;
    }
    changeClass();
});

$(document).on('click','.deleteModel_span',function(){
    var obj = $(this).parent();
    var i = obj.attr('sid');
    var temp = i;
    $(obj).nextAll().each(function(){
        $(this).attr('sid',i);
        i++;
    });
    files.splice(temp,1);
    obj.remove();
    changeClass();
});

//贴图文件
$('#addModelImg').bind('click',function(){
    $('#addModelImgInput').click();
});

$('#addModelImgInput').bind('change',function(){
    var f = document.querySelector("#addModelImgInput").files;
    for(var i = 0; i < f.length; i++){
        if(f[i].type.indexOf('image')==0){
            imgFiles.push(f[i]);
            var windowURL = window.URL || window.webkitURL;
            var dataURL = windowURL.createObjectURL(f[i]);
            var html = '<img name="modelImg" src="'+ dataURL +'" sid=' + imgIndex + '>';
            $('#addModelImg-box').append(html);
            //var fr = new FileReader();
            //fr.readAsDataURL(f[i]);
            //fr.onload = function(e){
            //    var img = new Image();
            //    img.src = e.target.result;
            //    $('#addModelImg-box').append(img);
            //}
        }else{
            alert('请确认 '+ f[i].name +' 的文件格式，本次未添加');
        }
        imgIndex++;
    }
});

$(document).on('click','img[name=modelImg]',function(){
    var obj = $(this);
    var i = obj.attr('sid');
    var temp = i;
    $(obj).nextAll().each(function(){
        $(this).attr('sid',i);
        i++;
    })
    imgFiles.splice(temp,1);
    obj.remove();
})

//模型预览
$('#addModelView').bind('click',function(){
    $('#addModelViewInput').click();
});

$('#addModelViewInput').bind('change',function(){
    viewFile = document.querySelector("#addModelViewInput").files[0];
    if(viewFile.type.indexOf('image')==0){
        var windowURL = window.URL || window.webkitURL;
        var dataURL = windowURL.createObjectURL(viewFile);
        document.getElementById('viewImg').src = dataURL;
    }else{
        alert('请确认 '+ viewFile.name +' 的文件格式，本次未添加');
    }
});

//ajax
$('#inputModel').bind('click', function(){
    var fd = new FormData();
    for(var i = 0; i <files.length; i++){
        console.log(i+'--------');
        fd.append('model',files[i]);
    }
    for(var i = 0; i <imgFiles.length; i++){
        console.log(i+'--------');
        fd.append('model-img',imgFiles[i]);
    }
    fd.append('model-view',viewFile);
    $.ajax({
        url: '/product/pdt/test',
        type: 'POST',
        data: fd,
        async: true,
        processData: false,
        contentType: false,

        success:function(obj){
            console.log(obj)
        }
    });
});

var changeClass = function(){
    var repeat = [];
    var flag = true;
    $('#addModelUl li').each(function(){
        $(this).removeClass('repeat_Li');
    })
    for(var i = 0; i < files.length - 1; i++){
        for(var j = i + 1; j < files.length; j++){
            if(files[j].name == files[i].name){
                repeat.push(i);
                repeat.push(j);
            }else{
            }
        }
    }
    for(var i = 0; i < repeat.length;i++){
        if(repeat.length != 0){
            flag = false;
            $('#addModelUl').children(':eq('+repeat[i]+')').addClass('repeat_Li');
        }
    }
    if(flag){
        $('#model-error-msg').attr('style','display: none;')
    }else{
        $('#model-error-msg').attr('style','display: inline-block;color:red')
    }
}

var modelmodifyApp = function () {
    return {
        init: function () {

        },
    }
}();
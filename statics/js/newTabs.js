/**
 * Created by yunxia on 16-3-31.
 */


var newTabs = function () {
    var tabsIdArr = new Array;

    var resizeFun = function(){
        $('.content-body>.tabs-main>div').css({height : (window.innerHeight - 160) + 'px'})
    };

    var resizeIframe = function(){
        var tmp = $(this).contents().find('div.main-body').height() - 20;
        $(this).height(tmp);
    };

    $(window).resize(function () {
        resizeFun($('iframe.show'));
    });
    return {
        init: function () {
            $('.js-parent-menu').on('click', function () {
                if ($(this).parent().hasClass('actived')){
                    $(this).parent().removeClass('actived');
                }else{
                    $(this).parent().addClass('actived');
                }
            });

            $('.js-sub-menu').on('click', function () {
                var flag = false;
                var url = $(this).attr('data-url');
                var name = $(this).find('.menu-name').html();
                var id = $(this).find('.menu-name').attr('data-id');
                for(var x in tabsIdArr){
                    if(tabsIdArr[x] == id) flag = true;
                }
                if (url != undefined) {
                    //if ($('.content-body>.tabs-title>div[data-name]').tabs('exists', name)) {
                    if(flag) {
                        $('.content-body>.tabs-title>div[data-name=' + id + ']').addClass('selected').siblings().removeClass('selected');
                        $('.content-body>.tabs-main>div>iframe[data-for=' + id + ']').addClass('show').siblings().removeClass('show');
                    } else {
                        tabsIdArr.push(id);
                        var content = '<iframe scrolling="auto" style="min-width: 1310px" frameborder="0" class="show"  src="' + url + '" data-for="' + id + '"></iframe>';
                        var contentTitle = '<div class="selected" data-name="' + id + '">&nbsp;&nbsp;&nbsp;&nbsp;' + name + '&nbsp;&nbsp;&nbsp;&nbsp;<span class="close-btn"></span></div>';
                        $('.content-body>.tabs-title>div[data-name]').removeClass('selected');
                        $('.content-body>.tabs-main>div>iframe[data-for]').removeClass('show');
                        $('.content-body>.tabs-title').append(contentTitle);
                        $('.content-body>.tabs-main>div').append(content);
                        resizeFun();
                        $('iframe[data-for=' + id + ']').load(resizeIframe);
                        //$(window.parent.document).find('iframe[data-for=' + id + ']').load(function(){
                        //    var main = $(window.parent.document).find('iframe[data-for=' + id + ']');
                        //    var mainheight = $(document).height() - 120;
                        //    main.height(mainheight);
                        //});
                    }
                }
            });

            $(document).on('click', '.content-body>.tabs-title>div[data-name]', function(){
                $(this).addClass('selected').siblings().removeClass('selected');
                $('.content-body>.tabs-main>div>iframe[data-for=' + $(this).attr('data-name') + ']').addClass('show').siblings().removeClass('show');
            });

            $(document).on('click', '.content-body>.tabs-title>div[data-name]>span', function(){
                var temp = $(this.parentNode).attr('data-name');
                var tmp;
                for(var x in tabsIdArr) {
                    if(tabsIdArr[x] == temp){
                        tmp = x;
                        break;
                    }
                }
                tabsIdArr.splice(x,1);
                if($(this.parentNode).attr('class') == 'selected'){
                    if($(this.parentNode).next().length > 0){
                        $(this.parentNode).next().addClass('selected');
                        $('.content-body>.tabs-main>div>iframe[data-for=' + $(this.parentNode).next().attr('data-name') + ']').addClass('show');
                    } else if ($(this.parentNode).prev().length > 0){
                        $(this.parentNode).prev().addClass('selected');
                        $('.content-body>.tabs-main>div>iframe[data-for=' + $(this.parentNode).prev().attr('data-name') + ']').addClass('show');
                    }
                }
                $(this.parentNode).remove();
                $('.content-body>.tabs-main>div>iframe[data-for=' + temp + ']').remove();
            });
        }
    }
}();

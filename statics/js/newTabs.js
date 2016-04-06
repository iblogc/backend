/**
 * Created by yunxia on 16-3-31.
 */


var newTabs = function () {
    var tabsIdArr = new Array;

    var tabHistory = new Array;

    var resizeFun = function(){
        $('.content-body>.tabs-main>div').css({height : (window.innerHeight - 160) + 'px'})
    };

    var resizeIframe = function(){
        var tmp = $(this).contents().find('div.main-body').height();
        $(this).height(tmp);
    };

    var tabActive = function(tabs, num){
        var thisTab = tabs.selector;
        var tmp = $(thisTab + ' .tab-main>div');
        for(var i = 1; i < tmp.length; i++){$(tmp[i]).hide()}
        $(document).on('click', thisTab + '>.tab-title>div', function(){
            var index = $(this).index();
            var cssArr = [{left:'-50px', opacity:'0'}, {left:'0px', opacity:'1'}, {left:'5  0px', opacity:'0'}];
            var tmpDom1 = 'div[data-name=' + $(this.parentNode.parentNode).attr('data-name') + ']>:eq(1)>:eq(' + tabHistory[num] + ')';
            var tmpDom2 = 'div[data-name=' + $(this.parentNode.parentNode).attr('data-name') + ']>:eq(1)>:eq(' + index + ')';
            if(index > tabHistory[num]) {
                var tmp = cssArr[2]; cssArr[2] = cssArr[0]; cssArr[0] = tmp;
            } else if(index == tabHistory[num]) {
                return;
            }
            $(tmpDom1).animate(cssArr[2], 100).hide(100);
            $(tmpDom2).css(cssArr[0]).show().animate(cssArr[1], 100);
            $(this).addClass('selected').siblings().removeClass('selected');
            tabHistory[num] = index;
        })
    };

    $(window).resize(function () {
        resizeFun($('iframe.show'));
    });

    var allowDrop =function(ev) {
        ev.preventDefault();
    };

    var drop = function(ev) {
        ev.preventDefault();
        var data=ev.dataTransfer.getData("Text");
        if(!$(ev.target).hasClass('tabs-title')) return;
        ev.target.appendChild($('.content-body>.tabs-title div[data-name=' + data + ']')[0]);
    };

    var appendDrop = function(){
        $('.content-body>.tabs-title')[0].ondrop = function(ev){
            drop(ev);
        };

        $('.content-body>.tabs-title')[0].ondragover = function(ev){
            allowDrop(ev);
        };

        var XTabs = $('.content-body>.tabs-title div[data-name]');
        var Ltabs = XTabs.length;
        for (var i=0; i<Ltabs; i++) {
            XTabs[i].onselectstart = function() {
                return false;
            };
            XTabs[i].ondragstart = function(ev) {
                ev.dataTransfer.effectAllowed = "move";
                ev.dataTransfer.setData("text", $(ev.target).attr('data-name'));
                ev.dataTransfer.setDragImage(ev.target, 0, 0);
                eleDrag = ev.target;
                return true;
            };
            XTabs[i].ondragend = function(ev) {
                /*拖拽结束*/
                ev.dataTransfer.clearData("text");
                eleDrag = null;
                return false
            };
        }
    };

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
                    if(flag) {
                        $('.content-body>.tabs-title>div[data-name=' + id + ']').addClass('selected').siblings().removeClass('selected');
                        $('.content-body>.tabs-main>div>iframe[data-for=' + id + ']').addClass('show').siblings().removeClass('show');
                    } else {
                        tabsIdArr.push(id);
                        var content = '<iframe scrolling="auto" style="min-width: 1310px" frameborder="0" class="show"  src="' + url + '" data-for="' + id + '"></iframe>';
                        var contentTitle = '<div draggable="true" class="selected" data-name="' + id + '">&nbsp;&nbsp;&nbsp;&nbsp;' + name + '&nbsp;&nbsp;&nbsp;&nbsp;<span class="close-btn"></span></div>';
                        $('.content-body>.tabs-title>div[data-name]').removeClass('selected');
                        $('.content-body>.tabs-main>div>iframe[data-for]').removeClass('show');
                        $('.content-body>.tabs-title').append(contentTitle);
                        $('.content-body>.tabs-main>div').append(content);
                        resizeFun();
                        $('iframe[data-for=' + id + ']').load(resizeIframe);
                        appendDrop();
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
        },

        iTab: function(domArr){
            var arr = domArr;
            for(var i = 0; i < arr.length; i++) {
                tabActive($('div[data-name=' + $(arr[i]).attr('data-name') + ']'), $(arr[i]).index());
                tabHistory[i] = 0;
            }
        },

        changeSize: function(height, obj){
            obj.height(height);
        }
    }
}();
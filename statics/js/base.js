/**
 * Created by hxhuang on 15-10-22.
 */
var baseApp = function () {

    var openLeftMenu = function () {
        $('div.left-menu-icon > a').click(function () {
            if ($('body.body-normal').hasClass('left-menu-open')) {
                $('body.body-normal').removeClass('left-menu-open');
                $.cookie('_LeftMenuOpen_', '', {path: "/", expires: -10})
            } else {
                $('body.body-normal').addClass('left-menu-open');
                $.cookie('_LeftMenuOpen_', 'true', {path: "/"})
            }
        });

    };

    var accountTopMenu = function () {
        $('.dropdown-toggle').dropdown();
    }

    var publicTooltip = function () {
        $('[data-toggle=tooltip]').tooltip({
            container: $('body')
        });
    };

    var onMouseOverActive = function () {
        $('div.content-table-data').mouseenter(function () {
            $(this).addClass('table-mouse-over');
        });
        $('div.content-table-data').mouseleave(function () {
            $(this).removeClass('table-mouse-over');
        })
    };

    var accountLocked = function () {
        $('div.account-lock-tag > a').click(function () {
            var workId = 0;
            $('body').append('<div class="locked-screen-overly"></div>');
            $('div.locked-screen-overly').css('height', $('body, html').height()).show();
            $(window).resize(function () {
                $('div.locked-screen-overly').css('height', $('body, html').height())
            });

            $.get('/users/lock', function (data) {
                if (data.result == 0) workId = data.data;
            }, 'JSON');

            swal({
                title: '',
                text: '<span class="unlock-icon"><span class="fa fa-unlock-alt"></span></span><br /><br /><input type="password" name="password" placeholder="填写登录密码" style="display:block;" />',
                html: true,
                closeOnConfirm: false
            }, function () {
                if ($('input[type=password]').val() == '') {
                    swal.showInputError('请填写登录密码');
                    return false;
                } else {
                    var password = md5($('input[type=password]').val());
                    $.post('/users/unlock', {
                        username: workId,
                        password: password
                    }, function (data) {
                        if (data.result == 0) {
                            // location.href = '/';
                            $('div.locked-screen-overly').remove();
                            swal.close()
                        } else {
                            swal.showInputError('密码');
                        }
                    }, 'JSON');
                }
            });
        });
    };




    var headerClock = function () {
        var time = new Date();
        var yr = time.getFullYear();
        var month = time.getMonth();
        var dt = time.getDate();
        var h = time.getHours();
        var min = time.getMinutes();

        month++;
        if (h < 10) h = '0' + h;
        if (min < 10) min = '0' + min;

        var week = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
        var formatTime = week[time.getDay()] + '&nbsp;,&nbsp;' + yr + '/' + month + '/' + dt + '<span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>' + h + ':' + min;

        $('#clock').html(formatTime);
    };

    var resizeFun = function () {
        var innerH = window.innerHeight - 130;
        $('.content-body').css({height: innerH + 'px'});
        $('.content-body .tabs-main>div').css({height: (innerH - 30) + 'px'});
        var copyR = window.innerWidth / 2 - $('#copyRight').width() / 2;
        $('#copyRight').attr('style', 'right:' + copyR + 'px');
        $('.left-menu-body').height(innerH + 50);
    };

    $(window).resize(function () {
        resizeFun();
    });

    var params = {
        left: 0,
        top: 0,
        currentX: 0,
        currentY: 0,
        flag: false
    };

    var getCss = function(o,key){
        return o.currentStyle? o.currentStyle[key] : document.defaultView.getComputedStyle(o,false)[key];
    };

    var startDrag = function(bar, target, callback){
        if(getCss(target, "left") !== "auto"){
            params.left = getCss(target, "left");
        }
        if(getCss(target, "top") !== "auto"){
            params.top = getCss(target, "top");
        }
        bar.onmousedown = function(event){
            params.flag = true;
            if(!event){
                event = window.event;
                bar.onselectstart = function(){
                    return false;
                }
            }
            var e = event;
            params.currentX = e.clientX;
            params.currentY = e.clientY;
        };
        document.onmouseup = function(){
            params.flag = false;
            if(getCss(target, "left") !== "auto"){
                params.left = getCss(target, "left");
            }
            if(getCss(target, "top") !== "auto"){
                params.top = getCss(target, "top");
            }
        };
        document.onmousemove = function(event){
            var e = event ? event: window.event;
            if(params.flag){
                var nowX = e.clientX, nowY = e.clientY;
                var disX = nowX - params.currentX, disY = nowY - params.currentY;
                target.style.left = parseInt(params.left) + disX + "px";
                target.style.top = parseInt(params.top) + disY + "px";
            }

            if (typeof callback == "function") {
                callback(parseInt(params.left) + disX, parseInt(params.top) + disY);
            }
        }
    };

    return {
        init: function () {
            // left menu bar
            openLeftMenu();
            // account menu
            accountTopMenu();
            onMouseOverActive();

            publicTooltip();

            accountLocked();

            headerClock();
            setInterval(function () {
                return headerClock();
            }, 500);
            resizeFun();
        },

        changeSize: function (height) {
            newTabs.changeSize(height, window.top.$('.tabs-main>div>iframe.show'))
        },

        dialogShow: function(obj){
            var tmp = eval(window.top.$('.tabs-main > div').scrollTop()) + 40;
            $($(obj).children()[0]).css('margin-top', tmp +'px');
        },

        startDrag: function(bar, target, callback){
            startDrag(bar, target, callback);
        }

        //compareDate: function (s, e) {
        //    var start = $(s);
        //    var end = $(e);
        //    if(start.val() != '' && end.val() == ''){
        //        end.datetimepicker('setStartDate', start.val());
        //    };
        //    //if (start.val() != '' && end.val() != '') {
        //    //    var a = new Date(start.val());
        //    //    var b = new Date(end.val());
        //    //    if( a > b ){
        //    //        var temp = start.val();
        //    //        start.val(end.val());
        //    //        end.val(temp);
        //    //    }
        //    //}
        //},
        //pickDate: function (obj) {
        //    $(obj).datetimepicker({
        //        language: 'zh-CN',
        //        weekStart: 1,
        //        todayBtn: 1,
        //        autoclose: 1,
        //        todayHighlight: 1,
        //        startView: 2,
        //        minView: 2,
        //        forceParse: 0,
        //    });
        //},


    }
}();


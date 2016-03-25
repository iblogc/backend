/**
 * Created by yunxia on 2015/12/14.
 */

//创建时间 绑定事件
$('input[sid=Date-created]').bind('change',function(){
    baseApp.compareDate(document.getElementById('startDate-created'),document.getElementById('endDate-created'));
});

//更新时间 绑定
$('input[sid=Date-update]').bind('change',function(){
    baseApp.compareDate(document.getElementById('startDate-update'),document.getElementById('endDate-update'));
});

var modelApp = function () {
    return {
        init: function () {

        },
    }
}();
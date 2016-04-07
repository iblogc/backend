/**
 * Created by yunxia on 2016/1/12.
 */

var managerApp = function(){

    return {

        init: function(){
            //创建时间 绑定事件
            $('input[sid=Date-created]').bind('change',function(){
                baseApp.compareDate(document.getElementById('startDate-created'),document.getElementById('endDate-created'));
            });
            $('div.bottom-content').bind('mouseover',function(e){
                $(this).addClass('bottom-content-mouseover');
            });
            $('div.bottom-content').bind('mouseout',function(){
                $(this).remove('bottom-content-mouseover');
            });
        }

    }

}();
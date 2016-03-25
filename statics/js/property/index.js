/**
 * Created by yunxia on 2016/3/1.
 */

var adminsIndexApp = function(){
    return {
        init:function(){
            $('input[name=checkAll]').bind('click',function(){
                var flag = this.checked;
                $('input[name=list-check]').each(function(){
                    this.checked = flag;
                })
            });

            $('span[name=delete]').on('click',function(){
                console.log('删除');
                //$(this).parentNode.parentNode.remove()
                $(this).parent().parent().parent()[0].remove()
            });

            $('div[data-group=info]').on('mouseover',function(){
                $(this).addClass('mouse-over');
            });

            $('div[data-group=info]').on('mouseout',function(){
                $(this).removeClass('mouse-over');
            });
        }
    }
}();
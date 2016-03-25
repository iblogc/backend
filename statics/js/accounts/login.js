/**
 * Created by hxhuang on 15-10-22.
 */
var loginApp = function(){



    return {
        init: function(){
            $('form#loginForms').submit(function(){
                var $this = $(this);
                var url = $this.attr('action');
                $('input[name=password]').val(md5($('input[name=password]').val()));

                $.post(url, $this.serialize(), function(data){
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
                return false;
            });
        }
    }
}();

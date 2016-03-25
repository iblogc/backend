/**
 * Created by yunxia on 2016/1/12.
 */

var managerAddApp = function(){
    var addAccount = function (){
        var fd = new FormData();
        var account = $('input[data-id=account]').val();
        var pwd = $('input[data-id=pwd]').val();
        var pwd2 = $('input[data-id=pwd2]').val();
        var name = $('input[data-id=name]').val();
        if(name !='' && pwd != '' && name !='' && pwd == pwd2){
            var mobile = $('input[data-id=mobile]').val();
            var email = $('input[data-id=email]').val();
            var department = $('input[data-id=department]').val();
            fd.append('account',account);
            fd.append('pwd',pwd);
            fd.append('name',name);
            fd.append('mobile',mobile);
            fd.append('email',email);
            fd.append('department',department);
            $.ajax({
                url: '/admin/manager/add',
                type: 'POST',
                data: fd,
                async: true,
                processData: false,
                contentType: false,
                success:function(){

                }
            })
        }else{
            console.log('Error');
        }
    };

    return {
        init: function(){
            $('#save').on('click',function(){
                addAccount();
            })
        },
    }
}();
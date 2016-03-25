var attributeApp = function () {
    return {
        init: function () {
            var flag = '';
            var type;
            var tempValue = '';

            $('tr.children').toggle();

            $('div#attraddFromDialog').on('show.bs.modal', function (e) {
                var cid = $(e.relatedTarget).attr('data-categoryId');
                var _this = $(this);

                $.get('/product/category/addattr?id=' + cid, function (data) {
                    _this.find('.modal-body').html(data);
                })
            });

            $('div#attraddFromDialog').on('hide.bs.modal',function(){
                window.location.reload();
            });

            $('div#valueaddFromDialog').on('show.bs.modal', function (e) {
                var aid = $(e.relatedTarget).attr('data-AttrId');
                var pid = $(e.relatedTarget).attr('data-ValId');
                var _this = $(this);
                type = $(e.relatedTarget).attr('data-type');
                //$.get('/product/category/attr/valadd?aid=' + aid + '&' + "pid=" + pid, function (data) {
                 //   _this.find('.modal-body').html(data);
                //}, 'html');
                $.ajax({
                   url:'/product/category/attr/valadd?aid=' + aid + '&' + "pid=" + pid,
                    type: 'get',
                    dataType: 'html',
                    success:function (data) {
                        _this.find('.modal-body').html(data);
                        if(type == 'text'){
                            $('span[name=add-list-item]').remove();
                            $('span[name=up-list-item]').remove();
                            $('span[name=down-list-item]').remove();
                            $('span[name=del-list-item]').remove();
                        };
                    }
                });
            });

            $('div#valueaddFromDialog').on('hide.bs.modal',function(){
                window.location.reload();
            });

            $('div#attrdelFromDialog').on('show.bs.modal', function (e) {
                var cid = $(e.relatedTarget).attr('data-categoryId');
                var attr_id = $(e.relatedTarget).attr('data-AttrId');
                var _this = $(this);
                $('#attrsetFromDialog').modal('hide');
                $.get('/product/category/delattr?id=' + attr_id + '&' + 'cid=' + cid, function (data) {
                    _this.find('.modal-body').html(data);
                })
            });

            $('div#attrdelFromDialog').on('hide.bs.modal',function(){
                window.location.reload();
            });

            $("select[name=attr-default]").bind("change", function(e){
                var aid = $(e.target).data()['aid'];
                var val = $(e.target).val();

                $.ajax({
                    url:"/product/category/attr/updatedefault/",
                    type:'post',
                    data:{
                        "attribute_id":aid,
                        "value":val
                    },
                    success : function(data){
                        if (data.result != 0){
                            alert('default change fail')
                        }else{

                        }
                    }
                })

            });

            $('div.tab_box > div').hide();
            $('div.tab_box > div').eq(0).show();

            $('span.span-value').bind('click',function(){
                var temp = $(this).attr("data-target")
                $('tr[data-id=pid-'+ temp +']').toggle();
                if($(this).html()=='展开属性'){
                    $(this).html('收起属性');
                }else{
                    $(this).html('展开属性');
                }
            });

            $('.modal-content').on('click','input[name=editAttr]',function(e){
                $('input[name=editAttr]').removeClass('selected-list-item');
                $(e.target).addClass('selected-list-item');
                flag = e.target;
            });

            $('.modal-content').on('click','span[name=edit-list-item]',function(e){
                if(flag!=''){
                    $(flag).removeAttr('readonly');
                    $(flag).select();
                    $(flag).addClass('edit-list-item');
                    $('span[sid=' + $(flag).attr('sid') + ']').removeClass('hidden');
                    tempValue = $(flag).val().trim();
                }
            });

            $('.modal-content').on('click','span[name=add-list-item]',function(e){
                var html = '<input name="newAttr" class="list-group-item edit-list-item"><span name="span-newAttr" class="span-edit-item list-group-item right">确定</span>';
                $('#newAttr-list').append(html);
            });

            $('.modal-content').on('click','span[name=del-list-item]',function(e){
                if(flag!=''){
                    attributeApp.attrvaldel(flag);
                    $(flag).next().remove();
                    $(flag).remove();
                }
                flag = '';
            });

            $('.modal-content').on('keyup','input[name=editAttr]',function(e){
                if(tempValue != $(e.target).val().trim()){
                    attributeApp.attr_val_change($(e.target).val().trim());
                }
            });

            $('.modal-content').on('keyup','input[name=newAttr]',function(e){
                attributeApp.attr_val_change($(e.target).val().trim());
            });

            $('.modal-content').on('click','span[name=span-modifyAttr]',function(e){
                attributeApp.modifyvalue($(e.target).prev().val().trim(),$(e.target),tempValue,type);
            });

            $('.modal-content').on('click','span[name=span-newAttr]',function(e){
                attributeApp.addvalue($(e.target).prev().val().trim(),$(e.target));
            });
        },

        del_attr: function () {
            var aid = document.getElementById('modal_data_attrdel_id').value;

            $.ajax({
                url: '/product/category/delattr',
                type: 'POST',
                data: {"attr_id": aid},
                success: function (data) {
                    resp = eval('(' + data + ')');
                    if (resp.result != 0) {
                        alert("del Wrong");
                    } else {
                        window.location.reload();
                    }
                }
            });
        },

        attrvaldel: function ( tag ) {
            var val_id = $(tag).attr('sid');
            $.ajax({
                url: "/product/category/attr/valdel",
                type: "POST",
                data: {"val_id": val_id},
                success: function (data) {
                    if (data.result != 0) {
                        alert("del val wrong");
                    } else {

                    }
                }
            })
        },

        attr_name_change: function () {
            var elem = document.getElementById('modal-data-attradd').elements;
            var attr_name = elem['attr-name'].value;
            var attr_name_repeat = document.getElementById('attr-name-repeat');
            var cid = $('input[name=id]').attr('value');
            var post_data = {
                "cid": cid,
                "attr_name": attr_name,
                "attr_type": 'no'
            };
            $.ajax({
                url: "/product/category/addattr",
                type: "post",
                data: post_data,
                success: function (resp) {
                    if (resp.result == 2) {
                        attr_name_repeat.textContent = "类别名称已存在！";
                    } else {
                        attr_name_repeat.textContent = "";
                    }
                }
            });
        },

        attr_val_change: function ( val ) {
            var attrval_name = val;
            var attr_val_repeat = document.getElementById('attr-val-repeat');
            var aid = $('input[name=aid]').attr('value');
            var post_data = {
                "aid": aid,
                "attrval_name": attrval_name,
                "msg": "existcheck"
            };
            $.ajax({
                url: "/product/category/attr/valadd",
                type: "post",
                data: post_data,
                success: function (resp) {
                    if (resp.result == 2) {
                        attr_val_repeat.textContent = "类别名称已存在！";
                    } else {
                        attr_val_repeat.textContent = "";
                    }
                }
            });
        },

        addattr: function () {
            var elem = document.getElementById('modal-data-attradd').elements;

            var cid = $('input[name=id]').attr('value');
            var name = elem['attr-name'].value;
            var attr_type = elem['attr-type'].value;
            var attr_cansearch = elem['attr-cansearch'].value;
            var attr_default = elem['attr-default'].value;

            var post_data = {
                "cid": cid,
                "attr_name": name,
                "attr_type": attr_type,
                "attr_issearch": attr_cansearch,
                "attr_default": attr_default
            };

            $.ajax({
                url: "/product/category/addattr",
                type: "post",
                data: post_data,
                success: function (resp) {
                    if (resp.result == 2) {
                        alert("attr name exists");
                    } else {
                        window.location.reload();
                    }
                }
            })
        },

        addvalue: function ( val , tag ) {
            var attrval_name = val;
            var aid = $('input[name=aid]').attr('value');
            var pid = $('input[name=pid]').attr('value');
            var post_data = {
                "aid": aid,
                "attrval_name": attrval_name,
                "pid": pid,
                "msg": "haha"
            };
            $.ajax({
                url: "/product/category/attr/valadd",
                type: "post",
                data: post_data,
                success: function (resp) {
                    if (resp.result == 2) {
                        alert("attr value 已存在！");
                    } else {
                        var html = '<input name="editAttr" type="text" class="list-group-item" sid="' + resp.data.valid + '" value="' + val + '" readonly><span name="span-modifyAttr" sid="' + resp.data.valid + '" class="span-edit-item list-group-item right hidden">确定</span>';
                        $('#Attr-list').append(html);
                        tag.prev().remove();
                        tag.remove();
                    }
                }
            });
        },

        modifyvalue: function ( val , tag , temp , type ){
            var id = tag.attr('sid');
            var aid = $('input[name=aid]').attr('value');
            if(temp != val){
                var post_data = {
                    'id': id,
                    'name': val,
                    'type': type,
                    'check': '',
                    'aid': aid
                };
                $.ajax({
                    url: '/product/category/attr/valmodify',
                    type: 'post',
                    data: post_data,
                    success:function(resp){
                        if(resp.result == 2){
                            alert('数据已存在！');
                            tag.prev().val(temp);
                        }else if(resp.result == 0){

                        }
                    }
                })
            }
            tag.prev().attr('readonly','readonly').removeClass('edit-list-item').removeClass('selected-list-item');
            tag.addClass('hidden');
            $('#attr-val-repeat').html('');
        },

        canseach_change: function ( obj ) {
            var aid = $(obj).data()['aid'];
            var value = $('select[name=attr-cansearch][data-aid=' + aid + '] option:selected').val();

            $.ajax({
                url: "/product/category/attr/search/",
                type: "POST",
                data: {"id": aid, "value": value},
                success: function () {
                    window.location.reload();
                }
            })
        }
    };

}();

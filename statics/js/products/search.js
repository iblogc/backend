var ruleApp = function () {
    return {
        init: function () {
            var flag = '';
            var tempValue = '';

            $('tr.children').toggle();

            $('div#ruleadd').on('show.bs.modal', function (e) {
                var cid = $(e.relatedTarget).attr('data-categoryId');
                var _this = $(this);

                $.get('/product/category/addrule?id=' + cid, function (data) {
                    _this.find('.modal-body').html(data);
                })
            });

            $('div#ruleadd').on('hide.bs.modal', function (e) {
                window.location.reload();
            });

            $('div#descriptionadd').on('show.bs.modal', function (e) {
                var sid = $(e.relatedTarget).attr('data-ruleId');
                var _this = $(this);

                $.get('/product/category/rule/valadd?sid=' + sid, function (data) {
                    _this.find('.modal-body').html(data);
                })
            });

            $('div#descriptionadd').on('hide.bs.modal', function (e) {
                window.location.reload();
            });

            $('div#descriptiondel').on('show.bs.modal', function (e) {
                var cid = $(e.relatedTarget).attr('data-categoryId');
                var attr_id = $(e.relatedTarget).attr('data-AttrId');
                var _this = $(this);
                $('#attrsetFromDialog').modal('hide');
                $.get('/product/category/delattr?id=' + attr_id + '&' + 'cid=' + cid, function (data) {
                    _this.find('.modal-body').html(data);
                })
            });

            $('div#descriptiondel').on('hide.bs.modal', function (e) {
                window.location.reload();
            });

            $('div.tab_box > div').hide();
            $('div.tab_box > div').eq(1).show();

            $('span.span-desc').bind('click',function(){
                var temp = $(this).attr("data-target")
                $('tr[data-id=pid-'+ temp +']').toggle();
                if($(this).html()=='展开属性'){
                    $(this).html('收起属性');
                }else{
                    $(this).html('展开属性');
                }
            });

            $('.modal-content').on('click','input[name=editRuleVal]',function(e){
                $('input[name=editRuleVal]').removeClass('selected-list-item');
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
                var html = '<input name="newRuleVal" class="list-group-item edit-list-item"><span name="span-newRuleVal" class="span-edit-item list-group-item right">确定</span>';
                $('#newRuleVal-list').append(html);
            });

            $('.modal-content').on('click','span[name=del-list-item]',function(e){
                if(flag!=''){
                    ruleApp.rulevaldel(flag);
                    $(flag).next().remove();
                    $(flag).remove();
                }
                flag = '';
            });

            $('.modal-content').on('keyup','input[name=editRuleVal]',function(e){
                if(tempValue != $(e.target).val().trim()){
                    ruleApp.rule_val_change($(e.target).val().trim());
                }
            });

            $('.modal-content').on('keyup','input[name=newRuleVal]',function(e){
                ruleApp.rule_val_change($(e.target).val().trim());
            });

            $('.modal-content').on('click','span[name=span-modifyRuleVal]',function(e){
                ruleApp.modifyvalue($(e.target).prev().val().trim(),$(e.target),tempValue);
            });

            $('.modal-content').on('click','span[name=span-newRuleVal]',function(e){
                ruleApp.addvalue($(e.target).prev().val().trim(),$(e.target));
            });
        },

        del_rule: function (e) {
            var sid = $(e).data()['ruleid'];
            $.ajax({
                url: '/product/category/delrule',
                type: 'POST',
                data: {"rule_id": sid},
                success: function (data) {
                    if (data.result != 0) {
                        alert("del Wrong");
                    } else {
                        window.location.reload();
                    }
                }
            });
        },

        rulevaldel: function (tag) {
            var val_id = $(tag).attr('sid');
            $.ajax({
                url: "/product/category/rule/valdel",
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

        rule_name_change: function () {
            var elem = document.getElementById('modal-data-ruleadd').elements;
            var rule_name = elem['rule-name'].value;
            var rule_name_repeat = document.getElementById('rule-name-repeat');
            var cid = $('input[name=id]').attr('value');
            var post_data = {
                "cid": cid,
                "rule_name": rule_name,
                "rule_type": 'no'
            };
            $.ajax({
                url: "/product/category/addrule",
                type: "post",
                data: post_data,
                success: function (resp) {
                    if (resp.result == 2) {
                        rule_name_repeat.textContent = "类别名称已存在！";
                    } else {
                        rule_name_repeat.textContent = "";
                    }
                }
            });
        },

        rule_val_change: function (val) {
            var ruleval_name = val;
            var rule_val_repeat = document.getElementById('rule-val-repeat');
            var sid = $('input[name=sid]').attr('value');
            var post_data = {
                "sid": sid,
                "ruleval_name": ruleval_name,
                "check": "existcheck"
            };
            $.ajax({
                url: "/product/category/rule/valadd",
                type: "post",
                data: post_data,
                success: function (resp) {
                    if (resp.result == 2) {
                        rule_val_repeat.textContent = "rule val 已存在！";
                    } else {
                        rule_val_repeat.textContent = "";
                    }
                }
            });
        },

        addrule: function () {
            var elem = document.getElementById('modal-data-ruleadd').elements;

            var cid = $('input[name=id]').attr('value');
            var name = elem['rule-name'].value;

            var post_data = {
                "cid": cid,
                "rule_name": name,
                "rule_type": 'sunny'
            };

            $.ajax({
                url: "/product/category/addrule",
                type: "post",
                data: post_data,
                success: function (resp) {
                    if (resp.result == 2) {
                        alert("rule name exists");
                    } else {
                        window.location.reload();
                    }
                }
            })
        },

        addvalue: function ( val , tag ) {
            var ruleval_name = val;
            var sid = $('input[name=sid]').attr('value');
            var post_data = {
                "sid": sid,
                "ruleval_name": ruleval_name,
                "msg": "haha"
            };
            $.ajax({
                url: "/product/category/rule/valadd",
                type: "post",
                data: post_data,
                success: function (resp) {
                    if (resp.result == 2) {
                        alert("attr value 已存在！");
                    } else {
                        var html = '<input name="editRuleVal" type="text" class="list-group-item" sid="' + resp.data.valid + '" value="' + val + '" readonly><span name="span-modifyRuleVal" sid="' + resp.data.valid + '" class="span-edit-item list-group-item right hidden">确定</span>';
                        $('#RuleVal-list').append(html);
                        tag.prev().remove();
                        tag.remove();
                    }
                }
            });
        },

        modifyvalue: function ( val , tag , temp){
            var id = tag.attr('sid');
            var sid = $('input[name=sid]').attr('value');
            if(temp != val){
                var post_data = {
                    'id': id,
                    'name': val,
                    'check': '',
                    'sid': sid
                };
                $.ajax({
                    url: '/product/category/rule/valmodify',
                    type: 'post',
                    data: post_data,
                    success:function(resp){
                        console.log(resp)
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

        canseach_change: function (obj) {
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

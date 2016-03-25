/**
 * Created by hxhuang on 15-11-3.
 */


var categoryApp = function(){
    var all_id = new Array;
    var spliceUl = function(obj){
        all_id.push(obj.id);
        var haschild = '';
        var third = '';
        if(obj.second || obj.third){
            haschild = '<img src="/statics/imgs/icon/more-bottom.png">';
            third = '<a href="javascript:;" data-categoryId="' + obj.id + '" data-toggle="modal" data-target="#menuFromDialog"><span><img src="/statics/imgs/icon/add.png"></span></a>&nbsp;&nbsp;&nbsp;&nbsp;';
        }else{
            third = '<a href="/product/category/attrset?cid=' + obj.id + '"><span><img src="/statics/imgs/icon/Settings.png"></span></a>&nbsp;&nbsp;&nbsp;&nbsp;</a>'
        }
        var temp = '<ul><li class="table-list-checkbox"><input type="checkbox" name="categoryId" value="' + obj.id + '" cname="' + obj.name + '"></li>'
            +   '<li class="table-list-sort"><input type="text" class="form-control" placeholder="0" name="sortId" value="' + obj.sort_id + '"></li>'
            +   '<li class="table-menu-name"><span name="showChild" data-target="' + obj.id + '">' + haschild + '</span>&nbsp;&nbsp;&nbsp;&nbsp;' + obj.name + '</li>'
            +   '<li class="table-list-operation">'
            +   '<a href="javascript:;" data-categoryId="' + obj.id + '" data-toggle="modal" data-target="#editFromDialog"><span><img src="/statics/imgs/icon/edit.png"></span></a>&nbsp;&nbsp;&nbsp;&nbsp;'
            +   third
            +   '<a href="javascript:;" data-categoryId="' + obj.id + '" onclick="categoryApp.del_category(this)"><span><img src="/statics/imgs/icon/delete.png"></span></a>'
            +   '</ul>';

        return temp;
    }

    return {

        saveaddBtn: function () {
            //data handle here
            var elem = document.getElementById('modal_data_add').elements;
            var post_data = {
                "category_name": elem["category_name"].value,
                "parent_id": elem["parent_id"].value
            };
            $.ajax({
                url: "category/add",
                type: "post",
                data: post_data,
                success: function (data) {
                    resp = eval('('+data+')');
                    if (resp.result == 2){
                        alert(resp.message)
                    }else{
                        $('#menuFromDialog').modal('hide');
                        window.location.reload();
                    }
                }
            });
        },

        saveeditBtn: function () {

            var elem = document.getElementById('modal_data_edit').elements;
            var post_data = {
                "id":elem["id"].value,
                "category_name": elem["category_name"].value,
                "parent_id": elem["parent_id"].value
            };
            $.ajax({
                url: "category/edit?id="+elem["id"].value,
                type: "post",
                data: post_data,
                success: function (data) {
                    resp = eval('('+data+')');
                    if (resp.result == 2){
                        alert(resp.message);
                    }else{
                        $('#menuFromDialog').modal('hide');
                        window.location.reload();
                    }
                }
            });
        },

        saveattrsetBtn: function () {

            var elem = document.getElementById('modal_data_attrset').elements;
            var post_data = {
                "id":elem["id"].value,
                "category_name": elem["category_name"].value,
                "parent_id": elem["parent_id"].value
            };
            $.ajax({
                url: "category/attrset?id="+elem["id"].value,
                type: "post",
                data: post_data,
                success: function (data) {
                    resp = eval('('+data+')');
                    if (resp.result == 2){
                        alert(resp.message);
                    }else{
                        $('#menuFromDialog').modal('hide');
                        window.location.reload();
                    }
                }
            });
        },

        category_name_change: function (idname) {
            var elem = document.getElementById(idname).elements;
            category_name_repeated = document.getElementById('category_name_repeated');
            var post_data = {
                "category_name": elem["category_name"].value,
                "parent_id": -1
            };
            if (idname == 'modal_data_add') {

                $.ajax({
                    url: "category/add",
                    type: "post",
                    data: post_data,
                    success: function (data) {
                        resp = eval('('+data+')');
                        if (resp.result == 2){
                            category_name_repeated.textContent = "类别名称已存在！";
                        }else{
                            category_name_repeated.textContent = "";
                        }
                    }
                });
            }
            else if (idname != 'modal_data_edit') {
            } else {
                post_data["id"] = elem["id"].value;
                $.ajax({
                    url: "category/edit",
                    type: "post",
                    data: post_data,
                    success: function (data) {
                        resp = eval('('+data+')');
                        if (resp.result == 2){
                            category_name_repeated.textContent = "类别名称已存在！";
                        }else{
                            category_name_repeated.textContent = "";
                        }
                    }
                });
            }
        },

        init: function () {

            $('div#menuFromDialog').on('show.bs.modal', function (e) {
                var id = $(e.relatedTarget).attr('data-categoryId');
                var _this = $(this);
                var _menu = [];

                for (i = 0; i < __menu__.length; i++) {
                    _menu.push({
                        id: __menu__[i].id,
                        text: __menu__[i].name,
                        level: __menu__[i].level
                    });
                }

                $.get('/product/category/add?id=' + id, function (data) {
                    _this.find('.modal-body').html(data);
                    $('select[name=parent_id]').select2({
                        data: _menu,
                        minimumResultsForSearch: -1,
                        templateResult: function (state) {
                            if (!state.id) return state.text;
                            return $('<span class="menu-depth-' + state.level + '">' + state.text + '</span>');
                        }
                    });
                    if(id != 0){
                        $('select[name=parent_id]').select2('val',id);
                    }
                });
            });

            $('div#editFromDialog').on('show.bs.modal', function (e) {
                var id = $(e.relatedTarget).attr('data-categoryId');
                var _this = $(this);
                var _menu = [];
                for (i = 0; i < __menu__.length; i++) {
                    _menu.push({
                        id: __menu__[i].id,
                        text: __menu__[i].name,
                        level: __menu__[i].level
                    });
                }

                $.get('/product/category/edit?id=' + id, function (data) {
                    _this.find('.modal-body').html(data);
                    $('input[name=id]').val(editData.id);
                    $('input[name=category_name]').val(editData.name);
                    $('select[name=parent_id]').select2({
                        data: _menu,
                        minimumResultsForSearch: -1,
                        templateResult: function (state) {
                            console.log(state);
                            if (!state.id) return state.text;
                            return $('<span class="menu-depth-' + state.level + '">' + state.text + '</span>');
                        }
                    });
                    var pid = editData.parent_id;
                    $("select[name=parent_id]").select2('val',pid);
                    var edit_selected = document.getElementById('edit_selected');
                    for (i=0; i<edit_selected.length;i++){
                        if(edit_selected[i].value == editData.parent_id){
                            edit_selected[i].selected='selected';
                        }
                    }
                });
            });

            $('div#attrsetFromDialog').on('show.bs.modal', function (e) {
                var id = $(e.relatedTarget).attr('data-categoryId');
                var aid = $(e.relatedTarget).attr('data-attrId');
                var _this = $(this);
                var _menu = [];

                $.get('/product/category/attrset?id=' + id, function (data) {
                    _this.find('.modal-body').html(data);
                    $('input[name=id]').val(id);
                    for (i = 0; i < categoryAttributeList.length; i++) {
                        _menu.push({
                            id: categoryAttributeList[i].id,
                            text: categoryAttributeList[i].name,
                            value: categoryAttributeList[i].value,
                            type: categoryAttributeList[i].type
                        });
                      }

                    $('select[name=parent_id]').select2({
                        data: _menu,
                        minimumResultsForSearch: -1,
                        templateResult: function (state) {
                            if (!state.id) return state.text;
                            return $('<span class="menu-depth-' + 1 + '">' + state.text + '</span>');
                        }
                    });

                    var initval = categoryAttributeList[0];
                    if(initval.id != 0){
                      $('select[name=parent_id]').select2('val',initval.id);
                    }
                });
            });

            $('div#attraddFromDialog').on('show.bs.modal',function(e){
              var cid = $(e.relatedTarget).attr('data-categoryId');
              var _this = $(this);

                $.get('/product/category/addattr?id=' + cid,function(data){
                    _this.find('.modal-body').html(data);
                })
            });

            $('div#attrdelFromDialog').on('show.bs.modal',function(e){
                var cid = $(e.relatedTarget).attr('data-categoryId');
                var attr_id = $(e.relatedTarget).attr('data-AttrId');
                var _this = $(this);
                $('#attrsetFromDialog').modal('hide');
                $.get('/product/category/delattr?id=' + attr_id + '&' +'cid='+cid,function(data){
                    _this.find('.modal-body').html(data);
                })
            });

            $('button[data-target=#batchDel]').on('click',function(){
                var tempArr =  $('input[name=categoryId]');
                var valueArr = [];
                var tempName = '';
                for(var i = 0; i < tempArr.length; i++){
                    if(tempArr[i].checked){
                        if(tempName != '') tempName += ',';
                        valueArr.push({
                            id:$(tempArr[i]).val()
                        });
                        tempName += $(tempArr[i]).attr('cname');
                    }
                };
                if(tempName != ''){
                    swal({
                        title:'是否删除？',
                        text:'删除' + tempName + '后无法恢复',
                        type:'warning',
                        showCancelButton:true,
                        confirmButtonColor: "#DD6B55",
                        confirmButtonText: "删除所选分类。",
                        cancelButtonText: "取消删除。",
                        closeOnConfirm: false,
                        closeOnCancel: false
                    },function(isConfirm){
                        if(isConfirm){
                            for(var i = 0; i < valueArr.length; i++){
                                swal("正在删除", "正在删除，请稍等", "success");
                                var cid = valueArr[i].id;
                                //$.ajax({
                                //    url: "/product/category/del/",
                                //    data: {"cid": cid},
                                //    type: "POST",
                                //    success: function (data) {
                                //        resp = eval('('+data+')');
                                //        if (resp.result != 0) {
                                //            alert("del Wrong");
                                //            console.log("wrong")
                                //        } else {
                                //            window.location.reload();
                                //        }
                                //    }
                                //})
                            }
                        }else{
                            swal("已取消", "该分类被保留", "error");
                        }
                    })
                }
            });

            var html = '';
            for(var x = 0; x < category_menu.length; x++){
                html =  '<div class="system-menu-table-body content-table menu-depth-1 content-table-data list-group-item" data-menu-line="menu-0" data-id=' + category_menu[x].id + '>'
                    +   spliceUl(category_menu[x])
                    +   '</div><div name="hide" data-target="pid-' + category_menu[x].id +'"></div>'
                $('div[data-target=div-body]').append(html);
            }
            var xLength = ($('div[data-target=div-body]').children().length-1)/2;
            for(var x = 0;x < xLength; x++){
                html='';
                for(var y = 0; y < category_menu[x].second.length; y++){
                    var second = category_menu[x].second[y];
                    html += '<div class="system-menu-table-body content-table menu-depth-2 content-table-data list-group-item" data-menu-line="menu-' + category_menu[x].id + '" data-id=' + second.id + '>'
                    +   spliceUl(second)
                    +   '</div><div name="hide" data-target="pid-' + second.id +'">'
                    for(var z =0; z < category_menu[x].second[y].third.length; z++){
                        var third = category_menu[x].second[y].third[z];
                        html += '<div class="system-menu-table-body content-table menu-depth-3 content-table-data list-group-item" data-menu-line="menu-' + category_menu[x].second[y].id + '">'
                             + spliceUl(third) + '</div>'
                    }
                    html += '</div>';
                }
                var id = x+1;
                $('div[data-target=pid-'+ id +']').append(html);
            };

            $('div[name=hide]').toggle();

            $('span[name=showChild]').bind('click', function(){
                $('div[data-target=pid-'+ $(this).attr('data-target') +']').toggle('slow');
                if($(this).children(':eq(0)').attr('src') == '/statics/imgs/icon/more-bottom.png'){
                    $(this).children(':eq(0)').attr('src','/statics/imgs/icon/more-up.png')
                }else{
                    $(this).children(':eq(0)').attr('src','/statics/imgs/icon/more-bottom.png')
                }
            });

            $('input[name=categoryAll]').bind('click',function(){
                var flag = this.checked;
                $('input[type=checkbox]').each(function(){
                    this.checked = flag;
                })
            });
        },

        del_category: function (e) {
            swal({
                title:'是否要删除该分类？',
                text:'删除该分类后无法恢复',
                type:'warning',
                showCancelButton:true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "删除该分类。",
                cancelButtonText: "不，取消删除。",
                closeOnConfirm: false,
                closeOnCancel: false
            },function(isConfirm){
                if(isConfirm){
                    swal("删除成功!", "该分类已经删除", "success");
                    var cid = e.getAttribute("data-categoryId");
                    $.ajax({
                        url: "/product/category/del/",
                        data: {"cid": cid},
                        type: "POST",
                        success: function (data) {
                            resp = eval('('+data+')');
                            if (resp.result != 0) {
                                alert("del Wrong");
                                console.log("wrong")
                            } else {
                                window.location.reload();
                            }
                        }
                    })
                }else{
                    swal("已取消", "该分类被保留", "error");
                }
            })
        },

        del_attr: function(){
            var aid = document.getElementById('modal_data_attrdel_id').value;

            $.ajax({
                url:'/product/category/delattr',
                type:'POST',
                data:{"attr_id":aid},
                success: function (data) {
                    resp = eval('('+data+')');
                    if (resp.result != 0) {
                        alert("del Wrong");
                        console.log("wrong")
                    } else {
                        //$('div#attrdelFromDialog').modal('hide');
                        window.location.reload();
                    }
                }
            });
        }
    }
}();



/**
 * Created by hxhuang on 15-11-3.
 */

var menuApp = function(){

    return {

        saveaddBtn: function () {
            //data handle here
            var elem = document.getElementById('modal_data_add').elements;
            var post_data = {
                "menu_name": elem["menu_name"].value,
                "parent_id": elem["parent_id"].value,
                "url": elem["url"].value,
                "params": elem["params"].value,
                "icon_class": elem["icon_class"].value,
                "style_css": elem["style_css"].value,
                "is_menu": elem["is_menu"].value
            };
            $.ajax({
                url: "menu/add",
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
                "menu_name": elem["menu_name"].value,
                "parent_id": elem["parent_id"].value,
                "url": elem["url"].value,
                "params": elem["params"].value,
                "icon_class": elem["icon_class"].value,
                "style_css": elem["style_css"].value,
                "is_menu": elem["is_menu"].value
            };
            $.ajax({
                url: "menu/edit?id="+elem["id"].value,
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

        menu_name_change: function (idname) {
            var elem = document.getElementById(idname).elements;
            menu_name_repeated = document.getElementById('menu_name_repeated');
            var post_data = {
                "menu_name": elem["menu_name"].value,
                "parent_id": -1,
                "url": 0,
                "params": 0,
                "icon_class": 0,
                "style_css": 0,
                "is_menu": 0
            };
            if (idname == 'modal_data_add') {

                $.ajax({
                    url: "menu/add",
                    type: "post",
                    data: post_data,
                    success: function (data) {
                        resp = eval('('+data+')');
                        if (resp.result == 2){
                            menu_name_repeated.textContent = "菜单名称已存在！"
                        }else{
                            menu_name_repeated.textContent = ""
                        }
                    }
                });
            }
            else if (idname != 'modal_data_edit') {
            } else {
                post_data["id"] = elem["id"].value;
                $.ajax({
                    url: "menu/edit",
                    type: "post",
                    data: post_data,
                    success: function (data) {
                        resp = eval('('+data+')');
                        if (resp.result == 2){
                            menu_name_repeated.textContent = "菜单名称已存在！"
                        }else{
                            menu_name_repeated.textContent = ""
                        }
                    }
                });
            }
        },

        init: function () {
            $('div#menuFromDialog').on('show.bs.modal', function (e) {
                var id = $(e.relatedTarget).attr('data-menuId');
                var _this = $(this);
                var _menu = [];

                    _menu.push({
                        id: 0,
                        text: '系统主菜单',
                        leave: '1'
                    });

                for (i = 0; i < __menu__.length; i++) {
                    _menu.push({
                        id: __menu__[i].id,
                        text: __menu__[i].name,
                        level: __menu__[i].level
                    });
                }

                $.get('/system/menu/add?id=' + id, function (data) {
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
                var id = $(e.relatedTarget).attr('data-menuId');
                var _this = $(this);
                var _menu = [];

                    _menu.push({
                        id: 0,
                        text: '系统主菜单',
                        leave: '1'
                    });

                for (i = 0; i < __menu__.length; i++) {
                    _menu.push({
                        id: __menu__[i].id,
                        text: __menu__[i].name,
                        level: __menu__[i].level
                    });
                }

                $.get('/system/menu/edit?id=' + id, function (data) {
                    _this.find('.modal-body').html(data);
                    $('input[name=id]').val(editData.id);
                    $('input[name=menu_name]').val(editData.menu_name);
                    $('input[name=url]').val(editData.url);
                    $('input[name=params]').val(editData.params);
                    $('input[name=icon_class]').val(editData.icon_class);
                    $('input[name=style_css]').val(editData.style_css);
                    $('input[name=is_menu]').val(editData.is_menu);
                    $('select[name=parent_id]').select2({
                        data: _menu,
                        minimumResultsForSearch: -1,
                        templateResult: function (state) {
                            if (!state.id) return state.text;
                            return $('<span class="menu-depth-' + state.level + '">' + state.text + '</span>');
                        }
                    });
                    var pid = editData.parent_id;
                    $('select[name=parent_id]').select2('val',pid);
                    var edit_selected = document.getElementById('edit_selected');
                    for (i=0; i<edit_selected.length;i++){
                        if(edit_selected[i].value == editData.parent_id){
                            edit_selected[i].selected='selected';
                        }
                    }
                });
            });
        },

        del_menu: function (e) {
            menuId = e.getAttribute("data-menuId");
            $.ajax({
                url: "/system/menu/del/",
                data: {"menuId": menuId},
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
        }

    }
}();
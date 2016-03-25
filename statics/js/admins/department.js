/**
 * Created by hxhuang on 15-11-3.
 */

var departmentApp = function(){

    return {

        saveaddBtn: function () {
            //data handle here
            var elem = document.getElementById('modal_data_add').elements;
            var post_data = {
                "name": elem["name"].value,
                "description": elem["description"].value
            };
            $.ajax({
                url: "/admin/department/add",
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
                "name": elem["name"].value,
                "description": elem["description"].value
            };
            $.ajax({
                url: "/admin/department/edit?id="+elem["id"].value,
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


        init: function () {
            $('div#menuFromDialog').on('show.bs.modal', function (e) {
                var id = $(e.relatedTarget).attr('data-menuId');
                var _this = $(this);

                $.get('/admin/department/add?id=' + id, function (data) {
                    _this.find('.modal-body').html(data);
                });
            });
            //$('div#editFromDialog').on('show.bs.modal', function (e) {
            //    var id = $(e.relatedTarget).attr('data-menuId');
            //    var _this = $(this);
            //
            //    $.get('/admin/department/edit?id=' + id, function (data) {
            //        _this.find('.modal-body').html(data);
            //        $('input[name=id]').val(editData.id);
            //        $('input[name=name]').val(editData.name);
            //        $('input[name=description]').val(editData.description);
            //    });
            //});
        },

        del_department: function (e) {
            departmentId = e.getAttribute("data-menuId");
            $.ajax({
                url: "/admin/department/del",
                data: {"departmentId": departmentId},
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
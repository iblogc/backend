var ctrl_selectApp = function () {

    //select初始化
    var initSelect = function () {
        var xLength = arguments.length;
        for (var x = 0; x < xLength; x += 2) {
            $('select[data-name=' + arguments[x] + ']').html('');
            var html = '';
            for (var i = 0; i < arguments[x + 1].length; i++) {
                html += '<option value=' + arguments[x + 1][i].id + ' data-index=' + i + '>' + arguments[x + 1][i].name + '</option>';
            }
            $('select[data-name=' + arguments[x] + ']').html('<option value="empty">请选择</option>' + html);
        }
    };

    //select加载原有数据
    var loadSelect = function (groupName, array, targetArr) {
        var selectArr = $('select[data-group=' + groupName + ']');
        var tmpArr = array;id
        for (var i = 0; i < targetArr.length; i++) {
            if (targetArr[i] == null) {
                break;
            }
            var flag = true;
            $(tmpArr).each(function (x) {
                if (this.name == targetArr[i]) {
                    console.log($(selectArr[i]));
                    $(selectArr[i]).find('option[value='+ targetArr[i] +']').attr('selected','true');
                    changeSelectVal(selectArr[i],array);
                    tmpArr = tmpArr[x].arrChild;
                    flag = false;
                }
            });
            if (flag) break;
        }
    };


    var changeSelectVal = function (obj, array) {
        var index = $('select[data-name=' + $(obj).attr('data-name') + '] option:selected').attr('data-index');

        //更新localStorage 用于url拼接
        if (index) {
            localStorage.setItem($(obj).attr('data-group'), index);
        }

        //寻找下一级select
        var next = $('select[data-for=' + $(obj).attr('data-name') + ']');

        //若没下一级 则返回
        if (!next[0]) return;

        //清除之后select内容
        clearSelect(next, index);

        //判断是否继续
        if($(obj).val() == 'empty') return;

        //增加下一级select内容
        next.html('');
        var tmpArr = index.split('-');
        var tmp = array;
        for (var i = 0; i < tmpArr.length; i++) {
            tmp = tmp[tmpArr[i]].arrChild;
        }
        var html = '';
        for (var i = 0; i < tmp.length; i++) {
            html += '<option value=' + tmp[i].id + ' data-index=' + index + '-' + i + '>' + tmp[i].name + '</option>'
        }
        next.html('<option value="empty" data-index="' + index + '">请选择</option>' + html);
    };

    //清除select内容
    var clearSelect = function (obj, index) {
        obj.html('<option value="empty" data-index="' + index + '">请选择</option>');

        //调用changeSelectVal 若有下一级select 则确保下一级select清空
        obj.change();
    };

    var changeObject = function () {
        $('select[data-name=select1]').on('change', function () {
            changeSelectVal(this, select_area)
        });
        $('select[data-name=select2]').on('change', function () {
            changeSelectVal(this, select_area)
        });
        $('select[data-name=select3]').on('change', function () {
            changeSelectVal(this, select_area)
        });
    };

    return {
        init: function () {
            initSelect('select1', select_area);
            //console.log(select_area);
            changeObject();
        },
        selectLoad: function(groupName, array, targetArr){
            loadSelect(groupName, array, targetArr);
        }
    }
}();
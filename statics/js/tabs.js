/**
 * Created by hxhuang on 15-10-22.
 */
var Tab = function () {
    return {
        init: function () {
            $('.js-parent-menu').on('click', function () {
                if ($(this).parent().hasClass('actived')){
                    $(this).parent().removeClass('actived');
                }else{
                    $(this).parent().addClass('actived');
                }
            });
            $('.js-sub-menu').on('click', function () {
                var url = $(this).attr('data-url');
                var name = $(this).find('.menu-name').html();
                if (url != undefined) {
                    console.log(url);
                    if ($('#content-body-sheet').tabs('exists', name)) {
                        $('#content-body-sheet').tabs('select', name);
                    } else {
                        var width = $('#content-body-sheet').width();
                        var height = $('#content-body-sheet').height();
                        var content = '<iframe scrolling="auto" frameborder="0"  src="' + url + '" style="width:'+width+'px;height:'+height+'px;"></iframe>';
                        $('#content-body-sheet').tabs('add', {
                            title: name,
                            content: content,
                            closable: true
                        });
                    }
                }
            });
        }
    }
}();


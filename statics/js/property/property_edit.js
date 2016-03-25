var estateAddApp = function () {
    return {
        init: function () {
            $(document).ready(function () {
                var $tab_li = $('#tab>ul>li');
                $('div.tab_box > div').hide();
                $('div.tab_box > div').eq(0).show();
                $tab_li.click(function () {
                    $(this).addClass('selected').siblings().removeClass('selected');
                    var index = $tab_li.index(this);
                    console.log(index);
                    $('div.tab_box > div').each(function (i) {
                        if (i != index) {
                            $('div.tab_box > div').eq(i).hide();
                        } else {
                            $('div.tab_box > div').eq(i).show();
                        }
                    })
                });
                $('#img').click();
            });

            $('#info-btn').on('click', function () {
                console.log('save');
            });

            $('button[data-id=btn-add]').on('click', function () {
                var temp = $(this.parentNode).next()[0];
                var x = $(this.parentNode).nextAll().length + 1;
                $(temp.parentNode).append('<br>');
                $(temp.parentNode).append($(temp).clone());
                $(temp.parentNode.lastChild).attr('data-id', x / 2);
                if(temp.parentNode.children.length > 3){
                    var n = $(this).attr('data-name');
                    $('button[data-btn-name=' + n + ']').removeClass('hidden');
                }
            })

            $('div[name=around]').on('click','button[data-id=btn-delete]', function () {
                var temp = this.parentNode.parentNode;
                if(temp.parentNode.children.length <= 5){
                    $('button[data-btn-name=' + $(this).attr('data-btn-name') + ']').addClass('hidden')
                }
                var x = $(temp).attr('data-id');
                var removeDOM;
                var y = 0;
                $(temp).nextAll().each(function(e,a){
                    if(x == 0 && e == 0){
                        removeDOM = a;
                    }
                    if($(a).attr('name') == 'section-info'){
                        $(a).attr('data-id', x * 1 + y * 1);
                        y++;
                    }
                })
                if(removeDOM){
                    $(removeDOM).remove();
                } else {
                    $(temp).prev().remove();
                }
                $(temp).remove();
            })


            $('section[name=type-info]').on('mouseover',function(){
                $(this).addClass('mouse-over');
            });

            $('section[name=type-info]').on('mouseout',function(){
                $(this).removeClass('mouse-over');
            });
        }
    }
}();
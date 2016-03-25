/**
 * Created by yunxia on 2015/12/17.
 */

var productInfoApp = function () {
    return {
        init: function () {
            $('.div-more').attr('style','display:none');
            $('.div-more').html();
            $('.btn-more').click(function () {
                if ($('.btn-more').html() == '更多'){
                    $('.div-more').slideDown('fast');
                    $('.btn-more').html('隐藏');
                }else{
                    $('.div-more').slideUp('fast');
                    $('.btn-more').html('更多');
                }
            });
        }
    }
}();
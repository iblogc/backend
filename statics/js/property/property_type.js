var roomTypeAddApp = function () {
    return {
        init: function () {
            var imgArr = new Array();
            $(document).on('click', 'img[name=uploadimg]', function () {
                $('#getImg').click();
            });

            $('#getImg').on('change', function () {
                var f = new FileReader;
                var file = document.querySelector("#getImg").files[0];
                if (file.type.indexOf('image') != 0) {
                    return;
                }
                f.readAsDataURL(file);
                var sum = $('.img-box').children().length / 2;
                f.onload = function () {
                    $('div.img-box').append('<img data-id="' + sum + '" src="' + this.result + '"><span data-name="deleteImg" data-id="' + sum + '"></span>')
                    imgArr[sum] = this;
                }
                if($('.img-box>img').length >= 3){
                    $('img[name=uploadimg]').addClass('hidden');
                }
            });

            $(document).on('click', 'span[data-name=deleteImg]', function () {
                var x = $(this).attr('data-id') * 1;
                var a = imgArr.slice(x + 1, imgArr.length);
                var b = imgArr.slice(0, x);
                imgArr = b.concat(a);
                var temp = $('.img-box>img');
                for (var i = x + 1; i < temp.length; i++) {
                    $(temp[i]).attr('data-id', i - 1);
                }
                var temp = $('.img-box>span');
                for (var i = x + 1; i < temp.length; i++) {
                    $(temp[i]).attr('data-id', i - 1);
                }
                $(this).prev().remove();
                $(this).remove();
                if($('.img-box>img').length < 4){
                    $('img[name=uploadimg]').removeClass('hidden');
                }
            })
        }
    }
}();
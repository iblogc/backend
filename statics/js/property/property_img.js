var estateImgEditApp = function () {
    return {
        init: function () {
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
                var sum = $('.img-box').children().length - 1;
                f.onload = function () {
                    $($('img[name=uploadimg]').parent()).before('<div name="img" data-id="' + sum + '"><img src="' + this.result + '"><span data-name="deleteImg" data-id="' + sum + '"></span></div>')
                    imgArr[sum] = this;
                }
                //if($('.img-box>img').length >= 10){
                //    $('img[name=uploadimg]').addClass('hidden');
                //}
            });

            $(document).on('click', 'span[data-name=deleteImg]', function () {
                var x = $(this).parent().attr('data-id') * 1;
                var a = imgArr.slice(x + 1, imgArr.length);
                var b = imgArr.slice(0, x);
                imgArr = b.concat(a);
                var temp = $('.img-box>div[name=img]');
                for (var i = x + 1; i < temp.length; i++) {
                    $(temp[i]).attr('data-id', i - 1);
                }
                $(this).parent().remove();
                //if($('.img-box>img').length < 11){
                //    $('img[name=uploadimg]').removeClass('hidden');
                //}
            })
        }
    }
}();
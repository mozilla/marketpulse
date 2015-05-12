$(document).ready(function() {
    'use strict';

    $("#pickimage").click(function(e){
        e.preventDefault();
        $('#form-image').click();
    });

    $("#form-image").change(function(){
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                var img = $('<img id="upload-image" style="width:100%;">');
                img.attr('src', e.target.result);
                $('#upload-container').html(img);
            }
            reader.readAsDataURL(this.files[0]);
        }
        $('#pickimage').text('Change Image');
    });
});

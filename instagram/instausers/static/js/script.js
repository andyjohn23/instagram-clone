var toValidate = $('#email, #username, #password'),
    valid = false;
toValidate.keyup(function () {
    if ($(this).val().length > 0) {
        $(this).data('valid', true);
    } else {
        $(this).data('valid', false);
    }
    toValidate.each(function () {
        if ($(this).data('valid') == true) {
            valid = true;
        } else {
            valid = false;
        }
    });
    if (valid === true) {
        $('input[type=submit]').prop('disabled', false);
    } else {
        $('input[type=submit]').prop('disabled', true);
    }
});

$(function () {
    $('#profile-image').on('click', function () {
        $('#profile-image-upload').click();
    });
});
$(document).ready(function(){
    $("#heart").click(function(){
      if($("#heart").hasClass("liked")){
        $("#heart").html('<i class="fa fa-heart-o" aria-hidden="true"></i>');
        $("#heart").removeClass("liked");
      }else{
        $("#heart").html('<i class="fa fa-heart" aria-hidden="true"></i>');
        $("#heart").addClass("liked");
      }
    });
  });
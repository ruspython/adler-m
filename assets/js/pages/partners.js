$(function(){
    $('#select-city').selectBox().change(function(){
        var cID = $(this).val();
        $('.partners-list').removeClass('selected').filter('[data-city='+cID+']').addClass('selected')
    });
});
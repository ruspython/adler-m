/*! adler-m v0.0.0, 2014-08-07 */
$(function(){$("#select-city").selectBox().change(function(){var a=$(this).val();$(".partners-list").removeClass("selected").filter("[data-city="+a+"]").addClass("selected")})});
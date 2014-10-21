$(function(){
    var $carSound = $('#car-sound');
    $('#footer-car').click(function(){
        var $car = $(this),
            pathLength = $(window).width();
        $carSound[0].play();
        setTimeout(function(){
            $car.addClass('starts');
            setTimeout(function(){
                $car.removeClass('starts')
            }, 29000)
        }, 1660)
    })
});
(function() {
  $(function() {
    var $itemGallery, $mainPhoto, after, currentPhotoIndex, photoUrls;
    after = function(ms, cb) {
      return setTimeout(cb, ms);
    };
    $('.catalog-filter').on('reset', function() {
      $(this).find('select').select2("val", "");
      return $(this).find(':checkbox').iCheck('uncheck');
    });
    $itemGallery = $('#item-gallery');
    $mainPhoto = $('#main-photo');
    photoUrls = $itemGallery.find('.slide').map(function() {
      return $(this).attr('href');
    }).get();
    currentPhotoIndex = 0;
    $itemGallery.iosSlider({
      snapToChildren: true,
      desktopClickDrag: true,
      infiniteSlider: true,
      navNextSelector: $('.gallery__button.next'),
      navPrevSelector: $('.gallery__button.prev')
    }).on('click', '.slide', function(e) {
      var $newImage, $oldImage, photoUrl;
      e.preventDefault();
      photoUrl = $(this).attr('href');
      currentPhotoIndex = parseInt($(this).data('index'));
      $oldImage = $mainPhoto.children('img');
      $oldImage.addClass('old');
      after(1000, function() {
        return $oldImage.remove();
      });
      return $newImage = $("<img src=" + photoUrl + ">").load(function() {
        $(this).addClass('new').prependTo($mainPhoto);
        return after(1, function() {
          return $newImage.removeClass('new');
        });
      });
    });
    $(window).resize(function() {
      return $('.item-card .item-card-gallery').iosSlider('update');
    });
    $mainPhoto.on('click', 'img', function() {
      return $.fancybox.open(photoUrls, {
        index: currentPhotoIndex,
        helpers: {
          overlay: {
            locked: false
          }
        }
      });
    });
    $('.item-card').hover(function() {
      var $card, $galleryPlace, galleryURL;
      $card = $(this);
      galleryURL = $card.data('gallery');
      $galleryPlace = $card.find('.gallery');
      return $.ajax({
        url: galleryURL,
        success: function(data) {
          return $galleryPlace.html(data).find('.item-card-gallery').iosSlider({
            snapToChildren: true,
            desktopClickDrag: true,
            infiniteSlider: true,
            navNextSelector: $galleryPlace.find('.gallery__button.next'),
            navPrevSelector: $galleryPlace.find('.gallery__button.prev')
          });
        }
      });
    });
    $('#id_q').autocomplete({
      source: function(request, response) {
        $.ajax({
          url: $('#id_q').data("catalog-source"),
          dataType: "json",
          data: {
            q: request.term
          },
          success: function(data) {
            response(data);
          }
        });
      },
      minLength: 2,
      position: {
        my: "left top",
        at: "left bottom"
      },
      select: function(event, ui) {
        window.location = ui.item['url'];
      }
    });
  });

}).call(this);

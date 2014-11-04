$ ->
  after = (ms, cb) -> setTimeout cb, ms


  $('.catalog-filter').on 'reset', ->
    $(@).find('select').select2("val", "")
    $(@).find(':checkbox').iCheck 'uncheck'

  $itemGallery = $ '#item-gallery'
  $mainPhoto = $ '#main-photo'
  photoUrls = $itemGallery.find('.slide').map( ->
    $(@).attr 'href'
  ).get()
  currentPhotoIndex = 0

  $itemGallery
    .iosSlider
      snapToChildren: true
      desktopClickDrag: true
      infiniteSlider: true
      navNextSelector: $('.gallery__button.next')
      navPrevSelector: $('.gallery__button.prev')
    .on 'click', '.slide', (e) ->
      e.preventDefault()
      photoUrl = $(@).attr('href')
      currentPhotoIndex = parseInt $(@).data('index')
      $oldImage = $mainPhoto.children 'img'
      $oldImage.addClass 'old'
      after 1000, -> $oldImage.remove()
      $newImage = $("<img src=#{photoUrl}>").load ->
        $(@).addClass('new').prependTo $mainPhoto
        after 1, -> $newImage.removeClass 'new'
  $(window).resize -> $('.item-card .item-card-gallery').iosSlider 'update'

  $mainPhoto.on 'click', 'img', ->
    $.fancybox.open photoUrls
      , index: currentPhotoIndex
      , helpers:
        overlay:
          locked: false




  $('.item-card').hover ->
    $card = $(@)
    galleryURL = $card.data 'gallery'
    $galleryPlace = $card.find '.gallery'
    $.ajax
      url: galleryURL
      success: (data) ->
        $galleryPlace
          .html data
          .find('.item-card-gallery')
            .iosSlider
              snapToChildren: true
              desktopClickDrag: true
              infiniteSlider: true
              navNextSelector: $galleryPlace.find('.gallery__button.next')
              navPrevSelector: $galleryPlace.find('.gallery__button.prev')


  $('#id_q').autocomplete
    source: (request, response) ->
      $.ajax
        url: $('#id_q').data "catalog-source"
        dataType: "json"
        data:
          q: request.term
        success: (data) ->
          response data
          return
      return
    minLength: 2
    position:
      my: "left top"
      at: "left bottom"
    select: (event, ui) ->
      window.location =  ui.item['url']

      return
  return
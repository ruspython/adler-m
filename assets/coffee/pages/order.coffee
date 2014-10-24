$ ->
  after = (ms, cb) ->
    setTimeout cb, ms


  selectDeliveryCity = ->
    city = $('#id_address_city').val()
    url = $('#delivery-location-name').data 'delivery-source'
    $.get url, "city=#{city}", (data) ->
      $('#delivery-variants').html data
      $('#delivery-variants input').iCheck
        checkboxClass: 'icheckbox_fs'
        radioClass: 'iradio_fs'
      $('#delivery-location-name').text city
      $('#delivery-location').show()

  selectDeliveryCity()
  $('#id_address_city').change selectDeliveryCity

  $('#id_address_city').autocomplete
    source: (request, response) ->
      $.ajax
        url: "../get_city"
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
      selectDeliveryCity()
      return $('#id_address_city').change selectDeliveryCity
  return



#  $('.delivery-variants').on 'click', 'a.direction_map', (e)->
#    e.preventDefault()
#    $.fancybox
#      href: $(@).attr 'href'


#  $('.order-make-form .personal_item .change').click ->
#    $(@).closest '.personal_item'
#      .addClass 'edit'
#      .find '.new_value'
#      .val('')
#      .focus()
#  $('.order-make-form .personal_item .save_now').click ->
#    $container = $(@).closest '.personal_item'
#    if $container.hasClass 'address'
#      newValue = "#{$container.find('.street').val()} #{$container.find('.house').val()} #{$container.find('.building').val()} #{$container.find('.flat').val()}"
#    else
#      newValue = $container.find('.new_value').val()
#    $container.removeClass 'edit'
#    $container.find('.value').text newValue if newValue



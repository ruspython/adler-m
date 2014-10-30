split_cost = (value) ->
  return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")

rubalyze = (value) ->
  value = parseInt value
  if value % 10 == 1 && value % 100 != 11
    return split_cost(value) + " рубль"
  if (value % 10 == 2 && value % 100 != 12) || (value % 10 == 3 && value % 100 != 13) || (value % 10 == 4 && value % 100 != 14)
    return split_cost(value) + " рубля"
  return split_cost(value) + " рублей"

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
        url: window.cityUrl
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

  total_elem = $('.total_cost span')
  total_cost = parseInt(total_elem.attr('data-price'))

  $(document).on 'ifChecked', 'input[name="delivery"]', ->
    value = $(this).val()
    city = $('#id_address_city').val()
    url = $('#delivery-location-name').data 'delivery-source'
    methods = {}
    $.ajax
      url: '/ru/personal/orders/get_delivery_method/'
      type: 'GET'
      dataType: "json"
      data:
        city: city
      success: (data) ->
        for entry in data

          if entry['type'] == 'postal'
            methods['post'] = entry
          if entry['type'] == 'courier'
            methods['courier'] = entry
          if entry['type'] == 'points'
            methods['pickup'] = entry


        total_elem.text(rubalyze(total_cost + parseInt(methods[value]['price'])))
        return
    return
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
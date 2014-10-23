$ ->
  $('#select-city').on "change", ->
    cID = $(@).val()
    $('.partners-list')
      .removeClass 'selected'
      .filter "[data-city=#{cID}]"
      .addClass 'selected'
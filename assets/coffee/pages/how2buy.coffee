$ ->
  $('#country-select').on "change", ->
    countryID = $(@).val()
    $ '.city-select'
      .removeClass 'selected'
      .filter "[data-country=#{countryID}]"
      .addClass 'selected'
  $('#city-select').on "change", ->
    cityID = $(@).val()
    $ '.delivery-variant'
      .removeClass 'selected'
      .filter "[data-city=#{cityID}]"
      .addClass 'selected'

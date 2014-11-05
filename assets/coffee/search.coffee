$ ->
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
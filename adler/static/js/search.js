(function() {
  $(function() {
    return $('#id_q').autocomplete({
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

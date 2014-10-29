(function() {
  $(function() {
    var after, selectDeliveryCity, total_cost, total_elem;
    after = function(ms, cb) {
      return setTimeout(cb, ms);
    };
    selectDeliveryCity = function() {
      var city, url;
      city = $('#id_address_city').val();
      url = $('#delivery-location-name').data('delivery-source');
      return $.get(url, "city=" + city, function(data) {
        $('#delivery-variants').html(data);
        $('#delivery-variants input').iCheck({
          checkboxClass: 'icheckbox_fs',
          radioClass: 'iradio_fs'
        });
        $('#delivery-location-name').text(city);
        return $('#delivery-location').show();
      });
    };
    selectDeliveryCity();
    $('#id_address_city').change(selectDeliveryCity);
    $('#id_address_city').autocomplete({
      source: function(request, response) {
        $.ajax({
          url: window.cityUrl,
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
        selectDeliveryCity();
        return $('#id_address_city').change(selectDeliveryCity);
      }
    });
    total_elem = $('.total_cost span');
    total_cost = parseInt(total_elem.text());
    $(document).on('ifChecked', 'input[name="delivery"]', function() {
      var city, url, value;
      value = $(this).val();
      city = $('#id_address_city').val();
      url = $('#delivery-location-name').data('delivery-source');
      $.ajax({
        url: '/ru/personal/orders/get_delivery_method/',
        type: 'GET',
        dataType: "json",
        data: {
          city: city
        },
        success: function(data) {
          var entry, sett, _i, _len;
          sett = {};
          for (_i = 0, _len = data.length; _i < _len; _i++) {
            entry = data[_i];
            sett = {};
            if (entry['type'] === 'postal') {
              sett['post'] = entry;
            }
            if (entry['type'] === 'courier') {
              sett['courier'] = entry;
            }
            if (entry['type'] === 'points') {
              sett['pickup'] = entry;
            }
          }
          alert(sett[value]['price']);
          total_elem.text(total_cost + sett[value]['price']);
        }
      });
    });
  });

}).call(this);

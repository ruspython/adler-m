(function() {
  var rubalyze, split_cost;

  split_cost = function(value) {
    return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  };

  rubalyze = function(value) {
    value = parseInt(value);
    if (value % 10 === 1 && value % 100 !== 11) {
      return split_cost(value) + "рубль";
    }
    if ((value % 10 === 2 && value % 100 !== 12) || (value % 10 === 3 && value % 100 !== 13) || (value % 10 === 4 && value % 100 !== 14)) {
      return split_cost(value) + "рубля";
    }
    return split_cost(value) + "рублей";
  };

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
    total_cost = parseInt(total_elem.attr('data-price'));
    $(document).on('ifChecked', 'input[name="delivery"]', function() {
      var city, methods, url, value;
      value = $(this).val();
      city = $('#id_address_city').val();
      url = $('#delivery-location-name').data('delivery-source');
      methods = {};
      $.ajax({
        url: '/ru/personal/orders/get_delivery_method/',
        type: 'GET',
        dataType: "json",
        data: {
          city: city
        },
        success: function(data) {
          var entry, _i, _len;
          for (_i = 0, _len = data.length; _i < _len; _i++) {
            entry = data[_i];
            if (entry['type'] === 'postal') {
              methods['post'] = entry;
            }
            if (entry['type'] === 'courier') {
              methods['courier'] = entry;
            }
            if (entry['type'] === 'points') {
              methods['pickup'] = entry;
            }
          }
          total_elem.text(rubalyze(total_cost + parseInt(methods[value]['price'])));
        }
      });
    });
  });

}).call(this);

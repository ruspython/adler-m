(function() {
  $(function() {
    var after, selectDeliveryCity;
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
    return $('#id_address_city').change(selectDeliveryCity);
  });

}).call(this);

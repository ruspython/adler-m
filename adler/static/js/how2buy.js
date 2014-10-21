(function() {
  $(function() {
    $('#country-select').on("change", function() {
      var countryID;
      countryID = $(this).val();
      return $('.city-select').removeClass('selected').filter("[data-country=" + countryID + "]").addClass('selected');
    });
    return $('#city-select').on("change", function() {
      var cityID;
      cityID = $(this).val();
      return $('.delivery-variant').removeClass('selected').filter("[data-city=" + cityID + "]").addClass('selected');
    });
  });

}).call(this);

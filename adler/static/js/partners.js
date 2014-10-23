(function() {
  $(function() {
    return $('#select-city').on("change", function() {
      var cID;
      cID = $(this).val();
      return $('.partners-list').removeClass('selected').filter("[data-city=" + cID + "]").addClass('selected');
    });
  });

}).call(this);

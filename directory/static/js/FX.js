$(document).ready( function() {
    $(document).on("submit", "#filter", function(e) {

      e.preventDefault();
      var data = $(this).serialize()
      $.ajax({
        type: "POST",
        data: data,
        url: "/filter/",
        success: function(data) {
          $(".container2").replaceWith(data);
        }

      });
    });
})
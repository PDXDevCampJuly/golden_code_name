var $form = $("form");

if ($form.attr('id') === "started") {
  $("#enter").show()
  $("#restart").hide()
} else {
  $("#enter").hide()
  $("#restart").show()
}

$("#enter").on( "click", function() {
  window.location.href = "http://maps.google.com";
});
$("#restart").on( "click", function() {
  window.location.href = "http://www.google.com";
});


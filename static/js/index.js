var $form = $("form");

// status either started or waiting
if ($form.attr('id') === "started") {
  $("#enter").show()
  $("#restart").hide()
} else {
  $("#enter").hide()
  $("#restart").show()
}


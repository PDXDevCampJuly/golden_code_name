// window.alert("sometext");
var $player_turn_status = $("#game_status");
if ($player_turn_status.attr('class') === "True") {
  $("header").css('background-color', '#6699CC');
} else {
  $("header").css('background-color', '#FF6666');
}

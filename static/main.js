$('#left').click(left);
$('#right').click(right);
$('#shutdown').click(shutdown);
$('#reboot').click(reboot);


function left() {
  $.get('/turn/left');
}

function right() {
  $.get('/turn/right');
}

function shutdown() {
  $.get('/shutdown');
}

function reboot() {
  $.get('/reboot');
}

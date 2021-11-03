$('#left').click(left);
$('#right').click(right);
$('#shutdown').click(shutdown);
$('#reboot').click(reboot);
$('#clear_log').click(clear_log);

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


function clear_log() {
  $.get('/clear_log');
}

var socket = io();

socket.on('connect', () => {
  console.log('connected');
  socket.emit('init', {});
});

socket.on('log', (data) => {
  console.log(data)
  let lines = JSON.parse(data.lines);
  for (line of lines) {
    addLine(line);
  }
});

socket.on('msg', (data) => {
  addLine(data.msg);
});

function addLine(line) {
  $('#log').append(`<div>${line}</div>`)
}

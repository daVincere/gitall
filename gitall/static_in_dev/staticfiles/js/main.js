function rotate(){
  var angle = 0,
  img = document.getElementById('container');
  document.getElementById('button').onclick = function() {
  angle = (angle + 90) % 360;
  img.className = "rotate" + angle;
}

}
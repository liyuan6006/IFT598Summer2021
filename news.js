$(document).ready(function () {
  $(".newsMenu").click(function () {
    $("#newsSection").removeAttr("hidden");
    $("#galleriesSection").attr("hidden", true);
    $("#donateSection").attr("hidden", true);
    $("#contactusSection").attr("hidden", true);
  });
});

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}
function allowDrop(ev) {
  ev.preventDefault();
}
function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
}

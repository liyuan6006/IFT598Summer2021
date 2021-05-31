$(document).ready(function () {
  $(".contactusMenu").click(function () {
    $("#contactusSection").removeAttr("hidden");
    $("#donateSection").attr("hidden", true);
    $("#galleriesSection").attr("hidden", true);
    $("#newsSection").attr("hidden", true);
  });
});

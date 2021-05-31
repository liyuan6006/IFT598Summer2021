$(document).ready(function () {
  $(".donateMenu").click(function () {
    $("#donateSection").removeAttr("hidden");
    $("#contactusSection").attr("hidden", true);
    $("#galleriesSection").attr("hidden", true);
    $("#newsSection").attr("hidden", true);
  });
});

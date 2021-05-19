$(document).ready(function () {
  $(".gallerisMenu").click(function () {
    $("#galleriesSection").removeAttr("hidden");
    $("#donateSection").attr("hidden", true);
    $("#contactusSection").attr("hidden", true);
  });
});

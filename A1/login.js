$(document).ready(function () {
  //check if user has logged in or not
  if (!sessionStorage.isLogin) {
    $("#loginModal").modal("show");
  }
  //lunch login model dialog
  $("#btnLoginHeader").click(function () {
    $("#loginModal").modal("show");
  });

  //log in
  $("#btnLogin").click(function () {
    var loginForm = $("#loginFrom");
    var isLoginFormInvalid = loginForm.is(":invalid");

    if (isLoginFormInvalid) {
    } else {
      sessionStorage.isLogin = true;
      $("#loginModal").modal("hide");
    }
  });
});

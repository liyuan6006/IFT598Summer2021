$(document).ready(function () {
  //lunch login model dialog
  $("#btnRegisterHeader").click(function () {
    $("#registerModal").modal("show");
  });

  //log in
  $("#btnRegister").click(function () {
    var registerForm = $("#registerFrom");
    var isValid = registerForm.valid();

    if (!isValid) {
    } else {
      $("#registerModal").modal("hide");
    }
  });
});

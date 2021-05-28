// Wait for the DOM to be ready
$(function() {
  var registerForm = $("#registerFrom");
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  registerForm.validate({
	  focusCleanup: true,
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
			username: {
				required: true,
				rangelength: [2, 8]
			},
			psw: {
				required: true,
				maxlength: 8,
				minlength: 8
			},
			pswrepeat: {
				required: true,
				equalTo: "#psw",
				maxlength: 8,
				minlength: 8	
			},
			lastname: {
				required: true
			},
			gender: {
				required: true 
			},
			streetaddress: {
				required: true,
			},
			city: {
				required: true 
			},
			state: {
				required: true
			},
			zipcode: {
				required: true,
				digits: true,
				minlength: 5,
				maxlength: 5
			},
			email: {
				required: true,
				email: true 
			},
			cellphonenumber: {
				required: true, 
				phoneUS: true
			},
			origincountry: {
				required: true
			},
			dob: {
				required: true 
			}
		},
    // Specify validation error messages
		messages: {
			username: {
				required: 'Username is required',
				rangelength: 'Must be 2 to 8 characters'
			},
			gender: {
				required: 'Please select your gender'
			},
			pswrepeat: {
				required: 'Verify Password',
				equalTo: 'Must match password'
			},

			zipcode: {
				required: 'Please enter a valid zip code'
			},
			city: {
				required: 'Required - auto-populated by zipcode'
			},
			state: {
				required: 'US State Only! - auto-populated by zipcode'
			}
		},
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
$(function(){
	(".pr-password").passwordRequirements({
		numCharacters: 8,
		useLowercase: true,
		useUppercase: true,
		useNumbers: true,
		useSpecial: false
	})
});
$("#zipcode").blur(function() {
	var city = $("#city");
	var state = $("#state");
	if (!city.val() && $(this).valid()) {
		$.getJSON("http://www.geonames.org/postalCodeLookupJSON?&country=US&callback=?", {postalcode: this.value }, function(response) {
			if (!city.val() && response && response.postalcodes.length && response.postalcodes[0].placeName) {
				city.val(response.postalcodes[0].placeName);
			}
		})
	}
		if (!state.val() && $(this).valid()) {
		$.getJSON("http://www.geonames.org/postalCodeLookupJSON?&country=US&callback=?", {postalcode: this.value }, function(response) {
			if (!state.val() && response && response.postalcodes.length && response.postalcodes[0].adminName1) {
				state.val(response.postalcodes[0].adminName1);
			}
		})
	}
});
$(function(){
	$(".datepicker").datepicker({
		format: 'mm/dd/yyyy'
	})
});
});
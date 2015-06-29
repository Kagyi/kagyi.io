$(function(){

    $('#trainer_keyfile').removeClass('form-control');
    $('#enroll-form').submit(function() {

	if ($("#payment_received").is(':checked') == false) {
	    alert ("Please, enroll students only after the payment is fully received.");
	    return false;
	}
    });
});

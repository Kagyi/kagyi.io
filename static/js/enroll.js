$(function(){
    $('#trainer_email').val("thura@kagyi.io");
    $('#student_email').val("thura@kagyi.io");
    $('#student_name').val("Thura Hlaing");
    $('#student_phone').val("09 3200 900 650");
    $('#student_address').val("No(2), West horse Race course rD, tamwe");
    $('#course_fees').val("145000");
    $('#payment_received').prop('checked', true);

    $('#trainer_keyfile').removeClass('form-control');
    $('#enroll-form').submit(function() {

	if ($("#payment_received").is(':checked') == false) {
	    alert ("Please, enroll students only after the payment is fully received.");
	    return false;
	}
    });
});

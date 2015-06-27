$(function(){
    $('#trainer_email').val("thura@kagyi.io");
    $('#student_email').val("thura@kagyi.io");
    $('#student_name').val("THURA HLAING");
    $('#student_phone').val("12312321");
    $('#student_address').val("12312321");
    $('#course_fees').val("12312");
    $('#payment_received').prop('checked', true);

    $('#trainer_keyfile').removeClass('form-control');
    $('#enroll-form').submit(function() {

	if ($("#payment_received").is(':checked') == false) {
	    alert ("Please, enroll students only after the payment is fully received.");
	    return false;
	}
    });
});

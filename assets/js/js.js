$(document).ready(function() {

	$("#userType").change(function(){
		if($("#userType").val() =="student")
		{
			$("#levelSelect").show();
			$("#levelSelectLabel").show();
		}
		else
		{
			$("#levelSelect").hide();
			$("#levelSelectLabel").hide();
		}
	});
});

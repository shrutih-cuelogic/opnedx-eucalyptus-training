// $.ajax(
//     type: 'POST',
//     url:    '/polls/',
//     contentType: 'application/json'
//     data:   {ids:{"x":"a", "y":"b", "z":"c"}, type:'info'},
//     complete: function(response) {
//         console.log(response);
//     }
// );
$("#save").click(function(){
	var request_data = {"reference_name":$('#reference_name').text(),
						"reference_type":$('#reference_name').text(),
						"reference_link":$('#reference_name').text(),
						"reference_description":$('#reference_name').text(),
						"reference_status":$('#reference_name').text()}
	$.ajax({
	    url: "/polls/",
	    type: "post", // or "get"
	    data: {'reference_data':request_data},
	    success: function(data) {
	      alert(data.result);
    }});
});

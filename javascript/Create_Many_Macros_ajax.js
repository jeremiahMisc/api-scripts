//The following will make AJAX calls to create a specified number of macros
//To run this copy and paste this in the console window on the agent interface side
//Curently AJAX calls through the console is not rate limited

// Modify the loop counter and the variables as necessary
for (var i = 0; i < 1000; i++) { //currently creates 1000 macros
	$.ajax('/api/v2/macros.json', {
			'type': 'POST',
			'contentType': 'application/json',
			'data': JSON.stringify({ //The following is the JSON payload for the macro
				"macro": {
					"title": "Take it!",
					"actions": [{
						"field": "group_id",
						"value": "current_groups"
					}, {
						"field": "assignee_id",
						"value": "current_user"
					}]
				}
			})
		})
		.done(function(data) {
			console.log("added macro #", i);
		})
		.fail(function() {
			console.log("request failed");
		});
}
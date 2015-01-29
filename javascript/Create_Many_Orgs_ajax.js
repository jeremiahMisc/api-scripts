//The following will make AJAX calls to create a specified number of macros
//To run this copy and paste this in the console window on the agent interface side
//Curently AJAX calls through the console is not rate limited


// Modify the loop counter and the variables as necessary



for (i = 0; i < 200; i++) { //currently will create 200 orgs
	var name = 'Org_' + i; // Org name, will create Org_1, Org_2 etc.
	(function(index) {
		$.ajax('/api/v2/organizations.json', {
				'type': 'POST',
				'contentType': 'application/json',
				'data': JSON.stringify({ //The following is the JSON payload for the org
					'organization': {
						'name': name
					}
				})
			})
			.done(function(data) {
				console.log("added org ", index);
			})
			.fail(function(jqXHR) {
				console.log("request failed");
				console.log('Error creating org:\n' + jqXHR.status + ' ' + jqXHR.responseText);
			});
	})(name);

}
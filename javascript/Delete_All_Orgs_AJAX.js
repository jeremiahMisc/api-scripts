/*The following will make AJAX calls to delete all objects for an endpoint in a Zendesk

To run this:
- Modify the code below to the endpoint you want.
	- Currently it targets the organizations endpoint. If you want to delete all tickets,
	delete all instances of the word organizations and change it to tickets. 
- Log into the Zendesk Agent inteface
- Copy and paste the code below in the console window for the browser
- Hit enter
*/


var IDArray = [];
var next_page;

function deleteIDs(IDArray) {
	for (var i = 0; i < IDArray.length; i++) {
		(function(index) {
			$.ajax('/api/v2/organizations/' + IDArray[i] + '.json', { // change endpoint as you wish
					'type': 'DELETE'
				})
				.done(function(data) {
					console.log(index);
					console.log("Deleted org #" + index); // success message
				})
				.fail(function(data) {
					console.log("Delete failed for org #" + index); // failure message
				});
		})(IDArray[i]);

	}
}


function getIDs(pageNum) {
	if (next_page === null) {
		deleteIDs(IDArray);
		return;
	}
	pageNum++;
	$.getJSON('/api/v2/organizations.json?page=' + pageNum, function(request) { // change endpoint as you wish
			var k = 0;
			next_page = request.next_page;
			while (k < request.organizations.length) {
				var orgID = request.organizations[k].id;
				IDArray.push(orgID);
				k++;
			}
		})
		.done(function(data) {
			getIDs(pageNum);
		});
}


getIDs(0); //give me a pageNum to start from
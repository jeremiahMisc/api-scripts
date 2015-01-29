<!-- The Following Creates a ticket in Zendesk using the curl function-->
<?php
$ch = curl_init(); 
//there is error CURLOPT_FOLLOWLOCATION cannot be activated when an open_basedir is set 
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true); 
curl_setopt($ch, CURLOPT_MAXREDIRS, 10 );
//Change Subdomain Below
curl_setopt($ch, CURLOPT_URL, "https://{subdomain}.zendesk.com/api/v2/tickets.json");
//Chnage Email address below 
curl_setopt($ch, CURLOPT_USERPWD, "{email_address}/token:{api_token}");
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
//JSON Payload for tiket object
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"ticket":{"requester":{"name":"The Customer", "email":"thecustomer@domain.com"}, "submitter_id":410989, "subject":"My printer is on fire!", "comment": { "body": "The smoke is very colorful." }}}'); 
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-type: application/json')); 
// curl_setopt($ch, CURLOPT_USERAGENT, "MozillaXYZ/1.0");x
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 
curl_setopt($ch, CURLOPT_TIMEOUT, 10);
$response = curl_getinfo($ch);
$responses = curl_getinfo($ch [0]);
$output = curl_exec($ch);

echo "<br>output " .$output;
print_r($response);
?>
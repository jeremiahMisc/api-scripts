<!-- The Following Sets a user's password in Zendesk using the curl function-->
<?php
$ch = curl_init(); 
//there is error CURLOPT_FOLLOWLOCATION cannot be activated when an open_basedir is set 
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true); 
curl_setopt($ch, CURLOPT_MAXREDIRS, 10 );
//Change Subdomain Below and user_id
curl_setopt($ch, CURLOPT_URL, "https://{subdoman}.zendesk.com/api/v2/users/{user_id}/password.json");
//Change Email Address Below
curl_setopt($ch, CURLOPT_USERPWD, "{email_address}/token:{api_token}");
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
//Password to set for the user
curl_setopt($ch, CURLOPT_POSTFIELDS, '{"password": "php123456"}'); 
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
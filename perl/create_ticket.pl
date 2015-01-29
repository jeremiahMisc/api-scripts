use strict;
use warnings;
use LWP::UserAgent;
use JSON;
use MIME::Base64;

# New ticket info
my $subject = 'My printer is on fire!';
my $body = 'The smoke is very colorful.';

# Package the data in a data structure matching the expected JSON
my %data = (
    ticket => {
        subject => $subject,
        comment => {
            body => $body,
        },
    },
);

# Encode the data structure to JSON
my $json = JSON->new;
my $data = $json->encode(\%data);

# Set the request parameters
my $url = 'https://{subdomain}.zendesk.com/api/v2/tickets.json';
my $credentials = encode_base64('{email_address}/token:{api_token}');

# Create the user agent
my $ua = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 }); 

# Do the HTTP post request
my $response = $ua->post($url, 'Content' => $data, 'Content-Type' => 'application/json', 'Authorization' => "Basic $credentials");

# Check for HTTP errors
die 'http status: ' . $response->code . '  ' . $response->message 
    unless ($response->is_success);

# Report success
print "Successfully created the ticket.\n";
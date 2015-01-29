use strict;
use warnings;
use LWP::UserAgent;
use JSON;
use MIME::Base64;

# Section to create article in
my $section_id = '200100440';

# New article info
my $title = 'How to take pictures in low light';
my $body = 'Use a tripod';

# Package the data in a data structure matching the expected JSON
my %data = (
    article => {
        title => $title,
        body => $body,
    },
);

# Encode the data structure to JSON
my $json = JSON->new;
my $data = $json->encode(\%data);

# Set the request parameters
my $url = "https://{subdomain}.zendesk.com/api/v2/help_center/sections/$section_id/articles.json";
my $credentials = encode_base64('{email_address}/token:{api_token}');

# Create the user agent
my $ua = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 }); 

# Do the HTTP post request
my $response = $ua->post($url, 'Content' => $data, 'Content-Type' => 'application/json', 'Authorization' => "Basic $credentials");

# Check for HTTP errors
die 'http status: ' . $response->code . '  ' . $response->message 
    unless ($response->is_success);

# Report success
print "Successfully created the article.\n";
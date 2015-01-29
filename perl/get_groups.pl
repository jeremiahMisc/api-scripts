=Description

Gets the name of the first group, from the groups present in the account.

Gets the name of each group present in the account

=cut

use strict;
use warnings;
use LWP::UserAgent;
use JSON;

# Set the request parameters
my $url = 'https://{subdomain}.zendesk.com/api/v2/groups.json';
my $netloc = '{subdomain}.zendesk.com:443';        # omit https://
my $realm = 'Web Password';
my $uname = '{email_address}/token';
my $pass = '{api_token}';

# Create a user agent with your credentials
my $ua = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 }); 
#ssl_opts => { verify_hostname => 0 } added to prevent error: 
#http status: 500  Can't verify SSL peers without knowing which Certificate Authorities to trust
$ua->credentials($netloc, $realm, $uname, $pass);

# Do the HTTP get request
my $response = $ua->get($url);

# Check for HTTP error codes
die 'http status: ' . $response->code . '  ' . $response->message
    unless ($response->is_success);

# Decode the JSON into a Perl data structure and use the data
my $json = JSON->new;
my $data = $json->decode($response->content());

# Example 1: Get the name of the first group in the list
print "First group = " . $data->{'groups'}[0]{'name'} . "\n";

# Example 2: Get the name of each group in the list
my @groups = @{ $data->{'groups'} };
foreach my $group ( @groups ) {
    print $group->{"name"} . "\n";
}
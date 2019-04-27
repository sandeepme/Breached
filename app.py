import argparse
import api

# Create the parser object
parser = argparse.ArgumentParser(description = 'Check if your account has been breached.')

# Add the arguments we require
parser.add_argument('email', type = str, help= 'The email that you would like to check for breaches. Enter \'none\' if you\'re only checking for the password.')
parser.add_argument('password', type = str, help= 'The password that you would like to check for breaches. Enter \'none\' if you\'re only checking for the account.')

# Parse the arguments we received
args = parser.parse_args()

# Only check for args that are not 'none'
if args.email != 'none': 
    api.checkAccount(args.email)
if args.password != 'none':
    api.checkPassword(args.password)
import argparse
import api

# Create the parser object
parser = argparse.ArgumentParser(description = 'Check if your account has been breached.')

# Add the arguments we require
parser.add_argument('email', type = str, help= 'The email that you would like to check for breaches.')

# Parse the arguments we received
args = parser.parse_args()

api.checkAccount(args.email)
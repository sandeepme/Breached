# Breached

This is a simple python program to be run in the command line which allows you to check if your email address and/or password has been compromised. The passwords are checked using a k-anonymity model that allows a password to be searched using a partial hash which increases security. For more information, visit https://en.wikipedia.org/wiki/K-anonymity

## Running the Program

It is strongly suggested to use Pipenv to run the program and to ensure that you have Python 3.
```
pipenv shell
python app.py [email] [password]
```
If you do not want to check either the email or password, enter 'none' for that argument.

## Help

For more information in the command line, use the help flag.
```
python app.py --help
```

## Credits

Thank you to Have I Been Pwned for creating a wonderful API. Visit the docs at https://haveibeenpwned.com/API/v2

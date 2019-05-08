import requests
import json
import hashlib

def checkAccount(email: str) -> None:
    """
    Check and print whether an email address has been compromised.

    The method calls the api to check if it has been comprimised and if so, the
    number of times. It then prints out the appropriate output.

    Parameters
    ----------
    email : str
        The email address that we require to be checked.

    """

    # The api endpoint with the email that we would like to check for
    url = 'https://haveibeenpwned.com/api/v2/breachedaccount/' + email + '?truncateResponse=true'

    # Specify the user agent as required by the API
    headers = {
        'User-Agent': 'Python breach checker'
    }

    # Make the request and store it in response
    response = requests.get(url, headers = headers)

    # If there was at least 1 breach (we get a 200 response code)
    if response.status_code is 200:
        data = response.json()
        print('You have a total of ' + str(len(data)) + ' breach(es).')
        print('The websites that were breached are:')
        # Iterate through the list
        for each in data:
            # Each breach is stored as a dictionary
            print(each["Name"])
    # Else if there were no breaches
    else:
        print('Congrats! You have no breaches asscoiated with ' + email)

def checkPassword(password: str) -> None:
    """
    Check and print whether a password has been compromised.

    The method calls the api to check if it has been comprimised and if so, the
    number of times. We only send the first 5 chars of the hashed (SHA-1)
    password to maintain security. Upon receiving a list of hashed passwords
    that starts with those 5 chars, we search for our password. The method finally
    then prints out the appropriate output.

    Parameters
    ----------
    password : str
        The password that we require to be checked.

    """

    # Encode the password and then hash it using sha1
    hash = hashlib.sha1(password.encode('utf-8'))

    # Assign the hexadecimal value of the hash to hash
    hash = hash.hexdigest()

    # We only need to send the first 5 characters of the hash to the API
    url = 'https://api.pwnedpasswords.com/range/' + hash[:5]

    # Make the request
    response = requests.get(url)

    # If we have received passwords to search through (we get a 200 response code)
    if response.status_code == 200:
        numOfTimes = __comparePasswords(hash, response.text)     

    # Else if there were no passwords that we received
    if numOfTimes == 0:
        print('Congrats! Your password is not comprimised.')
    else:
        print('Uh oh! Your password has been comprimised. It appears in ' + str(numOfTimes) + ' records.')

def __comparePasswords(hashedPass: str, apiResponse: str) -> int:
    """
    A helper method to check for the number of times a password appears in the API response.

    This method does some string processing as the API response is not in an appropriate JSON
    format. Therefore, we have to trim some special chars.

    Parameters
    ----------
    hashedPass : str
        The SHA-1 hashed password that we are checking for.
    apiResponse : str
        A string containing all the passwords whose first 5 chars match ours.

    Returns
    -------
    int
        The number of times our password appeared.

    """

    # The number of times the password appeared
    numOfTimes: int = 0

    # Split the string by \n to create a list
    allHashes = apiResponse.split('\n')
    
    # Go through all the responses received to check if there was a match
    for aHash in allHashes:
        compareTo = aHash.split(':')

        # Compare the hashed password (excluding the first 5 chars) and the response
        if hashedPass[5:].upper() == compareTo[0]:
            # Remove '\r' and store the number of occurences
            numOfTimes = (compareTo[1].split('\r'))[0]

    return numOfTimes

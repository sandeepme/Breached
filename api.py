import requests

def checkAccount(email):
    # The api point with the email that we would like to check for
    url = 'https://haveibeenpwned.com/api/v2/breachedaccount/' + email + '?truncateResponse=true'

    # Specify the user agent as required by the API
    headers = {
        'User-Agent': 'Python breach checker'
    }

    # Make the request and store it in response
    response = requests.get(url, headers = headers)

    # If there was at least 1 breach
    if response.status_code is 200:
        data = response.json()
        print('You have a total of ' + str(len(data)) + ' breach(es).')
    # If there were no breaches
    else:
        print('Congrats! You have no breaches asscoiated with ' + email)
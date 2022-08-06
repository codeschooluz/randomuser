import requests

def get_randomuser()->dict:
    """
    Returns a random user from the randomuser.me API
    args: None
    returns: a dictionary with the user's data
    """
    url = 'https://randomuser.me/api/'
    response = requests.get(url)
    data = response.json()
    return data['results'][0]

def get_randomusers(amount:int)->list:
    """
    Returns a list of random users from the randomuser.me API
    args: amount:int
    returns: a list of dictionaries with the user's data
    """
    url = 'https://randomuser.me/api/?results={}'.format(amount)
    response = requests.get(url)
    data = response.json()
    return data['results']
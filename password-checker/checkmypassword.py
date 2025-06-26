import requests
import hashlib
import sys

def request_api_data(hash_char):
    url = 'https://api.pwnedpasswords.com/range/' + hash_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashe = (line.split(':') for line in hashes.text.splitlines())

    for h, count in hashe:
        if h == hash_to_check:
            return count
    return 0
    


def pwned_api_check(password):
    hash_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char , tail = hash_password[:5] , hash_password[5:]

    response = request_api_data(first5_char)
    
    # print(response)
    # print(hash_password)
    return get_password_leaks_count(response, tail)


# pwned_api_check('123')

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count :
            print(f'{password} was found {count} times... password badal lo')
        else:
            print(f'{password} was not found. lage raho')

main(sys.argv[1:])
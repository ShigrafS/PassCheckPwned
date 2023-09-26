import requests
import hashlib

def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, please check the api and try again.')
  return res
  
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(first5_char, tail)
    #return read_res(response)
    return get_password_leaks_count(response, tail)
  
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        #print(h, count)
        if h == hash_to_check:
            return count
    return 0
  
#pwned_api_check('123456789')

pass_check = input("Please enter the password to be checked.")
print(f'The password has been leaked {pwned_api_check(pass_check)} times.');

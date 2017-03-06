### Test for secrets.py
# Should return length of secret token

from functions import getSecret

def test_secrets():
    
    access_token = getSecret('twitter-rob')
    
    assert (len(access_token))
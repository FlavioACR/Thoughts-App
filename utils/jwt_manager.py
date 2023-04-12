from jwt import encode, decode

def create_token(data: dict) -> str:
    """
    create_token:
    Take a data in dictionary datatype, encode and return a string with the token of the data.
    
    Arguments:
    * data : dict
    
    Return:
    * token: str
    
    """
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    """
    validate_token:
    Take a token in string datatype and dencode to return the date encode.
    
    Arguments:
    * token : str
    
    Return:
    * data: dict
    
    """
    data: dict = decode(token, key="my_secret_key", algorithms=['HS256'])
    return data
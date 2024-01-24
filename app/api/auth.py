from flask_httpauth import HTTPTokenAuth


token_auth = HTTPTokenAuth(scheme="Bearer")

tokens = {"secret-token-1": "john", "secret-token-2": "susan"}


@token_auth.verify_token
def verify_token(token):
    print(f"my token {token}")
    if token in tokens:
        return tokens[token]

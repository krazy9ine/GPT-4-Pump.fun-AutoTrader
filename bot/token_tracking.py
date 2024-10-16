import requests

def get_token_data(token_address):
    url = f"https://api.mainnet-beta.solana.com"
    headers = {"Content-Type": "application/json"}
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenSupply",
        "params": [token_address]
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

# Example usage
token_address = "TOKEN_ADDRESS_HERE"
print(get_token_data(token_address))

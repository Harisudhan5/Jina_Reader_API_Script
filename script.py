import requests

# Base endpoint
base_url = "https://r.jina.ai/"

# Input URL to be appended
input_url = "https://www.bingotingo.in/canvas-design-software/"

# Full URL with the input URL appended after a plus (+) sign
full_url = base_url + input_url

# Headers to include in the request
headers = {
    "Accept": "text/event-stream"
}

# Make the request with streaming enabled
response = requests.get(full_url, headers=headers, stream=True)

# Handle the streaming response
try:
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            print(decoded_line)
finally:
    response.close()

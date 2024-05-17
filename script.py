import requests

base_url = "https://r.jina.ai/"
input_url = "https://www.bingotingo.in/canvas-design-software/"

full_url = base_url + input_url

headers = {
    "Accept": "text/event-stream"
}

response = requests.get(full_url, headers=headers, stream=True)

try:
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            print(decoded_line)
finally:
    response.close()

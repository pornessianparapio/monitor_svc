import requests

def upload_to_server(filepath):
    url = "https://your-server.com/upload"
    with open(filepath, 'rb') as file:
        response = requests.post(url, files={"file": file})
        if response.status_code == 200:
            print("Upload successful")
        else:
            print("Upload failed")

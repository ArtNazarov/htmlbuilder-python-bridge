from flask import Flask, request
import zipfile
import os

port_num = 8080
use_route = '/upload'
APIKey = 'myapi'
public = os.path.dirname(os.path.abspath(__file__))
print(public)

def unpack_zip(zip_file_path, destination_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_path)

app = Flask(__name__, static_url_path='/', static_folder=public)

@app.route(use_route, methods=['POST'])
def upload_file():
    api_key = request.values.get('API')
    print(api_key)
    if api_key == APIKey:
        file = request.files['file']
        filename = file.filename
        file.save(filename)
        full_path = os.path.dirname(os.path.abspath(__file__)) + '/' + filename
        unpack_zip(full_path, public)
        try:
            os.remove(full_path)
            print(f"File '{full_path}' deleted successfully.")
        except OSError as e:
            print(f"Error deleting file '{full_path}': {e}")
        return 'File uploaded successfully.'
    else:
        return 'Invalid APIKey. File upload not allowed.'


@app.route('/')
def home():
    return f"Wait zip arcive at route {use_route} and port {port_num}"


if __name__ == '__main__':
    app.run(port=port_num)





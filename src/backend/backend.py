from flask import Flask, request
import re
from Transcript_Filter import filter_vtt, filter_txt
from waitress import serve
from flask_cors import CORS, cross_origin

backend = Flask(__name__)
backend.config.from_object("config")

# For Rudy: should be translated to localhost:5000/receive-transcript
# can be tested on windows cmd with command:
# curl -X POST -H "Content-Type:application/json" -d "{\"transcript_data\":\"Hello\",\"file_extension\":\"World\"}" 47.155.248.89:8080/receive-transcript
@backend.route('/receive-transcript/')
@cross_origin(supports_credentials=True, origin='*')
def get_transcript():
    print(request.headers["file_extension"])
    return "Success"

def filter_transcript(transcript_data, file_extension):
    if file_extension == "vtt":
        transcript_data = filter_vtt(transcript_data)

    elif file_extension == "txt":
        pass




if __name__ == '__main__':
    if backend.config['DEBUG']:
        backend.debug = True
        backend.run()
    else:
        serve(backend, host='0.0.0.0',port=8080,threads=1)
 
import os
from flask import Flask, request, session, send_file, send_from_directory, safe_join, abort, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('HELLO WORLD')


UPLOAD_FOLDER = '/home/adhithya/AIkenist/Covid/covidbackend/static//'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

fname = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app, expose_headers='Authorization')

app.config["RESULT"] = "/home/adhithya/AIkenist/Covid/covidbackend/static/test_docs"


@app.route('/upload', methods=['POST'])
def fileUpload():
    target = os.path.join(UPLOAD_FOLDER,'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file = request.files['file']
    fname.append(file.filename)
    print(fname[0])
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])
    file.save(destination)
    session['uploadFilePath'] = destination
    return jsonify({'fileName': fname[0]})

@app.route("/get-image", methods=['GET'])
def get_image():

    try:
        return send_from_directory(app.config["RESULT"], filename=fname[0], as_attachment=True)
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=8000)
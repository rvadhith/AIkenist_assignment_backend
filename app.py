 
import os
from flask import Flask, request, session, send_file, send_from_directory, safe_join, abort, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('HELLO WORLD')


UPLOAD_FOLDER = '/home/adhithya/AIkenist/Covid/covidbackend/static//'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app, expose_headers='Authorization')

app.config["RESULT"] = "/home/adhithya/AIkenist/Covid/covidbackend/static/images"


@app.route('/upload', methods=['POST'])
def fileUpload():
    target = os.path.join(UPLOAD_FOLDER,'images')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])
    file.save(destination)
    session['uploadFilePath'] = destination
    return jsonify({'fileName': file.filename})

@app.route("/get-image/<image_name>", methods=['GET'])
def get_image(image_name):

    try:
        return send_from_directory(app.config["RESULT"], filename=image_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=8000)
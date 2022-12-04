from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import datetime
import os

ALLOWED_FILES = ["csv"]

def allowedFiles(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_FILES

def create_app():
    app = Flask(__name__)

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            file = request.files['file']
            if file and allowedFiles(file.filename):
                filename = secure_filename(file.filename)
                new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
                file.save(os.path.join('input', new_filename))

                return send_from_directory('output', new_filename)
            # return redirect(url_for('download'))
            return 'uploaded'
        return render_template('upload.html')
    return app

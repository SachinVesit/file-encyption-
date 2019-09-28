from flask import *
import os
from connection import *
from werkzeug.utils import secure_filename
app = Flask(__name__, static_url_path='/static')
app.secret_key = os.urandom(24)
UPLOAD_FOLDER = '/home/sachin/Desktop/uploadfile/temp'
ALLOWED_EXTENSIONS = set(['txt'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('upload.html')

def getextension(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload():

    # check if the post request has the file part
    if 'file' not in request.files:
        # flash('No file part')
        return render_template('upload.html',error="file not selected")
        
    file1 = request.files['file']

    # if user does not select file, browser also
    # submit an empty part without filename
    if file1.filename == '':
        # flash('No selected file')
        return render_template('upload.html',error="file not selected")


    if file1 and getextension(file1.filename):
        # if file1.content_type == "text/plain":
        filename = secure_filename(file1.filename)
        filepath = UPLOAD_FOLDER + '/' + filename
        if os.path.isfile(filepath):
            return render_template('upload.html',error = "file already uploaded or other file with same name exist")    
        else:
            db.uploadedfiles.insert(
				{
					'username': username,
					'filename': filename
				}
			)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('upload.html',d = "file uploaded")

if __name__ == "__main__":
    app.run(debug=True)

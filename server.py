import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename
from collections import OrderedDict
from operator import itemgetter

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

my_result={}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  # this has changed from the original example because the original did not work for me
    return filename[-3:].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/upload")
def upload():
	return render_template('upload.html')

@app.route("/uploader", methods=['POST','GET'])
def uploader():
	if request.method == 'POST':
		f = request.files['file']
		f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
		os.system("python label_image.py "+app.config['UPLOAD_FOLDER']+"/"+secure_filename(f.filename))
		fin = open("results.txt","r")
		my_result = eval(fin.read())
		fin.close()
		d = OrderedDict(sorted(my_result.items(), key=itemgetter(0),reverse=True))
		d = list(d.items())
	return str("Predicted Item : "+d[0][0]+" Probability :  "+str(d[0][1]))


if __name__ == "__main__":
    app.run()

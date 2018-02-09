import os
from flask import Flask, render_template, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
app = Flask(__name__)




@app.route('/upload',methods=['POST'])
def upload():
	imageFile = request.files['image']
	img_name = secure_filename(imageFile.filename)
	imageFile.save("./Uploads", img_name))

if __name__=='__main__':
    app.run()
import os
import sys 
from flask import (
     Flask, 
     request, 
     render_template,
     send_from_directory)

from predict import predict

UPLOAD_FOLDER='./static/mask_image'

app = Flask(__name__)

#ホーム画面
@app.route('/')
def index():
    return render_template('index.html')

#アップロード画面
@app.route('/predict')
def upload_user_files():
    return render_template('predict.html')

@app.route('/upload' , methods=['GET', 'POST'])
def upload():
    if request.method=='POST':
       upload_file = request.files['upload_file']
       img_path = os.path.join(UPLOAD_FOLDER,upload_file.filename)
       upload_file.save(img_path)
       predict(img_path)
       predict_img_path='./tmp/mask_remove.png'
       return render_template('result.html', img_path=img_path,predict_img_path=predict_img_path)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/logo'),'mask_logo.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/tmp/<path:filename>')
def send_file(filename): 
    return send_from_directory('tmp', filename)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, send_file
from pymongo import MongoClient
import gridfs
from io import BytesIO
from bson.objectid import ObjectId
from image_utils import save_image, get_content, save_text

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['dontpad']
fs = gridfs.GridFS(db)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        page_name = request.form.get('page_name')
        return redirect(url_for('page', page_name=page_name))
    return render_template('index.html')



# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if 'file' in request.files:
#             file = request.files['file']
#             save_image(db, file.read(), 'uploaded_image')
#             return 'Image uploaded successfully!'
#     return render_template('index.html')


@app.route('/<page_name>', methods=['GET', 'POST'])
def page(page_name):
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            save_image(db, file.read(), page_name)
        if 'text' in request.form:
            text = request.form.get('text')
            save_text(db, text, page_name) 

    content = get_content(db, page_name)
    return render_template('page.html', page_name=page_name, content=content)

@app.route('/image/<file_id>')
def get_image(file_id):
    try:
        file = fs.get(ObjectId(file_id))
        return send_file(BytesIO(file.read()), mimetype=file.content_type)
    except gridfs.errors.NoFile:
        return "File not found", 404


if __name__ == '__main__':
    app.run(debug=True)

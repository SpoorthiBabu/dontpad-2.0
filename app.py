from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import gridfs
from image_utils import save_image

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['dontpad']
fs = gridfs.GridFS(db)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/<page_name>', methods=['GET', 'POST'])
# def page(page_name):
#     if request.method == 'POST':
#         if 'file' in request.files:
#             file = request.files['file']
#             save_image(db, file.read(), page_name)
#         if 'text' in request.form:
#             # Save text content to the database
#             pass

#     content = get_content(db, page_name)
#     return render_template('page.html', page_name=page_name, content=content)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            save_image(db, file.read(), 'uploaded_image')
            return 'Image uploaded successfully!'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

# from pymongo import MongoClient, gridfs
# from datetime import datetime

# def save_image(db, image_bytes, page_name):
#     fs = gridfs.GridFS(db)
#     fs.put(image_bytes, filename=f"{page_name}_{datetime.now()}")

# def get_content(db, page_name):
#     fs = gridfs.GridFS(db)
#     content = []
#     for file in fs.find({"filename": {"$regex": f"^{page_name}_"}}):
#         content.append({
#             "type": "image",
#             "content": fs.get(file._id).read()
#         })
#     return content

import gridfs
from pymongo import MongoClient
from datetime import datetime


# def save_image(db, image_bytes, filename):
#     fs = gridfs.GridFS(db)
#     fs.put(image_bytes, filename=filename)

def save_image(db, image_bytes, page_name):
    fs = gridfs.GridFS(db)
    file_id = fs.put(image_bytes, filename=f"{page_name}_{datetime.now()}", content_type="image/jpeg")
    return file_id

def save_text(db, text, page_name):
    texts_collection = db['texts']
    texts_collection.insert_one({'page_name': page_name, 'text': text, 'timestamp': datetime.now()})

def get_content(db, page_name):
    fs = gridfs.GridFS(db)
    content = []
    
    # Get images
    for file in fs.find({"filename": {"$regex": f"^{page_name}_"}}):
        content.append({
            "type": "image",
            "content": fs.get(file._id).read()
        })

    # Get text
    texts_collection = db['texts']
    texts = texts_collection.find({"page_name": page_name}).sort("timestamp", -1)
    for text in texts:
        content.append({
            "type": "text",
            "content": text['text']
        })

    return content

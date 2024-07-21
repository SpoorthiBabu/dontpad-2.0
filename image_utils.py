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

def save_image(db, image_bytes, filename):
    fs = gridfs.GridFS(db)
    fs.put(image_bytes, filename=filename)


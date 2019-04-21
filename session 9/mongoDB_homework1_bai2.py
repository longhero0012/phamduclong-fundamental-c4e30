import pymongo
client = pymongo.MongoClient ("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
db = client.c4e

bai_post = {
    "title":"phạm đức long",
    "author":"nooo",
    "content":"em ở đây nè anh khánh <3"
}
db.posts.insert_one(bai_post)
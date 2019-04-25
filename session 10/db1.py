import pymongo
 

client = pymongo.MongoClient("mongodb+srv://admin:2fG9mSJu5OGSiWtI@demo-cluster-mvmw2.mongodb.net/test?retryWrites=true")
db = client.test

def get_all():
    return list(db.xedaps.find({}))

def add_bike(model,daily_fee,image_url,year):
    db.xedaps.insert_one({'Model' : model, 'Daily_fee' : daily_fee, 'Image_url' : image_url, 'Year' : year})

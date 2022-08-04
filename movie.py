import pymongo

if __name__ == '__main__':
    print("welcome to pymongo")
    from pymongo import MongoClient
    client = MongoClient()
    client = MongoClient("mongodb://localhost:27017")
    db = client['shreyashetty']
    collection = db['Movie']
    dictionary = { "name": "Harry Potter and the Order of the Phoenix", "img": "https://bit.ly/2IcnSwz", "summary":"Harry Potter and Dumbledore's warning about the return ofLord Voldemort is not heeded by the wizard authorities who, in turn, look toundermine Dumbledore's authority at Hogwarts and discredit Harry"}
    collection.insert_one(dictionary)


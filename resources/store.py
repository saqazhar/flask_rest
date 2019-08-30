from models.store import StoreModel
from flask_restful import Resource, reqparse

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"messgae":"Store Not Found"}

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"Message":"Store Already Exist"}
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"Message":"An Error occured"}
        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        try:
            store.delete_from_db()
        except:
            return {"Message":"An Error Occured"}
        return{"Message":"Store Deleted"}


class StoreList(Resource):
    def get(self):
        return{"stores": list(map(lambda x:x.json(), StoreModel.query.all()))}




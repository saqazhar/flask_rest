from flask_restful import Resource, reqparse
from flask import request
from flask_jwt import jwt_required
from models.item import ItemModel



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = "This field cannot be left blank"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store_id."
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        # item = next(filter(lambda x : x['name']== name, items), None)
        return {"Messgae":"Item Not Found"}, 404

    @jwt_required()
    def post (self, name):
        if ItemModel.find_by_name(name):
            return {"message":"An item already exist".format(name)}, 404

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return{"Messgae":"An Error Occurd"}, 500
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message":"Item deleted"}
        return {"Message":"Can't find the Item"}, 404

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
      
        if item:
            item.price = data['price']  
        else:
            item = ItemModel(name, **data)

        item.save_to_db()  

        return item.json()


class Newitem(Resource):
    @jwt_required()
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}








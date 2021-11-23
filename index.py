from flask import Flask,jsonify
from flask_restful import Resource, Api
import sqlite3
import traceback
import math 

app = Flask(__name__)
api = Api(app)


class Helpers:
    def distance_calculate(self,lat1,lon1,lat2,lon2):
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        distance = math.sqrt(dlat**2 + dlon**2)
        return distance

    def obj_append_distance(self,obj,latitude,longitude):
        distance = self.distance_calculate(latitude,longitude,obj['latitude'],obj['longitude'])
        tups = list(obj.items()) + [('distance',distance)]
        return dict(tups)

    def array_sort_distance(self,array,latitude,longitude):
        array_with_distance = [self.obj_append_distance(obj,latitude,longitude) for obj in array]
        return sorted(array_with_distance,key=lambda obj: obj['distance'])[:5]

class BoatsDB:
    def __init__(self):
        self.con = sqlite3.connect('boats.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE if not exists boats
                   (make text, model text, length real, latitude real, longitude real)''')
        self.con.commit()

    def update_table(self,make,model,length,latitude,longitude):
        self.cur.execute("INSERT INTO boats VALUES ('{make}','{model}',{length},{latitude},{longitude})".format(
            make=make,model=model,length=length,latitude=latitude,longitude=longitude))
        self.con.commit()

    def read_table(self):
        list_of_lists = [row for row in self.cur.execute('SELECT * FROM boats')]
        headers = ['make','model','length','latitude','longitude']
        array = [dict(zip(headers,row)) for row in list_of_lists]
        return array

db = BoatsDB()

class Retrieve(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('latitude',type=float,required=True)
        parser.add_argument('longitude',type=float,required=True)
        args = parser.parse_args()
        try:
            array = db.read_table()
            return jsonify(Helpers().array_sort_distance(array,args['latitude'],args['longitude']))
        except Exception as err:
            error_message = traceback.format_exc()
            return error_message

class Store(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('make',type=str,required=True)
        parser.add_argument('model',type=str,required=True)
        parser.add_argument('length',type=float,required=True)
        parser.add_argument('latitude',type=float,required=True)
        parser.add_argument('longitude',type=float,required=True)
        args = parser.parse_args()
        db.update_table(args['make'],args['model'],args['length'],args['latitude'],args['longitude'])
        return args


api.add_resource(Retrieve, '/retrieve')
api.add_resource(Store, '/store')

@app.route("/")
def index():
    return 'HarborMoor API'

if __name__ == '__main__':
    app.run(debug=True)
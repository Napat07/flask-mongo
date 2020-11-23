from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'ITSdb'
app.config['MONGO_URI'] = 'mongodb://ITSdb:new0865944040@its-shard-00-00.9hjx2.mongodb.net:27017,its-shard-00-01.9hjx2.mongodb.net:27017,its-shard-00-02.9hjx2.mongodb.net:27017/ITSdb?ssl=true&replicaSet=atlas-1jomad-shard-0&authSource=admin&retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/user', methods=['GET'])
def get_all_users():
  user = mongo.db.users
  output = []
  for s in user.find():
    output.append({'name' : s['name'], 'distance' : s['distance']})
  return jsonify({'result' : output})



if __name__ == '__main__':
    app.run(debug=True)

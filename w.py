from flask import Flask, Response
import json
import http

app = Flask(__name__)

# Route 1 'weapon/all'
@app.route('weapon/all')
def get_all_weapons():
  with open('weapons.json') as f:
    data = json.load(f)

  return data

# Route 2 'weapon/<item_id>'
@app.route('weapon/<item_id>')
def get_weapon_by_id(item_id):
  with open('weapon.json') as f:
    data = json.load(f)

  for weapon_name in data:
    if data[weapon_name]['item_id'] == int(item_id):
      return json.dumps(data[weapon_name])
#  return {'error':'No weapon with requested ID was found'}
  return Response("{'error':'No weapon with requested ID was found'}", status = http.HTTPSTATUS.NOT_FOUND)

# Route 3 'armour/all'

# Route 4 'armour/<item_id>'

# Route 5 
if __name__ == '__main__':
  app.run(debug=True)






















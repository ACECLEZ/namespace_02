from flask import Flask
app = Flask(__name__)
@app.route('/')

@app.route('/animal/<noise>')
def which_animal(noise):
  if noise == 'meow':
    return 'cat'
  elif noise == 'woof':
    return 'dog'
  else:
    return 'unknown'
  
app.run(debug=True, port=5500)
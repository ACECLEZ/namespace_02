from flask import Flask

app = Flask(__name__)

@app.route('/')
def wave():
    return "hi"

@app.route('/animal/<noise>')
def which_animal(noise):
    if noise == 'meow':
        return 'cat'
    elif noise == 'woof':
        return 'dog'
    else:
        return 'unknown'

if __name__ == '__main__':
    app.run(debug=True, port=5500)

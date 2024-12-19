from flask import Flask
import random

app = Flask(__name__)


# print(__name__)
# print(random, __name__)

@app.route('/')
def hello_world():
    # return "Hello, World!"
    return '<h1 style="text-align:center">Hello World</h1>'\
            '<p>This is a paragraph.</p>'\
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWozOHF2c2JkNTE1MXg1bHo4YWN5dGs2ZGd0dWM3b3B5Z2h3MHZyNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/guNXesWtLfqOfnWwmx/giphy.gif" width=1000px></img>'
            # '<img src="https://i.natgeofe.com/k/afe51970-80c6-46c3-b047-4c407c72d874/bald-eagle-closeup_4x3.jpg" width=1000px></img>'


@app.route('/bye')

def bye():
    return "Bye!"


# creating variable paths and converting the paths to a specified data type

# @app.route("/username/<name>")
# @app.route("/username/<path:name>")
@app.route("/username/<name>/<int:number>")
# def greet(name):
def greet(name, number):
    # return f"Hello {name + '12'}!"
    return f"Hello there {name}, you are {number} years old!"


# denotes file currently being run
if __name__ == "__main__":
    # run the app in debug mode to auto-refresh
    app.run(debug=True)

#  set FLASK_APP=hello.py
# flask run
# echo $env:FLASK_APP
# $env:FLASK_APP = "hello.py"
# flask --app hello run
# the kernel refers tp the actual program that interfaces with the hardware
# cli and gui are the ways to interface with kernel

# mkdir test : create new folder
# touch server.py : create file
# rm server.py : delete file
# you should be outside that to delete it
# rm -rf test : delete folder

# decorator function is a function giving additional functionality to a function
# python functions are first class objects, can be passes around as arguments, eg int/string/float etc

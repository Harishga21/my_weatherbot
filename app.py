from flask import Flask, request, make_response
import os, json
from flask_cors import CORS,cross_origin


app = Flask(__name__)
@app.route('/')
def index():
    return 'Web App with Python Flask!'


#if __name__ == '__main__':
    object=WeatherData()
    #port = int(os.getenv('PORT', 5000))
    #print("Starting app on port %d" % port)
    #app.run(debug=True)

if __name__=='__main__':
    app.run(host='127.0.0.1',port=5080)
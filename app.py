﻿from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Docker!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
#   T r i g g e r   C I  
 #   T r i g g e r i n g   C I  
 
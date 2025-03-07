from flask import Flask

app = Flask(__name__)

@app.route('/') #this is decorator to route the URL to the function below it
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__': #this is to run the app on localhost on port 8000 if the file is run directly and not imported as a module in another file 
  app.run(debug=True, host='0.0.0.0', port=8000) #this is to run the app on localhost on port 8000
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=8080) #Could have any port, but 8080 is the defualt python-server one.

def keep_alive():  
    t = Thread(target=run)
    t.start()
"""
This is for the webserver. So in other words, preventing it from shutting down after 1 hour. Which is the defualt of replit. And its understadable since you wont be using it. To test it simply just look at the top-right corner to see I'm Alive. Or use the link which is above it. Thats the link that the other site for keep it alive 
"""

from flask import Flask
from visualization import *
from microphone import *

app = Flask(__name__)

@app.route('/start/<effect>')
def start(effect):
    print("Starting " + effect)
    setEffect(effect)
    if(not isstarted()):
        print("First one, starting audio")
        visualization_start()

    return "True"

@app.route('/stop')
def stop():
    print("Stopping audio")
    stopStream()
    return "True"

if __name__ == '__main__':
    app.run()

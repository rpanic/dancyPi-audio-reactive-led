from flask import Flask
from visualization import *
from microphone import *

app = Flask(__name__)

@app.route('/start/<effect>')
def start(effect):
    print("Starting " + effect)
    setEffect(effect)
    if('stream' not in globals() or stream == None):
        print("First one, starting audio")
        visualization_start()

@app.route('/stop')
def stop():
    print("Stopping audio")
    stream.stop_stream()
    stream.close()

if __name__ == '__main__':
    app.run()

from flask import Flask
from visualization import *
from microphone import *

app = Flask(__name__)

@app.route('/start/<effect>')
def start(effect):
    setEffect(effect)
    if('stream' not in globals() or stream == None):
        visualization_start()

@app.route('/stop')
def stop():
    stream.stop_stream()
    stream.close()

if __name__ == '__main__':
    app.run()

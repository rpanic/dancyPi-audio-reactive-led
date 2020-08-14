from flask import Flask
from visualization import *
from microphone import *
import led
import numpy as np
import config

app = Flask(__name__)

@app.route('/start/<effect>')
def start(effect):
    print("Starting " + effect)
    setEffect(effect)
    if(not isstarted()):
        print("First one, starting audio")
        threading.Timer(0.001, visualization_start).start()

    return "True"

@app.route('/stop')
def stop():
    print("Stopping audio")
    stopStream()
    led.pixels = np.tile(0, (3, config.N_PIXELS))
    led.update()
    return "True"

if __name__ == '__main__':
    app.run()

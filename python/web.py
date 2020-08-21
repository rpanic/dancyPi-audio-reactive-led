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
        threading.Timer(0.001, visualization_start).start()

    return "True"

@app.route('/startScroll/<effect>/<top>/<speed>')
def start2(effect, top, speed):
    print("Starting " + effect + " top " + top + " speed " + speed)
    setEffect(effect, int(top), int(speed))
    if(not isstarted()):
        print("First one, starting audio")
        threading.Timer(0.001, visualization_start).start()

    return "True"

@app.route('/stop')
def stop():
    print("Stopping audio")
    stopStream()
    return "True"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

import time
import numpy as np
import pyaudio
import config

def isstarted():
    global streamstopped
    return 'streamstopped' in globals() and not streamstopped

def stopStream():
    global streamstopped
    streamstopped = True

def start_stream(callback):
    global stream, pya, streamstopped
    if 'streamstopped' not in globals():
        pya = pyaudio.PyAudio()
        frames_per_buffer = int(config.MIC_RATE / config.FPS)
        print("Using default input device: {:s}".format(pya.get_default_input_device_info()['name']))
        stream = pya.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=config.MIC_RATE,
                        input=True,
                        frames_per_buffer=frames_per_buffer)
    stream.start_stream()
    streamstopped = False
    overflows = 0
    prev_ovf_time = time.time()
    while not streamstopped:
        try:
            y = np.fromstring(stream.read(frames_per_buffer, exception_on_overflow=False), dtype=np.int16)
            y = y.astype(np.float32)
            stream.read(stream.get_read_available(), exception_on_overflow=False)
            callback(y)
        except IOError:
            overflows += 1
            if time.time() > prev_ovf_time + 1:
                prev_ovf_time = time.time()
                print('Audio buffer has overflowed {} times'.format(overflows))
    
    stream.stop_stream()
    #stream.close()
    #pya.terminate()

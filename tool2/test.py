import pyaudio
import wave
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
WAVE_OUTPUT_FILENAME = moment+'.wav'
p = pyaudio.PyAudio()
stream = p
frames= []
def record():
	#CHUNK = 1024
	#FORMAT = pyaudio.paInt16
	#CHANNELS = 2
	#RATE = 44100
	#RECORD_SECONDS = 10
	#WAVE_OUTPUT_FILENAME = "voice.wav"

	#p = pyaudio.PyAudio()

	global stream
	stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

	print("* recording")
	global frames
	#frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)

	print("* done recording")


def save():
	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

def stop():
	quit()

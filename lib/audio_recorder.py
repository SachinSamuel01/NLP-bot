# File: lib/audio_recorder.py

import pyaudio
import wave
import audioop
import time
import os

def record_until_silence(output_directory, threshold=800, chunk_size=1024, format=pyaudio.paInt16, channels=1, rate=16000, silence_limit=3):
    """
    Records audio from the microphone until there is silence for at least 'silence_limit' seconds.
    Saves the recording in the specified output directory with a timestamp.
    """
    current_time = time.strftime("%Y%m%d-%H%M%S")
    filename = f"recording-{current_time}.wav"
    output_path = os.path.join(output_directory, filename)

    p = pyaudio.PyAudio()
    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)
    frames = []
    last_sound_time = time.time()

    while True:
        data = stream.read(chunk_size)
        frames.append(data)
        amplitude = audioop.rms(data, 2)  # Get amplitude of chunk
        if amplitude < threshold:
            if time.time() - last_sound_time > silence_limit:
                break  # Silence long enough to stop recording
        else:
            last_sound_time = time.time()

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    return output_path

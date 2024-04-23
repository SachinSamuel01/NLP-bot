import whisper

# Load the Whisper model of your choice
model = whisper.load_model("base", device="cuda")

def transcribe_audio(filename):
    result = model.transcribe(filename)
    print(result['text'])
    return result['text']
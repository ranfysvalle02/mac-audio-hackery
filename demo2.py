import pyaudio  
import json  
import os  
from dotenv import load_dotenv  
import requests  
import io  
import wave  
  
# Load environment variables from .env file  
load_dotenv()  
  
# Fetch Deepgram API key from environment variable  
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY", "YOUR_DEEPGRAM_API_KEY_HERE")  # Replace with your actual API key  
  
# Audio settings  
CHANNELS = 1          # Mono audio  
FRAME_RATE = 16000    # Sample rate in Hz  
CHUNK = 2048          # Number of frames per buffer  
  
# Initialize PyAudio  
audio = pyaudio.PyAudio()  
  
# Open microphone stream  
stream = audio.open(  
    format=pyaudio.paInt16,      # 16-bit integer format  
    channels=CHANNELS,           # Mono channel  
    rate=FRAME_RATE,             # Sampling rate  
    input=True,                  # Enable input  
    frames_per_buffer=CHUNK      # Buffer size  
)  
  
def record_audio():  
    """  
    Records audio until the user presses Ctrl+C and returns the recorded data.  
    """  
    frames = []  
    print("Recording started... Press Ctrl+C to stop.\n")  
    try:  
        while True:  
            data = stream.read(CHUNK, exception_on_overflow=False)  
            frames.append(data)  
    except KeyboardInterrupt:  
        print("\nRecording stopped by user.")  
    except Exception as e:  
        print(f"Error reading audio stream: {e}")  
        raise  
    print("Audio capture finished.")  
    return b''.join(frames)  # Return the audio data as bytes  
  
def send_audio_to_deepgram(audio_data):  
    """  
    Sends the recorded audio data to Deepgram's API and prints the transcription with speaker labels using utterances.  
    """  
    # Create a BytesIO object to hold the WAV file data  
    wav_buffer = io.BytesIO()  
    with wave.open(wav_buffer, 'wb') as wf:  
        wf.setnchannels(CHANNELS)  
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))  
        wf.setframerate(FRAME_RATE)  
        wf.writeframes(audio_data)  
    wav_data = wav_buffer.getvalue()  
  
    url = "https://api.deepgram.com/v1/listen"  
    headers = {  
        "Authorization": f"Token {DEEPGRAM_API_KEY}",  
        "Content-Type": "audio/wav"  
    }  
    params = {  
        "diarize": "true",  
        "utterances": "true",  
        "paragraphs": "true",  
        "smart_format": "true",  
        "language": "en-US",  
        "punctuate": "true",  
        "model": "nova",  # Changed model to 'nova' for better diarization  
    }  
    print("Sending audio data to Deepgram for transcription...\n")  
    response = requests.post(url, headers=headers, params=params, data=wav_data)  
    if response.status_code == 200:  
        res = response.json()  
  
        # Process utterances with speaker labels  
        utterances = res.get("results", {}).get("utterances", [])  
        if utterances:  
            print("--- Transcription Received ---")  
            for utterance in utterances:  
                speaker = utterance.get("speaker", "Unknown")  
                transcript = utterance.get("transcript", "")  
                print(f"[Speaker {speaker}] {transcript}")  
            print("------------------------------\n")  
        else:  
            print("No utterances found in the response.")  
  
    else:  
        print(f"Error transcribing audio: {response.status_code} - {response.text}")  
  
if __name__ == "__main__":  
    audio_data = None  
    try:  
        # Record audio until Ctrl+C  
        audio_data = record_audio()  
  
        # Send the audio data to Deepgram  
        if audio_data:  
            send_audio_to_deepgram(audio_data)  
    except Exception as e:  
        print(f"An error occurred: {e}")  
    finally:  
        # Stop and close the stream after processing  
        stream.stop_stream()  
        stream.close()  
        audio.terminate()  
        print("Audio stream terminated. Exiting program.\n")  

import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import concurrent.futures

def transcribe_chunk(chunk, recognizer):
    with sr.AudioFile(chunk.export("temp.wav", format="wav")) as temp_audio_file:
        audio_data = recognizer.record(temp_audio_file)
        try:
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return ""

def split_audio_file(input_file, output_directory, target_duration_ms=7000):
    audio = AudioSegment.from_wav(input_file)
    recognizer = sr.Recognizer()

    chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-36, keep_silence=100)
    os.makedirs(output_directory, exist_ok=True)

    chunk_index = 1
    current_duration = 0
    combined_chunk = AudioSegment.empty()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        transcribed_chunks = list(executor.map(lambda chunk: transcribe_chunk(chunk, recognizer), chunks))

    for chunk, transcribed_chunk in zip(chunks, transcribed_chunks):
        current_duration += len(chunk)

        if current_duration >= target_duration_ms:
            if "." in transcribed_chunk or "?" in transcribed_chunk or "!" in transcribed_chunk:
                output_file = os.path.join(output_directory, f"chunk_{chunk_index:03d}.wav")
                combined_chunk.export(output_file, format="wav")
                chunk_index += 1
                current_duration = 0
                combined_chunk = AudioSegment.empty()
            else:
                current_duration -= len(chunk)
        else:
            combined_chunk += chunk

    if len(combined_chunk) > 0:
        output_file = os.path.join(output_directory, f"chunk_{chunk_index:03d}.wav")
        combined_chunk.export(output_file, format="wav")

if __name__ == "__main__":
    input_file = "/data/split/Rutte-presplit.wav"
    output_directory = "/data/split/rutte-split/"
    split_audio_file(input_file, output_directory)

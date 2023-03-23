import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr

def split_audio(file_path, target_duration=7, min_silence_len=500, silence_thresh=-32):
    audio = AudioSegment.from_wav(file_path)
    audio_chunks = split_on_silence(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh,
    )

    target_length = target_duration * 1000
    output_chunks = []
    temp_chunk = AudioSegment.empty()

    for chunk in audio_chunks:
        if len(temp_chunk) + len(chunk) < target_length:
            temp_chunk += chunk
        else:
            output_chunks.append(temp_chunk)
            temp_chunk = chunk

    if temp_chunk:
        output_chunks.append(temp_chunk)

    return output_chunks

def save_chunks(chunks, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, chunk in enumerate(chunks):
        output_file = os.path.join(output_dir, f"chunk_{i}.wav")
        chunk.export(output_file, format="wav")

if __name__ == "__main__":
    input_file = "path/to/your/input.wav"
    output_directory = "path/to/your/output/directory"

    target_duration = 7
    min_silence_len = 500
    silence_thresh = -32

    audio_chunks = split_audio(input_file, target_duration, min_silence_len, silence_thresh)
    save_chunks(audio_chunks, output_directory)

import os
import argparse
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

def main():
    parser = argparse.ArgumentParser(description="Split a WAV file into shorter clips.")
    parser.add_argument("--input", required=True, help="Path to the input WAV file.")
    parser.add_argument("--output", required=True, help="Path to the output directory.")
    parser.add_argument("--duration", type=int, default=7, help="Target duration of the clips in seconds.")
    parser.add_argument("--min_silence_len", type=int, default=500, help="Minimum silence length in milliseconds.")
    parser.add_argument("--silence_thresh", type=int, default=-32, help="Silence threshold in dB.")

    args = parser.parse_args()

    input_file = args.input
    output_directory = args.output

    target_duration = args.duration
    min_silence_len = args.min_silence_len
    silence_thresh = args.silence_thresh

    audio_chunks = split_audio(input_file, target_duration, min_silence_len, silence_thresh)
    save_chunks(audio_chunks, output_directory)

if __name__ == "__main__":
    main()

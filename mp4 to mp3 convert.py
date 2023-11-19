import os
from moviepy.editor import AudioFileClip
import glob

def convert_mp4_to_mp3(file_path):
    try:
        video = AudioFileClip(file_path)
        mp3_file = file_path.replace(".mp4", ".mp3")
        video.write_audiofile(mp3_file)
        video.close()
        os.remove(file_path)  # Remove the original MP4 file
        print(f"Conversion successful: {mp3_file}")
    except Exception as e:
        print(f"Conversion failed: {e}")

def convert_all_mp4_to_mp3(directory):
    os.chdir(directory)
    mp4_files = glob.glob("*.mp4")
    if not mp4_files:
        print("No MP4 files found in the directory.")
    else:
        for file in mp4_files:
            convert_mp4_to_mp3(file)

# Provide the directory where your MP4 files are located
directory_path = "C:/Users/CHRIS/Music"
convert_all_mp4_to_mp3(directory_path)

import os
import subprocess

def read_stream_info():
    """Reads stream key and URL from stream_info.txt"""
    with open("stream_info.txt", "r") as f:
        lines = f.readlines()
        stream_key = lines[0].split(": ")[1].strip()
        stream_url = lines[1].split(": ")[1].strip()
    return stream_key, stream_url

import subprocess

def start_stream(video_file, stream_url, stream_key):
    ffmpeg_path = "/app/vendor/ffmpeg/ffmpeg"  # Full path to FFmpeg
    command = [
        ffmpeg_path, "-re", "-stream_loop", "-1", "-i", video_file, "-c:v", "libx264",
        "-preset", "veryfast", "-b:v", "2500k", "-maxrate", "2500k", "-bufsize", "5000k",
        "-pix_fmt", "yuv420p", "-g", "50", "-c:a", "aac", "-b:a", "128k", "-f", "flv",
        f"{stream_url}/{stream_key}"
    ]
    subprocess.run(command)



def main():
    """Main function to start streaming"""
    video_file = "video.mp4"
    stream_key, stream_url = read_stream_info()
    start_stream(video_file, stream_url, stream_key)

if __name__ == "__main__":
    main()

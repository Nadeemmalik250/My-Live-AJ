import os
import subprocess

def read_stream_info():
    """Reads stream key and URL from stream_info.txt"""
    with open("stream_info.txt", "r") as f:
        lines = f.readlines()
        stream_key = lines[0].split(": ")[1].strip()
        stream_url = lines[1].split(": ")[1].strip()
    return stream_key, stream_url

def start_stream(video_file, stream_url, stream_key):
    """Starts the FFmpeg live stream"""
    command = [
        "ffmpeg", "-re", "-stream_loop", "-1",
        "-i", video_file, "-c:v", "libx264", "-preset", "veryfast", "-b:v", "4500k",
        "-maxrate", "4500k", "-bufsize", "6000k", "-c:a", "aac", "-b:a", "128k",
        "-f", "flv", f"{stream_url}/{stream_key}"
    ]
    print(f"Streaming {video_file} to {stream_url} with key {stream_key}...")
    subprocess.run(command)

def main():
    """Main function to start streaming"""
    video_file = "video.mp4"
    stream_key, stream_url = read_stream_info()
    start_stream(video_file, stream_url, stream_key)

if __name__ == "__main__":
    main()

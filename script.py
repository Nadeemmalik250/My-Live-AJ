import os
import re
import subprocess

def find_video_file(input_folder):
    for file in os.listdir(input_folder):
        if file.lower().endswith(('.mp4', '.mkv', '.mov', '.avi')):
            return os.path.join(input_folder, file)
    return None

def read_stream_details(txt_file):
    with open(txt_file, 'r') as file:
        content = file.read()
        stream_key_match = re.search(r"Stream key:\s*(\S+)", content)
        stream_url_match = re.search(r"Stream URL:\s*(\S+)", content)
        
        if stream_key_match and stream_url_match:
            return stream_url_match.group(1), stream_key_match.group(1)
        else:
            return None, None

def start_stream(video_file, stream_url, stream_key):
    full_url = f"{stream_url}/{stream_key}"
    command = [
        "ffmpeg", "-re", "-stream_loop", "-1", "-i", video_file,
        "-c:v", "libx264", "-preset", "veryfast", "-b:v", "4500k", "-maxrate", "4500k", "-bufsize", "6000k",
        "-c:a", "aac", "-b:a", "128k", "-f", "flv", full_url
    ]
    subprocess.run(command)

def main():
    input_folder = os.path.join(os.getcwd(), "Input")
    txt_file = os.path.join(input_folder, "stream_info.txt")
    
    if not os.path.exists(input_folder):
        print("Error: 'Input' folder not found!")
        return
    
    video_file = find_video_file(input_folder)
    if not video_file:
        print("Error: No video file found in 'Input' folder!")
        return
    
    stream_url, stream_key = read_stream_details(txt_file)
    if not stream_url or not stream_key:
        print("Error: Stream key or URL not found in stream_info.txt!")
        return
    
    print(f"Streaming {video_file} to {stream_url} with key {stream_key}...")
    start_stream(video_file, stream_url, stream_key)

if __name__ == "__main__":
    main()

# Railway-specific execution
if os.getenv("RAILWAY_ENVIRONMENT"):  # Detect Railway environment
    main()

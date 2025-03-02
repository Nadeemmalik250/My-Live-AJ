FROM jrottenberg/ffmpeg:latest
WORKDIR /app
COPY . /app
CMD ["ffmpeg", "-re", "-stream_loop", "-1", "-i", "Input/video.mp4", "-c:v", "libx264", "-preset", "fast", "-b:v", "5000k", "-maxrate", "5000k", "-bufsize", "10000k", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-f", "flv", "$(cat Input/stream_key.txt)"]

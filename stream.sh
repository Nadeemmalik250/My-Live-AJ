#!/bin/bash
STREAM_KEY=$(cat Input/stream_key.txt | grep "Stream key" | cut -d " " -f3)
STREAM_URL=$(cat Input/stream_key.txt | grep "Stream URL" | cut -d " " -f3)
VIDEO_FILE=$(ls Input/*.mp4 | head -n 1)

ffmpeg -re -stream_loop -1 -i "$VIDEO_FILE" -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k -c:a aac -b:a 128k -f flv "$STREAM_URL/$STREAM_KEY"

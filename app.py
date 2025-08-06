from flask import Flask, request, render_template, send_file
from moviepy.editor import VideoFileClip
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['video']
        if file:
            video_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.mp4")
            audio_path = video_path.replace(".mp4", ".mp3")
            file.save(video_path)

            clip = VideoFileClip(video_path)
            clip.audio.write_audiofile(audio_path)

            return send_file(audio_path, as_attachment=True)

    return render_template("index.html")

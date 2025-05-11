from flask import Flask, render_template, request, redirect, url_for, send_file
from gtts import gTTS
import os
import uuid

app = Flask(__name__)
AUDIO_FOLDER = 'static/audio'
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    filename = None

    if request.method == 'POST':
        text = request.form['text']
        if text.strip():
            filename = f"{uuid.uuid4()}.mp3"
            filepath = os.path.join(AUDIO_FOLDER, filename)
            tts = gTTS(text=text, lang='en')
            tts.save(filepath)

    return render_template('index.html', audio_file=filename, text=text)

@app.route('/download/<filename>')
def download(filename):
    path = os.path.join(AUDIO_FOLDER, filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

# 🔊 Text-to-Speech Narrator using Generative AI

This project is a simple and intuitive web application that converts your text input into spoken audio using **Google Text-to-Speech (gTTS)**. The backend is built using **Flask**, and the frontend is designed with **Bootstrap 5** for a clean and responsive user experience.

---

## 📌 Features

- 📝 Convert any entered text into speech
- 🎧 Playback the generated audio in the browser
- 📥 Download the MP3 file of the spoken audio
- 💻 Lightweight and fast
- 🎨 Stylish and mobile-friendly interface

---

## 🛠️ Tech Stack Used

| Technology | Description |
|------------|-------------|
| Python     | Core programming language |
| Flask      | Micro web framework used to build the backend |
| gTTS       | Google Text-to-Speech library for generating MP3 audio |
| HTML5/CSS3 | Web structure and styling |
| Bootstrap 5 | Frontend framework for styling and layout |
| Jinja2     | Templating engine used with Flask |
| UUID       | Used to generate unique filenames for each audio file |

---

## 📁 Project Structure

text-to-speech-narrator/
├── app.py # Main Flask application
├── templates/
│ └── index.html # HTML template for the UI
├── static/
│ └── audio/ # Folder where MP3 files are stored
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/text-to-speech-narrator.git
cd text-to-speech-narrator
```

# (Optional) Create and activate a virtual environment

python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

# Install the required packages

pip install -r requirements.txt

# Run the application

python app.py

# Open your browser and visit

http://127.0.0.1:5000/

# 🧪 Example Usage

Enter text: Welcome to our Text-to-Speech Narrator!

Click Convert to Speech

Listen to or download the generated MP3 file

# 🔮 Future Improvements

Support for multiple languages

Voice customization (speed, tone, gender)

Cloud deployment (Heroku, Render, etc.)

Upload text files or PDFs for conversion

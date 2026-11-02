# 🎙️ Speech-to-Text Transcription System

A web-based **Speech-to-Text Transcription System** built with **Python, Streamlit, SpeechRecognition, Pydub, and FFmpeg**. The application converts spoken audio from audio and video files into readable text.

This project was developed as part of an **Artificial Intelligence Internship at Codec Technologies**.

---

## 📌 Project Overview

Speech-to-Text technology enables computers to convert human speech into written text.

This application provides a simple web interface where users can upload an audio or video file, select the spoken language, and automatically generate a text transcript.

The system processes the uploaded media, extracts and prepares the audio, divides longer recordings into smaller chunks, and uses speech recognition to generate the final transcript.

---

## ✨ Features

- 🎙️ Convert speech into text
- 🎥 Support audio and video files
- 🌐 Multiple language support
- ⚡ Chunk-based processing for longer recordings
- 🔊 Automatic audio extraction from video
- 🎚️ Audio optimization for speech recognition
- 📝 Display generated transcript
- ⬇️ Download transcript as a `.txt` file
- 💻 Simple and user-friendly Streamlit interface

---

## 📂 Supported File Formats

### Audio

- WAV
- MP3
- M4A
- OGG
- FLAC
- AAC
- WMA

### Video

- MP4
- MKV
- AVI
- MOV
- WEBM

---

## 🌐 Supported Languages

The application currently supports:

| Language | Recognition Code |
|---|---|
| English | `en-US` |
| Telugu | `te-IN` |
| Hindi | `hi-IN` |
| Tamil | `ta-IN` |
| Kannada | `kn-IN` |
| Malayalam | `ml-IN` |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| SpeechRecognition | Speech-to-text processing |
| Pydub | Audio processing and conversion |
| FFmpeg | Audio/video conversion and extraction |
| Google Speech Recognition | Speech recognition engine |

---

## 🔄 System Workflow

```text
User Uploads Audio / Video
          ↓
      File Detection
          ↓
   FFmpeg Audio Extraction
          ↓
   Audio Format Conversion
          ↓
   Mono + 16 kHz Processing
          ↓
   Split into 10-Second Chunks
          ↓
   Speech Recognition
          ↓
   Combine Transcribed Text
          ↓
     Display Transcript
          ↓
    Download as TXT File
```

---

## 📁 Project Structure

```text
speech-to-text-transcription/
│
├── app.py
├── README.md
├── .gitignore
└── venv/
```

> The `venv/` directory is excluded from GitHub using `.gitignore`.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vishnu-panuganti/speech-to-text-transcription.git
```

### 2. Navigate to the Project

```bash
cd speech-to-text-transcription
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```powershell
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Required Packages

```bash
pip install streamlit SpeechRecognition pydub
```

---

## 🔧 FFmpeg Installation

FFmpeg is required for processing different audio and video formats.

### Windows

FFmpeg can be installed using:

```powershell
winget install Gyan.FFmpeg
```

Verify the installation:

```powershell
ffmpeg -version
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

Upload an audio or video file, select the language, and click:

**🎙️ Transcribe**

The generated transcript will appear on the screen and can be downloaded as a text file.

---

## 🧠 How It Works

### 1. File Upload

The user uploads an audio or video file through the Streamlit interface.

### 2. Media Processing

Pydub and FFmpeg process the uploaded file and extract the audio when a video is provided.

### 3. Audio Optimization

The audio is converted to:

- Mono channel
- 16 kHz sample rate
- WAV format

This provides a suitable format for speech recognition.

### 4. Audio Chunking

Long recordings are divided into **10-second chunks**.

This improves transcription reliability compared with sending a long recording as a single request.

### 5. Speech Recognition

Each chunk is processed using the Google Speech Recognition service.

### 6. Transcript Generation

The recognized text from all chunks is combined into a single transcript.

### 7. Download

The final transcript can be downloaded as a `.txt` file.

---

## 📊 Example

### Input

```text
Audio / Video File
        ↓
30-second recording
```

### Processing

```text
0–10 seconds  → Speech Recognition
10–20 seconds → Speech Recognition
20–30 seconds → Speech Recognition
```

### Output

```text
Artificial intelligence is transforming the world...
It helps computers learn from data...
It can understand language and recognize images...
```

---

## 🚀 Future Enhancements

The following features can be added in future versions:

- 🎤 Real-time microphone transcription
- 🌍 Automatic language detection
- 🔄 Speech translation
- 📄 Export transcripts to PDF and DOCX
- ⏱️ Timestamp generation
- 👥 Speaker identification
- 🤖 Advanced AI-based transcription
- 📱 Improved mobile interface
- ☁️ Cloud deployment
- 📊 Transcription history

---

## 🎯 Applications

Speech-to-Text systems can be useful for:

- Online meetings
- Lecture transcription
- Interview transcription
- Video subtitles
- Voice notes
- Accessibility applications
- Content creation
- Customer service
- Educational applications

---

## 👨‍💻 Author

**Vishnu Panuganti**

B.Tech – Computer Science Engineering  
Specialization: IoT, Cybersecurity & Blockchain Technology

---

## 🏢 Internship

**Artificial Intelligence Internship – Codec Technologies**

This project was developed as one of the projects completed during the internship.

---

## 📜 License

This project is intended for **educational and internship purposes**.

---

## ⭐ Acknowledgement

Thanks to **Codec Technologies** for providing the Artificial Intelligence internship opportunity and project requirements.

If you find this project useful, consider giving the repository a ⭐ on GitHub.

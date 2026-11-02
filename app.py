
import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os

st.set_page_config(
    page_title="Speech to Text",
    page_icon="🎙️"
)

st.title("🎙️ Speech-to-Text Transcription")
st.write("Upload an audio or video file and convert speech into text.")

language = st.selectbox(
    "Select Speech Language",
    {
        "English": "en-US",
        "Telugu": "te-IN",
        "Hindi": "hi-IN",
        "Tamil": "ta-IN",
        "Kannada": "kn-IN",
        "Malayalam": "ml-IN"
    }
)

supported_files = [
    "wav", "mp3", "m4a", "ogg",
    "flac", "aac", "wma",
    "mp4", "mkv", "avi",
    "mov", "webm"
]

uploaded_file = st.file_uploader(
    "Upload Audio or Video",
    type=supported_files
)

if uploaded_file is not None:

    file_extension = os.path.splitext(
        uploaded_file.name
    )[1].lower()

    # Display uploaded media
    if file_extension in [
        ".mp4", ".mkv", ".avi", ".mov", ".webm"
    ]:
        st.video(uploaded_file)
    else:
        st.audio(uploaded_file)

    if st.button("🎙️ Transcribe"):

        input_path = None

        try:
            # Save uploaded file
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=file_extension
            ) as temp_file:

                temp_file.write(
                    uploaded_file.getbuffer()
                )

                input_path = temp_file.name

            st.info("Preparing audio...")

            # Convert audio/video to WAV
            audio = AudioSegment.from_file(
                input_path
            )

            # Optimize audio for speech recognition
            audio = audio.set_channels(1)
            audio = audio.set_frame_rate(16000)

            # Split into 10-second chunks
            chunk_length = 10 * 1000

            total_chunks = (
                len(audio) + chunk_length - 1
            ) // chunk_length

            full_text = []

            progress = st.progress(0)

            st.info(
                f"Processing {total_chunks} audio chunks..."
            )

            recognizer = sr.Recognizer()

            for i in range(
                0,
                len(audio),
                chunk_length
            ):

                chunk = audio[
                    i:i + chunk_length
                ]

                chunk_path = None

                try:
                    with tempfile.NamedTemporaryFile(
                        delete=False,
                        suffix=".wav"
                    ) as chunk_file:

                        chunk_path = chunk_file.name

                    chunk.export(
                        chunk_path,
                        format="wav"
                    )

                    with sr.AudioFile(
                        chunk_path
                    ) as source:

                        audio_data = (
                            recognizer.record(source)
                        )

                    try:
                        text = (
                            recognizer.recognize_google(
                                audio_data,
                                language=language
                            )
                        )

                        if text.strip():
                            full_text.append(text)

                    except sr.UnknownValueError:
                        pass

                    except sr.RequestError:
                        st.error(
                            "Google Speech Recognition "
                            "service is unavailable."
                        )
                        break

                finally:

                    if (
                        chunk_path
                        and os.path.exists(chunk_path)
                    ):
                        os.remove(chunk_path)

                progress.progress(
                    min(
                        (i + chunk_length)
                        / len(audio),
                        1.0
                    )
                )

            # Combine transcript
            result = " ".join(full_text)

            if result.strip():

                st.success(
                    "✅ Transcription completed!"
                )

                st.subheader("📝 Transcript")

                st.text_area(
                    "Generated Text",
                    result,
                    height=300
                )

                st.download_button(
                    "⬇️ Download Transcript",
                    result,
                    file_name="transcript.txt",
                    mime="text/plain"
                )

            else:

                st.warning(
                    "No speech could be detected."
                )

        except Exception as e:

            st.error(f"Error: {e}")

        finally:

            if (
                input_path
                and os.path.exists(input_path)
            ):
                os.remove(input_path)

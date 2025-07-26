# PDF to Audiobook Converter 📖➡️🎧
A simple Python script that converts text from a PDF file into an MP3 audiobook using Google's Text-to-Speech (gTTS) library.

**Description:**
This project provides a straightforward way to turn any text-based PDF document into a series of MP3 audio files. It's perfect for listening to articles, study materials, or books on the go. The script extracts text from each page, chunks it to handle API limits, and saves each chunk as a separate MP3 file.

**Features:**
Extracts text directly from PDF files.
Uses Google Text-to-Speech (gTTS) for natural-sounding audio.
Splits long texts into smaller chunks to avoid errors.
Saves output as sequentially numbered MP3 files (e.g., Story_Audiobook_part1.mp3).

**Requirements**:
Python 3.x
gTTS
pypdf

You can install the necessary libraries using pip:
pip install gtts pypdf

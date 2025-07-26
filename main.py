#Audio Book
from gtts import gTTS
from pypdf import PdfReader

reader= PdfReader ('Story.pdf')

full_text=""
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        print(f"Reading page {i+1}...")
        full_text +=text+ "\n"
       
if full_text.strip()=="":
    print ("No readable text found.")
else:
    print ("Readable text found.")

    chunk_size = 4000
    chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]

    for index, chunk in enumerate(chunks):
        tts=gTTS(chunk)
        tts.save(f"Story_Audiobook_part{index+1}.mp3")
        print ("MP3 file saved successfully ")

# Import Modules
from PyPDF2 import PdfReader  # Module to convert pdf to string variable
from gtts import gTTS  # Google Text-to-Speech Module that can access Google's API to translate text to audio file

# Set starting variables that can be adjusted
language = "en"  # Language of text to speech. Utilizes IETF language tags. "en" is default for English
output_audio_file_name = "audio"  # This is the name of the audio file that will be outputted and relative location

# Utilize PyPDF2 Module to convert pdf to text string
reader = PdfReader(stream="Test_Doc.pdf")  # Create object from pdf file
# Page method creates dictionary from information. This creates a variable of the first element of the dictionary and
# converts it to a string text
document_string = reader.pages[0].extract_text()

# Utilize gTTS Module to create object from string text above
audio = gTTS(
    text=document_string,  # Input the string text created above
    lang=language,  # Specify language from variable above
    slow=False  # Default is to read slowly. Change this as you wish
)

# Utilize save method for gTTS Module to save the file in a directory of your choice
audio.save(
    savefile=f"{output_audio_file_name}.mp3"
)

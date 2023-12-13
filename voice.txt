
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize the Pyrogram client
api_id = 26788480
api_hash = "858d65155253af8632221240c535c314"
bot_token = "6593343536:AAHYW4ehuF535UHAS_KUYVTwBj26hqf8RQ8"

app = Client("text_to_voice_bot", api_id, api_hash, bot_token=bot_token)

# API endpoint for the ElevenLabs Text to Speech API
API_ENDPOINT = "https://api.elevenlabs.io/v1/text-to-speech/adam"

# Command to convert text to voice
@app.on_message(filters.command("voice"))
def convert_text_to_voice(_, message: Message):
    text = " ".join(message.command[1:])
    if text:
        # Send a request to the ElevenLabs API
        response = requests.post(
            API_ENDPOINT,
            json={"text": text[:512]},
            headers={"Authorization": "aaa8ac11336407eed87a0c569edfb359"}
        )

        if response.status_code == 200:
            audio_url = response.json().get("audio_url")

            audio_file = None
            
            if audio_url:
                
                # Download audio
                audio_file = f"{message.chat.id}.mp3"
                with requests.get(audio_url, stream=True) as r:
                    r.raise_for_status()
                    with open(audio_file, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)

                # Send the audio file to the user
                duration = response.json().get("duration", 0)
                if duration > 60:
                    message.reply_text("Sorry, the audio exceeds the 1-minute limit.")
                else:
                    message.reply_audio(audio_file, duration=duration)
            else:
                message.reply_text("Sorry, an error occurred while processing the text.")
        else:
            message.reply_text("Sorry, an error occurred while communicating with the API.")
    else:
        message.reply_text("Please provide the text to convert.")

    # Remove the audio file
    if audio_file:
        os.remove(audio_file)


# Run the bot
app.run()

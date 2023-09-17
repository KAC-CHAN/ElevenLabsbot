import pyrogram
from eleven_client import ElevenClient

api_id = 26788480
api_hash = "858d65155253af8632221240c535c314"
bot_token = "6593343536:AAHYW4ehuF535UHAS_KUYVTwBj26hqf8RQ8"

api_key = "aaa8ac11336407eed87a0c569edfb359"

# Initialize Pyrogram client
client = pyrogram.Client("text2voice", api_id, api_hash, bot_token)

# Initialize Eleven Labs client  
eleven = ElevenClient(api_key)

# Message handler
@client.on_message()  
async def handler(client, message):

  # Get user text
  text = message.text  

  # Limit text length
  if len(text) > 150:
    text = text[:150] + "..."

  # Generate voice with Adam voice
  voice = eleven.generateVoice(text, voice="adam")   

  # Trim if audio > 1 min
  if len(voice) > 60000:
    voice = voice[:60000]

  # Reply audio to user
  await client.send_audio(chat_id=message.chat.id, audio=voice)

# Run bot
if __name__ == "__main__":
  client.run()

import pyrogram
from eleven_client import ElevenClient

api_id = 26788480
api_hash = "858d65155253af8632221240c535c314"
bot_token = "6593343536:AAHYW4ehuF535UHAS_KUYVTwBj26hqf8RQ8"

api_key = "aaa8ac11336407eed87a0c569edfb359"

client = pyrogram.Client("text2voice", api_id, api_hash, bot_token)
eleven = ElevenClient(api_key) 

@client.on_message()
async def text2voice(client, message):

  text = message.text

  if len(text) > 150:
    text = text[:150] + "..."

  # Generate voice with Adam voice
  voice = eleven.generateVoice(text, voice="adam")   

  if len(voice) > 60000:
    voice = voice[:60000]

  await client.send_audio(chat_id=message.chat.id, audio=voice)

client.run()

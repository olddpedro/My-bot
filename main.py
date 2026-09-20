import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'تم تشغيل البوت بنجاح! اسم البوت: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!هلا':
        await message.channel.send('أهلاً وسهلاً بك! البوت شغال على Koyeb 🚀')

token = os.environ.get('DISCORD_TOKEN')
client.run(token)

import os
import discord
import messageController
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def send_message(message, user_message, is_private):
    try:
        response = messageController.get_response(user_message, message.channel.id, message.author.display_name, message.attachments )
        await message.author.send(response, reference=message) if is_private else await message.channel.send(response, reference=message)

    except Exception as e:
        print(e)

def run_discord_bot():
    load_dotenv()   
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        print("channel")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author.display_name)
        user_message = str(message.content)
        channel = str(message.channel)
        channel_id = str(message.channel.id)

        print(f'{username} said: "{user_message}" ({channel}) ({channel_id})')
        if user_message[0] == '?':
            user_message = user_message[1:] 
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

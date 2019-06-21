import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("구매문의 Telegram9524")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("구매방법"):
        await message.channel.send("구매는 Telegram#9524 에게 해주세요")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

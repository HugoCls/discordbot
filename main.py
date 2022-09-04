from discord.ext import commands
import os

client=commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('BOT Gdc is ready.')

@client.command()
async def Hello(ctx):
    await ctx.reply('test')
    await ctx.message.delete()

client.run(os.environ['DISCORD_TOKEN'])
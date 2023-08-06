import voltage
from voltage.ext import commands
import random
import asyncio
import aiohttp

client = commands.CommandsClient("br!")

@client.command(description="Make the bot say your message")
async def say(ctx, *, question):
    await ctx.send(f'{question}')
    await ctx.message.delete()

@client.command(description="Make the bot say your message in an embed")
async def esay(ctx, *, question):
    embed = voltage.SendableEmbed(description=f'{question}', color='#00FF4F')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(description="Get Tikals Services social media pages")
async def tikalsocials(ctx):
    embed = voltage.SendableEmbed(title="TIKALS SOCIAL MEDIA PAGES", description="Youtube: https://www.youtube.com/channel/UC6vNUcFhQNNC6rLLN-383QA\nTwitter: https://twitter.com/TikalServices\nInstagram: https://www.instagram.com/tikalservices/\nGithub: https://github.com/TikalServices", color='#FF00FF')
    await ctx.send(embed=embed)



client.run("YOURBOTTOKEN")

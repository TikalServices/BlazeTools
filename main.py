import discord
from discord.ext import commands
import random
import asyncio
import sys

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = 'br!', intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print("Bot is Online and Ready")

@client.command()
async def help(ctx):
    embed = discord.Embed(title="HELP MENU", description="Here is my List of Commands", color=(14287103))
    embed.add_field(name="CORE COMMANDS", value="b!help - This message\nb!ping - Checks the latency of the bot\nb!tikalsocials - Get Tikals Services social media pages\nb!sonicsocials - Get Sonic the Hedgehogs social media links", inline=False)
    embed.add_field(name="MISC COMMANDS", value="b!say - Make me say anything\nb!esay - Make me say anything in an embed\nb!userinfo - Get information about a user", inline=False)
    embed.add_field(name="DEVELOPER COMMANDS", value="b!restart - Restarts the Bot", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send("Pong")

@client.command()
async def sonicsocials(ctx):
    embed = discord.Embed(title="SONIC THE HEDGEHOG SOCIAL MEDIA PAGES", description="Youtube: https://www.youtube.com/channel/UCp6JU855jCI6yOU-hfmZ5ew\nTwitter: https://twitter.com/SonicX_Hedgehog\nInstagram: https://www.instagram.com/SonicTheHedgehogDev/\nGithub: https://github.com/SonicTheDev", color=(40191))
    embed.add_field(name="DISCORD", value="Discord Account: SonicTheHedgehog#4570 (User ID: 691801844577730590)\nDiscord Server: https://discord.gg/j9Tt7h2UkG", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def tikalsocials(ctx):
    embed = discord.Embed(title="TIKALS SOCIAL MEDIA PAGES", description="Youtube: https://www.youtube.com/channel/UC6vNUcFhQNNC6rLLN-383QA\nTwitter: https://twitter.com/TikalServices\nInstagram: https://www.instagram.com/tikalservices/\nGithub: https://github.com/TikalServices", color=(14287103))
    embed.add_field(name="DISCORD", value="Discord Account: tikalservices (User ID: 1041993747950485595)\nDiscord Server: https://discord.gg/5jKN6kfAyf", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def say(ctx, *, question: commands.clean_content):
    await ctx.send(f'{question}')
    await ctx.message.delete()

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("What do you want me to say?")
    else:
        raise error

@client.command()
async def esay(ctx, *, question):
    embed = discord.Embed(description=f'{question}', color=(14287103))
    await ctx.send(embed=embed)
    await ctx.message.delete()

@esay.error
async def esay_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("What do you want me to say?")
    else:
        raise error

@client.command(aliases=["_userinfo", "ui"])
async def userinfo(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author
    date_format = "%a, %b %d %Y %I:%M %p"
    embed = discord.Embed(title="USER INFORMATION/STATS", description=f"USERNAME + DISCRIMINATOR TAG: {user.name}#{user.discriminator}\nUSER ID: {user.id}\nDiscord User Since: {user.created_at.strftime(date_format)}\nJoined Server Since: {user.joined_at.strftime(date_format)}", color=(64255))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    embed.set_footer(text="Blaze the Cat R")
    embed.set_thumbnail(url=user.avatar)
    await ctx.send(embed=embed)





client.run("YOURBOTTOKEN")

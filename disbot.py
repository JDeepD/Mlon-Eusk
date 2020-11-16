import discord  # pylint: disable=import-error
from discord import Game  # pylint: disable=import-error
from discord.ext import commands  # pylint: disable=import-error
import requests
import apis.redditapi as redditapi
import apis.spacexapi as spacexapi
import apis.nasaapi as nasaapi


bot = commands.Bot(command_prefix='-')  # define command decorator


@bot.command(pass_context=True)
async def fetch(ctx, subreddit="ProgrammerHumor"):
    title, text, url = redditapi.jokes(val=subreddit)
    await ctx.send(title)
    await ctx.send(url)


@bot.command(pass_context=True)
async def pics(ctx, subreddit="unixmemes"):
    title, url = redditapi.meme(val=subreddit)
    await ctx.send(title)
    await ctx.send(url)


@bot.command(pass_context=True)
async def gifs(ctx, con=None):
    title, url = redditapi.meme()
    await ctx.send(title)
    await ctx.send(url)


@bot.command(pass_context=True)
async def troll(ctx, hooked: discord.Member):
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=txt"
    st = requests.get(url)
    await ctx.send(str(hooked.mention)+st.content.decode("utf-8"))


@bot.command(pass_context=True)
async def wallpaper(ctx, query="random"):
    base_url = "https://source.unsplash.com/1600x1900/?"
    url = base_url + query
    await ctx.send(url)


@bot.command(pass_context=True)
async def indianmemes(ctx, subreddit="IndianMeyMeys"):
    title, url = redditapi.meme(val=subreddit)
    await ctx.send(title)
    await ctx.send(url)


@bot.command(pass_context=True)
async def linuxmemes(ctx, subreddit="linuxmemes"):
    title, url = redditapi.meme(val=subreddit)
    await ctx.send(title)
    await ctx.send(url)


@bot.command(pass_context=True)
async def spacex(ctx):
    data = spacexapi.latest()
    title = data["details"]
    img = data["links"]["patch"]["small"]
    ytlink = data["links"]["webcast"]
    await ctx.send(title)
    await ctx.send(img)
    await ctx.send(ytlink)


@bot.command(pass_context=True)
async def apod(ctx):
    title, explanation, url = nasaapi.apod()
    await ctx.send(title)
    await ctx.send(url)


bot.run("<Your token>")

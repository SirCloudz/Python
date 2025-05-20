import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Ya cargo esta huevada compare, {bot.user.name}")


class JoinDistance:
    def _init_(self, joined, created):
        self.joined = joined
        self.created = created

    @classmethod
    async def converts(cls, ctx, argument):
        member = await commands.MemberConverter().convert(ctx, argument)
        return cls(member.joined_at, member.created_at)

    @property
    def delta(self):
        return self.joined - self.created


@bot.command()
async def delta(ctx, *, member: JoinDistance):
    is_new = member.delta.days < 100
    if is_new:
        await ctx.send(f"Bienvenido a este nuevo server, chupapi {member.name}")
    else:
        await ctx.send(f"Tu no eres nuevo, especial de mierda {member.name}")


# @bot.event
# async def on_member_join(member):
#    await member.send(f"Welcome to the server {member.name}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} don't use that word mf")
    elif "puta" in message.content.lower():
        await message.channel.send(f"{message.author.mention} Eres jijij")
    elif "insultame" in message.content.lower():
        await message.channel.send(f"Eres tont@ {message.author.mention}")

    await bot.process_commands(message)


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")


@bot.command()
async def hola(ctx):
    await ctx.send(f"Hola que tal {ctx.author.mention}!")


@bot.command()
async def apodos(ctx):
    await ctx.send(f"-Toro: El señor de la caverna, \n-Godoy: Tu Cachero, \n-Tu: Chupapinga")


bot.run(token)

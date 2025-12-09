from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from utils import notify_user
import datetime as d
import random
import memes2
import requests
import discord
import re
import load

ChanID = {
    'erniegang': 393726535418380291,
    'ernie-bilder': 394279789181141002,
    'ernie-mange-bilder': 691605752661540885,
    'ernie-sanger': 394276923465007104,
    'ijkar': 394279822156627979,
    'ijkar-automotive': 507231667765772288,
    'ernie-gaming': 513078456939184170,
    'ernie-quotes': 622479724437831690,
    'ernie-templates': 627564817535860738,
    'ernie-emojis': 619951705634766868,
    'ernie-council-and-venting-channel-formely-known-as-ernie-reddit': 694147310950547527,
    'ernie-ooc': 666902568814903296,
    'graduation-channel': 554275032457674794,
    'ernie-hungergames': 672093804672843787,
    'ernie-pc': 683012582151684097,
    'test': 692315307057872907,
    'invasion': 694498940380250123,
    'bot': 832526234553810954,
    'spam': 819305751046127657
}

class Basic(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command(
        name='ping',
        description='The ping command',
        aliases=['p']
    )
    async def ping_command(self, ctx):
        start = d.datetime.now().timestamp()
        msg = await ctx.send(content='Pinging')
        await msg.edit(content=f'Pong!\nOne message round-trip took {(d.datetime.now().timestamp() - start) * 1000:.2f}ms.')
        return

    @commands.command(
        name='drunk',
        description='This doesnt work, its just silly anyways',
        aliases=['dr']
    )
    async def drunk_command(self, ctx):
        drunkqotes = [
            'Oh hello there',
        ]
        await ctx.send(f"So here is a drunk quote:\n{random.choice(drunkqotes)}")
        return

    @commands.command(
        name='prime',
        description='Todays prime number',
        aliases=['today']
    )
    async def prime_number(self, ctx):
        await ctx.send("Prime feature coming soon!")
        return

    @commands.command(
        name='say',
        description='Say stuff',
        aliases=['s']
    )
    async def say_stuff(self, ctx, arg1, *, arg2):
        channel = ctx.bot.get_channel(ChanID.get(arg1))
        if channel:
            await channel.send(arg2)
            print(arg1, arg2)
            user = ctx.author.name
            print(user)
            archive = ctx.bot.get_channel(832526234553810954)
            if archive:
                now = d.datetime.now()
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                msg = f"{date_time} - {user} Said: {arg2} in #{arg1}"
                await archive.send(msg)
        return

    @commands.command(
        name='meme',
        description='Ernie memes are the best memes',
        aliases=['erniememe']
    )
    async def meme(self, ctx):
        randmeme = random.choice(memes2.erniememe)
        await ctx.send('Here is an ernie meme ' + randmeme)

    @commands.command(
        name='shutdown',
        description='Shuts down Ernie bot, Manual restart needed to turn back on again.',
        aliases=['Turnoff']
    )
    @has_permissions(ban_members=True)
    async def Shutdown(self, ctx):
        user = ctx.message.author
        channel = ctx.message.channel
        await ctx.send("Are you completly sure? Y/N")
        
        def check(m):
            return m.author == user and m.channel == channel
        
        try:
            msg = await ctx.bot.wait_for('message', check=check, timeout=30.0)
            if msg.content.upper() == "Y":
                await ctx.send("Logging out")
                await ctx.bot.close()
            elif msg.content.upper() == "N":
                await ctx.send("OK then, I'll stay :)")
        except:
            await ctx.send("Timed out waiting for response.")

    @Shutdown.error
    async def Shutdown_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            text = f"Sorry {ctx.message.author}, you do not have permissions to do that!"
            await ctx.send(text)

    @commands.command(
        name='quote',
        description='Random quote from inspirobot.com',
        aliases=['qo']
    )
    async def random_quote(self, ctx):
        website = requests.get('https://inspirobot.me/api?generate=true')
        await ctx.send(website.text)

    @commands.command(
        name='DM',
        description='Direct message to another user, remember to use @mention. If else it wont work and thats sad',
        aliases=['PM'] 
    )
    async def poke(self, ctx, member: discord.Member = None, *, message):
        if member is not None:
            await notify_user(member, message)
            archive = ctx.bot.get_channel(832526234553810954)
            if archive:
                user = ctx.author.name
                msg = f"{user} Said: {message} to: {member.name}"
                await archive.send(msg)
        else:
            await ctx.send("Please use @mention to poke someone.")

    @commands.command(
        name='insult',
        description='Ernie memes are the best memes',
        aliases=['jævla']
    )
    async def instults(self, ctx):
        rand = random.choice(load.banneord)
        str_to_send = f"Jævla {rand.rstrip()}"
        await ctx.send(str_to_send)
    
    @commands.command(
        name='regler',
        description='Ernie memes are the best memes',
        aliases=['rules']
    )
    async def rule(self, ctx):
        rand = random.choice(load.banneord)
        rand1 = random.choice(load.verb)
        str_to_send = f"Regel nr {random.randint(0, 1000)}, det er ikke lov å {rand1.rstrip()} {rand.rstrip()}"
        await ctx.send(str_to_send)

    @commands.command(
        name='pickup',
        description='Ernie memes are the best memes',
        aliases=['lines']
    )
    async def pickup(self, ctx):
        rand = random.choice(load.pickup)
        await ctx.send(rand)

async def setup(client):
    await client.add_cog(Basic(client))

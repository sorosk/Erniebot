from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from datetime import datetime as d
import random
import todayprime
import memes2
import requests
import re
# New - The Cog class must extend the commands.Cog class

ChanID = { #used for the say command.
  'erniegang':393726535418380291,
  'ernie-bilder':394279789181141002,
  'ernie-mange-bilder':691605752661540885,
  'ernie-sanger':394276923465007104,
  'ijkar':394279822156627979,
  'ijkar-automotive':507231667765772288,
  'ernie-gaming':513078456939184170,
  'ernie-quotes':622479724437831690,
  'ernie-templates':627564817535860738,
  'ernie-emojis':619951705634766868,
  'ernie-council-and-venting-channel-formely-known-as-ernie-reddit':694147310950547527,
  'ernie-ooc':666902568814903296,
  'graduation-channel':554275032457674794,
  'ernie-hungergames':672093804672843787,
  'ernie-pc':683012582151684097,
  'test':692315307057872907,
  'invasion':694498940380250123
}

class Basic(commands.Cog):
    
  def __init__(self, bot):
      self.bot = bot
      
  # Define a new command
  @commands.command(
      name='ping',
      description='The ping command',
      aliases=['p']
  )
  async def ping_command(self, ctx):
    start = d.timestamp(d.now())
    # Gets the timestamp when the command was used

    msg = await ctx.send(content='Pinging')
    # Sends a message to the user in the channel the message with the command was received.
    # Notifies the user that pinging has started

    await msg.edit(content=f'Pong!\nOne message round-trip took {( d.timestamp( d.now() ) - start ) * 1000 }ms.')
    # Ping completed and round-trip duration show in ms
    return
  @commands.command(
      name='drunk',
      description='The drunken sailor',
      aliases=['dr']
  )
  async def drunk_command(self, ctx):
    drunkqotes = [
      'Oh hello there',

    
    ]
    await ctx.send("So here is a drunk quote:\n", drunkqotes)
    return
  @commands.command(
      name='prime',
      description='Todays prime number',
      aliases=['today']
  )
  async def prime_number(self, ctx):
    todayprime.prime()
    await ctx.send(todayprime.todayprime)
    return
  @commands.command(
        name='say',
        description='Say stuff',
        aliases=['s']
    )
  async def say_stuff(self, ctx, arg1, *, arg2):
    channel = ctx.bot.get_channel(ChanID[arg1])
    await channel.send(arg2)
    owner = ctx.bot.get_user(173792811169218570)
    print(arg1, arg2)
    user = ctx.message.author #hvem som har skrevet meldingen
    print(user)
    await owner.send(user) #sender 3 meldinger til eieren. Smart for å vite hvem som har sagt hva
    await owner.send(arg2)
    await owner.send(arg1)
    return
  @commands.command(
      name='meme',
      description='Ernie memes are the best memes',
      aliases=['erniememe']
  )
  async def meme(self, ctx):
    randmeme = random.choice(memes2.erniememe)
    await ctx.send('Here is a ernie meme' + randmeme)

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
            user2 = ctx.message.author
            if user == user2:
              return 'shutting down' and m.channel == channel
            else:
              msg.content = "None"
    msg = await ctx.bot.wait_for('message', check=check)
    if msg.content == "Y":
      await ctx.send("Logging out")
      await ctx.bot.close()
    if msg.content == "N":
      await ctx.send("OK then, I'll stay :)")
    if msg.content == "None":
      await ctx.send("You are not the same person")

  @Shutdown.error
  async def Shutdown_error(error, ctx):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send_message(ctx.message.channel, text)
  @commands.command(
      name='quote',
      description='Random quote from inspirobot.com',
      aliases=['qo']
  )
  async def random_quote(self, ctx):
    website = requests.get('https://inspirobot.me/api?generate=true')
    html = website.text
    pat = re.compile(r'<\s*img [^>]*src="([^"]+)')
    img = pat.findall(html)
    await ctx.send(html)
    

def setup(client):
    client.add_cog(Basic(client))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file

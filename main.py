from discord.ext import commands
import discord
import os
from keep_alive import keep_alive
import datetime
from datetime import date, timedelta
import asyncio

originaldate = date.today()
onlycheck = True

def get_prefix(client, message):
    prefixes = ['=', '==']
    if not message.guild:
        prefixes = ['==']
    return commands.when_mentioned_or(*prefixes)(client, message)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=get_prefix,
    description='Erniebot, the homemade bot run on Repl.it server (free). Anyways, the bot is quite shit. And has almost no commands. But hey, its name has Ernie in it at least.',
    owner_id=173792811169218570,
    case_insensitive=True,
    intents=intents
)

cogs = ['cogs.basic']

@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            print(f"Loaded cog: {cog}")
        except Exception as e:
            print(f"Failed to load cog {cog}: {e}")
    print(f"Loaded commands: {[cmd.name for cmd in bot.commands]}")
    asyncio.create_task(sleepfunction())

@bot.event
async def on_command(ctx):
    try:
        owner = await bot.fetch_user(bot.owner_id)
        if owner:
            server = ctx.guild.name if ctx.guild else "DM"
            channel = ctx.channel.name if hasattr(ctx.channel, 'name') else "DM"
            await owner.send(f"Command used: `{ctx.command.name}` by **{ctx.author}** in #{channel} ({server})")
    except Exception as e:
        print(f"Failed to send DM notification: {e}")

async def morning_post():
    channel = bot.get_channel(393726535418380291)
    if channel:
        today = date.today()
        await channel.send(f"God morgen dere! Datoen i dag er {today}")
        await channel.send("Takk for meg! Kommer tilbake med oppdatering i morgen :)")
    await sleepfunction()

async def sleepfunction():
    global onlycheck
    print("sleepfunction active")
    now = datetime.datetime.now()
    today6am = now.replace(hour=6, minute=0, second=0, microsecond=0)
    
    if now < today6am:
        print("Waiting until 6am")
        await discord.utils.sleep_until(today6am)
        await morning_post()
    else:
        nextdate = date.today() + timedelta(days=1)
        schedule = today6am.replace(day=nextdate.day)
        print(f"Scheduled for: {schedule}")
        await discord.utils.sleep_until(schedule)
        await morning_post()

keep_alive()
token = os.environ.get('secretkey')
if token:
    bot.run(token, reconnect=True)
else:
    print("ERROR: No 'secretkey' environment variable found. Please set your Discord bot token.")

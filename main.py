from discord.ext import commands
import discord
import os
from keep_alive import keep_alive
import datetime
from datetime import date, datetime, timedelta
originaldate = date.today()
import todayprime
used = True


async def morning_post():
  channel = channel = bot.get_channel(393726535418380291)
  prime = todayprime.prime
  await channel.send("God morgen dere! Datoen i dag er",originaldate)
  await channel.send("Dagens primtall er forresten:", prime)
  await channel.send("Takk for meg! Kommer tilbake med oppdatering i morgen :)")
  sleepfunction()
def get_prefix(client, message): #Sets prefix

    prefixes = ['=', '==']    # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['==']   # Only allow '==' as a prefix when in DMs, this is optional

    # Allow users to @mention the bot instead of using a prefix when using a command. Also optional
    # Do `return prefixes` if u don't want to allow mentions instead of prefix.
    return commands.when_mentioned_or(*prefixes)(client, message)
bot = commands.Bot(                         # Create a new bot
    command_prefix=get_prefix,              #calls the prefix function
    description='Erniebot, the homemade bot run on Repl.it server (free). Anyways, the bot is quite shit. And has almost no commands. But hey, its name has Ernie in it at least.',  # Sets a description for the bot
    owner_id=173792811169218570,  #owner id for 'say'command. Not used anymore though...
    case_insensitive=True       
)
cogs = ['cogs.basic'] #which cogs is active
@bot.event
async def on_ready(): #When bot have started
    print("I'm in")
    print(bot.user)
    for cog in cogs: #loads all cogs
        bot.load_extension(cog)
    await sleepfunction()

    
async def sleepfunction():
  print("sleepfunction active")
  global used
  if used == True: #Hvis ikke brukt
    print("Is used")
    used = False
    now = datetime.now()
    today6am = now.replace(hour=6, minute=0, second=0, microsecond=0)
    if now < today6am: #If before 6am
      print("Waiting until 6am")
      await discord.utils.sleep_until(today6am)
      morning_post()
    if now > today6am: #If after 6am
      nextdate = date.today() + timedelta(days=1)
      nextday = nextdate.day
      schedule = today6am.replace(day=nextday)
      print(schedule)
      await discord.utils.sleep_until(schedule)
      morning_post()
  if used == False: #Hvis brukt
    global onlycheck
    if onlycheck == True: #Hvis kun en er der
      onlycheck = False
      now = datetime.datetime.now()
      nextdate = datetime.date.today() + datetime.timedelta(days=1)
      today6am = now.replace(hour=6, minute=0, second=0, microsecond=0)
      nextday = nextdate.day
      schedule = today6am.replace(date=nextday)
      await discord.utils.sleep_until(schedule)
      onlycheck = True
      morning_post()
    if onlycheck == False:
      print("ONLYCHECK ERROR")
  return

keep_alive() #calls keep_alive for keeping the bot alive and preventing it from shutting down after 1 hour
token = ("NjcxMDEzOTM0ODk1MDcxMjMy.Xi2wbA.k70Dqc08MJyU1pqCXH8uEN4qKyE") #secret token
bot.run(token, bot = True, reconnect = True) #runs bot
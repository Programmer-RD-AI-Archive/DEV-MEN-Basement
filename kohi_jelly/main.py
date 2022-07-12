import nextcord
import os
from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.members = True
cmdpre = "U>"

client = commands.Bot(command_prefix = cmdpre, intents = intents)

client.remove_command("help")

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  print(cmdpre)


@client.command()
async def help(ctx):
  embed = nextcord.Embed(title='Keep Calm ☕', description='**THE MENU**', color=0xc96f52, timestamp=ctx.message.created_at)
  embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/943421971683762206/995640340105150505/c601eef9665b7acd17692c7a384dc8ea.jpg') 
  embed.add_field(name= '''__help__📗''',value = '''```this is self explanatory```''', inline = False)
  await ctx.reply(embed=embed)

@client.command()
async def ping(ctx):
  await ctx.send(f'''```the ping = {round(client.latency * 1000)}```''')




client.run(os.environ['TOKEN']) 
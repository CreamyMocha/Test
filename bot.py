import discord
import asyncio
import random
import datetime
import aiohttp
from discord.ext.commands import Bot
from discord.ext import commands
  
Client = discord.Client()
bot_prefix= "+"
client = commands.Bot(command_prefix=bot_prefix)
  
@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    #Extra 1
    await client.change_presence(game=discord.Game(name='with Stress'))

@client.command(pass_context=True)
async def cheryl(ctx):
    await client.say("Tac reload!")
 
#command1
@client.command(pass_context = True)
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to ban!")
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")
 
    embed = discord.Embed(description = "**%s** has been banned!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)
 
#command2
@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to kick!")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")
 
    embed = discord.Embed(description = "**%s** has been kicked!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)

#command3

assignable_roles = ["na", "sa", "eu", "sea", "ea"]

@client.command(pass_context = True)
async def role(ctx, role=None):
    if not role: return await client.say("You did not specify a role.")
    
    server_role = [item for item in ctx.message.server.roles if item.name.lower() == role.lower()]

    if len(server_role) == 0: return await client.say(f"Could not find role **{role}**")
    server_role = server_role[0]

    try:
        await client.add_roles(ctx.message.author, server_role)
        await client.say(f"Successfully added **{server_role.name}**.")
    except Exception as e:
        await client.say(f"Error: `{e}`")

#command4
still_triggered = False
@client.event
async def on_message(message):
    global still_triggered
    if message.content.startswith("+"): return await client.process_commands(message) #So it doesn't trigger on commands
    if not message.server: return #So its not in a dm channel
    if message.author == client.user: return #so its not triggering itself
    if still_triggered: return #if its already been triggered

    still_triggered = True
    await asyncio.sleep(300)
    await client.send_message(message.channel, "Test")
    still_triggered = False

#command5
@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
#command6
@client.command(pass_context=True)
async def poll(ctx,*, message: str):
    embed = discord.Embed(color = ctx.message.author.color, timestamp = datetime.datetime.utcnow())
    embed.set_author(name = "Poll", icon_url = ctx.message.author.avatar_url)
    embed.description = (message)
    embed.set_footer(text = ctx.message.author.name)
    x = await client.say(embed = embed)
    await client.add_reaction(x, "👍")
    await client.add_reaction(x, "👎")
#command7
@client.command(pass_context = True, no_pm = True)
async def announce(ctx, *, announcement: str):
    if ctx.message.author.server_permissions.administrator:
     """Sends an announcement in the channel you use the command"""
    embed=discord.Embed(title = "__Announcement__", description= announcement, color = 0xFF0000)
    await client.delete_message(ctx.message)
    await client.say(embed = embed)
    if not ctx.message.author.server_permissions.administrator:
        await bot.say("**You do not have permissions for this command!**")
#command8
@client.command()
async def ud(*msg):
    """Search words on Urban Dictionary"""
    word = ' '.join(msg)
    api = "http://api.urbandictionary.com/v0/define"
    async with aiohttp.ClientSession() as session:
        async with session.get(api, params={'term': word}) as r:
            response = await r.json()

        if len(response["list"]) == 0:
            x = "Could not find that word!"
            embed=discord.Embed(title='Error', color=0xFF0000)
            embed.description = x
            await client.say(embed=embed)
            
        else:
                embed = discord.Embed(title='Urban Dictionary - ' + word, color=0x00FF00)
                embed.description = response['list'][0]['definition']
                embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/B4lcjSHEDA8RcuizSOAdc92ithHovZT6WkRAX-da_6o/https/erisbot.com/assets/emojis/urbandictionary.png')
                embed.add_field(name="Examples:", value=response['list'][0]["example"][:1000])
                embed.set_footer(text="Tags: " + ', '.join(response['tags']))
                await client.say(embed=embed)
#command9
@client.command(pass_context = True)
async def warn(ctx, member : discord.Member, *, message):
    return await client.send_message(member, message)
#command10
@client.command(pass_context=True)
async def lol(ctx):
    with open("lol/FGGGHHDZ.gif", "rb") as f: 
    	await client.delete_message(ctx.message)
        await client.upload(f) # This is the part that uploads the file
client.run(process.env.BOT_TOKEN);

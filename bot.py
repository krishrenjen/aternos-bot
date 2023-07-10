import discord
from discord.ext import commands
from python_aternos import Client
from discord.ui import Button, View


#aternos shit
username = {username}
password = {password}

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "!", case_insensitive=True, intents = intents)
token = {token}
aternos = Client.from_credentials(username, password)

@client.command(pass_context=True)
async def status(ctx):
    embed=discord.Embed(color=0xae00ff)
    embed.set_author(name="Servers Statuses")
    servs = aternos.list_servers(cache=False)
    count = 0

    for serv in servs:
        count+=1
        embed.add_field(name=f"{serv.address}", value= f"*{serv.status}*", inline=True)

    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def info(ctx):
    embed=discord.Embed(color=0xae00ff)
    embed.set_author(name="Servers")
    servs = aternos.list_servers(cache=False)
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    count = 0
    view = View(timeout=10)
    

    async def button_callback(interaction):
        try:
            serv = servs[int(interaction.custom_id)]
            embed2=discord.Embed(color=0xae00ff)
            embed2.set_author(name="Server Information")
            embed2.add_field(name=f"Server Address", value= f"*{serv.address}:{serv.port}*", inline=False)
            embed2.add_field(name=f"Status", value= f"*{serv.status}*", inline=False)
            embed2.add_field(name=f"Software", value= f"*{serv.software} {serv.version}*", inline=False)
            embed2.add_field(name=f"Player Count", value= f"*{serv.players_count}/{serv.slots}*", inline=False)
            embed2.add_field(name=f"MOTD", value= f"*{serv.motd}*", inline=False)
            playerNames = ""
            for i, plr in enumerate(serv.players_list):
                if(i == len(serv.players_list)-1):
                    playerNames += plr
                else:
                    playerNames += plr + ", "

            if len(serv.players_list) == 0:
                playerNames = "None"
            embed2.add_field(name=f"Players", value= f"*{playerNames}*", inline=False)

            await interaction.response.edit_message(embed=embed2, view=None)
        except:
            await interaction.response.edit_message(content="We ran into a problem...", embed=None, view=None)

            

    
    for serv in servs:
        count+=1
        embed.add_field(name=f"Server {count}", value= f"*{serv.address}*", inline=True)
        if count <= len(emojis) + 1:
            button = Button(label=f"Server {count} - {serv.address}", style=discord.ButtonStyle.green, emoji = emojis[count-1], custom_id=str(count-1))
            button.callback = button_callback
            view.add_item(button)
        else:
            button = Button(label=f"Server {count} - {serv.address}", style=discord.ButtonStyle.green, custom_id=str(count-1))
            button.callback = button_callback
            view.add_item(button)

    await ctx.send(embed=embed, view=view)

@client.command(pass_context=True)
async def start(ctx):
    embed=discord.Embed(color=0xae00ff)
    embed.set_author(name="Servers")
    servs = aternos.list_servers(cache=False)
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    count = 0
    view = View(timeout=10)
    

    async def button_callback(interaction):
        try:
            servs[int(interaction.custom_id)].start()
            await interaction.response.edit_message(content="Starting server...", embed=None, view=None)
        except:
            await interaction.response.edit_message(content="Server already started or we ran into a problem...", embed=None, view=None)

    
    for serv in servs:
        count+=1
        embed.add_field(name=f"Server {count}", value= f"*{serv.address}*", inline=True)
        if count <= len(emojis) + 1:
            button = Button(label=f"Server {count} - {serv.address}", style=discord.ButtonStyle.green, emoji = emojis[count-1], custom_id=str(count-1))
            button.callback = button_callback
            view.add_item(button)
        else:
            button = Button(label=f"Server {count} - {serv.address}", style=discord.ButtonStyle.green, custom_id=str(count-1))
            button.callback = button_callback
            view.add_item(button)

    await ctx.send(embed=embed, view=view)

@client.command(pass_context=True)
async def stop(ctx):
    embed=discord.Embed(color=0xae00ff)
    embed.set_author(name="Servers")
    servs = aternos.list_servers(cache=False)
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    count = 0
    view = View(timeout=10)
    

    async def button_callback(interaction):
        try:
            servs[int(interaction.custom_id)].stop()
            await interaction.response.edit_message(content="Stopping server...", embed=None, view=None)
        except:
            await interaction.response.edit_message(content="Server already stopped or we ran into a problem...", embed=None, view=None)

    
    for serv in servs:
        count+=1
        embed.add_field(name=f"Server {count}", value= f"*{serv.address}*", inline=True)
        if count <= len(emojis) + 1:
            button = Button(label=f"Server {count} - {serv.address}", style=discord.ButtonStyle.green, emoji = emojis[count-1], custom_id=str(count-1))
            button.callback = button_callback
            view.add_item(button)
        else:
            button = Button(label=f"Server {count} - {serv.address}", style=discord.ButtonStyle.green, custom_id=str(count-1))
            button.callback = button_callback
            view.add_item(button)

    await ctx.send(embed=embed, view=view)

@client.command(pass_context=True)
async def restart(ctx):
    embed=discord.Embed(color=0xae00ff)
    embed.set_author(name="Servers")
    servs = aternos.list_servers(cache=False)
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    count = 0
    view = View(timeout=10)
    

    async def button_callback(interaction):
        try:
            servs[int(interaction.custom_id)].restart()
            await interaction.response.edit_message(content="Starting server...", embed=None, view=None)
        except:
            await interaction.response.edit_message(content="Server already started or we ran into a problem...", embed=None, view=None)

    
    for serv in servs:
        count+=1
        embed.add_field(name=f"Server {count}", value= f"*{serv.address}*", inline=True)
        if count <= len(emojis) + 1:
            button = Button(label=f"Server {count} - {serv.address}", style=discord.ButtonStyle.green, emoji = emojis[count-1], custom_id=str(count-1))
            button.callback = button_callback
            view.add_item(button)
        else:
            button = Button(label=f"Server {count} - {serv.address}", style=discord.ButtonStyle.green, custom_id=str(count-1))
            button.callback = button_callback
            view.add_item(button)

    await ctx.send(embed=embed, view=view)

@client.event
async def on_ready():
    print("bot online")


client.run(token)

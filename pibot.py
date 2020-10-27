import discord
import jlrpy

from discord.ext import commands

token = open("token.txt", "r").read()
password = open("password.txt", "r").read()

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
        
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    c = jlrpy.Connection('username', 'password')
    v = c.vehicles[0]
    brand = v.get_attributes()['vehicleBrand']
    color = v.get_attributes()['exteriorColorName']
    fuel = v.get_attributes()['engineCode']
    year = v.get_attributes()['modelYear']
    doors = v.get_attributes()['numberOfDoors']
    if message.content.lower() == 'info':
        response = ('info about your vehicle: ' + brand + '\n' + color + '\n' + fuel)
        await message.channel.send(response)
bot.run(token)

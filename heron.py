# Code by Fernando Assad and Pedro Squisati

import discord, matplotlib.pyplot as plt, numpy as np
from math import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  #id = client.get_guild(CHANGE THIS)
  
  if message.author == client.user:
        return

  # PLOT A FUNCTION 
  if message.content.startswith('plot'):
    function = message.content[5:]
    x_axis = list(np.linspace(-50, 50, 10001))
    y_axis = []
    for x in x_axis:
        y_axis.append(eval(function))
    plt.plot(x_axis, y_axis)
    plt.grid(color='k', linestyle='-', linewidth=0.3)
    plt.title(f'f(x) = {message.content[5:].replace("**", "e")}')
    plt.savefig('graph.png')
    plt.clf()
    await message.channel.purge(limit=1)
    await message.channel.send(file=discord.File('graph.png'))

  # FIND ROOTS
  if message.content.startswith('roots'):
    await message.channel.purge(limit=1)
    raw = message.content[6:]
    function = raw.strip('][').split(',')
    function1 = []
    for n in function:
      n =  float(eval(n))
      function1.append(n)
    power = len(function1) - 1
    fx = ''
    for n in function1:
      fx = fx + f'{str(n)}x^{str(power)} + '
      power -= 1
    fx = f"```{fx[:len(fx) - 2].replace('x^0', '')}```"
    await message.channel.send(fx)
    lista = np.roots(function1)
    for i in range(len(lista)):
        await message.channel.send(f'Root {i+1}: {round(lista[i], 5)}')

# client.run('CHANGE THIS')

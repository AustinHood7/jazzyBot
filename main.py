import discord
import random
import numpy as np

TOKEN = 'OTc1OTM2NzY4NzQ0NTA1Mzg1.GOcvjI.Z-E0DQUP6JInDkbDmP-1cyj_ht3eTumRF2CL_w'
client = discord.Client()

arr = np.array(["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "G", "G#"])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    root = ''
    third = ''
    fifth = ''
    seventh = ''
    ninth = ''

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number : {random.randrange(1000000)}'
            await message.channel.send(response)
            return

        elif user_message.lower() == '!menu':
            await message.channel.send(
                f'!jazz (chord name)- Gives alternative options to your choice of major or minor triad\n'
                f'!comp (chord name) - Gives the note composition of major or minor triads\n'
                f'!chord list - Gives a list of valid chord names to use with comp or jazz\n')
            return
        elif user_message.lower() == '!comp a':
            root = "A"
            third = getThird(root)
            # fifth = getFifth(root);
            await message.channel.send(root + ' ' + third + ' E')
        return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return

def getThird(chord):
    for x, note in enumerate(arr):  # for all elements of the array
        if note == chord:  # move pointer to the selected chord
            third = (x + 4) % 12
            return arr[third]


client.run(TOKEN)


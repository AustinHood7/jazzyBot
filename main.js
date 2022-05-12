const { Client, Intents } = require('discord.js');

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

client.once('ready', () => {
    console.log('jazzyBot is online!');
});

//token to be made invalid
client.login('OTc0MTcxNzQ0NDA5NjI0NTg3.G7hsXu.JKCHnPbftRqVu1KEstICjx00f__GAWJriFYM6E');
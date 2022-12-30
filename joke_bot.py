import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content == '/programmer-joke':
        jokes = [
            "Why do programmers always mix up Halloween and Christmas? Because Oct 31 equals Dec 25.",
            "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
            "Why do programmers hate nature? It has too many bugs.",
            "Why do programmers always have caffeine on hand? Because it's a debugging tool.",
            "Why did the computer go to the doctor? It had a virus.",
            "Why was the computer cold? Because it left its Windows open.",
            "Why was the computer tired when it got home? It had too many tabs open.",
            "Why did the computer get a ticket? It was parked in a USB port.",
            "Why was the computer wet? It left its Windows open during a rainstorm.",
            "Why did the computer go to therapy? It was suffering from CPU stress."
        ]
        random_joke = jokes[random.randint(0, len(jokes) - 1)]
        await message.channel.send(random_joke)

client.run('MTA1ODIzMjAyNzkwOTk4ODM3Mg.GKBs70.Y211I0niusBd3hAq8S7wie_gLGiVt-cNlrwzpM')

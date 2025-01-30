import random

import discord

from . import tarot

cards = ""
names = tarot.names  # TODO

client = discord.Client(intents=discord.flags.Intents.none())


@client.event
async def on_message(message):

    global names

    ## Respond if user sends "!tarot"
    if message.content.startswith("!tarot"):

        ## Split into into "!tarot" and number of cards to draw
        bits = message.content.split(" ")

        num = ""
        comment = ""
        sep = " "
        nl = "\n"

        ##        print(bits)

        # If no other arguments, default to drawing 5 cards
        if len(bits) == 1:
            num = 5

        if len(bits) > 1:
            if list(bits[1])[0] == "#":
                comment = sep.join(bits[1:])
                num = 5
            elif list(bits[1])[0] == "?":
                comment = ""
            elif bits[1] == "info":
                comment = ""
            elif bits[1] in ["ind", "loc", "cul", "plo", "cre", "art"]:
                num = 5
                if bits[1] == "ind":
                    tmp = tarot.ind
                elif bits[1] == "loc":
                    tmp = tarot.loc
                elif bits[1] == "cul":
                    tmp = tarot.cul
                elif bits[1] == "plo":
                    tmp = tarot.plo
                elif bits[1] == "cre":
                    tmp = tarot.cre
                elif bits[1] == "art":
                    tmp = tarot.art

            elif isinstance(int(list(bits[1])[0]), int):
                num = int(bits[1])
                if len(bits) > 2:
                    if bits[2] in ["major", "maj"]:
                        names = tarot.major_arcana
                    elif bits[2] in ["minor", "min"]:
                        names = tarot.minor_arcana

        if len(bits) > 2:
            if list(bits[2])[0] == "#":
                comment = sep.join(bits[2:])

        if len(bits) > 3:
            if list(bits[3])[0] == "#":
                comment = sep.join(bits[3:])

        msg = "```md\n"
        if comment != "":
            msg += comment
            msg += "\n"

        if isinstance(num, int):
            ## Restrict/check the number of cards to be drawn
            if num > 10:
                num = 10
                msg = "10 is the maximum number of cards.\n\n"

            if num < 1:
                num = 1
                msg = "You must draw at least 1 card.\n\n"

            ## Draw a randow sample (without replacement) from list of cards
            cards = random.sample(names, k=num)

            ## Loop through 1 to n, adding card number and descriptor to message each time
            ## Creates a single string, with newline characters separateing each card.
            for i in range(1, num + 1):
                msg += "Card {0}: {1}\n".format(i, cards[i - 1])

        if len(bits) > 1 and list(bits[1])[0] == "?":
            msg = "```md\n"
            if bits[1] in ["?", "help"]:
                msg += "# Usage:\n"
                msg += "!tarot ? - displays this message\n"
                msg += "!tarot info - displays bot code info\n"
                msg += "!tarot - draws 5 cards\n"
                msg += "!tarot n - draws n cards (1-10)\n"
                msg += "!tarot n # comment - adds a comment to the output\n"
                msg += "!tarot n maj - draws n cards from the major arcana\n"
                msg += "!tarot n min - draws n cards from the minor arcana\n"
                msg += "!tarot ?xxx - lists card definitions for template xxx\n"
                msg += "!tarot xxx - makes a 5 card draw for template xxx\n"
                msg += "# Templates: individuals (ind), locations (loc), cults (cul), plots (plo), creatures (cre) or artifacts (art)\n"

            if bits[1] == "?ind":
                msg += nl.join(tarot.ind)

            elif bits[1] == "?loc":
                msg += nl.join(tarot.loc)

            elif bits[1] == "?cul":
                msg += nl.join(tarot.cul)

            elif bits[1] == "?plo":
                msg += nl.join(tarot.plo)

            elif bits[1] == "?cre":
                msg += nl.join(tarot.cre)

            elif bits[1] == "?art":
                msg += nl.join(tarot.art)

        if len(bits) > 1 and bits[1] in ["ind", "loc", "cul", "plo", "cre", "art"]:
            msg = "```md\n"
            msg += tmp[0]
            msg += ":"
            msg += comment[1:]
            msg += "\n"
            for i in range(0, 5):
                msg += "{0}\n#       {1}\n".format(tmp[i + 1], cards[i])

        ## Bot info
        if len(bits) > 1 and bits[1] == "info":
            msg = "```md\n"
            msg += "# KultTarotBot\n"
            msg += "Code available at: https://github.com/rpgmik/KultTarotBot\n"
            ## Collect server install info
            msg += (
                "Currently running on "
                + str(len(list(client.guilds)))
                + " Discord guilds.\n"
            )

        msg += "```"

        ##        print('bits[1]='+bits[1]+'\n')
        ## Send message to channel

        ##        print(bits)
        ##        print(msg)

        await message.channel.send(msg)


## Write login details locally (i.e., on linux box where bot code is running)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Kult: !tarot ? for help"))
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

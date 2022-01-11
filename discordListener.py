import discord
import sendWebhook as d
from config import c
import tda
import json

client = discord.Client()
guild = discord.Guild

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game('Listening For Alerts'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('MACD'):

        cmd = message.content

        # Bot Commands
        answer = discord.Embed(title="Sending Order",
                               description= cmd,
                               colour=0x1a7794) 

        await message.channel.send(embed=answer)

        #MACD Buy NIO 674.86'
        cmdArray = cmd.split(" ")
        inst, tkr, prc = d.getCmds(cmdArray)

        tdaClient = tda.auth.easy_client(
            api_key= c.api_key,
            redirect_uri=c.redirect_url,
            token_path=c.token_path)

        order = ""

        if inst == "Buy":
            prc = round(float(prc)*(1 - c.macdPercentDiff),2)
            order = tda.orders.equities.equity_buy_limit(tkr, c.shareNumber, prc).build()
        elif inst == "Sell":
            prc = round(float(prc)*(1 + c.macdPercentDiff),2)
            order = tda.orders.equities.equity_sell_limit(tkr, c.shareNumber, prc).build()
        
        response = tdaClient.place_order(c.account_number_77g, order)

        if (str(response) == '<Response [201 ]>'):
            d.send("Sent " + str(1) + " " + tkr + " " + inst + " at $" + str(prc))
            print("Succesfully Placed Order")

        else:
            error = json.loads(response.content)
            errorS = error['error']
            d.send(errorS)

    elif message.content.startswith('RSI'):

        cmd = message.content

        #Bot Commands
        answer = discord.Embed(title="Sending Order",
                               description= cmd,
                               colour=0x1a7794) 

        await message.channel.send(embed=answer)

        #RSI Buy SKLZ 10.86'
        cmdArray = cmd.split(" ")
        inst, tkr, prc = d.getCmds(cmdArray)

        tdaClient = tda.auth.easy_client(
            api_key= c.api_key,
            redirect_uri=c.redirect_url,
            token_path=c.token_path)

        order = ""

        if inst == "Buy":
            prc = round(float(prc)*(1 - c.rsiPercentDiff),2)
            order = tda.orders.equities.equity_buy_limit(tkr, c.shareNumber, prc).build()
        elif inst == "Sell":
            prc = round(float(prc)*(1 + c.rsiPercentDiff),2)
            order = tda.orders.equities.equity_sell_limit(tkr, c.shareNumber, prc).build()

        response = tdaClient.place_order(c.account_number_77g, order)

        if (str(response) == '<Response [201 ]>'):
            d.send("Sent " + str(1) + " " + tkr + " " + inst + " at $" + str(prc))
            print("Succesfully Placed Order")

        else:
            error = json.loads(response.content)
            errorS = error['error']
            d.send(errorS)

try:
    client.run(c.discordToken)
except KeyboardInterrupt:
    client.close()
import nextcord, os, requests, util
from dotenv import load_dotenv
from table2ascii import table2ascii as t2a, PresetStyle
from nextcord.ext import commands
load_dotenv(dotenv_path="key.env")

auth_session = util.auth()[0]
access_token = auth_session["access_token"]
refresh_token = auth_session["refresh_token"]
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.slash_command(name="reauth", description="Reauthenticate the bot with the FishTank.live API", guild_ids=[int(os.getenv("TESTING_GUILD_ID"))])
async def reauth(interaction: nextcord.Interaction):
    global auth_session, access_token, refresh_token
    auth_session = util.auth()[0]
    access_token = auth_session["access_token"]
    refresh_token = auth_session["refresh_token"]

    await interaction.response.send_message("Reauthenticated successfully!")

@bot.slash_command(name="getstoxreport", description="Get a report of the StoX fluctuations", guild_ids=[int(os.getenv("TESTING_GUILD_ID"))])
async def get_stox_report(interaction: nextcord.Interaction):
    stocks = []
    stocks_response = requests.get(url="https://api.fishtank.live/v1/stocks", headers={f"Authorization": f"Bearer {access_token}"}).json()
    message = "Here is your report:\nName | Price | TodayPrice | LowSell | HighBuy\n"
    for stock in stocks_response["stocks"]:
        #print(stock)
        message += (str(stock["tickerSymbol"]) + " | " + str(stock["currentPrice"]) + " | " + str(stock["today"]) + " | " + str(stock["lowestSellOrder"]) + " | " + str (stock["highestBuyOrder"]) + "\n")
    #message = t2a(header=["Name", "Current Price", "Today Price", "Lowest Sell Order", "Highest Buy Order"], body=stocks[0], style=PresetStyle.thin_compact)
    await interaction.response.send_message(f"```\n{message}\n```")

@bot.slash_command(name="getownedstox", description="Get information on the owned StoX", guild_ids=[int(os.getenv("TESTING_GUILD_ID"))])
async def get_owned_stox(interaction: nextcord.Interaction):
    stocks_response = requests.get(url="https://api.fishtank.live/v1/stocks", headers={f"Authorization": f"Bearer {access_token}"}).json()
    data_response = requests.get(url="https://api.fishtank.live/v1/initial-data", headers={f"Authorization": f"Bearer {access_token}"}).json()
    message = "Here is your owned StoX:\nTicker | Amount | Investment | Value\n"
    portfolio = 0
    for stock in stocks_response["stocks"]:
        if stock["myHoldings"] > 0:
            portfolio += stock["currentPrice"] * stock["myHoldings"]
            message += (str(stock["tickerSymbol"]) + " | " + str(stock["myHoldings"]) + " | " + str(stock["totalInvestment"]) + " | " + str(stock["currentPrice"] * stock["myHoldings"]) + "\n")
    await interaction.response.send_message(f"```\n{message}\nCurrent Balance: {data_response["initialData"]["profile"]["tokens"]}\nTotal Portfolio Value: {portfolio}\n```")

@bot.slash_command(name="clearchannel", description="Clear the current channel", guild_ids=[int(os.getenv("TESTING_GUILD_ID"))])
async def clear_channel(interaction: nextcord.Interaction):
    if interaction.channel.permissions_for(interaction.guild.me).manage_messages:
        deleted = await interaction.channel.purge(limit=100)
        await interaction.response.send_message(f"Deleted {len(deleted)} messages.", ephemeral=True)
    else:
        await interaction.response.send_message("I do not have permission to manage messages in this channel.", ephemeral=True)


bot.run(os.getenv("BOT_TOKEN"))
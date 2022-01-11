import json

class Config():
    def __init__(self):

        #TDA Info
        self.client_id = "Enter Client ID"
        self.api_key = "Enter API Key"
        self.account_number = 123456789
        self.token_path = "token"
        self.redirect_url = "https://localhost"

        #Discord Info
        self.webhookUrl = "Enter Webhook URL"
        self.discordToken = "Enter Discord Token"

        #Custom Order Constants
        self.rsiPercentDiff = 0.01
        self.macdPercentDiff = 0.00
        self.shareNumber = 1

c = Config()
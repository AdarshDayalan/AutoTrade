import requests
from config import c

def send(msg):
    data = {'content': str(msg)}
    requests.post(url = c.webhookUrl, json = data)

def cSend(msg, url):
    data = {'content': str(msg)}
    requests.post(url = url, json = data)

def getCmds(a):
    return a[1], a[2], a[3]
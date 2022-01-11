from config import c
import tda
from selenium import webdriver

driver = webdriver.Chrome(executable_path='Enter Chrome Driver Path')

td = tda.auth.client_from_login_flow(driver, c.api_key, 
c.redirect_url, c.token_path, redirect_wait_time_seconds=0.1, 
max_waits=3000, asyncio=False, token_write_func=None)

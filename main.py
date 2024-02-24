from dotenv import load_dotenv
import sys
import os
# from modules.calculator_bot import CalculatorBot
from modules.count_till_thouthand import CountBot

load_dotenv(".env")
token = os.getenv("token")

try:
    n = int(sys.argv[1])
except:
    n = -1

if n == -1:
    n = None

# bot = CalculatorBot(token)
bot = CountBot(token)
bot.loop(n)

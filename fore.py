from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep, time
from colorama import Fore,Style, init as color_ama
color_ama(autoreset=True)
import json, re, sys, os, random

banner = Style.BRIGHT+Fore.MAGENTA +  """ _____           _                    _        _____   _______
 |   \         | |                  | |      |_   _| |   |
 | |) |   ___  | |_   _    _   _  | |      | |      | |
 |  ___/   / _ \ | | | '| | | | | | |/ /     | |      | |
 | |      |  / | |_  | |    | |_| | |   <     _| |_     | |
 |_|       \___|  \| |_|     \__,_| |_|\_\   |_____|    |_|
"""+Style.BRIGHT+Fore.WHITE+"""================================================================
"""+Style.BRIGHT+Fore.YELLOW + """[+]Auto Click Bonus @Earn_Daily_cash_bot
[+]Author: Petruk Sensei
[+]Blog: https://petruk-internet.blogspot.com
"""
putih = Style.BRIGHT+Fore.WHITE
hijau = Style.BRIGHT+Fore.GREEN
merah = Style.BRIGHT+Fore.RED
kuning = Style.BRIGHT+Fore.YELLOW
reset = Fore.RESET
biru = Style.BRIGHT+Fore.BLUE

def jeda():
  sys.stdout.write(f'\r')

os.system('clear') 
print(banner)
if not os.path.exists('session'):
    os.makedirs('session')
if len(sys.argv) < 2:
    print( Fore.RED + '\n\nUsage : python main.py +62' + Fore.RESET)
    sys.exit(1)
api_id = 1148490
api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
phone_number = sys.argv[1]
client = TelegramClient('session/' + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input(Fore.WHITE + 'Enter Yout Code Code : '))
    except SessionPasswordNeededError:
        passw = input(Fore.RESET + 'Your 2fa Password : ')
        me = client.start(phone_number, passw)
saia = client.get_me()
print('[*]Account:',saia.first_name)
print('[*]Phone:',saia.phone,'\n')
channel_username = '@BTC_Forecast_Group'
channel_entity = client.get_entity('@BTC_Forecast_Group')
print('Memulaii!!')

while True:
  try:
    client.send_message(entity=channel_entity, message='/d')
    posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
    s = re.search(r'Current value: [0-9.]*',posts.messages[1].message).group(0)
    print(f'{putih}Success add Bonus | {hijau}{s}')
  except:
    print(f'{hijau}Sudah terkirim')

sys.exit()
client.disconnect()

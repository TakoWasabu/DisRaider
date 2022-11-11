import threading, requests, time, random, os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
os.system("title Disraider - Before Settings")
print("""
       ██████╗ ██╗███████╗██████╗  █████╗ ██╗██████╗ ███████╗██████╗
       ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
       ██║  ██║██║███████╗██████╔╝███████║██║██║  ██║█████╗  ██████╔╝
       ██║  ██║██║╚════██║██╔══██╗██╔══██║██║██║  ██║██╔══╝  ██╔══██╗
       ██████╔╝██║███████║██║  ██║██║  ██║██║██████╔╝███████╗██║  ██║
       ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
         Made by Tak0_User             Remaked by Milkey_Crypto """)
channel = input('Id of channel: ')
mess = input('Message to spam: ')
delay = input('Delay: ')
sent = 0

tokens = open("tokens.txt", "r").read().splitlines()

def spam(token, channel, mess):
    global sent
    url = 'https://discord.com/api/v9/channels/'+channel+'/messages'
    while True:
        testa = random.randrange(6, 15)
        BypassStrings = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-_,.'
        Bypass = ''.join(random.choice(BypassStrings) for _ in range(testa))
        header = {"authorization": token}
        data = {"content": mess + Bypass}
        time.sleep(float(delay))
        r = requests.post(url, data=data, headers=header)
        print(r.status_code)
        sent += 1

def thread():
    channel_id = channel
    for token in tokens:
        global sent
        os.system(f"title Disraider - Sent Message {sent}")
        text = mess
        time.sleep(float(delay))
        threading.Thread(target=spam, args=(token, channel_id, text)).start()

os.system("title Disraider - Enter to Start Spam")
start = input('Press eny key when you will be ready ')
start = thread()

import requests
import discord
import os

yazi = """
 ██████╗ ██████╗  █████╗ ██╗   ██╗██╗████████╗██╗   ██╗    ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗
██╔════╝ ██╔══██╗██╔══██╗██║   ██║██║╚══██╔══╝╚██╗ ██╔╝    ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
██║  ███╗██████╔╝███████║██║   ██║██║   ██║    ╚████╔╝     ███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝ 
██║   ██║██╔══██╗██╔══██║╚██╗ ██╔╝██║   ██║     ╚██╔╝      ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝  
╚██████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║   ██║      ██║       ███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║   
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝   ╚═╝      ╚═╝       ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝                                      
_____________________________________________________________________
"""

os.system("cls")
print(yazi)
print("[1] Clear")
print("[2] Yardım")   
print("[3] Discord Webhook Deleter")
print("[4] Discord Webhook Spammer")
print("[5] Sunucuya Token Basma")
print("[6] Discord Bot Aktif Etme")
print("[7] Discord Token Checker")
print("[8] Çıkış")
surum = int(input("\nHangi Özelliği Kullanacağını Belirt: "))

if surum == 1:
 	os.system("cls")
 	print(yazi)

elif surum == 2:
	os.system("cls")
	print("[1] Clear")
	print("[2] Yardım")   
	print("[3] Discord Webhook Deleter")
	print("[4] Discord Webhook Spammer")
	print("[5] Sunucuya Token Basma")
	print("[6] Discord Bot Aktif Etme")
	print("[7] Discord Token Checker")
	print("[8] Çıkış")

elif surum == 3:
    os.system("cls")
    print(yazi)
    vblink = input("Webhook Url Girin:")
    requests.delete(vblink)
    print("Webhook Başarıyla silindi.")

elif surum == 4:
	os.system("cls")
	print(yazi)
	kacdefagonderildi = 0
	url = input("Webhook URL Girin: ")
	isim = input("Webhook Ismi Girin: ")
	avatarurl = input("Webhook Avatar URL Girin: ")
	mesaj = input("Mesajınızı Girin: ")
	while True:
		bilgiler = {
    		"username": isim,
    		"avatar_url": avatarurl,
    		"content": mesaj
		}
		requests.post(url, data=bilgiler)
		kacdefagonderildi = kacdefagonderildi + 1
		print(str(kacdefagonderildi) + " Mesaj Gönderildi")

elif surum == 5:
	os.system("cls")
	print(yazi)
	link = input('Discord Davet Linki: ')
	apilink	= "https://discordapp.com/api/v6/invite/" + str(link)
	print(link)
	with open('tokens.txt','r') as handle:
		tokens = handle.readlines()
		for x in tokens:
			token = x.rstrip()
			headers={
    			'Authorization': token
    		}
			requests.post(apilink, headers=headers)
			print("Tüm Çalışan Tokenler Sunucuya Giriş Yaptı.")

elif surum == 6:
    os.system("cls")
    print(yazi)
    bottoken = input('Bot Tokeninizi Girin: ')
    client = discord.Client()
    client.run(bottoken)
    print("Bot Başarıyla Aktif Edildi.")

elif surum == 7:
    os.system("cls")
    print(yazi)
    with open("tokens.txt") as f:
        for line in f:
            tokenn = line.strip("\n")
            headerss = {'Content-Type': 'application/json', 'authorization': tokenn}
            url = "https://discordapp.com/api/v6/users/@me/library"
            r = requests.get(url, headers=headerss)
            if r.status_code == 200:
                print("{} Token Çalışıyor.".format(line.strip("\n")))
            else:
                print("Token Çalışmıyor.")

elif surum == 8:
    quit()

else:
  pass	

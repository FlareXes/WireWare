import subprocess
import webbrowser
import sys
import re


def wfdet():
    data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    for i in profiles:
        results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')
        for i in results:
            print(i)


def wfpass():
    data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    for i in profiles:
        results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30}      ------>>     {:<}".format(i,results[0]))
        except IndexError:
            print("{:<30}      ------>>     {:<}".format(i, ""))


def netdet():
    data = subprocess.check_output(['netsh','wlan','show','all']).decode('utf-8').split('\n')
    for i in data:
        print(i)


def wlanreport():
    y = input("Year: ")
    m = input("Month: ")
    d = input("Day: ")
    url = "file:///C:/ProgramData/Microsoft/Windows/WlanReport/wlan-report-{}-{}-{}.html".format(y,m,d)
    webbrowser.open(url)


def wfdel():
    data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
    list = ['']
    for i in data:
        print(i)
        
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    
    prfname = input("Select Profile : ")
    if prfname in profiles:
        data = subprocess.check_output(['netsh','wlan','delete','profile',prfname]).decode('utf-8').split('\n')
        print("* {} Has Been Deleted From This System".format(prfname))
    else:
        print('Profile Not Found Try Again...')


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

   
prCyan('''
 __      __.__               __      __                       
/  \    /  \__|______   ____/  \    /  \_____ _______   ____  
\   \/\/   /  \_  __ \_/ __ \   \/\/   /\__  \\_  __ \_/ __ \ 
 \        /|  ||  | \/\  ___/\        /  / __ \|  | \/\  ___/ 
  \__/\  / |__||__|    \___  >\__/\  /  (____  /__|    \___  >
       \/                  \/      \/        \/            \/ 
                               
''')

while(1): 
    prRed('''
1. Complete Wireless Device And Networks Information Summary\n
2. Configured Wireless Device Information\n
3. Configured Wireless Device SSID And Password\n
4. Delete Configured Wireless Device From System\n
5. Generate Report Of Recent Wireless Session\n
6. Quit 
    ''')

    try:
        choise = int(input("==> "))
        print()
        if choise == 1:
            netdet()
        elif choise == 2:
            wfdet()
        elif choise == 3:
            wfpass()
        elif choise == 4:
            print("\n---------------------------------")
            wfdel()
        elif choise == 5:
            print("Genrating Report")
            wlanreport()
        elif choise == 6:
            print("Good Bye!!!\n")
            sys.exit()
        else:
            print('''
___________                                  _______             ________        ___.                       .__                      _____  .__  .__                           .___ 
\_   _____/_____________  ___________        \      \   ____     \______ \   ____\_ |__  __ __  ____   ____ |__| ____    ____       /  _  \ |  | |  |   ______  _  __ ____   __| _/ 
 |    __)_\_  __ \_  __ \/  _ \_  __ \       /   |   \ /  _ \     |    |  \_/ __ \| __ \|  |  \/ ___\ / ___\|  |/    \  / ___\     /  /_\  \|  | |  |  /  _ \ \/ \/ // __ \ / __ |  
 |        \|  | \/|  | \(  <_> )  | \/      /    |    (  <_> )    |    `   \  ___/| \_\ \  |  / /_/  > /_/  >  |   |  \/ /_/  >   /    |    \  |_|  |_(  <_> )     /\  ___// /_/ |  
/_______  /|__|   |__|   \____/|__|     /\  \____|__  /\____/    /_______  /\___  >___  /____/\___  /\___  /|__|___|  /\___  /    \____|__  /____/____/\____/ \/\_/  \___  >____ |  
        \/                              )/          \/                   \/     \/    \/     /_____//_____/         \//_____/             \/                             \/     \/  
''')
    except ValueError:
        print('''
___________                                  _______             ________        ___.                       .__                      _____  .__  .__                           .___ 
\_   _____/_____________  ___________        \      \   ____     \______ \   ____\_ |__  __ __  ____   ____ |__| ____    ____       /  _  \ |  | |  |   ______  _  __ ____   __| _/ 
 |    __)_\_  __ \_  __ \/  _ \_  __ \       /   |   \ /  _ \     |    |  \_/ __ \| __ \|  |  \/ ___\ / ___\|  |/    \  / ___\     /  /_\  \|  | |  |  /  _ \ \/ \/ // __ \ / __ |  
 |        \|  | \/|  | \(  <_> )  | \/      /    |    (  <_> )    |    `   \  ___/| \_\ \  |  / /_/  > /_/  >  |   |  \/ /_/  >   /    |    \  |_|  |_(  <_> )     /\  ___// /_/ |  
/_______  /|__|   |__|   \____/|__|     /\  \____|__  /\____/    /_______  /\___  >___  /____/\___  /\___  /|__|___|  /\___  /    \____|__  /____/____/\____/ \/\_/  \___  >____ |  
        \/                              )/          \/                   \/     \/    \/     /_____//_____/         \//_____/             \/                             \/     \/  
''')


import sys, pyperclip, pprint, re, os, shutil, datetime

#Improvements to add -
#Edit proxy function
#Multi-delete function
#General stream lining of copy function etc


def backup():
    datestr = datetime.date.today().strftime("%d-%m-%y")
    print(datestr)
    print('Backing up current files...')
    #ProxyFileList = open('C:\Users\???\???\Lists_Backup\ProxyListBackups' + datestr, 'w')

    with open('C:\Users\???\???\ProxyListIG') as f:
        proxies = f.read().splitlines()

    openfilewrite = open('C:\Users\???\???\Lists_Backup\ProxyListBackups - ' + datestr, 'w')
    openfilewrite.write(datestr + "\n")
    for item in proxies:
        if (len(str(item)) > 1):
            openfilewrite.write("%s\n" % item)

FileExists = os.path.isfile('C:\Users\???\???\ProxyList')
if (FileExists == False):
    print('Using Write Method: Overwriting current directory...')
    ProxyFileList = open('ProxyList.txt', 'w')
    ProxyFileList.close()
else:
    backup()

UserChoiceLoop = False #asks user to continue enter/delete
UserChoiceLoop2 = True #asks user to continue entering or not
results = []


def viewProxies():
    with open('C:\Users\???\???\ProxyList') as f:
        proxies = f.read().splitlines()

    if (len(proxies) == 0):
        print('There are no proxies')
        sys.exit()

    pprint.pprint(proxies)

#def editProxies():
    #backup file w/ date using shutil
    #print file contents
    #ask which line to edit
    #ask which value to edit (one by one)
    #delete line and re-write new line at the end

def copyProxy():
    ProxyArray = []
    LengthOfList =  0
    UserChoice = False
    stringplaceholder = ''
    ProxyArrayFilteredToBeCopiedToClibpoard = []
    ClipboardEndOutput = ''
    z = 0
    jkl = 0
    ItemsToCopy = ['', '', '', '']
    results = ['']
    k = 0
    abcd = 0
    valuestodelete= []
    #asks after printing list in view function if you wish to copy or not
    #if you say no it goes to continue/no
    #if you say yes then it asks what to copy (list of stuff to copy is asked
    # to be seperated by commas via user - i.e. user input)
    #these items are copied to the clipboard and the items copied are printed
    # to make sure the correct items are copied (i.e. user checks system output)


    with open('C:\Users\???\???\ProxyList') as f:
        ProxyArray = f.read().splitlines()


    LengthOfList = len(ProxyArray)

    UserInput = raw_input('Copy items? (To clipboard) (Y/N)\n')
    if ((UserInput.lower()) == 'y'):
        PotentialInput = ['ip', 'port', 'proxy_user', 'proxy_pass']
        UserInput = raw_input('Items to be copied? (IP/PORT/PROXY_USER/PROXY_PASS)\nEnter items to be copied in the aforementioned format\n Items will be seperated with colons\n')

        for x in range(0, 4):
            if (PotentialInput[x] in UserInput.lower()):
                ItemsToCopy[x] = (PotentialInput[x])

        pprint.pprint(ProxyArray)

        while (UserChoice == False):
            UserInput = raw_input('Line to be copied?\nEnter a numerical number from %s to %d \n' % ('1', (LengthOfList)))
            try:
                (int(UserInput))
                try:
                    randomint = ((int(UserInput)) - 1)
                    ProxyArray[randomint]
                    UserChoice = True
                except IndexError:
                    print('Enter a number that is in range of the list length given')
            except ValueError:
                print('Enter a whole number, that corresponds to the list length')

            ProxyArrayFilter = ProxyArray[randomint]

            for x in ProxyArrayFilter:
                xyz = x
                for y in range(0, (len(x))):

                    if ((str(xyz[y:(y+1)])) == ':'):
                        results.append('')
                        z += 1
                        continue

                    results[z] += (str(xyz[y:(y+1)]))

            for x in results:
                k += 1
                if (x == ''):
                    valuestodelete.append(k)

            for x in range(0, len(valuestodelete)):
                del results[((valuestodelete[abcd] - abcd) - 1)]
                abcd += 1

                #ip:port:uservps:pwvps:userproxy:pwproxy
                #1:2:3:4:5:6 (array values, well subtract one from each)
                # dual iteration loop, each time a value comes up positive
                # add it to a list with a tag i.e. VPS PW - (VPS PW)
                #pyperclip After

            for x in PotentialInput:
                for y in ItemsToCopy:
                    if x == y:
                        if jkl == 0:
                            #IP
                            ClipboardEndOutput += (results[0] + ' ')
                        elif jkl == 1:
                            #PORT
                            ClipboardEndOutput += (results[1] + ' ')
                        elif jkl == 2:
                            #VPSUSER
                            ClipboardEndOutput += (results[2] + ' ')
                        elif jkl == 3:
                            #vpspw
                            ClipboardEndOutput += (results[3] + ' ')
                        elif jkl == 4:
                            #proxyuser
                            ClipboardEndOutput += (results[4] + ' ')
                        elif jkl == 5:
                            #proxypw
                            ClipboardEndOutput += (results[5] + ' ')
                jkl += 1 # identifying the ip/port etc

            print (ClipboardEndOutput)
            print('Copying desired output to clipboard...')
            pyperclip.copy(ClipboardEndOutput)


def EnteringProxies():
    ProxyTrue = None
    IP_Address_Proxy =  ''

    backup()

    # ask for userinput, check if input is a certain Number of digits + only digits + dots
    # ask for vps password and username and port w/ ip + key i.e. (pw: port: vps user etc)
    # Append data to file

    #while (ProxyTrue == None): 
    #    IP_Address_Proxy_Regex = re.compile(r'''(
    #    \d{3}| # Looks for 3 digits, 1 dot etc etc
    #    \D{1}|
    #    \d{2}
    #    \D{1}|
    #    \d{3}|
    #    \D{1}|  Regex isn't working - debug it later
    #    \d{2})''')


        #IP_Address_Proxy = raw_input('Enter the ip address of the proxy')

        #ProxyTrue = IP_Address_Proxy_Regex.search(IP_Address_Proxy)
        #if (ProxyTrue == None):
            #print('Enter a correct IP address.')
            #print('DEBUG: ' + ProxyTrue.group())


    IP_Address_Proxy = raw_input('Enter the ip address of the proxy\n')

    Portproxy = raw_input('Enter the port of the proxy\n')

    VPSUsername = raw_input('Enter the username of the vps\n')

    VPSPassword = raw_input('Enter the password of the VPS\n')

    ProxyUserName = raw_input('Enter the username of the proxy\n')

    ProxyPassword = raw_input('Enter the password of the proxy\n')

    CombinationEntering = IP_Address_Proxy + ':' + Portproxy + ':' + VPSUsername + ':' + VPSPassword + ':' + ProxyUserName + ':' + ProxyPassword
    print('Writing Proxy...')
    openfilewrite2 = open('C:\Users\???\???\ProxyList', 'a')
    openfilewrite2.write("%s\n" % CombinationEntering)
    openfilewrite2.close()
    print('Saved proxy!')


def DeletingProxies():
    UserChoice = False
    writeopening = False
    openfilewrite = ''

    backup()

    with open('C:\Users\???\???\ProxyList') as f:
        proxies = f.read().splitlines()


    if (len(proxies) == 0):
        print('There are no proxies to be deleted')
        sys.exit()

    pprint.pprint(proxies)


    while (UserChoice == False):
        ProxiesToBeDeleted = raw_input('Which proxy would you like to delete? \nEnter a numerical number from %s to %s \n' % ('1', str(len(proxies))))
        try:
            (int(ProxiesToBeDeleted))
            try:
                randomint = ((int(ProxiesToBeDeleted)) - 1)
                proxies[randomint]
                UserChoice = True
            except IndexError:
                print('Enter a number that is in range of the list length given')
        except ValueError:
            print('Enter a whole number, that corresponds to the list length')

    del proxies[randomint]

    with open('C:\Users\???\???\ProxyList') as f:
        if 'Format - IP:PORT:VPSUSER:VPSPASS:PROXYUSER:PROXYPASS' not in f.read():
            writeopening = True

    openfilewrite = open('C:\Users\???\???\ProxyList', 'w')

    if (writeopening == True):
        openfilewrite.write('Format - IP:PORT:VPSUSER:VPSPASS:PROXYUSER:PROXYPASS\n')

    for item in proxies:
        if (len(str(item)) > 1):
            openfilewrite.write("%s\n" % item)

    openfilewrite.close()
    print('Proxy Deleted')

while (UserChoiceLoop == False):
    while (UserChoiceLoop2 == False):
        UserInput = raw_input('Continue or exit program? (Y/N)\n')
        UserInput = UserInput.lower()
        if (UserInput == 'y'):
            UserChoiceLoop2 = True
        elif (UserInput == 'n'):
            sys.exit()
        else:
            print('User\'s input is to be given as (Y/N)')

    UserInput = raw_input('Entering, Deleting, Viewing or Copying proxies? \n(entering/deleting/viewing/copying)\n')
    UserInput = UserInput.lower()

    if (UserInput == 'entering'):
        EnteringProxies()
        UserChoiceLoop2 = False
    elif (UserInput == 'deleting'):
        DeletingProxies()
        UserChoiceLoop2 = False
    elif (UserInput == 'viewing'):
        viewProxies()
        UserChoiceLoop2 = False
    elif (UserInput == 'copying'):
        copyProxy()
        UserChoiceLoop2 = False
    else:
        print('User\'s input is to be given as entering, deleting or viewing!')

sys.exit()

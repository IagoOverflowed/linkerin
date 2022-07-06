import math
from time import sleep
from requests import request as req
from validators import url
from sys import argv
rundata = {"limit":math.inf,"limit-per-pass":math.inf,"delay":0.0,"deep-dive":1,"starting-at":""}
i = 0
argv = argv[1:]
while i < len(argv):

    if argv[i] == "--help":

        print("To get help go to https://github.com/IagoOverflowed/linkerin")
        exit(0)

    if argv[i].startswith("--"):

        if i+1 >= len(argv):

            print("Malformed command line. No value provided for '"+argv[i][2:]+"'")
            exit(1)

        if list(rundata.keys()).count(argv[i][2:]) == 0:

            print("Unrecognized option:"+argv[i])
            continue
        
        try:
            rundata[argv[i][2:]] = type(rundata[argv[i][2:]])(argv[i+1])
            i += 2 
            continue
        except:
            print("Invalid value for "+argv[i])
            exit(1)
        
    print("Unrecognized option:"+argv[i])
    i += 1

links = [input("Starting position?") if rundata["starting-at"] == '' else rundata["starting-at"]]
passes = 0

while (len(links) > 0 or passes > rundata["limit"]):

    indexing = links.pop(0)
    try:
        pag = req("GET",indexing,headers={"User-Agent":"Python 3.9.x / linkerin","Mono":"In peaceful bots we trust (https://github.com/IagoOverflowed/linkerin)"})
    except:
        print("Cloudn't get on "+indexing)
        break
    txt = str(pag.content)[2:-1]
    i = 0
    adresses = []
    
    while (txt.count("http://",i) > 0 or txt.count("https://",i) > 0) and len(adresses) < rundata["limit-per-pass"]:

        if txt.count("http://",i) > 0:

            start = txt.index("http://",i)
            if txt.count('"') == 0:

                print("no double quotation mark string on "+indexing+" anymore moving on...")
                break

            end = txt.index('"',start)

            try:
                if url(txt[start:end]) != True:
                    adresses.append(txt[start:end])
            except:
                print("link too long. continuing")
                break
            i = end+1
            continue
        
        start = txt.index("https://",i)
        if txt.count('"') == 0:

            print("no double quotation mark string on "+indexing+" anymore moving on...")
            break
        end = txt.index('"',start)
        
        try:
            if url(txt[start:end]) != True:
                adresses.append(txt[start:end])
        except:
            print("link too long. continuing")
            break
        i = end+1
    
    c = open("links.log","r").read()

    for adress in adresses:

        if c.count(adress) == 0:

            c += adress + "\n"
            open("links.log","a").write(adress+"\n")
            if rundata["deep-dive"]:
                links.append(adress)
    
    print("pass #{} indexed {} found {} links".format(passes,indexing,len(adresses)))
    passes += 1
    sleep(rundata["delay"])

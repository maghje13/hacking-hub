import os


program_list = ["msf-payload-generator", "nmap-helper", "arp-discover", "RED_HAWK", "sqlmap", "setoolkit", "socialphish"
                "subfinder", "wireshark", "brutal", "venom", "slowloris", "xsscon"]


def clear():
    os.system("clear")


def install(program):
    if program == "msf-payload-generator":
        os.system("cd programs/msf-payload-generator && bash install.sh")
    elif program == "nmap-helper":
        os.system("cd programs/nmap-helper && bash install.sh")
    elif program == "RED_HAWK":
        os.system("sudo apt install php")
        os.system("cd programs && git clone git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
    elif program == "sqlmap":
        os.system("sudo apt install sqlmap")
    elif program == "setoolkit":
        setoolkit_option = str(input("Install via apt or github (a/g/e, e=exit): "))
        if setoolkit_option == "a" or setoolkit_option == "A":
            os.system("sudo apt install set")
        elif setoolkit_option == "g" or setoolkit_option == "G":
            os.system("cd programs && git clone https://github.com/trustedsec/social-engineer-toolkit/")
            os.system("cd programs && mv social-engineer-toolkit setoolkit")
            os.system("cd programs/setoolkit && sudo python3 setup.py")
    elif program == "socialphish":
        os.system("cd programs && git clone https://github.com/rizzy01/SocialPhish.git")
    elif program == "subfinder":
        os.system("sudo apt install subfinder")
    elif program == "wireshark":
        os.system("sudo apt install wireshark")
    elif program == "brutal":
        os.system("cd programs && sudo git clone https://github.com/Screetsec/Brutal.git")
        os.system("cd programs/Brutal && sudo chmod +x Brutal.sh")
    elif program == "venom":
        os.system("cd programs && git clone https://github.com/r00t-3xp10it/venom.git")
        os.system("cd programs/venom/aux && sudo ./setup.sh && cd .. && bash venom.sh -u")
    elif program == "slowloris":
        os.system("sudo pip install slowloris")
    elif program == "xsscon":
        os.system("pip install bs4 requests")
        os.system("cd programs && git clone https://github.com/menkrep1337/XSSCon && chmod 755 -R XSSCon")


def run(program):
    if program == "msf-payload-generator":
        os.system("cd programs/msf-payload-generator && python3 main.py")
    elif program == "nmap-helper":
        os.system("cd programs/nmap-helper && python3 main.py")
    elif program == "arp-discover":
        os.system("arp -a")
    elif program == "RED_HAWK":
        os.system("cd programs/red_hawk && php rhawk.php")
    elif program == "sqlmap":
        sqlmap_option = str(input("Site to scan (with http/https): "))
        os.system(f"sudo sqlmap -u {sqlmap_option}")
    elif program == "setoolkit":
        os.system("cd programs/setoolkit && sudo setoolkit")
    elif program == "socialphish":
        os.system("cd programs/socialphish && sudo bash socialphish.sh")
    elif program == "subfinder":
        sublist3r_option = str(input("Site to scan (e.g. example.com):"))
        os.system(f"sudo subfinder -d {sublist3r_option}")
    elif program == "brutal":
        os.system("cd programs/Brutal && sudo bash Brutal.sh")
    elif program == "venom":
        os.system("cd programs/venom && sudo bash venom.sh")
    elif program == "slowloris":
        slowloris_option = str(input("Site to DDoS (e.g. example.com): "))
        slowloris_option2 = str(input("Is the site using https? (y/n): "))
        if slowloris_option2 == "Y" or slowloris_option2 == "Y":
            os.system(f"slowloris {slowloris_option} --https")
        else:
            os.system(f"slowloris {slowloris_option}")
    elif program == "xsscon":
        xsscon_option = str(input("Domain: "))
        os.system(f"cd programs/XSSCon && python3 xsscon.py -u {xsscon_option}")


# main program
clear()

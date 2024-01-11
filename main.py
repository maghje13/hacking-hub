import os
import sys


program_list = ["msf-payload-generator", "nmap-helper", "arp-discover", "RED_HAWK", "sqlmap", "setoolkit", "socialphish"
                "subfinder", "wireshark", "brutal", "venom", "slowloris", "xsscon"]


def pause():
    input("\npress enter to continue...")


def clear():
    os.system("clear")


def show_description(program):
    if program == "msf-payload-generator":
        print("msf payload generator is a program created by me (maghje13)!\n"
              "it uses metasploit-frameworks msfvenom command to create a backdoor payload\n"
              "and can create a listener!\n"
              "source: https://github.com/maghje13/payload-generator")
    elif program == "nmap-helper":
        print("nmap-helper is a program created by me (maghje13)!\n"
              "it contains multiple presets for nmap scans\n"
              "so you dont have to remember every single option :)")
    elif program == "arp-discover":
        print("arp discover is literally not even a program, just a command!\n"
              "it does \"arp -a\" which shows all devices (and their mac addresses) it could find on your networks")
    elif program == "RED_HAWK":
        print("Redhawk is an advanced website recon and vulnerability scanner\n")


def show_options(program):
    while True:
        clear()
        show_description(program)
        menu_choice_2 = str(input("""
Options:
[1] Install
[2] Run
[3] Back

> """))
        if menu_choice_2 == "1":
            install(program)
        elif menu_choice_2 == "2":
            run(program)
        elif menu_choice_2 == "3":
            break
        else:
            pass


def install(program):
    if program == "msf-payload-generator":
        os.system("cd programs/msf-payload-generator && bash install.sh")
    elif program == "nmap-helper":
        os.system("cd programs/nmap-helper && bash install.sh")
    elif program == "arp-discover":
        print("nothing to install for this...")
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
    pause()


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
    pause()


# main program
while True:
    clear()
    menu_choice_1 = str(input("""Choose one of these options:
[1] msf payload generator
[2] nmap helper
[3] arp discover tool
[4] red hawk
[5] sqlmap
[6] setoolkit
[7] socialphish
[8] subfinder
[9] wireshark
[10] Brutal
[11] venom
[12] slowloris
[13] xsscon
[14] Exit

> """))
    if menu_choice_1 == "1":
        show_options("msf-payload-generator")
    elif menu_choice_1 == "2":
        show_options("nmap-helper")
    elif menu_choice_1 == "3":
        show_options("arp-discover")
    elif menu_choice_1 == "4":
        show_options("RED_HAWK")
    elif menu_choice_1 == "5":
        show_options("sqlmap")
    elif menu_choice_1 == "6":
        show_options("setoolkit")
    elif menu_choice_1 == "7":
        show_options("socialphish")
    elif menu_choice_1 == "8":
        show_options("subfinder")
    elif menu_choice_1 == "9":
        show_options("wireshark")
    elif menu_choice_1 == "10":
        show_options("brutal")
    elif menu_choice_1 == "11":
        show_options("venom")
    elif menu_choice_1 == "12":
        show_options("slowloris")
    elif menu_choice_1 == "13":
        show_options("xsscon")
    elif menu_choice_1 == "14":
        print("Exiting...")
        sys.exit()
    else:
        pass

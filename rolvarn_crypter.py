from colorama import Fore

print(Fore.RED + """
 ██▀███   ▒█████   ██▓  ██▒   █▓ ▄▄▄       ██▀███   ███▄    █ 
▓██ ▒ ██▒▒██▒  ██▒▓██▒ ▓██░   █▒▒████▄    ▓██ ▒ ██▒ ██ ▀█   █ 
▓██ ░▄█ ▒▒██░  ██▒▒██░  ▓██  █▒░▒██  ▀█▄  ▓██ ░▄█ ▒▓██  ▀█ ██▒
▒██▀▀█▄  ▒██   ██░▒██░   ▒██ █░░░██▄▄▄▄██ ▒██▀▀█▄  ▓██▒  ▐▌██▒
░██▓ ▒██▒░ ████▓▒░░██████▒▒▀█░   ▓█   ▓██▒░██▓ ▒██▒▒██░   ▓██░
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▐░   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ 
  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░ ▒  ░░ ░░    ▒   ▒▒ ░  ░▒ ░ ▒░░ ░░   ░ ▒░
  ░░   ░ ░ ░ ░ ▒    ░ ░     ░░    ░   ▒     ░░   ░    ░   ░ ░ 
   ░         ░ ░      ░  ░   ░        ░  ░   ░              ░ 
                            ░                                 
 ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓▓█████  ██▀███    
▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒  
▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒  
▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄    
▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒  
░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  
  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░     ░ ░  ░  ░▒ ░ ▒░  
░          ░░   ░ ▒ ▒ ░░  ░░         ░         ░     ░░   ░   
░ ░         ░     ░ ░                          ░  ░   ░       
░                 ░ ░                                         

                                                    by ~ ROLVARN

""")
datafile = input(Fore.GREEN + "[#] " + Fore.WHITE+ "Enter your file with path : ")

print(Fore.GREEN + "\n[#] " + Fore.WHITE+"Select Option:\n\n"+ Fore.GREEN+"[1] "+ Fore.WHITE+ "Crypt\n"+Fore.GREEN+"[2] " +Fore.WHITE + "Decrypt\n")
option = input("> ")

def crypt(data1):

    with open(data1, "r", encoding="utf-8") as file_read:
        file_content = file_read.read()
    
    letters = list(file_content)

    for i, x in enumerate(letters):
        if x in "a": letters[i] = "⊕"
        if x in "A": letters[i] = "⊗"
        if x in "b": letters[i] = "☯"
        if x in "B": letters[i] = "☸"
        if x in "c": letters[i] = "✪"
        if x in "C": letters[i] = "✰"
        if x in "ç": letters[i] = "❀"
        if x in "Ç": letters[i] = "✿"
        if x in "d": letters[i] = "♠"
        if x in "D": letters[i] = "♣"
        if x in "e": letters[i] = "♥"
        if x in "E": letters[i] = "♦"
        if x in "f": letters[i] = "♤"
        if x in "F": letters[i] = "♧"
        if x in "g": letters[i] = "⚡"
        if x in "G": letters[i] = "☀"
        if x in "ğ": letters[i] = "☁"
        if x in "Ğ": letters[i] = "☂"
        if x in "h": letters[i] = "☃"
        if x in "H": letters[i] = "☄"
        if x in "ı": letters[i] = "★"
        if x in "I": letters[i] = "☆"
        if x in "i": letters[i] = "☽"
        if x in "İ": letters[i] = "☾"
        if x in "j": letters[i] = "☼"
        if x in "J": letters[i] = "☻"
        if x in "k": letters[i] = "✈"
        if x in "K": letters[i] = "✉"
        if x in "l": letters[i] = "✆"
        if x in "L": letters[i] = "✇"
        if x in "m": letters[i] = "✌"
        if x in "M": letters[i] = "✍"
        if x in "n": letters[i] = "✎"
        if x in "N": letters[i] = "✏"
        if x in "o": letters[i] = "✑"
        if x in "O": letters[i] = "✒"
        if x in "ö": letters[i] = "✓"
        if x in "Ö": letters[i] = "✔"
        if x in "p": letters[i] = "✕"
        if x in "P": letters[i] = "✖"
        if x in "q": letters[i] = "✗"
        if x in "Q": letters[i] = "✘"
        if x in "r": letters[i] = "☢"
        if x in "R": letters[i] = "☣"
        if x in "s": letters[i] = "☠"
        if x in "S": letters[i] = "☤"
        if x in "ş": letters[i] = "⚑"
        if x in "Ş": letters[i] = "⚐"
        if x in "t": letters[i] = "☘"
        if x in "T": letters[i] = "☙"
        if x in "u": letters[i] = "♛"
        if x in "U": letters[i] = "♕"
        if x in "ü": letters[i] = "♚"
        if x in "Ü": letters[i] = "♔"
        if x in "v": letters[i] = "♞"
        if x in "V": letters[i] = "♘"
        if x in "w": letters[i] = "♟"
        if x in "W": letters[i] = "♙"
        if x in "x": letters[i] = "♖"
        if x in "X": letters[i] = "♜"
        if x in "y": letters[i] = "❂"
        if x in "Y": letters[i] = "❃"
        if x in "z": letters[i] = "❄"
        if x in "Z": letters[i] = "❅"
        if x in "0": letters[i] = "❆"
        if x in "1": letters[i] = "❇"
        if x in "2": letters[i] = "❈"
        if x in "3": letters[i] = "❉"
        if x in "4": letters[i] = "❊"
        if x in "5": letters[i] = "❋"
        if x in "6": letters[i] = "◉"
        if x in "7": letters[i] = "◌"
        if x in "8": letters[i] = "◇"
        if x in "9": letters[i] = "◆"
        if x in "(": letters[i] = "○"
        if x in ")": letters[i] = "●"
        if x in ":": letters[i] = "□"
        if x in ",": letters[i] = "■"


        #don't touch this
        if x == "\n": letters[i] = ";"

        

    crypted_text = ''.join(letters)

    return crypted_text
def decrypt(data2):
    
    with open(data2, "r", encoding="utf-8") as file_read:
        file_content = file_read.read()
    
    letters = list(file_content)

    for i, x in enumerate(letters):
        if x in "⊕": letters[i] = "a"
        if x in "⊗": letters[i] = "A"
        if x in "☯": letters[i] = "b"
        if x in "☸": letters[i] = "B"
        if x in "✪": letters[i] = "c"
        if x in "✰": letters[i] = "C"
        if x in "❀": letters[i] = "ç"
        if x in "✿": letters[i] = "Ç"
        if x in "♠": letters[i] = "d"
        if x in "♣": letters[i] = "D"
        if x in "♥": letters[i] = "e"
        if x in "♦": letters[i] = "E"
        if x in "♤": letters[i] = "f"
        if x in "♧": letters[i] = "F"
        if x in "⚡": letters[i] = "g"
        if x in "☀": letters[i] = "G"
        if x in "☁": letters[i] = "ğ"
        if x in "☂": letters[i] = "Ğ"
        if x in "☃": letters[i] = "h"
        if x in "☄": letters[i] = "H"
        if x in "★": letters[i] = "ı"
        if x in "☆": letters[i] = "I"
        if x in "☽": letters[i] = "i"
        if x in "☾": letters[i] = "İ"
        if x in "☼": letters[i] = "j"
        if x in "☻": letters[i] = "J"
        if x in "✈": letters[i] = "k"
        if x in "✉": letters[i] = "K"
        if x in "✆": letters[i] = "l"
        if x in "✇": letters[i] = "L"
        if x in "✌": letters[i] = "m"
        if x in "✍": letters[i] = "M"
        if x in "✎": letters[i] = "n"
        if x in "✏": letters[i] = "N"
        if x in "✑": letters[i] = "o"
        if x in "✒": letters[i] = "O"
        if x in "✓": letters[i] = "ö"
        if x in "✔": letters[i] = "Ö"
        if x in "✕": letters[i] = "p"
        if x in "✖": letters[i] = "P"
        if x in "✗": letters[i] = "q"
        if x in "✘": letters[i] = "Q"
        if x in "☢": letters[i] = "r"
        if x in "☣": letters[i] = "R"
        if x in "☠": letters[i] = "s"
        if x in "☤": letters[i] = "S"
        if x in "⚑": letters[i] = "ş"
        if x in "⚐": letters[i] = "Ş"
        if x in "☘": letters[i] = "t"
        if x in "☙": letters[i] = "T"
        if x in "♛": letters[i] = "u"
        if x in "♕": letters[i] = "U"
        if x in "♚": letters[i] = "ü"
        if x in "♔": letters[i] = "Ü"
        if x in "♞": letters[i] = "v"
        if x in "♘": letters[i] = "V"
        if x in "♟": letters[i] = "w"
        if x in "♙": letters[i] = "W"
        if x in "♖": letters[i] = "x"
        if x in "♜": letters[i] = "X"
        if x in "❂": letters[i] = "y"
        if x in "❃": letters[i] = "Y"
        if x in "❄": letters[i] = "z"
        if x in "❅": letters[i] = "Z"
        if x in "❆": letters[i] = "0"
        if x in "❇": letters[i] = "1"
        if x in "❈": letters[i] = "2"
        if x in "❉": letters[i] = "3"
        if x in "❊": letters[i] = "4"
        if x in "❋": letters[i] = "5"
        if x in "◉": letters[i] = "6"
        if x in "◌": letters[i] = "7"
        if x in "◇": letters[i] = "8"
        if x in "◆": letters[i] = "9"
        if x in "○": letters[i] = "("
        if x in "●": letters[i] = ")"
        if x in "□": letters[i] = ":"
        if x in "■": letters[i] = ","


        #don't touch this
        if x == ";": letters[i] = "\n"

    decrypted_text = ''.join(letters)

    return decrypted_text

if option == "1":
    try:
        wdata = crypt(datafile)
        with open("crypted_data.txt","w",encoding="utf-8") as sdata:
            sdata.write(wdata)
        print(Fore.GREEN + "\n[#] " + Fore.WHITE + "Crypted data successfully generated and saved to crpyted_data.txt!\n\n" + Fore.YELLOW+ wdata)
    except Exception as e:
        print(Fore.RED + "[#]" + Fore.WHITE + f"Something went wrong: {e}")


elif option == "2":
    try:
        wdata = decrypt(datafile)
        with open("decrypted_data.txt", "w", encoding="utf-8") as sdata:
            sdata.writelines(wdata)
        print(Fore.GREEN + "\n[#] " + Fore.WHITE + "Decrypted data saved to decrypted_data.txt!\n\n" + Fore.YELLOW + wdata)
    except Exception as e:
        print(Fore.RED + "[#] " + Fore.WHITE + "Something went wrong: " + str(e))
else:
    print(Fore.RED + "[#] " + Fore.WHITE + "Invalid option selected.")
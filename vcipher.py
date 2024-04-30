#dictionary for the cypher
from colorama import Fore, Style
alpha = {
    "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7,
    "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15,
    "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
    "y": 24, "z": 25
}

def arguments():
        from argparse import ArgumentParser
        parser = ArgumentParser()
        parser.add_argument("-k", "--key", type = str, required=True, help="enter key")
        parser.add_argument("-t", "--text", type = str, choices=["plaintext", "ciphertext"], help = "choose if plain or cipher", required = True)
        parser.add_argument("-w", "--word", type = str, help = "enter text", required = True)
        parser.add_argument("-c", "--cipher", type = str, help = "enter cipher", required = False)
        parser.add_argument("-m", "--mode", type = str, choices=["enc", "dec"], required=True, help = "encrypt or decrypt")
        return parser.parse_args()

args = arguments()
key = str(args.key).lower()
word = str(args.word).lower()
if str(args.text).lower() == "plaintext":
    text = args.text
elif str(args.text).lower() == "ciphertext":
    text = args.text
else:
    pass
cypher_num = []

key_num = [alpha[char] for char in key]
word_num = [alpha[char] for char in word]

if args.mode == "enc":
    #encryption class
    class Encryption:
        for k, t in zip(key_num, word_num):
            sum_val = (k + t) % 26
            cypher_num.append(sum_val)

        #function to convert value to key
        def find_key(dictionary, value):
            cypher_alpha = []
            for key, val in dictionary.items():
                if val == value:
                    cypher_alpha.append(key)
            return cypher_alpha
    
        cypher_alpha = []
        for x in cypher_num:
            cypher_alpha.extend(find_key(alpha, x))
        print(f"{Fore.GREEN}Decryption successful{Style.RESET_ALL}")
        print(f"{Fore.CYAN}key:       {Fore.LIGHTYELLOW_EX}{key} {Style.RESET_ALL}")
        print(f"{Fore.CYAN}Text:      {Fore.LIGHTYELLOW_EX}{word} ")
        enc = ""
        for x in cypher_alpha:
            enc += x
        print(f"{Fore.CYAN}Encrypted: {Fore.LIGHTYELLOW_EX}{enc} {Style.RESET_ALL}")
    
    Encryption()

elif args.mode == "dec":
    #decryption class
    class Decryption:
        for k, t in zip(word_num, key_num):
            sum_val = (k - t) % 26
            cypher_num.append(sum_val)

        #function to convert value to key
        def find_key(dictionary, value):
            cypher_alpha = []
            for key, val in dictionary.items():
                if val == value:
                    cypher_alpha.append(key)
            return cypher_alpha

        cypher_alpha = []
        for x in cypher_num:
            cypher_alpha.extend(find_key(alpha, x))
        print(f"{Fore.GREEN}Decryption successful{Style.RESET_ALL}")
        print(f"{Fore.CYAN}key:       {Fore.LIGHTYELLOW_EX}{key} {Style.RESET_ALL}")
        print(f"{Fore.CYAN}Text:      {Fore.LIGHTYELLOW_EX}{word} ")
        enc = ""
        for x in cypher_alpha:
            enc += x
        print(f"{Fore.CYAN}Decrypted: {Fore.LIGHTYELLOW_EX}{enc} {Style.RESET_ALL}")

    Decryption()

else:
    pass
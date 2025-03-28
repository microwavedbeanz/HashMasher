import hashlib
import time
import sys

title = """
  _    _           _     __  __           _               
 | |  | |         | |   |  \/  |         | |              
 | |__| | __ _ ___| |__ | \  / | __ _ ___| |__   ___ _ __ 
 |  __  |/ _` / __| '_ \| |\/| |/ _` / __| '_ \ / _ \ '__|
 | |  | | (_| \__ \ | | | |  | | (_| \__ \ | | |  __/ |   
 |_|  |_|\__,_|___/_| |_|_|  |_|\__,_|___/_| |_|\___|_|   
                                                          
                                                          
"""

def dehash(mode):
        hash_algorithm = getattr(hashlib, mode)
        hash_to_plain = input("Enter HEX Hash to be cracked:")
        hash_to_plain = hash_to_plain.strip()
        wordlist = input("Drag Wordlist here --->")
        with open(wordlist, "r", encoding="utf-8-sig") as f:
            line_count = sum(1 for line in f)
            print(f"{line_count} words loaded...")
            f.close()
        attempts = 0
        found = False
        with open(wordlist, "r", encoding="utf-8-sig") as f:
            for line in f:
                attempts += 1
                test_word = line.strip()
                hash_function = hash_algorithm()
                hash_function.update(test_word.encode("utf-8"))
                string_hash = hash_function.hexdigest().strip()
                sys.stdout.write(f"\rWords tried: {attempts}/{line_count}")
                sys.stdout.flush()
                """print(string_hash)
                print(hash_to_plain)
                break"""
                if string_hash == hash_to_plain:
                    print("\n ----------- WORD FOUND ----------- ")
                    print(f"{hash_to_plain}:{test_word}")
                    found = True
                    time.sleep(5)
                    menu()
        if not found:
            if attempts > line_count:
                    print("----------Hash Not Found----------")
                    time.sleep(5)
                    menu()
                    
                

def menu():
    print(title)
    print("Currently Supported Hash Modules Consist Of:")
    supported_hashes = sorted(hashlib.algorithms_guaranteed)
    temp = "]---[".join(map(str, supported_hashes))
    print("["+temp+"]")
    print(f"Selection Order is as show above eg: {list(supported_hashes)[6]} is 7th so enter 7")
    hash_algo = int(input(">>>"))
    hash_algo = list(supported_hashes)[hash_algo-1]
    print(hash_algo, "Selected...")
    
    dehash(hash_algo)
    
menu()
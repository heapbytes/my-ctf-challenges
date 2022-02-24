import random
import string
import zipfile
import time

with zipfile.ZipFile('flag.zip') as zip_file:
    with open('wordlist', 'w') as file:
        for i in range(int(time.time()), 1645608370, -1):


            random.seed(i)
            length, letters = 32, string.ascii_letters
            result_str = ''.join(random.choice(letters) for i in range(length))

            try:
                zip_file.extractall(pwd=result_str.encode())
            except:

                continue
            else:
                print("[+] Password found:", result_str)
                exit(0)

            file.write(f'{result_str}\n')
    print("[!] Password not found, try other wordlist.")

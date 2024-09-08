
## Here goes the challenge description

<center>
<img src="https://raw.githubusercontent.com/AidenPearce369/AidenPearce369.github.io/main/_posts/CTF/1337UP-Live-Pics/1.png" style="width:50%">
</center>

Seems like the challenge title is an username

After some OSINT recon, we could fine the username in github

[GitHub link](https://github.com/0pt1muspr1me) 

There are two repositories in it,

<center>
<img src="https://raw.githubusercontent.com/AidenPearce369/AidenPearce369.github.io/main/_posts/CTF/1337UP-Live-Pics/2.png" style="width:90%">
</center>

- Viewing the commits of first repo,

<center>
<img src="https://raw.githubusercontent.com/AidenPearce369/AidenPearce369.github.io/main/_posts/CTF/1337UP-Live-Pics/3.png" style="width:90%">
</center>

So there is some interesting string ```DJVL4REEXP76YXCTXOKK5NQGQM``` and some hints

```bypthon stuff``` and ```pastes buffer```

After some googling, you can find this [site](https://bpa.st/) is relevant to the hint

<center>
<img src="https://raw.githubusercontent.com/AidenPearce369/AidenPearce369.github.io/main/_posts/CTF/1337UP-Live-Pics/4.png" style="width:90%">
</center>

Seems like, it allows us to share code with long URI

Pasting our string value in the URI to get the data from it,

<center>
<img src="https://raw.githubusercontent.com/AidenPearce369/AidenPearce369.github.io/main/_posts/CTF/1337UP-Live-Pics/5.png" style="width:90%">
</center>

We are able to get a python script from this [link](https://bpa.st/DJVL4REEXP76YXCTXOKK5NQGQM)

```flag.zip``` seems interesting

Viewing the second repo of the username, we can see ```flag.zip```,

<center>
<img src="https://raw.githubusercontent.com/AidenPearce369/AidenPearce369.github.io/main/_posts/CTF/1337UP-Live-Pics/6.png" style="width:90%">
</center>

It is a ```password protected zip file``` which we have created from the python script

By understanding the python script, we could see that it generates a random string to compress the zip file

And the seed value is important to find the exact password

By analysing the metadata we could find the time of modification of this file, which is not always equal to time of creation

```c
└─$ file flag.zip                        
flag.zip: Zip archive data, at least v2.0 to extract, compression method=deflate
              
              
└─$ exiftool flag.zip 
ExifTool Version Number         : 12.40
File Name                       : flag.zip
Directory                       : .
File Size                       : 201 bytes
File Modification Date/Time     : 2022:03:11 10:19:14-05:00
File Access Date/Time           : 2022:03:12 12:38:50-05:00
File Inode Change Date/Time     : 2022:03:12 12:38:42-05:00
File Permissions                : -rwxrw-rw-
File Type                       : ZIP
File Type Extension             : zip
MIME Type                       : application/zip
Zip Required Version            : 20
Zip Bit Flag                    : 0x0003
Zip Compression                 : Deflated
Zip Modify Date                 : 2022:02:24 10:00:00
Zip CRC                         : 0xb53c49d5
Zip Compressed Size             : 69
Zip Uncompressed Size           : 59
Zip File Name                   : flaggers\flag.txt
```

By logic, this is the exact/approximate time when the python script should be ran to create this zip file

Calculating the timestamps values for these two interals,

```c
>>> from datetime import datetime
>>> int(datetime.timestamp(datetime(2022,2,24,10,0,0,0)))
1645714800
>>>> int(datetime.timestamp(datetime(2022,2,25,10,0,0,0)))
1645801200
>>> int(datetime.timestamp(datetime(2022,2,23,10,0,0,0)))
1645628400
```

So if we bruteforce the seed value with the range of timestamp, it should crack the zip successfully at one point

Creating a python script to bruteforce the logic,
Official <a href="https://github.com/heapbytes/1337UP-Official-Writeups/blob/main/OSINT/0pt1muspr1me/solve.py"> solve.py </a> 

```c

└─$ cat solve.py          
import time
import string
import random
from datetime import datetime
import zipfile
length, letters = 32, string.ascii_letters
for x in range(1645628400,1645801200):
        random.seed(x)
        result_str = ''.join(random.choice(letters) for i in range(length))
        try:
                file_name = 'flag.zip'
                pswd = result_str
                with zipfile.ZipFile(file_name) as file:
                        file.extractall(pwd = bytes(pswd, 'utf-8'))
                print("Successfully cracked!!")
                print(datetime.fromtimestamp(x))
                break
        except Exception as e:
                pass
```

- By running this script, we would get the flag

```bash

└─$ python3 solve.py
Successfully cracked!!
2022-02-24 04:53:00
   
   
└─$ cat flaggers\\flag.txt 
1337UP{W3ll_1_n3v3r_th0ught_U_c0uuuuuuld_f1nd_m3_308240202}
```


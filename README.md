|Name|
This program was originally temp named pytalk, 
after consideration re-named LibTalk, 
and published on GitLab first by Liam https://gitlab.com/liamlabuschagne/pytalk 
and later by Rubles here as SkHype.

|My Fascination|
Perpetuating the free-open Linux community, 
I saw a lack and need for a new communication program, 
as everything I saw that allowed: 
voice calling + live file/data sharing relied on a centralised, 
or semi-centralised server, 
and this allows for a single point of failure, and requires trust/dis-trust. 

|Vision|
I planned to found a program which: 
1st allows for a voice caller, 
but without relying on even a de-centralised middleman server whatsoever! 
2nd uses the Privyweb [Private-web (my name for self contained networks {like I2P & Tor})], 
to publish content and live data sharing, 
3rd verifiably respects privacy, freedom, full 'distributed' de-centralisation, 
full-encryption including on the meta-data and headers, 
pure distributed peer to peer, and torrenting.

|Accomplishments|
I had a lot of fun engineering SkHype with my friend Liam over the holidays, 
and he said "It's amazing how you made so many improvements on your own". 
The first prototype was Alpha6-FF, which took 3 days to develop, 
which allowed for a live voice call, 
using port forwarding directly between the routers' peers, 
without any middle-man in-between whatsoever! 
The latest version is Alpha8.5 which has a Graphical User Interface, 
address-book, and texting capabilities (copy & paste links), among others. 
Alpha1 which was developed in one day supports unlimited file-sharing size! 

|Read-Me-Instructions|
The most convenient way to execute the program is to launch the Alpha8.5 SkHype.exe. 
https://bit.do/skhype8-5 
Important: Make sure the Contacts.txt is in the same folder as SkHype before running, 
and that it has at least 2 empty lines. 
For Linux and Mac Alpha8.5 you need to in-sure Python2-Tkinter, 
and Python2-PyAudio, and Python2 are installed. 
Then, open the directory for SkHype in your console. 
For Windows the console is CMD. Just type python.exe libtalk.py 
For Linux the console is Terminal. Just type python2 libtalk.py

But first enable port forwarding on your machine on port 8000, 
through your Internet Service Provider Router Settings. 
To do so just search whats my IPv4, then, 
visit that in the address bar, then, 
click advanced, then, click WAN, then, 
do the port-forwarding as expressed prior. 

Alpha6-FF-[First-Finished] also has a Windows executable you might wana try for some reason https://bit.do/skhype6 

Alpha1 executes similar to V8.5 on Linux except other versions must be closed while running.

|Future-Improvements|
1. It still needs encryption. 
I'm considering using Obfs4, Format-Transforming-Encryption, 
and Dust2 - The Polymorphic Protocol Engine as my encrypted protocols. 
2. Compile executable cross-platform including Android. 
3. Group chat. 
4. It also needs to minamize into a tray icon when closed, 
so that it'll continue to work. 
5. The voice call needs to catch up in a smart way when it gets delayed. 
6. Unlimited file sharing size with simultaneous voice calling. 
7. Save account data on Zeronet. 
8. Make a more convenient way to connect peer-to-peer, 
either without port forwarding or with port forwarding built-in. 
All other future improvements was already discussed under 'Vision' 

|Similar Projects|
I don't recommend using SkHype yet because similar projects like: 
Jami, Tox, and RetroShare are better. 
However if you want a high quality audio call, fast texting, 
fun experimenting, or just want to borrow some source, use SkHype!
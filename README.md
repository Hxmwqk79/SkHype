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
The latest version is v8.7 which has a Graphical User Interface, 
address-book, and texting capabilities (copy & paste links), and Linux Executable with Encrypted connection.
Unlike TLS, SSH, and Diffie-Hellman which are vulnerable, 
SkHype is resistant to Man-in-The-Middle (albeit due to simplicity)
Alpha1 which was developed in one day supports unlimited file-sharing size! 

|Read-Me-Instructions|

On Linux the most convenient way to run the program is to launch the v8.7/dist/SkHype executable. 
Important: (For any new version), Make sure the Contacts.txt is in the same folder as SkHype before running, 
and that it has at least 2 empty lines. 
For running the .py file in Windows, Mac, or Linux: you need to insure Python Tkinter, 
and Python PyAudio, and Python are installed (after the right version of Python, 2 or 3). 
Then, open the directory for SkHype in your console. 
For Windows the console is CMD. Just type python.exe libtalk.py 
For Linux the console is Terminal. Just type python2 libtalk.py

But first enable port forwarding on your machine on port 8000, 
through your Internet Service Provider Router Settings. 
To do so just search whats my IPv4, then, 
visit that in the address bar, then, 
click advanced, then, click WAN, then, 
do the port-forwarding as expressed prior. 

Alpha1 executes similar to V8.5 except other versions must be closed while running.

|Future-Improvements|
1. I̶t̶ ̶s̶t̶i̶l̶l̶ ̶n̶e̶e̶d̶s̶ ̶e̶n̶c̶r̶y̶p̶t̶i̶o̶n̶.̶ ̶
̶I̶'̶m̶ ̶c̶o̶n̶s̶i̶d̶e̶r̶i̶n̶g̶ ̶u̶s̶i̶n̶g̶ ̶O̶b̶f̶s̶4̶,̶ ̶F̶o̶r̶m̶a̶t̶-̶T̶r̶a̶n̶s̶f̶o̶r̶m̶i̶n̶g̶-̶E̶n̶c̶r̶y̶p̶t̶i̶o̶n̶,̶ ̶
̶a̶n̶d̶ ̶D̶u̶s̶t̶2̶ ̶-̶ ̶T̶h̶e̶ ̶P̶o̶l̶y̶m̶o̶r̶p̶h̶i̶c̶ ̶P̶r̶o̶t̶o̶c̶o̶l̶ ̶E̶n̶g̶i̶n̶e̶ ̶a̶s̶ ̶m̶y̶ ̶e̶n̶c̶r̶y̶p̶t̶e̶d̶ ̶p̶r̶o̶t̶o̶c̶o̶l̶s̶.̶ Encryption added (see v8.7), 
but I need help getting something better like Obfs4/Dust/Replicant-Shapeshifter Transport, to work with own Python code. https://pypi.org/project/Dust/ or https://github.com/OperatorFoundation/shapeshifter-dispatcher/ or https://github.com/twisteroidambassador/ptadapter)
2. Compile executable cross-platform including Android. 
3. Group chat. 
4. It also needs to minamize into a tray icon when closed, 
so that it'll continue to work. 
5. The voice call needs to catch up in a smart way when it gets delayed. 
6. Unlimited file sharing size while simultaneous voice calling. 
7. Save account data on Zeronet. 
8. Make a more convenient way to connect peer-to-peer, 
either without port forwarding or with port forwarding built-in. (might want to copy how qBitTorrent does P2P)
All other future improvements was already discussed under 'Vision' 

|Similar Projects|

I don't recommend using SkHype yet because similar projects like: 
Jami, Tox, and RetroShare are better. 
However if you want a high quality audio call, fast texting, 
fun experimenting, afraid of man-in-the-middle attack, 
if you don't trust big projects, or just want to borrow some source, use SkHype!

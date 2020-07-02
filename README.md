# AUTO_WHATSAPP_MESSAGING
The one-stop shop to sending whatsapp messages automatically so u don't have to (esp during shro !!!!!)



### Why it was built.
It's the year 2020. Coronavirus has inVADED THE EARTH and here at singapore, things seem pretty good.
While the rest of the world's struggling and dying, we're here making election memes. Life's good. Or at least not as bad as it could be.
BUT WAIT. Life's not all that great. 



### Introducing: SHRO.
Stay Home Rxxx Oxxx (no idea wtf RO stands for but ok). If you're an NSF Admin/Office worker, you knoW wtf this is.
Basically, the gahmen decided to force everyone to work from home so coRONAVIRUS doesn't spread.
Due to this, NSFs now have to attend roll call via whatsapp. w h a t a c h o r e. 
If you're a lazy idiot with messed up body clock like me, you might've missed your roll call mULTIPLE times. xd
Unfortunately for me I'm under fking RSM (discipline master of the camp/stn). So WEEKEND CONFINEMENT FOR YOU!!!!! >:(



### How does this help?
This script basically sends the roll call messages via whatsapp on whatever time your roll call is (u may change this value manually).
It is by default set at 0800 and 1400 on weekdays.
NO MORE MISSING ROLL CALL. and extra sleep for me. >;)\\\



## REQUIREMENTS
- Python 3.8.x & above
- Google Chrome Version 83.0.4103.116 (don't worry, u don't HAVE to use this version, it's just the version im using)
- Chromedriver (executible file that allows python control of chrome)
- Selenium (python package, installation guide down below)



## Installation Guide
1. Check your chrome version.  
     
   1.1. Open google chrome and click the 3 dots on the top right of your browser  
   1.2. Hover your mouse on the help tab  
   1.3. Click on "About Google Chrome"  
   1.4. A new tab will pop up with your chrome version shown    
     
2. Install python 3.8.x  
  
   2.1. Head to https://www.python.org/downloads/  
   2.2. Download the latest version of python 3  
  
3. Install Chromedriver  

   3.1. Head to https://chromedriver.chromium.org/downloads and download the chromedriver for your version of chrome (version 83.0.4103.116 for me xd)  
   3.2. Run the executable file   
   
4. Install Selenium (python packages) via pip  
  
   4.1. Open your command prompt after you've installed python  
   4.2. Enter the command "pip install selenium"   



## Customize values (whatsapp_script.py)
1. Set your roll call timings (line 28)
2. Set your name (line 50)
3. Set your desired temperature (line 51)
4. Set your medical status (line 52)
5. Set your location (line 53)
6. Set your target (name of person/group you're sending the roll call message to)

   
   
## Usage details
1. Open your command prompt
2. Customize your roll call values (roll call timing, name, temperature, etc)
3. Run the main script with the command "python whatsapp_script.py
4. Open whatsapp on your phone and scan the QR code that pops up on the new chrome window.
5. Leave your laptop on 24/7. 
6. PROFIT.  



## Credits
This project was heavily inspired by https://medium.com/dsc-srm/make-a-whatsapp-spammer-in-under-10-lines-of-python-code-b414024db8e 
Thanks you so much for contributing to my growth & mental health !!



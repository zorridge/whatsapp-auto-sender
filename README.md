# Automated WhatsApp Bulk Messaging

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#disclaimer">Disclaimer</a></li>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#troubleshooting">Troubleshooting</a></li>
  </ol>
</details>



<!-- DISCLAIMER -->
## Disclaimer

Automated bulk messaging is actually against WhatsApp's Term of Service. However, this project implements the "bulk messaging" function by taking over the system with PyAutoGui and using WhatsApp Web in the browser. So essentially, we are just mimicking human action so I suppose we are good to proceed. 

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ABOUT THE PROJECT -->
## About The Project

![image](https://user-images.githubusercontent.com/86993236/158977241-a3264236-2445-4fa0-9e88-7f9c9512127c.png)

### Problem

I encountered a situation where I was given a list of targets to reach out to via WhatsApp. 

Normally, one would have to save their contact; initiate chat; send out message *(best practice is of course to include some form of personalisation to your copy-pasted message)*. 

It sucked. Nobody likes doing the same things over and over again, it is also error-prone.

Then I remembered Python exists.

### Solution

Did you know that you can initiate a chat without saving contacts using WhatsApp Web and query strings? You can even pre-populate the message. Now you know.

![image](https://user-images.githubusercontent.com/86993236/158981398-3da1158a-a04a-4553-854c-296a927a4fd6.png)

However there is no WhatsApp API (I think... I hope so or else I just wasted 2 days of my life) to actually send out the message.

PyAutoGui enters the scene. PyAutoGui will take over your mouse and keyboard to send out the message. However this does mean your device will be unusable during the script.

Building on top of that, I have added a GUI using Tkinter for customisable message inputs.

View source code [here](/app.py).

### Built With

* [Python](https://www.python.org/)
* [PyAutoGui](https://pyautogui.readthedocs.io/en/latest/)
* [Tkinter](https://tkdocs.com/tutorial/index.html)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- DEMO -->
## DEMO

https://user-images.githubusercontent.com/86993236/161220534-4e9be970-f3a8-4ff6-a810-28c60cac1118.mp4

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

I have compiled the script as an executable, so ignore the below if you are running ```app.exe```.

But if you'd like to get a local copy up and running, follow these steps below (Windows):

### Prerequisites

Ensure that the latest version of Python 3 is installed (written in Python 3.10.1)
* python
  ```sh
  python --version
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/zorridge/whatsapp-auto-sender.git
   ```
2. Install required modules
   ```sh
   pip install pyautogui
   ```
3. Run
   ```sh
   python app.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Admittedly, this project is very bare-boned and lacking in many ways, especially in the client-side error handling department.

Please kindly follow the steps below to a T in order for optimal execution.

I implore you to try it once with your own number (yes, you can WhatsApp yourself) before starting with your actual targets.

Please.

***

### Set up WhatsApp Web

Self explanatory. Do it [here](https://web.whatsapp.com/).

IMPORTANT: If you have multiple monitors, make sure when the script starts the browser is at your main screen and maximised as that is where PyAutoGui will click and enter.

***

### Data preparation

![image](https://user-images.githubusercontent.com/86993236/159036833-8ed2f31e-f17a-40b3-9c08-b0e6270d04a2.png)

Populate merchantContact.csv inside the current directory with the businesses' names and contact numbers.

Do not use person's name as all messages will start with "Hi there owner of { business's name }".

IMPORTANT: DO NOT edit the column headers! DO NOT add/remove/edit any columns other A and B!

Numbers MUST have country codes! The script will add "+" prefix to the number so it will not work if there is no country code.

***

### Using app.exe

![image](https://user-images.githubusercontent.com/86993236/158977241-a3264236-2445-4fa0-9e88-7f9c9512127c.png)

Just double-click app.exe and it should open up to the GUI app.

Make sure ```whatsapp.ico``` and ```merchantContract.csv``` are inside the same folder.

***

### Message input

All messages begin with "Hi there owner of { business's name }" followed by your message input on a new paragraph.

You may leave this empty (why would you ever) and the code will still run.

Avoid emojis at all costs.

***

### Delay

Delay is the time the script will wait for WhatsApp Web to load up in your browser.

Leaving it empty will default delay to 15 seconds, which I find is quite comfortable personally.

My suggestion is to start with ~30 seconds, depending on your device speed and internet speed, and work your way down to a comfortable delay.

IMPORTANT: Only enter POSITIVE INTEGERS please! I have yet to implement error handling for delay.

***

### Running the script

Once you are happy with your message, press "Submit". A status will be displayed at the bottom.

![image](https://user-images.githubusercontent.com/86993236/159035488-26f83072-ed0e-48a2-b4e3-d4d86f05ac04.png)

IMPORTANT: You CANNOT use your device when the script is running, please refer to "About The Project" > "Solution". DO NOT move or click your mouse.

Input boxes and "Submit" button will be disabled when script is running.

The previously disabled "Kill" button will be enabled.

***

### Killing the running script

IMPORTANT: DO NOT try to kill the script by closing the app window (you cannot close it anyways).

You will be greeted with this lovely pop-up:

![image](https://user-images.githubusercontent.com/86993236/159037722-cfa563f5-9611-4d39-a0b7-e47b10e1091c.png)

*OPTIONAL: Under the hood the function doing the work is running on a separate thread from the main thread that is displaying the GUI so even if you close the GUI the function will still run. To completely kill the script, either use the "Kill" button or close app.exe via Task Manager.*

![image](https://user-images.githubusercontent.com/86993236/159038912-e849b89f-3df6-41cb-b9ab-1f93d23ba75f.png)

To stop the script, press the "Kill" button.

You still cannot close the app window as the script will take some time to act on the kill request due to the delay.

But the message will never be sent out as long as the kill request is live, do not fret.

![image](https://user-images.githubusercontent.com/86993236/159039398-2c9f816b-cc75-44dd-94eb-d1779d49ba7d.png)

Congratulations, you just killed my boy.

You can re-run it by pressing "Submit" again.

<p align="right">(<a href="#top">back to top</a>)</p>



## Troubleshooting

Please kindly make sure you have strictly adhered to the comments labelled as IMPORTANT.

Do feel free to reach out to me and we can figure this out together.

<p align="right">(<a href="#top">back to top</a>)</p>




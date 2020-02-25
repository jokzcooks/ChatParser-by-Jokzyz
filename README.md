You will need python for this! I would recommend Python 3.7, as that is what I used to create it.

Clone the repository:
```
open command prompt and do the following:
cd desktop
git clone https://github.com/jokzcooks/ChatParserForVansBot
cd desktop/ChatParserForVansBot
```

In order to download your chats, you will need the Discord Chat Exporter and you will need to download and install .NET Core runtime from https://github.com/Tyrrrz/DiscordChatExporter/wiki/Install-.NET-Core-runtime

Download the exporter https://github.com/Tyrrrz/DiscordChatExporter/releases/download/2.18/DiscordChatExporter.zip
Extract the files
Launch DiscordChatExporter.exe

It will want your personal user discord token! To get this:
```~ Go to discord and open inspect element (CTRL + SHIFT + I)
~ Go to the network tab and click the clear button (next to the red record button)
~ Reload the page, and you will see a bunch of things pop up
~ Do CTRL+f, and type "authorization:", and hit enter
~ You should see detectable, library, messages, and science pop up
~ Click any of these, and scroll until you see "authorization:"
~ The following key will be what you want to enter into DiscordChatExporter.exe
```
Once you have logged into DiscordChatExporter with your token:
```
~ Scroll down until you see #Private/VansBot
~ Click it, then click the download button
~ Change format to TXT, and click export
~ After saving, open this file up and copy and paste the conents into messages.txt
```
To run the program, go back to cmd and input the command "py account.py"

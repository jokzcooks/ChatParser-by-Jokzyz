### Greetings, my name is [jokzyz](https://twitter.com/jokzyzz), and I am the owner of [JokzCooks](https://twitter.com/jokzcooks) and a developer for [Odyssey AIO](https://twitter.com/odysseyaio)

I would like to credit Sauce from SauceSteals for providing me access to his Vans Bot, and hope that anybody else who is lucky enough to be in SauceSteals and take advantage of his bot will benefit from this!

# Introduction
The two main functions of this program are:

#### 1: Scraping an email:password list from a chat log from a discord bot that served as an account generator.
  
>This is beneficial if you would just like a master list of the login info of every account you generated in an email:password format.

>You could then implement this list into a bot that automatically logs in and redeems the rewards on each account.

#### 2: Allowing you to select a specific account from the list.

>This is beneficial if you would like to manually log in to each account and redeem the rewards yourself.


# Setup



#### You will need python for this! I would recommend Python 3.7, as that is what I used to create it.

#### Clone the repository:
```
open command prompt and do the following:
cd desktop
git clone https://github.com/jokzcooks/ChatParserForVansBot
cd ChatParserForVansBot
```

#### In order to download your chatlog with the bot, you will need the [Discord Chat Exporter](https://github.com/Tyrrrz/DiscordChatExporter/releases/download/2.18/DiscordChatExporter.zip) and [.NET Core Runtime](https://github.com/Tyrrrz/DiscordChatExporter/wiki/Install-.NET-Core-runtime)


> After downloading the exporter and installing the .NET Core Runtime, extract the exporter files and launch DiscordChatExporter.exe

#### You will also need your personal discord account token, to get this:
```~ Go to discord and open inspect element (CTRL + SHIFT + I)
~ Go to the network tab and click the clear button (next to the red record button)
~ Reload the page, and you will see a bunch of things pop up
~ Do CTRL+f, and type "authorization:", and hit enter
~ You should see detectable, library, messages, and science pop up
~ Click any of these, and scroll until you see "authorization:"
~ The following key will be what you want to enter into DiscordChatExporter.exe
```
#### Once you have logged into DiscordChatExporter with your token:
```
~ Scroll down until you see #Private/VansBot
~ Click it, then click the download button
~ Change format to TXT, and click export
~ After saving, open this file up and copy and paste the conents into messages.txt
```
# Using My Parser

#### To run the program, go back to cmd and input the command "py account.py"

> This will first parse the chat and save all of the accounts to output.txt in the format "email:password"

#### The program will then ask for a specific line for you to input.
> This will output a certain account login based on which number you input.

> I have also implemented some simple math, so if you want Account #1, you can input 1!

# Important

This program is curated to work with direct messages between you and `Vans Bot#1459`! If you are using a different account generator, you may have to change up a few things with the code:

The success message that is  being parsed is:
```
Signed up and verified account with email `email` and password `password`
```
If your bot sends a different message, you will want to replace "Signed" in line 7 with whatever first word(s) are present in your bot's message.

Since the character "`" is used to split the email and password, that is what I have put into the split function in lines 10, 21, and 24.

If your bot uses a different character to split the email and password, put that into the split functions instead. If there is not a character splitting them except for a space, put " " into the spit function instead

If you make changes to the split function, you will likely need to change the integers in lines 12, 25, and 26. Just try out different numbers until you find one that works. If you have never worked with python lists or arrays, placing the integer 0 will return the first section in that line after being split, placing the integer 1 will return the second section in that line and so forth. 

## Need Help?
Contact me on [twitter](https://twitter.com/jokzyzz) or by adding me @ jokzyz#4121 on discord!

# License
[MIT](https://github.com/jokzcooks/ChatParserForVansBot/blob/master/README.md)

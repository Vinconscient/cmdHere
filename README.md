# cmdHere


WHAT IS CMDHERE ?

cmdHere is a program that will help you to open a cmd in the actual folder location, so instead of open a cmd, copy the path of your folder, and type "cd : (THE PATH)" all will be done by cmdHere ! And it's easy to access it because I'll explain to you how to add it in the context menu (the menu when you right click) of windows.


HOW TO ADD THIS FILE IN THE CONTEXT MENU ?

  1. Copy the path to cmdHereV2.1.exe (and make sure it will not change) 

  2. Open the Registry Editor (search it in the windows bar)

  3. Go to this location : "HKEY_CLASSES_ROOT\Directory\Background\shell"

  4. Right click the "shell" folder and add a new key

  5. Name it "cmdHere" or whatever you want (it will be the name that you will see in the right click menu)

  6. Now right click the new folder and add a key named "command" (you have to name it like that)

  7. Double right click on "(Default)" and enter the path of the .EXE file in the "value data" input box

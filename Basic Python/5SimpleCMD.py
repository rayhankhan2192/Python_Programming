command = ""
isStarted = False
while True:
    command = input("> ").lower()
    if(command == "/start"):
        if isStarted:
            print("Music is already started...")
        else:
            isStarted = True
            print("Music started...")
    elif(command == "/stop"):
        if not isStarted:
            print("Music already stopped...")
        else:
            isStarted = False
            print("Music stopped..")
    elif(command == "/help"):
        print("""
/start - to start the music
/stop - to stop the music
/quit - to quit
""")
    elif(command == "/quit"):
        break
    else:
        print("Sorry! I didn't understand that")
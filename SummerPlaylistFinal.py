Playlist = {
    "chill": ["1979 - The Smashing Pumpkins", "Piledriver Waltz - Alex Turner", "Dreams - Fleetwood Mac"],
    "hype": ["Sweet Child O' Mine - Guns n' Roses", "Bohemian Rhapsody - Queen", "Beat It - Michael Jackson"],
    "roadtrip": ["Life Is a Highway - Cars", "Blaze Of Glory - Bon Jovi", "SOS - ABBA"],
    "mc": ["The Less I Know The Better - Tame Impala", "Cupid De Locke - the Smashing Pumpkins", "Die With A Smile - Lady Gaga&Bruno Mars"]
}

"mc" == "main character"

def playgen():
    print ("Lets make your summer playlist! What kind of playlist are you looking for? chill, hype, roadtrip, main character")
    choice = input()

    if choice in Playlist:
        playlistuser = Playlist[choice]
        print("Alright, here you go!", playlistuser)
    else:
        print("Oopsies, looks like we don't have that one. Try choosing between: chill, hype, roadtrip, or main character")
        return

    while True:
        print("Nice choice, here's a", playlistuser)
        change = input("Do you want to edit the playlist? Type 'add' or 'remove.' Type 'DONE' to finish.")

        if change == "DONE":
            print("Okay! Enjoy your summer playlist!")
            break 

        elif change == "add":
            musique = input("Enter song in format: song - artist")
            playlistuser.append(musique)

        elif change == "remove":
            musique = input("Enter song in format: song - artist")
            if musique in playlistuser:  
                playlistuser.remove(musique)
            else: 
                print("That's not in the playlist, try again")

playgen()





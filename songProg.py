from song import Song


def findShortestSong(songlist):
    minLength = 1000
    minSongIndex = 0
    for i in range(len(songlist)):
        lengthInSeconds = songlist[i].getMinutes()*60 + songlist[i].getSeconds()
        if lengthInSeconds < minLength:
            minLength = lengthInSeconds
            minSongIndex = i
    print('The shortest song is:')
    print(songlist[minSongIndex])

def calcRuntime(songs):
    totalRuntime = 0 
    for element in range(len(songs)):
        songLength = songs[element].getMinutes()*60 + songs[element].getSeconds()
        totalRuntime += songLength
    minutes = totalRuntime//60
    seconds = totalRuntime%60
    print("Playlist is", minutes, "minutes and", seconds, "seconds long")
    return totalRuntime
        

def main():
    print("Welcome to Music Player")
    favoriteSong = Song("Ticket to L.A", "Brett young", 3, 28)
    leastfavSong = Song("Whiskey Lullaby", "Brad Paisley", 4, 58)
    

    print("Enter your own favorite")
    favoriteName = input("Enter the title of your favorite song: ")
    favoriteArtist = input("Enter the artist of your favorite song: ")
    favoriteMinutes = int(input("Enter the length in minutes of your favorite song: "))
    favoriteSeconds = int(input("Enter the remaining seconds of your favorite song: "))
    userFavorite = Song(favoriteName, favoriteArtist, favoriteMinutes, favoriteSeconds)

    print("Enter your own least favorite")
    leastfavoriteName = input("Enter the title of your least favorite song: ")
    leastfavoriteArtist = input("Enter the artist of your least favorite song: ")
    leastfavoriteMinutes = int(input("Enter the length in minutes of your least favorite song: "))
    leastfavoriteSeconds = int(input("Enter the remaining seconds of your least favorite song: "))
    userleastFavorite = Song(leastfavoriteName, leastfavoriteArtist, leastfavoriteMinutes, leastfavoriteSeconds)

    
    print("My favorite is", favoriteSong)
    print("My least favorite is", leastfavSong)
    print("Your favorite is", userFavorite)
    print("Your least favorite is", userleastFavorite)

    
    userChoice = 'X'
    while userChoice != "Q":
        
        print('T - change title')
        print('A - change artist')
        print('M - change minutes')
        print('S - change seconds')
        print('P - print details')
        print('Q - quit')
        userChoice = input("Enter your choice: ")

        if userChoice == 'T' or userChoice == 't':
            userTitle = input("Enter the new title: ")
            favoriteSong.setTitle(userTitle)
        elif userChoice == 'A' or userChoice == 'a':
            userArtist = input("Enter the new artist: ")
            favoriteSong.setArtist(userArtist)
        elif userChoice == 'M' or userChoice == 'm':
            userMinutes = int(input("Enter the new minutes: "))
            favoriteSong.setMinutes(userMinutes)
        elif userChoice == 'S' or userChoice == 's':
            userSeconds = int(input("Enter the new seconds: "))
            favoriteSong.setSeconds(userSeconds)
        elif userChoice == 'P'or userChoice == 'p':
            print(favoriteSong)
        elif userChoice == 'Q':
            print("Goodbye")

    playList = []
    playList.append(favoriteSong)
    playList.append(leastfavSong)
    playList.append(userFavorite)
    playList.append(userleastFavorite)
    count = 0
    for element in playList:
        print("Song", count+1, "is")
        print(element)
        count +=1

    maxLength = 0
    maxSongIndex = 0
    for i in range(len(playList)):
        lengthInSeconds = playList[i].getMinutes()*60 + playList[i].getSeconds()
        if lengthInSeconds > maxLength:
            maxLength = lengthInSeconds
            maxSongIndex = i

    print("The longest song is")
    print(playList[maxSongIndex])
        
    shortest = findShortestSong(playList)
    runTime = calcRuntime(playList)


main()



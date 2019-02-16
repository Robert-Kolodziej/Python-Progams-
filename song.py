"""
File:song.py

This module defines the song class.
"""

class Song:
    """This class represents a song. """

    def __init__(self, title, artist, minutes, seconds):
        self.myTitle = title
        self.myArtist = artist
        self.myMinutes = minutes
        self.mySeconds = seconds

    def __str__(self):
        """Returns the string representation."""
        ans = "Title: " + str(self.myTitle) + "\n"
        ans += "Artist: " + str(self.myArtist) + "\n"
        ans += "Minutes: " + str(self.myMinutes) + "\n"
        ans += "Seconds: " + str(self.mySeconds)

        return ans

    def getTitle(self):
        """Returns the title of the song."""
        return self.myTitle

    def getArtist(self):
        """Returns the artist of the long."""
        return self.myArtist
    
    def getMinutes(self):
        """Returns the length of the song in minutes."""
        return self.myMinutes
    
    def getSeconds(self):
        """Returns the additional time left in the song after the minutes."""
        return self.mySeconds
    

    def setTitle(self, newTitle):
        """Sets the title of the song."""
        self.myTitle = newTitle

    def setArtist(self, newArtist):
        """Sets the artist of the song."""
        self.myArtist = newArtist

    def setMinutes(self, newMinutes):
        """Sets the length of the song in minutes."""
        self.myMinutes = newMinutes

    def setSeconds(self, newSeconds):
        """Sets the additional length of the song after the minutes."""
        self.mySeconds = newSeconds

    


        
        

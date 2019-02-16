#Name Bobby Kolodziej

#File Prog2Kolodziej.py

#Purpose: This is a program designed to compute the score for a promoted tweet.

#Input: The input values for this program are the Number of retweets, the number of atreplys, and the number of days the tweet has been up.

#Output: The output values for this program is the score of the tweet.

#Certification of authenticity:
    #I certify that this ab is entirely my own work.

def main():
    print("This program calculates the score of a promoted tweet")
    #Number of re-tweets - higher value is better.
    #Number of @ replys - higher number is better.
    #Number of days - lower number is better.
    #Input the umber of retweets
    numRetweets = float(input("Please enter the number of re-tweets: "))
    #calculate the score of retweets
    scoreRetweets=0.3333*numRetweets
    print("The retweet score is", scoreRetweets)
    #Input the number of @replys.
    numAtreplys= float(input("Please enter the number of @ replys: "))
    #calculate the score of @ replys
    scoreAtreplys= 0.3333*numAtreplys
    print("The @ reply score is", scoreAtreplys)
    #Input the number of days since the tweet was posted.
    numDays= float(input("Please enter the number of days the tweet has been up for: "))
    #calculate the score of days
    scoreDays=0.3333/(numDays)**2
    print("The days score is", scoreDays)
    #Calculate the total score
    totalscore=(scoreRetweets+scoreAtreplys+scoreDays)
    print("The total score of your tweet is", totalscore, "(higher is better)")
    
main()

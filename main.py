from sim import *

def main():
    while(True):
        print(teams)
        team1 = input("Who should be the home team? (3 letter abbreviation): ")
        if(team1 in teams):
            break
        print("Incorrect abbreviation, try again")
    while(True):
        team2 = input("Who should be the away team? (3 letter abbreviation): ")
        if(team2 in teams):
            break
        print("Incorrect abbreviation, try again")
    num_times = int(input("How many times do you want the teams to play? "))
    spread = float(input("What is the spread relative to the home team? "))
    points = float(input("What is the over/under of the game? "))
    play_many_games(num_times,spread,team1,team2,points)



if __name__ == '__main__':
    main()

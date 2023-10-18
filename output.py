from sim import *

def calc_full_bet(a_ml,h_ml,overs,h_covers,a_covers,num_sims,h_wins,a_wins):
    aml_money = 0
    if(a_ml < 0):
        aml_money = ((((100/abs(a_ml))+1)*a_wins)-num_sims)/num_sims
    else:
        aml_money = ((((abs(a_ml)/100)+1)*a_wins)-num_sims)/num_sims

    hml_money = 0
    if(a_ml < 0):
        hml_money = ((((100/abs(h_ml))+1)*h_wins)-num_sims)/num_sims
    else:
        hml_money = ((((abs(h_ml)/100)+1)*h_wins)-num_sims)/num_sims

    overs_money = overs/num_sims
    unders_money = (1-overs)/num_sims
    h_covers_money = (h_covers)/num_sims
    a_covers_money = (a_covers)/num_sims

    return [aml_money, hml_money, overs_money, unders_money, h_covers_money, a_covers_money]


def play_many_games(num,home,away):
    num_wins_home = 0
    num_wins_away = 0
    hpy = 0
    hry = 0
    apy = 0
    ary = 0
    scores = []
    yards_gained = []
    for x in range(num):
        h_score, a_score, hpy, hry, apy, ary = play_game(home,away)
        if(h_score > a_score):
            num_wins_home += 1
        else:
            num_wins_away += 1
        scores.append([h_score,a_score])
        yards_gained.append([hpy,hry,apy,ary])
    print("\nRESULTS:")
    print("Home team wins:", num_wins_home)
    print("Away team wins:", num_wins_away)
    print()

def play_many_games(num,spread,home,away,ou):
    num_wins_home = 0
    num_wins_away = 0
    home_covers = 0
    pushes = 0
    overs = 0
    hpy = 0
    hry = 0
    apy = 0
    ary = 0
    scores = []
    yards_gained = []
    for x in range(num):
        h_score, a_score, hpy, hry, apy, ary = play_game(home,away)
        if(h_score > a_score):
            num_wins_home += 1
        else:
            num_wins_away += 1
        if(h_score + spread > a_score):
            home_covers += 1
        elif(h_score + spread == a_score):
            pushes += 1
        if(h_score + a_score > ou):
            overs += 1
        scores.append([h_score,a_score])
        yards_gained.append([hpy,hry,apy,ary])
    print("\nRESULTS:")
    print("Home team wins:", num_wins_home)
    print("Away team wins:", num_wins_away)
    print("Home team covers:", home_covers)
    if(pushes != 0):
        print("With",pushes,"pushes")
    print("Overs hit:",overs)
    count = False
    print("\nOPINION OF THIS SIM:")
    if(home_covers >= num*0.65):
        print("Bet Home Team Covering")
    elif(home_covers <= num*0.35):
        print("Bet Away Team Covering")
    else:
        count = True
    if(overs >= num*0.65):
        print("Bet Over")
    elif(overs <= num*0.35):
        print("Bet Under")
    elif(count):
        print("\nStay away from this game")
    print()








def play_many_games(num,spread,home,away,ou,risk):
    num_wins_home = 0
    num_wins_away = 0
    home_covers = 0
    pushes = 0
    overs = 0
    hpy = 0
    hry = 0
    apy = 0
    ary = 0
    scores = []
    yards_gained = []
    for x in range(num):
        h_score, a_score, hpy, hry, apy, ary = play_game(home,away)
        if(h_score > a_score):
            num_wins_home += 1
        else:
            num_wins_away += 1
        if(h_score + spread > a_score):
            home_covers += 1
        elif(h_score + spread == a_score):
            pushes += 1
        if(h_score + a_score > ou):
            overs += 1
        scores.append([h_score,a_score])
        yards_gained.append([hpy,hry,apy,ary])
    print("\nRESULTS:")
    print("Home team wins:", num_wins_home)
    print("Away team wins:", num_wins_away)
    print("Home team covers:", home_covers)
    if(pushes != 0):
        print("With",pushes,"pushes")
    print("Overs hit:",overs)
    count = False
    print("\nOPINION OF THIS SIM:")
    if(home_covers >= num*0.65):
        if(overs >= num*0.65):
            print("\nBet {money:.2f} on Home Team Covering".format(money=(risk*(home_covers/(home_covers+overs)))))
            print("\nBet {money:.2f} on Over".format(money=(risk*(overs/(home_covers+overs)))))
        elif(overs <= num*0.35):
            print("\nBet {money:.2f} on Home Team Covering".format(money=(risk*(home_covers/(home_covers+(1-overs))))))
            print("\nBet {money:.2f} on Over".format(money=(risk*((1-overs)/(home_covers+(1-overs))))))
        else:
            print("\nBet {money:.2f} on Home Team Covering".format(money=risk))
    elif(home_covers <= num*0.35):
        if(overs >= num*0.65):
            print("\nBet {money:.2f} on Away Team Covering".format(money=(risk*((1-home_covers)/((1-home_covers)+overs)))))
            print("\nBet {money:.2f} on Over".format(money=(risk*(overs/(home_covers+overs)))))
        elif(overs <= num*0.35):
            print("\nBet {money:.2f} on Away Team Covering".format(money=(risk*((1-home_covers)/((1-home_covers)+(1-overs))))))
            print("\nBet {money:.2f} on Over".format(money=(risk*((1-overs)/((1-home_covers)+(1-overs))))))
        else:
            print("\nBet {money:.2f} on Away Team Covering".format(money=risk))
    else:
        count = True
    if(overs >= num*0.65):
        print("\nBet {money:.2f} on Over".format(money=risk))
    elif(overs <= num*0.35):
        print("\nBet {money:.2f} on Under".format(money=risk))
    elif(count):
        print("\nStay away from this game")
        print("But if you want to bet no matter what, here is my choice:")
        if(home_covers > num-home_covers-pushes):
            if(overs > num-overs):
                print("\nBet {money:.2f} on Home Team Covering".format(money=(risk*(home_covers/(home_covers+overs)))))
                print("\nBet {money:.2f} on Over".format(money=(risk*(overs/(home_covers+overs)))))
            elif(overs == num-overs):
                print("Don't bet Over/Under")
                print("\nBet {money:.2f} on Home Team Covering".format(money=risk))
            else:
                print("\nBet {money:.2f} on Home Team Covering".format(money=(risk*(home_covers/(home_covers+(1-overs))))))
                print("\nBet {money:.2f} on Over".format(money=(risk*((1-overs)/(home_covers+(1-overs))))))
        elif(home_covers == num-home_covers-pushes):
            if(overs == num-overs):
                print("Run again, or just don't bet on this game :)")
            elif(overs > num-overs):
                print("Don't bet on the spread")
                print("Bet {money:.2f} on Over".format(money=risk))
            else:
                print("Don't bet on the spread")
                print("Bet {money:.2f} on Under".format(money=risk))
        else:
            if(overs > num-overs):
                print("\nBet {money:.2f} on Away Team Covering".format(money=(risk*((1-home_covers)/((1-home_covers)+overs)))))
                print("\nBet {money:.2f} on Over".format(money=(risk*(overs/((1-home_covers)+overs)))))
            elif(overs == num-overs):
                print("Don't bet Over/Under")
                print("\nBet {money:.2f} on Away Team Covering".format(money=risk))
            else:
                print("\nBet {money:.2f} on Away Team Covering".format(money=(risk*((1-home_covers)/((1-home_covers)+(1-overs))))))
                print("\nBet {money:.2f} on Under".format(money=(risk*((1-overs)/((1-home_covers)+(1-overs))))))

    print()



def play_many_games(num,spread,home,away,ou,aml,hml):
    num_wins_home = 0
    num_wins_away = 0
    home_covers = 0
    pushes = 0
    overs = 0
    hpy = 0
    hry = 0
    apy = 0
    ary = 0
    scores = []
    yards_gained = []
    for x in range(num):
        h_score, a_score, hpy, hry, apy, ary = play_game(home,away)
        if(h_score > a_score):
            num_wins_home += 1
        else:
            num_wins_away += 1
        if(h_score + spread > a_score):
            home_covers += 1
        elif(h_score + spread == a_score):
            pushes += 1
        if(h_score + a_score > ou):
            overs += 1
        scores.append([h_score,a_score])
        yards_gained.append([hpy,hry,apy,ary])
    print("\nRESULTS:")
    print("Home team wins:", num_wins_home)
    print("Away team wins:", num_wins_away)
    print("Home team covers:", home_covers)
    if(pushes != 0):
        print("With",pushes,"pushes")
    print("Overs hit:",overs)
    count = 0
    print("\nOPINION OF THIS SIM:")
    if(home_covers >= num*0.65):
        print("\nBet Home Team Covering")
    elif(home_covers <= num*0.35):
        print("\nBet Away Team Covering")
    else:
        count += 1
    if(overs >= num*0.65):
        print("\nBet Over")
    elif(overs <= num*0.35):
        print("\nBet Under")
    a_ml_money = ((((100/abs(aml))+1)*num_wins_away)-num)
    h_ml_money = ((((100/abs(hml))+1)*num_wins_home)-num)
    if(a_ml_money >= num*0.1):
        print("Bet Away Moneyline")
    elif(h_ml_money >= num*0.1):
        print("Bet Home Moneyline")
    else:
        count += 1
    if(count == 2):
        print("\nStay away from this game")
    print()






def play_many_games(num,spread,home,away,ou,risk,aml,hml):
    home_ml = False
    away_ml = False
    num_wins_home = 0
    num_wins_away = 0
    home_covers = 0
    pushes = 0
    overs = 0
    hpy = 0
    hry = 0
    apy = 0
    ary = 0
    scores = []
    yards_gained = []
    for x in range(num):
        h_score, a_score, hpy, hry, apy, ary = play_game(home,away)
        if(h_score > a_score):
            num_wins_home += 1
        else:
            num_wins_away += 1
        if(h_score + spread > a_score):
            home_covers += 1
        elif(h_score + spread == a_score):
            pushes += 1
        if(h_score + a_score > ou):
            overs += 1
        scores.append([h_score,a_score])
        yards_gained.append([hpy,hry,apy,ary])
    print("\nRESULTS:")
    print("Home team wins:", num_wins_home)
    print("Away team wins:", num_wins_away)
    print("Home team covers:", home_covers)
    if(pushes != 0):
        print("With",pushes,"pushes")
    print("Overs hit:",overs)
    count = 0
    money_vals = calc_full_bet(aml,hml,overs,home_covers,num-home_covers-pushes,num,num_wins_home,num_wins_away)
    print("\nAway Money Line earnings per game ($1 bet):",money_vals[0])
    print("Home Money Line earnings per game ($1 bet):",money_vals[1])
    print("Over earnings per game ($1 bet):",money_vals[2])
    print("Under earnings per game ($1 bet):",money_vals[3])
    print("Home Covering earnings per game ($1 bet):",money_vals[4])
    print("Away Covering earnings per game ($1 bet):",money_vals[5])
    print("\nOPINION OF THIS SIM:")
#[aml_money, hml_money, overs_money, unders_money, h_covers_money, a_covers_money]
    sum = 0
    for x in money_vals:
        if(x < num*0.1):
            x = 0
        sum += x
    if(sum != 0):
        if(money_vals[0] != 0):
            print("\nBet {money:.2f} on away money line".format(money = (risk*(money_vals[0]/sum))))
        if(money_vals[1] != 0):
            print("\nBet {money:.2f} on home money line".format(money = (risk*(money_vals[1]/sum))))
        if(money_vals[2] != 0):
            print("\nBet {money:.2f} on over".format(money = (risk*(money_vals[2]/sum))))
        if(money_vals[3] != 0):
            print("\nBet {money:.2f} on under".format(money = (risk*(money_vals[3]/sum))))
        if(money_vals[4] != 0):
            print("\nBet {money:.2f} on home team covering".format(money = (risk*(money_vals[4]/sum))))
        if(money_vals[5] != 0):
            print("\nBet {money:.2f} on away team covering".format(money = (risk*(money_vals[5]/sum))))
    else:
        print("\nReally, you shouldn't bet on this game")


    print()


import os;

# Clear the screen
def ClearScreen():
	if os.name == "nt":
		os.system("cls");
	else:
		os.system("clear");

# Show table (assuming list data structure for listData[row])
def ShowTableByList(title, listRowNames, listColNames, listData):

    print(title);

    noRowNames = True if len(listRowNames) == 0 else False;

    # Find the maximum length for row names
    rmaxLen = 0 if len(listRowNames) == 0 else max([len(rname) for rname in listRowNames]);
    
    # Find the maximum length for columns
    cmaxLen = [len(colName) for colName in listColNames];
    for row in range(len(listData)):
        for col in range(len(listData[row])):
            cmaxLen[col] = max(cmaxLen[col], len(str(listData[row][col])));

    # Create header string with listColNames
    listStart = [] if noRowNames else [' ' * rmaxLen];
    listColNamesJustified = [listColNames[col].center(cmaxLen[col]) for col in range(len(listColNames))];
    listHeaderName = listStart + listColNamesJustified;
    header = " | ".join(listHeaderName);

    # Create Border
    listHeaderNameLength = [len(c) for c in listHeaderName];
    listColBorder = ["-" * l for l in listHeaderNameLength];
    border = "-+-".join(listColBorder);

    # Show full headers (border + header + border)
    print(f"+-{border}-+");
    print(f"| {header} |");
    print(f"+-{border}-+");

    # Show all rows of data
    for row in range(len(listData)):
        # Create row string
        listRowStr = [] if noRowNames else [listRowNames[row].ljust(rmaxLen)];
        
        for col in range(len(listData[row])):
            if listData[row][col] != None:
                colStr = str(listData[row][col]);
                listRowStr.append(colStr.rjust(cmaxLen[col]));
            else:
                listRowStr.append(" " * cmaxLen[col]);

        # Construct a row string from listRowStr
        rowStr = " | ".join(listRowStr);

        # Show row string
        print(f"| {rowStr} |");
        print(f"+-{border}-+");

    print();

# Trio
def trio(diceValue):
        new_diceValue = set(diceValue) 
        for dupli_num in new_diceValue:  
            count = diceValue.count(dupli_num)  
            if count>=3:  
                    Trio = sum(diceValue)
            else:
                    Trio = 0

            return Trio
            
# Quartet
def quartet(diceValue):  
        new_diceValue = set(diceValue)  
        for dupli_num in new_diceValue:  
            count = diceValue.count(dupli_num)  
            if count>=4:  
                    Quartet = sum(diceValue)
            else:
                    Quartet = 0

            return Quartet

# Band
def band(diceValue):  
        new_diceValue = set(diceValue)  
        for dupli_num1 in new_diceValue:  
            count1 = diceValue.count(dupli_num1)
            for dupli_num2 in new_diceValue:  
                    count2 = diceValue.count(dupli_num1)
                
            if count1==3 and count2==2:  
                    Band = sum(diceValue)
            else:
                    Band = 0

            return Band

# Doremi
def doremi(diceValue):
    if (1 in diceValue) and (2 in diceValue) and (3 in diceValue) and (4 in diceValue):
            Doremi = 20
    else:
            Doremi = 0

    return Doremi

# Orchestra
def orchestra(diceValue):  
        new_diceValue = set(diceValue)  
        for dupli_num in new_diceValue :  
            count = diceValue.count(diceValue)  
            if count==5:  
                    Orchstra = 40                    
            else:
                    Orchestra = 0

            return Orchestra


# Trio for cheat
def trio_cheat(num_list):
        new_num_list = set(num_list) 
        for dupli_num in new_num_list :  
            count = num_list.count(dupli_num)  
            if count>=3:  
                    Trio = sum(num_list)
            else:
                    Trio = 0

            return Trio
            
# Quartet for cheat
def quartet_cheat(num_list):  
        new_num_list  = set(num_list)  
        for dupli_num in new_num_list:  
            count = num_list.count(dupli_num)  
            if count>=4:  
                    Quartet = sum(num_list)
            else:
                    Quartet = 0

            return Quartet

# Band for cheat
def band_cheat(num_list):  
        new_num_list = set(num_list)  
        for dupli_num1 in new_num_list :  
            count1 = num_list.count(dupli_num1)
            for dupli_num2 in new_num_list :  
                    count2 = num_list.count(dupli_num1)
                
            if count1==3 and count2==2:  
                    Band = sum(num_list)
            else:
                    Band = 0

            return Band

# Doremi for cheat
def doremi_cheat(num_list):
    if (1 in num_list) and (2 in num_list) and (3 in num_list) and (4 in num_list):
            Doremi = 20
    else:
            Doremi = 0

    return Doremi

# Orchestra for cheat
def orchestra_cheat(num_list):  
        new_num_list = set(num_list)  
        for dupli_num in new_num_list :  
            count = num_list.count(dupli_num)  
            if count==5:  
                    Orchstra = 40                    
            else:
                    Orchestra = 0

            return Orchestra

# Check if the numbers are in range from 1 to 4
def check_num(num_list): 
      
    for num in num_list: 
        if num>4 or num<1: 
            return False 
    return True


ClearScreen()
game_title=" Battle of the Sexes (B.O.T.S) "
print(game_title.center(80, '=')) 

if __name__ == "__main__":

    
    names = ["Player 1", "Player 2"];
    category = ["1S", "2S", "3S", "4S", "Trio", "Quartet", "Band", "Doremi", "Orchestra"];

    # Marks organized in a list for each player, to be used for ShowTableByList()
    marksList = [ 
        ['', '', '', '', '', '', '', '', ''], # marks of player 1 
        ['', '', '', '', '', '', '', '', ''], # marks of player 2  
    ];


    # Show table (data stored as list of list)
    ShowTableByList("Scoreboard", names, category, marksList);

player1 = []
player2 = []
marks_p1 = [None,None,None,None,None,None,None,None,None]
marks_p2 = [None,None,None,None,None,None,None,None,None]
total_score_p1=0
total_score_p2=0
current_player = 1

print("Player 1: 0")
print("Player 2: 0")

# 9 rounds for each player
for i in range(18):
        
    if current_player==1:
        print("\nPlayer 1 \n========")
                        
    elif current_player==2:
        print("\nPlayer 2 \n========")

    input("Press ENTER to roll dice.\n")

    # create list of random int    
    diceValue = []
    import random
    for num in range(5):
        num = random.randint(1,4)
        diceValue.append(num)
             
    print("Roll #1 :", diceValue)
    print("\n")

    if __name__ == "__main__":
    
        S1 = 1*diceValue.count(1) 
        S2 = 2*diceValue.count(2)
        S3 = 3*diceValue.count(3)    
        S4 = 4*diceValue.count(4)
        Trio = trio(diceValue)
        Band = band(diceValue)
        Quartet = quartet(diceValue)
        Doremi = doremi(diceValue)
        Orchestra = orchestra(diceValue)
    
    
        category = ["1S", "2S", "3S", "4S", "Trio", "Quartet", "Band", "Doremi", "Orchestra"];

        # Scores organized in a list for each player, to be used for ShowTableByList()
        scoreList = [
            [S1, S2, S3, S4, Trio, Quartet, Band, Doremi, Orchestra], # score of player
            
             ];

    # Show table of Category Scores
    ShowTableByList("Category Scores", [], category, scoreList);

    print("\nInput Options:")
    print("  SAVE\t\t :- Accept these dice.")
    print("  ROLL\t\t :- Re-roll ALL dice.")
    print("  ROLL d1 ... dn :- Re-roll specified dice only.")

    option = input("Input >")
        
    option = option.upper()
    roll_time = 2
    second_roll = True
    cheat = False

    while second_roll==True:
        
        # if input is 'SAVE'/dice is rolled twice and loop back
        if option=='SAVE' or roll_time==4:
            
            retry=True
            # Back to get user input again if error message is out
            while retry==True:  
                category_name = input('Enter your desired category: ').upper()
                lower_category_name = category_name.lower()

                if cheat==True: # for cheat option only
                    S1 = 1*num_list.count(1)
                    S2 = 2*num_list.count(2)
                    S3 = 3*num_list.count(3)    
                    S4 = 4*num_list.count(4)
                    Trio = trio_cheat(num_list)
                    Band = band_cheat(num_list)
                    Quartet = quartet_cheat(num_list)
                    Doremi = doremi_cheat(num_list)
                    Orchestra = orchestra_cheat(num_list)
                else:   # for options other than cheat

                    S1 = 1*diceValue.count(1) 
                    S2 = 2*diceValue.count(2)
                    S3 = 3*diceValue.count(3)    
                    S4 = 4*diceValue.count(4)
                    Trio = trio(diceValue)
                    Band = band(diceValue)
                    Quartet = quartet(diceValue)
                    Doremi = doremi(diceValue)
                    Orchestra = orchestra(diceValue)
                    
                # Insert score for player 1
                if current_player == 1: 
                    if category_name == '1S':
                
                        if marks_p1[0] == None:
                            marks_p1[0]=S1
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    elif category_name  == '2S':
                
                        if marks_p1[1] == None:
                            marks_p1[1]=S2
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                   
                    elif category_name == '3S':
                
                        if marks_p1[2] == None:
                            marks_p1[2]=S3
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    elif category_name == '4S':
                
                        if marks_p1[3] == None:
                            marks_p1[3]=S4
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    elif category_name == 'TRIO':
                
                        if marks_p1[4] == None:
                            marks_p1[4]=Trio
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
               
                    elif category_name  == 'QUARTET':
                
                        if marks_p1[5] == None:
                            marks_p1[5]=Quartet
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    elif category_name == 'BAND':
                
                        if marks_p1[6] == None:
                            marks_p1[6]=Band
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                   
                    elif category_name == 'DOREMI':
                
                        if marks_p1[7] == None:
                            marks_p1[7]=Doremi
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    elif category_name == 'ORCHESTRA':
                
                        if marks_p1[8] == None:
                            marks_p1[8]=Orchestra
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    else:
                        print(f"ERROR: Category '{lower_category_name}' does not exist.")
                        retry=True
                        continue
                    
                # Insert score for player 2
                elif current_player==2: 
                    if category_name == '1S':
                
                        if marks_p2[0] == None:
                            marks_p2[0]=S1
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    elif category_name  == '2S':
                
                        if marks_p2[1] == None:
                            marks_p2[1]=S2
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                   
                    elif category_name == '3S':
                
                        if marks_p2[2] == None:
                            marks_p2[2]=S3
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    elif category_name == '4S':
                
                        if marks_p2[3] == None:
                            marks_p2[3]=S4
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    elif category_name == 'TRIO':
                
                        if marks_p2[4] == None:
                            marks_p2[4]=Trio
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
               
                    elif category_name  == 'QUARTET':
                
                        if marks_p2[5] == None:
                            marks_p2[5]=Quartet
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    elif category_name == 'BAND':
                
                        if marks_p2[6] == None:
                            marks_p2[6]=Band
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                   
                    elif category_name == 'DOREMI':
                
                        if marks_p2[7] == None:
                            marks_p2[7]=Doremi
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    elif category_name == 'ORCHESTRA':
                
                        if marks_p2[8] == None:
                            marks_p2[8]=Orchestra
                            retry=False
                        else:
                            print(f"ERROR: Category '{lower_category_name}' has been used.")
                            retry=True
                            continue
                    
                    else:
                        print(f"ERROR: Category '{lower_category_name}' does not exist.")
                        retry=True
                        continue

                

                ClearScreen()
            
                game_title=" Battle of the Sexes (B.O.T.S) "
                print(game_title.center(80, '=')) 
            
                if __name__ == "__main__":
    
                    names = ["Player 1", "Player 2"];
                    category = ["1S", "2S", "3S", "4S", "Trio", "Quartet", "Band", "Doremi", "Orchestra"];

                    # Scores organized in a list for each player, to be used for ShowTableByList()
                    marksList = [ 
                    [marks_p1[0],marks_p1[1],marks_p1[2],marks_p1[3],marks_p1[4],marks_p1[5],marks_p1[6],marks_p1[7],marks_p1[8]], # marks of player 1 
                    [marks_p2[0],marks_p2[1],marks_p2[2],marks_p2[3],marks_p2[4],marks_p2[5],marks_p2[6],marks_p2[7],marks_p2[8]], # marks of player 2  
                    ];


                    # Show table (data stored as list of list)
                    ShowTableByList("Scoreboard", names, category, marksList);

                    # Calculate total score & change turn
                    if current_player==1:
                        score_p1 = list(filter(None, marks_p1))
                        total_score_p1 = sum(score_p1)
                        print('Player 1:',total_score_p1)
                        print('Player 2:',total_score_p2)
                        current_player=2
                        
                    else:
                        score_p2 = list(filter(None, marks_p2))
                        total_score_p2 = sum(score_p2)
                        print('Player 1:',total_score_p1)
                        print('Player 2:',total_score_p2)
                        current_player=1

                    second_roll = False
                        
                
        # cheat
        elif option.startswith('CHEAT'):
        
                num_list = [int(i) for i in option.split() if i.isdigit()] 
                countValue = len(num_list)

                # proceed only if there are 5 integers & each is in range from 1 to 4 & every element is integer
                if countValue==5 and check_num(num_list) and all(isinstance(num, int)for num in num_list):

                        if __name__ == "__main__":
        
                                S1 = 1*num_list.count(1)
                                S2 = 2*num_list.count(2)
                                S3 = 3*num_list.count(3)    
                                S4 = 4*num_list.count(4)
                                Trio = trio_cheat(num_list)
                                Band = band_cheat(num_list)
                                Quartet = quartet_cheat(num_list)
                                Doremi = doremi_cheat(num_list)
                                Orchestra = orchestra_cheat(num_list)


                                category = ["1S", "2S", "3S", "4S", "Trio", "Quartet", "Band", "Doremi", "Orchestra"];

                                # Scores organized in a list for each player, to be used for ShowTableByList()
                                scoreList = [
                                [S1, S2, S3, S4, Trio, Quartet, Band, Doremi, Orchestra], 
            
                                ];
                                
              
                                # Show table of Category Scores
                                ShowTableByList("Category Scores", [], category, scoreList);
    
                        if roll_time==3:  # Other option is chosen previously   
                                roll_time+=1
                                second_roll = True
                                cheat = True
                                continue
                        else:
                                roll_time+=2
                                second_roll = True
                                cheat = True
                                continue

                else:
                        print('ERROR: Invalid input.')
                        option = input('Input>')
                        option = option.upper()
                        second_roll = True
                        continue
                        
                                                        
        ## reroll all dice and reroll specific dice
        elif option.startswith('ROLL'):
        
                roll_value = option.split(' ')
                # reroll all dice
                if len(roll_value)==1:
            
                    diceValue = []
                    import random
                    for num in range(5):
                        num = random.randint(1,4)
                        diceValue.append(num)
                             
                    print(f"Roll #{roll_time} :", diceValue)
                    print("\n")
                        
                    if __name__ == "__main__":
        
                        S1 = 1*diceValue.count(1)
                        S2 = 2*diceValue.count(2)
                        S3 = 3*diceValue.count(3)    
                        S4 = 4*diceValue.count(4)
                        Trio = trio(diceValue)
                        Band = band(diceValue)
                        Quartet = quartet(diceValue)
                        Doremi = doremi(diceValue)
                        Orchestra = orchestra(diceValue)


                        category = ["1S", "2S", "3S", "4S", "Trio", "Quartet", "Band", "Doremi", "Orchestra"];

                        # Scores organized in a list for each player, to be used for ShowTableByList()
                        scoreList = [
                        [S1, S2, S3, S4, Trio, Quartet, Band, Doremi, Orchestra], 
            
                        ];
              
                        # Show table of Category Scores
                        ShowTableByList("Category Scores", [], category, scoreList);
                        
                    if roll_time<3: # if dice is rolled once
                        print("\nInput Options:")
                        print("  SAVE\t\t :- Accept these dice.")
                        print("  ROLL\t\t :- Re-roll ALL dice.")
                        print("  ROLL d1 ... dn :- Re-roll specified dice only.")
                        option = input('Input>')
                        option = option.upper()
                        roll_time+=1
                        second_roll = True
                        continue 
                        
                    else:   # if dice is rolled twice
                        roll_time+=1
                        second_roll = True
                        continue

                                                    
                
                # reroll specific dice                                                             
                else:
                        num_list = [int(i) for i in option.split() if i.isdigit()]
                    
                        # proceed only if each element is in range from 1 to 4 & every element is integer
                        if check_num(num_list) and all(isinstance(num, int)for num in num_list):
                
                                import random
                                for num in num_list:
                                    diceValue[num-1]= random.randint(1,4) # dice re-rolled according to numbering start from 1   
                                                                           
                                print(f"Roll #{roll_time} :", diceValue)
          
                                if __name__ == "__main__":
        
                                        S1 = 1*diceValue.count(1)
                                        S2 = 2*diceValue.count(2)
                                        S3 = 3*diceValue.count(3)    
                                        S4 = 4*diceValue.count(4)
                                        Trio = trio(diceValue)
                                        Band = band(diceValue)
                                        Quartet = quartet(diceValue)
                                        Doremi = doremi(diceValue)
                                        Orchestra = orchestra(diceValue)


                                        category = ["1S", "2S", "3S", "4S", "Trio", "Quartet", "Band", "Doremi", "Orchestra"];

                                        # Scores organized in a list for each player, to be used for ShowTableByList()
                                        scoreList = [
                                        [S1, S2, S3, S4, Trio, Quartet, Band, Doremi, Orchestra], 
            
                                        ];
              
                                        # Show table of Category Scores
                                        ShowTableByList("Category Scores", [], category, scoreList);

                                if roll_time<3: # if dice is rolled once
                                        print("\nInput Options:")
                                        print("  SAVE\t\t :- Accept these dice.")
                                        print("  ROLL\t\t :- Re-roll ALL dice.")
                                        print("  ROLL d1 ... dn :- Re-roll specified dice only.")
                                        option = input('Input>')
                                        option = option.upper()
                                        roll_time+=1
                                        second_roll = True
                                        continue

                                else:   # if dice is rolled twice
                                        roll_time+=1
                                        second_roll = True
                                        continue
                        
                        else: 
                                print('ERROR: Invalid input.')
                                option = input('Input>')
                                option = option.upper()
                                second_roll = True
                                continue
                    
        # Option is invalid                        
        else:
            print('ERROR: Invalid input.')
            option = input('Input>')
            option = option.upper()
            second_roll = True
            continue

# Final result after 9 rounds        
if total_score_p1>total_score_p2:
    print("\n"+"Player 1 wins!")

elif total_score_p2>total_score_p1:
    print("\n"+"Player 2 wins!")

else:
    print("It's a tie.")
                
####################################################
# Program: A01_LeeAnnThong.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: A01
# Year: 2019/20 Trimester 1
# Names: ADELINE_FONG_LI_LING | LEE_ANN_THONG
# IDs: 1191100708 | 1191100464
# Emails: 1191100708@student.mmu.edu.my | 1191100464@student.mmu.edu.my
# Phones: 019-2620596 | 016-8641624
####################################################

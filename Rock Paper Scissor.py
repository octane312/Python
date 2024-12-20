strt=input("Do you wanna start the game(Y/N) : ")
if(strt=='Y'):
    print("Let's dive into the game")
    p1_name=input("Enter player 1 name : ")
    p2_name=input("Enter player 2 name : ")
    p1_move=input("Choose Rock(R) Paper(P) or Scissor(S) %s : "%p1_name)
    p2_move=input("Choose Rock(R) Paper(P) or Scissor(S) %s : "%p2_name)
    if(p1_move=='R' and p2_move=='P'):
        print(p2_name,"won the game")
    elif(p1_move=='P' and p2_move=='R'):
        print(p1_name,"won the game")
    elif(p1_move=='S' and p2_move=='P'):
        print(p1_name,"won the game")
    elif(p1_move=='P' and p2_move=='S'):
        print(p2_name,"won the game")  
    elif(p1_move=='S' and p2_move=='R'):
        print(p2_name,"won the game")
    elif(p1_move=='R' and p2_move=='S'):
        print(p1_name,"won the game") 
    else:
        print("Its a draw")         
elif(strt=='N'):
    print("Thanks for visiting")
else:
    print("Invalid response")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
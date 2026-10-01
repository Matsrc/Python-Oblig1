import random 



print("I am thinking of a number between 1 and 100")

while True:
    # Genererer et nytt hemmelig tall for hvert spill
    hemmelig_tall = random.randint(1,100) 
    vunnet = False 
    
    # Gir brukeren 5 forsøk på å gjette det hemmelige tallet 
    for forsøk in range(1, 6): 
    
        # Fortsetter å spørre til brukeren skriver inn et gyldig tall 
        while True:
            svar = input("\nGuess my secret number: ") 
            
            if svar.isdigit(): 
                gjett_tall = int(svar)  

                if 1 <= gjett_tall <= 100:
                    break  
                else:
                    print("You need to enter a number between 1 and 100") 
            else:
                print("You need to enter a number")

        # Sjekker om gjetningen er riktig, for høy eller for lav 
        if gjett_tall == hemmelig_tall:  
            vunnet = True 
            print(f"Congratulations! You guessed the number in {forsøk} attempt(s).") 
            print(f"The correct number was {hemmelig_tall}") 
            break 

        elif gjett_tall > hemmelig_tall: 
            print("Your guess is too high") 
    
        else:
            print("Your guess is too low") 
        
        # Beregner hvor mange forsøk brukeren har igjen
        forsøk_igjen = 5 - forsøk 
        print(f"You have {forsøk_igjen} attempt(s) remaining.") 
    
    if vunnet == False:
        print("\nSorry! You did not manage to guess the number. You have reached the guessing limit.") 
        print(f"The correct number was {hemmelig_tall}.") 
            
    # Spør brukeren om de ønsker å spille igjen
    # Spør spiller om å skrive YES/NO igjen hvis de skriver noe annet.
    while True:
        spill_igjen = input("\nDo you want to play again? (YES/NO): ").upper()
        if spill_igjen == "YES":
            break
        elif spill_igjen == "NO":
            print("Thanks for playing!")
            break
        else:
            print("Please enter YES or NO") # Gir brukeren beskjed hvis de skriver noe annet enn YES eller NO

# la til denne her, bare å fjerne om du føler det er unødvendig 

    

if spill_igjen == "YES":
        continue
    else:
        break

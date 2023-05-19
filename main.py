def match_results():
    while True:
        
        try: 
            rounds = int(input("Hány forduló volt?"))
            if rounds > 0:
                break
            else:
                pass
        except:
            print("Invalid character")
            
    results = {}
    final_list = []
    win_difference_list = []
    task_6 = 0
    loss = 0 
    win = 0
    draw = 0
    
    for n in range(rounds):
        
        falabuak_goals = int(input("Hány gólt löttek a falábúak?"))
        enemy_goals = int(input("Hány gólt lött az ellenfél?"))
        results.update({falabuak_goals:enemy_goals})
 
    for fal_goals,en_goals in results.items():
        result = fal_goals - en_goals
        if result > 0: 
            try:
                if result > win_difference_list[-1]:
                    task_6 += 1 
                else:
                    pass
            except:
                pass
            win_difference_list.append(result)
                    
        if result > 0 :
            win += 1
        elif result < 0:
            loss += 1
        else:
            draw += 1
            
        result_strg = f"Falábúak - ellenfél: {fal_goals} - {en_goals} Gólkülönbség : {result}"
        final_list.append(result_strg)

    print("A meccsek eredményei és gólkülönbségei:")
    
    for item in final_list:
        print(item)   
    print(f"Csapatstatisztikák: \n Lejátszott meccsek:{rounds} \n Gyözelem:{win},\n Döntetlen:{draw} \n Vereség: {loss}")
    
    points = win*3 + draw*1
    print(f"A falábúak szezonban elért pontjai: {points} ")
    
    if win > loss + draw:
        print("A  csapatnak több győztes mérkőzése volt, mint veresége és döntelene együttvéve.")  
    else:
        print("A  csapatnak kevesebb győztes mérkőzése volt, mint veresége és döntelene együttvéve.")
        
    print(f"A kitüzött célt a csapatnak {task_6} alkalommal sikerült elérnie")       
match_results()    

""" Olvassa be a jel.txt állomány tartalmát, tárolja el a rögzített jelek adatait, és azok 
felhasználásával oldja meg a következő feladatokat! """


jel_data = []
jel_data_dict = {}
with open("jel.txt", "r") as jel:
    for n in jel:
        jel_data.append(n.strip())

"""Indexing for finding elements of dictionary values """  

hour = 0
minute = 1
second = 2
x = 3
y = 4

""" Enumerating(indexing all iterables starting from nr.1, this value will be the key of the dictionary element, and the value 
    will be a list of the numbers given in the original text file, line by line. """
for n, item in enumerate(jel_data, start=1):
    jel_data_dict[n] = item.split(" ")
    
    
""" Excercise 2: Kérje be a felhasználótól egy jel sorszámát (a sorszámozás 1-től indul), és írja a képernyőre 
az adott jeladáshoz tartozó x és y koordinátát! """

user_input = int(input("Add meg a koordináta sorszámát:"))

print(f"A megadott sorszám: {user_input}, a hozzá tartozó koordináták : x={jel_data_dict[user_input][x]} y={jel_data_dict[user_input][y]}")

"""3. Készítsen függvényt eltelt néven, amely megadja, hogy a paraméterként átadott két 
időpont között hány másodperc telik el! A két időpontot, mint paramétert tetszőleges módon 
átadhatja. Használhat három-három számértéket, két tömböt vagy listát, de más, a célnak 
megfelelő típusú változót is. Ezt a függvényt később használja fel legalább egy feladat 
megoldása során!"""
from datetime import timedelta


def eltelt(time1_id, time2_id):
    """ Creating time variables for the delta function from the dictionary values. time1_id is the key, from the func argument, hour-minuts is just the
    index variable above """
    
    t1_hour = jel_data_dict[time1_id][hour]
    t1_minute = jel_data_dict[time1_id][minute]
    t1_second = jel_data_dict[time1_id][second]
    t2_hour = jel_data_dict[time2_id][hour]
    t2_minute = jel_data_dict[time2_id][minute]
    t2_second = jel_data_dict[time2_id][second]
    
    time1 = timedelta(hours=int(t1_hour), minutes=int(t1_minute), seconds=int(t1_second))
    time2 = timedelta(hours=int(t2_hour), minutes=int(t2_minute), seconds=int(t2_second))
    
    delta = time2 - time1
    
    return f"A két idöpont között eltelt idö : {delta}"

length = len(jel_data_dict)  
print(eltelt(1,length))


"""Határozza meg azt a legkisebb, a koordináta-rendszer tengelyeivel párhuzamos oldalú 
téglalapot, amelyből nem lépett ki a jeladó! Adja meg a téglalap bal alsó és jobb felső 
sarkának koordinátáit! """

""" Puffer lists for min-max func"""
min_x = []
min_y = []
max_x = []
max_y = []

""" Inserting all the data from the dictionary to the coordinates list """
for n in range(1, length):
    min_x.append(int(jel_data_dict[n][x]))
    min_y.append(int(jel_data_dict[n][y]))
    max_x.append(int(jel_data_dict[n][x]))
    max_y.append(int(jel_data_dict[n][y]))
    
""" Getting min-max values for all coordinates """
    
min_xx = min(min_x)
min_yy = min(min_y)
max_xx = max(max_x)
max_yy = max(max_y)

print("Bal alsó: "min_xx, min_yy," Jobb felsö:", max_xx, max_yy)

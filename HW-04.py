import csv

def hashFunction(name):
    sum_of_chars = 0
    for char in name:
        sum_of_chars += 1

    return sum_of_chars
    
    
def titleTable():
    
    table = []
    empty = 0
    collisions = 0
    
    with open("MOCK_DATA.csv", mode="r", newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for line in file:
            title = line.split(",")[0]
            
            index = hashFunction(title)
            table[index].append(line)
            
            
            
            
                    

def quoteTable():
    
    table = []
    
    with open("MOCK_DATA.csv", mode="r", newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for line in file:
            title = line.split(",")[8]
            
            searching = True
            i = 0
            collisions = 0
            
            while(searching):
                if(table[i] == None):
                    table[i] = line
                    searching = False
                else:
                    collisions+=1
                    
        empty = 0
        for item in table:
            if(table[i] == None):
                empty +=1
                
        print("Title: \n")
        print(f"Collisions: {collisions} \n")
        print(f"Empty Space: {empty}\n")            
            
    
    

    
titleTable()
quoteTable()
import csv
import time

def hashFunction(name):
    name = name.strip()
    num = 0
    for char in name:
        num+=ord(char)
    return num % 10
    
    
def titleTable():

    empty = 0
    collisions = 0
    start = time.perf_counter()
    
    with open("MOCK_DATA.csv", mode="r", newline='', encoding="utf-8") as file:
        length = sum(1 for line in file)
        table = [None]*length
        
        file.seek(0)
        for line in file:
            title = line.split(",")[0]
            index = hashFunction(title)
            if (table[index] == None):
                table[index] = line
            else:
                searching = True
                while(searching):
                    index+=1
                    collisions +=1
                    if (table[index] == None):
                        table[index] = line
                        searching = False
        
        end = time.perf_counter()
        
        timer = end - start
           
        for item in table:
            if(item is None):
                empty +=1
                
        print(f"\n Title Key: \n Collisions: {collisions} \n Empty: {empty}\n Time: {timer}\n")
            
            
            
            
                    

def quoteTable():

    empty = 0
    collisions = 0
    start = time.perf_counter()
    
    with open("MOCK_DATA.csv", mode="r", newline='', encoding="utf-8") as file:
        
        length = sum(1 for line in file)
        table = [None]*length
        
        file.seek(0)
        for line in file:
            title = line.split(",")[8]
            index = hashFunction(title)
            if (table[index] == None):
                table[index] = line
            else:
                searching = True
                while(searching):
                    index+=1
                    collisions +=1
                    if (table[index] == None):
                        table[index] = line
                        searching = False
        
        end = time.perf_counter()
        
        timer = end - start
           
        for item in table:
            if(item is None):
                empty +=1
                
        print(f"\n Quote Key: \n Collisions: {collisions} \n Empty: {empty}\n Time: {timer}\n")
    


print("hash key 2:")
titleTable()
quoteTable()
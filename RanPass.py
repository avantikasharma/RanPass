import random

def randomisation(): 
    small = int(input("Number of small alphabets: "))
    big = int(input("Number of capital letters: "))
    nums = int(input("Number of numerics: "))
    sp = int(input("Number of special characters: "))
    

    ranpass = []
    spchar = []    
    smallalpha = []
    bigalpha = []
    numbers = []
    
    # making a list of all special characters
    for i in range(33,48):
        spchar.append(chr(i))
    for i in range(58,65):
        spchar.append(chr(i)) 
    for i in range(91,97): 
        spchar.append(chr(i)) 
    for i in range(123,127):
        spchar.append(chr(i)) 


    # making a list of all small alphabets
    for i in range(97,123):
        smallalpha.append(chr(i)) 
    print(smallalpha)

    # making a list of all numbers
    for i in range(48,58):
        numbers.append(chr(i))

    # making a list of all capital letters
    for i in range(65,91):
        bigalpha.append(chr(i))

    # sm_alpha, caps, number and specialchar will contain the randomly selected values

    sm_alpha = []
    for j in range(small):
        sm_alpha.append(random.choice(smallalpha))
     
    caps = []
    for k in range(big):
        caps.append(random.choice(bigalpha))

    number = []
    for l in range(nums):
        number.append(random.choice(numbers))

    specialchar = []
    for m in range(sp):
        specialchar.append(random.choice(spchar))

    
    #Randomly generated password contained in ranpass as a list
    ranpass = []        
    ranpass = sm_alpha + caps + number + specialchar
    random.shuffle(ranpass) 

    pw = ""
    print(pw.join(ranpass))
    

randomisation()


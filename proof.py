import random

n = 100000 # number of times to run the estimation

woncar = 0

for i in range(n):
    doors = [1,2,3]
    car = random.randint(1,3)
    choice = random.randint(1,3)

    doors.remove(car) # remove for now to choose which one reveal
    if(choice in doors):
        doors.remove(choice) # dont reveal the choice
    reveal = random.sample(doors,1)[0]

    '''
        Here is where you find the proof...
        In the following we check if our other option which is != choice is the same as car. 
        Since the other non car options has been removed we only need to check if choice!=car
        You can notice that we dont need lines 12-15 
        This is too obvious that the chance is 66% not 50%.
    '''
    if(choice != car):
        woncar += 1
    
    print("Chance that you win a car if you switch:", woncar/(i+1))
    
    
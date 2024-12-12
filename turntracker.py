# Python Turn Tracker
# By Ada

from operator import attrgetter

usersList = []

class Player:
    def __init__(self, name, initiative):
        self.name = name
        self.initiative = initiative
        self.turn = ''
    def __str__(self):
        return f'{self.name}: {self.initiative}'
    def __repr__(self):
        return repr((self.name, self.initiative))

def showMenu():
    print('1. Add User')
    print('2. Add Users from file')
    print('3. Delete User')
    print('4. Clear Initiative')
    print('5. Set Initiative')
    print('6. Track Initiative')
    print('Q to Quit')

def addUser():
    name = input('Name: ')
    user = Player(name, 0)
    usersList.append(user)

def addUserFromFile():
    with open('users.txt') as f:
        read_data = f.read().splitlines()
    for line in read_data:
        entry = line.split()
        user = Player(entry[0], int(entry[1]))
        usersList.append(user)
    print(usersList)

def deleteUser():
    print(str(usersList))
    choice = input('Choose a user from list: ')
    for user in usersList:
        if user.name == choice:
            usersList.remove(user)

def clearInitiative():
    for user in usersList:
        user.initiative = 0

def setInitiative():
    print(str(usersList))
    choice = input('Choose a user from list: ')
    for user in usersList:
        if user.name == choice:
            user.initiative = int(input('Input initiative: '))

def listPlayersSorted():
    return sorted(usersList, key=attrgetter('initiative'), reverse=True)

def trackInitiative():
    sortedList = listPlayersSorted()
    i = 0
    length = len(sortedList)
    while(True):
        if i < length:
            sortedList[i].turn = '*'
            for user in sortedList:
                print(f'{user.initiative} {user.name} {user.turn}')
            sortedList[i].turn = ''
            i += 1
            if(input('Press Enter for next turn, press Q to end tracking: ').upper() == 'Q'):
                print('Ending Tracking...')
                break
        else:
            i = 0
            

while(True):
    showMenu()
    choice = input('Enter your choice: ')

    if choice == '1':
        addUser()
    elif choice == '2':
        addUserFromFile()
    elif choice == '3':
        deleteUser()
    elif choice == '4':
        clearInitiative()
    elif choice == '5':
        setInitiative()
    elif choice == '6':
        trackInitiative()
    elif choice.upper() == 'Q':
        print('Exiting...')
        break
    else:
        print('Incorrect Input')
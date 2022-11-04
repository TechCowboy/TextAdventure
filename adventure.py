import re

global inventory
global dropped_inventory
global x
global y
x = 0
y = 0
inventory = []
dropped_inventory = [['sign', 0, 0],
                     ['tree', 1, 0],
                     ['carpet',  0, 1],
                     ['house', 1,1]]
                     

def adventure_v1(command):
    global inventory
    global dropped_inventory
    global x
    global y
    
    command = command.lower()
    result = re.split(r' |,', command)
    #print(result)
    match result:
        case ['quit']:
            print("See ya!")
            exit(0)
        case [('read' | 'examine'), *things]:
            print(things)
                
            sign_here = False
            for item, x1, y1 in dropped_inventory:
                if x == x1 and y == y1 and item=='sign':
                    sign_here = True
            
            if 'sign' in inventory:
                sign_here = True
                    
            if sign_here:
                if 'sign' in inventory:
                    print('You look at your inventory and find a sign.  It says:')
                else:
                    print('Looking around you see a sign.  It says:')
                print('You can pick up anything you can imagine.')
            else:
                if things == []:
                    print("What do you want to do that to?")
        case ['get', *things]:
            for item in things:
                if item in ['', 'the', 'and', '&']:
                    continue
                
                print(f"You pick up the {item}")
                inventory.append(item)
                
            
                for ditem, x1, y1 in dropped_inventory:
                    if ditem == item:
                        dropped_inventory.remove([item,x1,y1])
                        
        case ['drop', *things]:
            if things == ['all']:
                things = inventory
                
            for item in things:
                if item in inventory:
                    print(f"{item} is now on the ground")
                    inventory.remove(item)
                    dropped_inventory.append([item, x, y])
                else:
                    print(f"You don't have a {item}")
            # code to remove files
        case ['inv']:
            print(f"You have in your inventory: ")
            stuff = False
            for item in inventory:
                stuff = True
                print(f"{item}")
                
            if not stuff:
                print("Nothing")
        case ['north' | 'n']:
            print("You move north")
            y = y + 1
        case ['south' | 's']:
            print('You move south')
            y = y - 1
        case ['east' | 'e']:
            print('You move east')
            x = x - 1
        case ['west' | 'w']:
            print('You move west')
            x = x + 1
        case other:
            print('Huh? I don''t understand.')
    
    stuff = False
    for item,x1,y1 in dropped_inventory:
        if x == x1 and y == y1:
            print(f"you see a {item} on the ground")
            stuff = True
            
    if x == 0 and y == 0:
        print("You're at the starting point")
    else:
        if stuff == False:
            print("There's nothing to see here")
        
print("Norman's Simple Adventure")
print("Commands")
print("\tlook")
print("\tget <item>")
print("\tdrop <item> or all")
print("\tinv")
print("\tquit")


while True:
    command = input(">")

    adventure_v1(command)
    
print("Stopped.")


    
'''
Although a terrible example of general programming
it does show how to use the case-match statement
'''

import re


class adventure:
    def __init__(self):
        self.inventory = []
        self.dropped_inventory  = [
                     ['sign',    0, 0],
                     ['tree',    1, 0],
                     ['carpet',  0, 1],
                     ['house',   1, 1]
                     ]
        self.x = 0;
        self.y = 0;

    def parse_command(self, command):
        
        command = command.lower()
        result = re.split(r' |,', command)
        #print(result)
        match result:
            # single keyword match
            case ['quit']:
                print("See ya!")
                return False
            # display the commands available
            case ['help']:
                self.help()
            case ['look']:
                pass
                
            # multiple keyword match, with arguments
            case [('read' | 'examine'), *things]:
                print(things)
                    
                sign_here = False
                for item, x1, y1 in self.dropped_inventory:
                    if self.x == x1 and self.y == y1 and item=='sign':
                        sign_here = True
                
                if 'sign' in self.inventory:
                    sign_here = True
                        
                if sign_here:
                    if 'sign' in self.inventory:
                        print('You look at your inventory and find a sign.  It says:')
                    else:
                        print('Looking around you see a sign.  It says:')
                    print('You can pick up anything you can imagine.')
                else:
                    if things == []:
                        print("What do you want to do that to?")
            # single keyword match, with arguments
            case ['get', *things]:
                for item in things:
                    if item in ['', 'the', 'and', '&']:
                        continue
                    
                    print(f"You pick up the {item}")
                    self.inventory.append(item)
                    
                
                    for ditem, x1, y1 in self.dropped_inventory:
                        if ditem == item:
                            self.dropped_inventory.remove([item,x1,y1])
                            
            case ['drop', *things]:
                # if argument is simply 'all'
                if things == ['all']:
                    # make everything in our inventory
                    # an item to drop
                    things = self.inventory
                    
                for item in things:
                    if item in self.inventory:
                        print(f"{item} is now on the ground")
                        self.inventory.remove(item)
                        self.dropped_inventory.append([item, self.x, self.y])
                    else:
                        print(f"You don't have a {item}")
                # code to remove files
            case ['inv']:
                print(f"You have in your inventory: ")
                if self.inventory != []:
                    for item in inventory:
                        print(f"{item}")
                else:
                    print("Nothing")
            # multiple keyword match
            case ['north' | 'n']:
                print("You move north")
                self.y = self.y + 1
            case ['south' | 's']:
                print('You move south')
                self.y = self.y - 1
            case ['east' | 'e']:
                print('You move east')
                self.x = self.x - 1
            case ['west' | 'w']:
                print('You move west')
                self.x = self.x + 1
            case other:
                print('Huh? I don''t understand.')
        
        # is there anything to that has been dropped here?
        stuff = False
        for item,x1,y1 in self.dropped_inventory:
            if self.x == x1 and self.y == y1:
                print(f"you see a {item} on the ground")
                stuff = True
        
        # special case - print a message if we're back to where we started
        if self.x == 0 and self.y == 0:
            print("You're at the starting point")
        
        if stuff == False:
            print("There's nothing to see here")
                
        return True

    def help(self):
        print("Norman's Simple Adventure")
        print("Commands:")
        print("\tlook")
        print("\tget <item>")
        print("\tdrop <item> or all")
        print("\tinv")
        print("\tquit")
        print("\tNorth, South, East, West")

def main():
    
    a = adventure()
    a.help()
    again = True

    while again:
        command = input(">")

        again = a.parse_command(command)

if __name__ == "__main__":

    main()
    print("Stopped.")


    
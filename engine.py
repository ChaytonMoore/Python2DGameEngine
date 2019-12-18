#Actually this will be entirely 2D
class scene():#Nothing can happen in a scene it just contains a description
    desc = "This is a place."

class level():#Gameplay can actually happen here 
    objs = []
    actors = []
    charcters = [] #Should only call charcters here.
    
    def __init__(self, objs,actors,characters):

class controller(): #Thing that controlls the player character
    inuse = False
    inbuiltcommands = []

class character():#This should be something for the player to interract with in someway.
    name = ""
    attribs = []
    stat = []
    location = [0,0]
    DlgFile = ""
    base = "" #Which actor it by default inherits 
    
class actor():
    hidden = False
    faction = ""
    sympathies = []
    
    
    
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Dina = Character("Dina", color="#1b221b", image="dina_bored")
define Betty = Character("Betty", color="#4c5e00", image="betty_scared")
define Buddy = Character("Buddy", color="#00256b",  image="buddy_confident")
define Player = Character("Player", color="#3d009e")
define Coach = Character("Coach", color="#360000", image="coach")
define Teacher = Character("Teacher", color="#2b1c00", image="teacher")

default Dina_skill = 3
default Betty_skill = 1
default Buddy_skill = 0
default Player_skill = 0

default mood = 2
default moods = ["exhausted", "tired", "fine", "relaxed", "happy"]

default horror = False
default performance = 0

default Betty_ready = False
default Betty_hiding = True
default Buddy_ready = False 
default Buddy_dumb_idea = False
default Dina_ready = False
default Dina_date = False
default Buddy_hospital = False

# The game starts here.

label start:
    jump day1_bedroom





















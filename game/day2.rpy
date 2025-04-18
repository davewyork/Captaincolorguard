label day2_bedroom:
    scene home
    with dissolve
    "You wake up in your bed, ready to start the day."
    "You have some breakfast and then head to school."
    jump day2_class

label day2_class:
    scene school
    with dissolve
    "You arrive at school and head to class."
    show teacher at left
    Teacher "Mitocondria is the powerhouse of the cell."
    hide teacher
    "Class is boring, but you manage to get through it."
    jump day2_after_class
      
label day2_after_class:
    scene school
    with dissolve
    "You finish with class and head to practice."
    jump day2_practice

label day2_practice:
    scene gym
    with dissolve
    "You arrive at the practice field, ready to meet your team."
    show coach at left
    Coach "Buddy had to miss practice today. Because he has roof or something..."
    if (Dina_date == True):
        "and I don't even know where Dina is."
    hide coach
    "You could help one of your teammates, or just practice on your own."    
    # The player can choose to talk to Dina, Betty, or Buddy.
    menu:
        "Talk to Dina" if (Dina_date == False):
            jump day2_talk_dina
        "Talk to Betty":
            jump day2_talk_betty
        "Just focus on practice":
            jump day2_practice_makes_perfect
    jump day2_home

label day2_talk_dina:
    scene gym
    with dissolve
    show dina_bored at right
    "You approach Dina"
    "Her eyes look glazed over."
    Dina "Hey."
    "She seems distracted."
    menu:
        "Hey, Dina. How's it going?":
            hide dina_bored
            show dina_ready at right
            "You ask her about her day."
            "She seems a little more engaged."
            "Dina Skill +1"
            $ Dina_skill += 1
            $ Dina_ready = True
        "Hey, Dina. Do you want to practice together?":
            "You ask her to practice with you."
            "She seems very bored. But you still learn from watching her."
            $ Player_skill += 1
            "Skill +1"                
    hide dina_bored
    hide dina_ready    
    "You head home."
    jump day2_home

label day2_talk_betty:
    scene gym
    with dissolve
    show betty_scared at right
    "You find Betty, she looks nervous."
    "When you look closer, you see she's doing something weird her grip."
    menu:
        "Hey Betty, why are holding your flag weird?":
            "You adjust betty's grip on her flag."
            "She seems grateful for your help, but also shaken."
            "Betty Skill +1"
            $ Betty_skill += 1
        "Hey Betty I have an idea that might help you.":
            "You help Betty with her grip."
            "She seems grateful for your help."
            "Betty Skill +1"
            $ Betty_skill += 1
    hide betty_scared
    "You head home."
    jump day2_home
        
label day2_home:
    scene home
    with dissolve
    "You arrive home after a long day of practice."
    "You feel tired but accomplished."
    menu:
        "Practice more":
            jump day2_practice_at_home
        "Scroll through TikTok on your phone":
            jump day2_cellphone

label day2_cellphone:
    "You spend some time scrolling on your phone." 
    "Mood + 2" 
    $ mood += 2
    if mood > 4:
        $ mood = 4  
    jump day2_dinner

label day2_practice_at_home:
    "You practice in yard for a while."
    "Skill + 1"
    $ Player_skill += 1
    jump day2_dinner

label day2_dinner:
    scene home night    
    "You grab some dinner and head to bed."
    jump day2_sleep   

label day2_sleep:
    scene home night
    with dissolve
    "You close your eyes and drift off to sleep."
    jump day3_bedroom
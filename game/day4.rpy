

label day4_bedroom:
    scene home
    with dissolve
    "You wake up in your bed, ready to start the day."
    "You have some breakfast and then head to the big event."
    jump day4_event_start

label day4_event_start:
    scene big_event
    with dissolve
    "You arrive at the practice field, ready to meet your team."
    if(Dina_date == True):
        "You see Betty and Buddy warming up. No sign of Dina."
        Coach "Dina is out today. Don't know why. You'll have to do without her."
    else:
        "You see Dina, Betty, and Buddy warming up."
    "You can tell they are a bit nervous."
    "You watch the other teams perform."
    "Some of them are pretty good."
    "Others are not so good."
    jump day4_event_go

label day4_event_go:
    "Its your team's turn to perform."
    if(Dina_date == True):
        "Dina's absence is noticeable."
    else:
        if(Dina_skill >= 3):
            "Dina is enthusiastic."
            "Performance + 2"
            "The crowd wakes up a little."
            $ performance += 2
        else:
            "Dina looks unfocused. She doesn't make any mistakes..."
            "But she doesn't really shine either."
            "Performance + 1"
            $ performance += 1
    
    if(Betty_skill >= 2 and Betty_hiding == False):
        "Betty is ready and focused. She tosses and twirls the flags with confidence and skill."
        "Performance + 2"
        $ performance += 1

    if(Buddy_skill >= 2 and Buddy_dumb_idea == False):
        "Buddy is ready and focused. He twirls the flag with confidence and skill."
        "Performance + 1"
        $ performance += 1
    elif(Buddy_skill < 2 and Buddy_dumb_idea == True):
        scene black
        "And then it all goes terribly wrong."
        show flag_toss
        "He begins a move you have never seen before."
        "Almost in slow motion, you see him launch his flag into the air... and lose track of it."
        show flag_tossed
        "He then spins in place, and looks up to catch it."
        "..."
        show flag_hit
        "But it is too late. The flag lands squarely in his chest, impaling him."
        "The crowd is silent."
        "Performace - 5"
        $ Buddy_hospital = True
        jump day4_event_horror
    else:
        "Buddy is not ready. His confidence disappears immediately on the floor. He tries to keep up with even the most basic moves, but fails."
        "He drops his flag."
        "Performance + 0"

    "You throw yourself into the performance, showing off your skills."
    $ performance += Player_skill
    "Performance + [Player_skill]"


    if(performance > 6):
        jump day4_event_great
    elif(performance < 6 and performance > 2):
        jump day4_event_mid
    else:
        jump day4_event_bad


label day4_event_horror:    
    "The event ends with police and an ambulance."
    jump final_score

label day4_event_mid:
    "The event ends with a mediocre performance."
    "You feel like you could have done better."
    "You head home feeling a bit disappointed."    
    jump final_score   

label day4_event_great:    
    "The event ends with a great performance."
    "You feel proud of yourself and your team."
    "You head home feeling accomplished."
    jump final_score  
    
label day4_event_bad:
    "The event ends with a terrible performance."
    "You feel embarrassed and ashamed."
    "You head home feeling defeated."
    jump final_score


label final_score:
    "Your final score is [performance]."
    "You feel [moods[mood]]."
    return
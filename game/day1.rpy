label day1_bedroom:
    scene home
    with dissolve
    "You wake up in your bed, ready to start the day."
    "You have some breakfast and then head to school."
    jump day1_class

label day1_class:
    scene school
    with dissolve
    "You arrive at school and head to class."
    show teacher at left
    Teacher "A squared plus B squared equals C squared."
    hide teacher
    "You try to pay attention, but your mind wanders."
    jump day1_after_class
      
label day1_after_class:
    scene school
    with dissolve
    "You finish with class and head to practice."
    jump day1_practice

label day1_practice:
    scene gym
    with dissolve
    "You arrive at the practice field."
    show coach at left
    Coach "Alright team, we have a big event coming up. I want you all to practice hard."
    Coach "Remember, teamwork is key! Let's make sure we all work together."
    Coach "Betty is out sick today."
    hide coach    
    "You could help one of your teammates, or just practice on your own."
    # The player can choose to talk to Dina, Betty, or Buddy.
    menu:
        "Talk to Dina":
            jump day1_talk_dina
        "Talk to Buddy":
            jump day1_talk_buddy
        "Just focus on practice":
            jump day1_practice_makes_perfect
    jump day1_home

label day1_practice_makes_perfect:
    scene gym
    with dissolve
    "You work hard and feel like you've improved."
    "Skill + 1"
    $ Player_skill += 1
    jump day1_home

label day1_talk_dina:
    scene gym
    with dissolve
    show dina_bored at right
    "You approach Dina"
    "She lets out a big sigh. Her twirls look perfect, effortless."
    "She's not even paying attention."
    Player "Hey, Dina. How's it going?"
    Dina "Oh, hey. Did you hear about the new transfer student?"
    menu:
        "Not much. What about him?":
            Dina "I don't know... there's just something about him. He's mysterious."
        "The pasty pale guy? The who stares straight ahead with his eyes all the way open?":
            Dina "He's not that bad. I mean, maybe he just needs someone to talk to."
    menu:
        "Maybe you should ask him out.":
            Dina "What? You think so..."
            hide dina_bored
            show dina_ready at right
            "She blushes and changes the subject to training."
            $ Dina_skill += 1
            $ Player_skill += 1
            $ Dina_date = True
            "You learn from watching her."
            "Skill +1"
            "Dina Skill +1"
        "Maybe you should ask him out...after the big event. In case he murders you.":
            Dina "Haha, very funny."
            "She changes the topic to training."
            $ Dina_skill += 1
            $ Player_skill += 1
            "You learn from watching her."
            "Skill +1"
            "Dina Skill +1"            
        "Dina. Maybe you should ask out a normal person.":
            "She narrows her eyes and walks off."
    hide dina_ready
    hide dina_bored
    "You head home."
    jump day1_home

label day1_talk_buddy:
    scene gym
    with dissolve
    show buddy_confident at right    
    "You approach Buddy, the arrogant slacker."
    Buddy "Hey, you ready for the big event?"
    "He smiles stupidly."
    menu: 
        "Yes":
            Buddy "You better be. I don't want to have to carry the whole team on my back."
        "No":
            hide buddy_confident
            show buddy_stupid at right
            Buddy "Well, you better get ready. Here watch this. I'll teach you something you haven't seen before."
            "Buddy shows you a move you have never seen before. The flag hits him in the face."
            "After watching him, you think you might have unlearned how to twirl."
            $ Player_skill -= 1
            "Skill - 1"
    "You try to help buddy. But he clearly doesn't practice and he also doesn't listen."
    $ Buddy_skill += 1
    "Buddy Skill +1"
    "Mood - 1" 
    $ mood -= 1
    if mood < 0:
        $ mood = 0     
    hide buddy_stupid
    hide buddy_confident
    "You head home."
    jump day1_home

label day1_home:
    scene home
    with dissolve
    "You arrive home after a long day of practice."
    "You feel tired but accomplished."
    menu:
        "Practice more":
            jump day1_practice_at_home
        "Scroll through TikTok on your phone":
            jump day1_cellphone

label day1_cellphone:
    "You spend some time scrolling on your phone."
    "You see a video of someone falling off a skateboard and down some stairs." 
    "Mood + 1" 
    $ mood += 1
    if mood > 4:
        $ mood = 4  
    jump day1_dinner

label day1_practice_at_home:
    "You practice in yard for a while. You hear your neighbor yelling at a squirrel."
    "Skill + 1"
    $ Player_skill += 1
    jump day1_dinner

label day1_dinner:
    scene home night    
    "You grab some dinner and head to bed."
    jump day1_sleep    

label day1_sleep:
    with dissolve
    "You close your eyes and drift off to sleep."
    jump day2_bedroom
label day3_bedroom:
    scene home
    with dissolve
    "You wake up in your bed, ready to start the day."
    "You have some breakfast and then head to school."
    jump day3_class

label day3_class:
    scene school
    with dissolve
    "You arrive at school and head to class."
    show teacher at left
    Teacher "Semicolons are used to join two independent clauses that are related but not directly linked by a coordinating conjunction like 'and' or 'but'."
    scene black
    Teacher "Hey, wake up." 
    "You wake back up."
    Teacher "You need to pay attention. This is going to be on the test!"
    "You nod and try to focus."
    hide teacher
    jump day3_after_class
      
label day3_after_class:
    scene school
    with dissolve
    "You finish with class and head to practice."
    jump day3_practice

label day3_practice:
    scene gym
    with dissolve
    "You arrive at the practice field, ready to meet your team."
    show coach at left
    Coach "Dina is out today. She has a family emergency."
    Coach "Has anyone seen Betty?"
    hide coach 
    "You could help one of your teammates, or just practice on your own."    
    # The player can choose to talk to Dina, Betty, or Buddy.
    menu:
        "Go look for Betty":
            jump day3_talk_betty
        "Talk to Buddy":
            jump day3_talk_buddy
        "Just focus on practice":
            jump day3_practice_makes_perfect
    jump day3_home

label day3_practice_makes_perfect:
    scene gym
    with dissolve
    "You work hard and feel like you've improved."
    "Skill + 1"
    $ Player_skill += 1
    jump day3_home

label day3_talk_betty:
    scene school
    with dissolve
    "You take a quick look around for Betty." 
    "As you pass the lockers, you hear something from a locker."
    "You open the locker and find Betty hiding inside." 
    show betty_hiding at right
    Betty "Just leave me. I don't want to practice today."
    Player "You need to practice. We have a big event coming up."
    "She stares away blankly."
    "You realize that betty is nervous about the upcoming event."
    menu:
        "Betty, what's the worst that could happen? Don't be afraid. It's just a flag routine, no one's going to remember it.":
            Betty "The worst that could happen... We could embarass ourselves in front of the whole school."
            "Her eyes widen. She curls up into a ball."
            "You are unable to convince her to come out."
        "Betty, you need to practice. You're very good and we need you out there with us.":
            hide betty_hiding
            show betty_ready at right
            Betty "I guess you're right."
            Betty "I'll join you all in a few minutes."
            Player "The other schools aren't perfect either. Let's just have fun."
            Betty "Thanks for being so nice."
            "She seems a little more relaxed."
            $ Betty_skill += 1
            $ Betty_ready = True
            $ Betty_hiding = False
    hide betty_ready
    hide betty_hiding
    "You head home."    
    jump day3_home

label day3_talk_buddy:
    scene gym 
    with dissolve
    show buddy_confident at right
    "You approach Buddy."
    "He seems to be in a good mood."
    "The flag flies out of his hand, smacking into your leg."
    Buddy "That never happens, you probably distracted me."
    "He picks up the flag."
    "You have a moment to coach him, if you feel like it."
    menu:
        "Buddy, you need to practice more. Don't do any of those stupid moves, just focus on the basics.":
            Buddy "You're not the coach. I can do whatever I want."
        "*Grab Buddy by the Shirt* Buddy, if you drop the flag again, I'm going drop kick you into the next world.":
            hide buddy_confident
            show buddy_serious
            Buddy "Whoa, chill out. I was just trying to have some fun."
            "You grab him by the shirt and shake him a little."
            "He looks a little scared."
            "Buddy Skill +1"
            $ Buddy_skill += 1
        "Buddy, you're the real talent. People don't realize it, but you're carrying the team. You need to stop playing things so safe and take some risks.":
            hide buddy_confident
            show buddy_stupid
            Player "That move you did yesterday was super cool. I'm pretty sure the whole school will be talking about it if you just throw it a little higher and spin a little more."
            Buddy "You think so?"
            Player "Uh, yeah."
            $ Buddy_dumb_idea = True
    hide buddy_serious
    hide buddy_confident
    hide buddy_stupid
    "You head home."
    jump day3_home
        
label day3_home:
    scene home
    with dissolve
    "You arrive home after a long day of practice."
    "You feel tired but accomplished."
    menu:
        "Practice more":
            jump day3_practice_at_home
        "Scroll through TikTok on your phone":
            jump day3_cellphone

label day3_cellphone:
    "You spend some time scrolling on your phone." 
    "You see a video of huskies howling and woofing at their owner."
    "Mood + 1" 
    $ mood += 1
    if mood > 4:
        $ mood = 4  
    jump day3_dinner

label day3_practice_at_home:
    "You practice in yard for a while."
    "You see your neighbor running from some squirrels."
    "Skill + 1"
    $ Player_skill += 1
    jump day3_dinner

label day3_dinner:
    scene home night    
    "You grab some dinner and head to bed."
    jump day3_sleep   

label day3_sleep:
    scene home night
    with dissolve
    "You close your eyes and drift off to sleep."
    jump day4_bedroom
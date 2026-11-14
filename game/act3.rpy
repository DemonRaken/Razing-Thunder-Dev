label act3:

scene placeholder_paddock
with fade
tl "Razing Thunder Derby.\n Paddock. \n Evening."
tt "Running at full speed, the gathering crowd immediately gets my attention. Following their gaze, I move past people to see what's got their attention…"

tt "...and in that moment, the sense of dread that had been building up in my chest as I rushed over washes away, overcome by anger and disbelief."

#Insert here CG of Vicente dead on the ground.
scene placeholder_bodycg
with dissolve

tt "On the ground of the parade ring area lay the body of Vicente Ruiz, whom I had just spoken with not long ago, blood seeping from his head."

t "What the hell…!?"

tt "I quickly glance around my immediate surroundings, searching for anyone trying to run away." 

tt "I only see people gasping and muttering among themselves, some even pulling out their phones to snap pictures."

t "Nnh.."

tt "Unable to pinpoint the attacker, I rush over, crouching next to where Vicente lies."

tt "Expecting the worst, I check for a pulse at his neck, hoping to find even the faintest sign of life…!"

t "......he's dead."

tt "Damn it… how did this happen!?"

tt "I hear more footsteps rushing in, familiar voices reacting to the gruesome scene as I move my hand away from the corpse."

show lu nervous2 at center
show rena nervous4 at left
show cata nervous2 at right
with dissolve

lu "Don Vicente…!"

r "Woah- what the fuck is going on here!?"

c "That's one of the trainers…"

hide rena
hide cata
with dissolve

show me angry at right with dissolve


me "Everyone, back off. Now. I'm clearing the area, this is a crime scene."

lu "This can't be happening…"

show en yell3 at left
with dissolve

en "Ah- it must be a misunderstanding, inspector!"

show me yell

me "I don't care how you try to spin it, that's a dead body. I'm having my people come in to secure the scene."

show en nervous2

en "Yes, I am aware that's your duty…! But see, the race is about to start in about thirty minutes…"

show me yell2

me "Are you kidding me? That's what you're concerned about?"

hide me
hide en
hide lu
with dissolve

show seb frown at slightleft 
with dissolve

s "The wondrous host is quite serious. We really can't have yet another cancellation of the event."

show me angry at slightright
with dissolve

me "You've got your priorities pretty screwed, Castillo. Listen here, whatever happened here…"

show me sweat2
me "...needs to be dealt with right away. There could be a murderer lurking around for all we know."

hide me
hide seb
with dissolve

show en nervous2 with dissolve
en "Mmngh…"
hide en
with dissolve

show seb smile2 at slightleft
show me angry at slightright
with dissolve

s "That would be concerning! But rest assured, I just asked a few people around here- they all said the same thing. This old fool- I mean, this man fell off the grandstands."

show me sweat

me "What…?"

tt "We all look up in unison towards the top of the grandstands. True, a fall from there would be lethal depending on how you land."

show seb neutral

s "If you don't believe me, go ahead and ask around. I'm sure you'll be met with the same responses."

tt "Only sparing him a glare, the inspector immediately begins questioning some of the nearby onlookers… who pretty much say the same thing."

show seb smile2
s "So you see, this is but a tragic accident."

en "It is quite regrettable… however, these things can happen. I will take care of it."

tt "With a snap of his fingers, security staff begin to approach from within the crowd. Oh no, are they already going to dispose of the body…?"

me "Tch, you're pulling that card now?"

tt "Whatever reinforcements the inspector could call, they'll arrive too late. By then, some evidence might be lost."

tt "I have to do something, quick! I-"

menu:
    "Speak up and intervene.":
        jump intervene
    "Stay quiet and watch things play out.":
        jump silent

label silent:
"Bad end."
return

label intervene:
    t "Wait a moment! This is no accident! It's murder."

    me "Ortiz..."

    s "Hah? Wait a moment, y-you...! What are you doing-"

    s "I mean... what are you saying? Didn't you hear what all these people said already?"

    tt "Hmph. Surprised I'm still hanging around...?"

    t "I did. But that doesn't make it an accident."

    s "As expected of a country bumpkin, I'll have to explain it nice and slow for you to understand..."

    #Tony vs Seb
    label vs_sebCE:
        scene placeholder_bodycg
        show seb smile3
        with fade
        call CE_start
        
        s "Get this through your thick skull: this was an accident."
        if ce_mode == "object":
            call vs_sebCE_wrong
        if ce_mode == "press":
            $ ce_mode = None
            t "Why are you so sure about that?"
            s "I'm getting to it, you impatient dolt! Hmph..."
    
    s "He fell down from the grandstands and died when he hit the floor."
    if ce_mode == "object":
        call vs_sebCE_wrong
    if ce_mode:
        $ ce_mode = None
        t "Would a fall from that height actually kill him?"
        s "H-He's dead, isn't he? So obviously it is!"

    s "It's obvious! There is nothing suspicious about him. Do you understand?"
    if ce_mode == "object":
        if ce_object in [de_mate, dp_leo]:
            call vs_sebCE_right
        else:
            call vs_sebCE_wrong
    if ce_mode:
        $ ce_mode = None
        t "You are absolutely certain about this?"
        s "You are so dense. I'm telling you, that's what happened, end of story!"
        tt "Yeah, right. There's something clearly wrong about what he just said."


    s "Now, get out of the way so these gentlemen can do their job."
    if ce_mode == "object":
        call vs_sebCE_wrong
    if ce_mode:
        $ ce_mode = None
        t "I think you're jumping the gun a bit, trying to clean up so fast!"
        s "Mr. Villareal here has an event to run. The more time we waste on this, the more things will go off schedule."
        t "Zero thoughts spared for the victim here.."

    hide screen ce_ui
    tt "He won't budge from this until I throw some evidence at his face. I know I have something somewhere in my Dossier."
    jump vs_sebCE
    
    label vs_sebCE_wrong:
        $ ce_mode = None
        t "Your testimony contradicts the evidence!!"
        show seb smile
        s "No."
        t "Fuck!"
        # Penalty Damage
        $ ce_rep -= 1
        return
    
    label vs_sebCE_right:
        $ ce_mode = None
        $ ce_rep += 2
        show objection
        t "It's true that depending on how he landed, he could have died from that height..."
        s "So you get it. So do us all a favor and-"
        call CE_end
        jump act3_continue

    
    
    
    

    
    label act3_continue:
    #Objection
    t "It's true that depending on how he landed, he could have died from that height..."
    s "So you get it. So do us all a favor and-"
    t "However."
    t "There are a few inconsistencies with that."
    s "Eh?"
    t "Think about it. What is your first instinct when you trip and fall?"
    r "That's easy. Catch myself with my arms... ah!"
    t "Exactly. But if you look at the body... his arms are just lying at his sides, and they don't appear broken."
    s "A-And?"
    t "And... that's really odd for someone plummeting to their doom. Survival instincts should have kicked in."
    s "Ugh... maybe he jumped on purpose then! Yeah! Midlife crisis!"
    lu "How dare you! Don Vicente would never do that!"
    s "Says you!"
    t "...those instincts would have kicked in anyway. But even then, it doesn't explain why it's such an odd way to fall."
    s "So he fell in a weird way! Big deal!"
    s "He still has his legs broken or something, right!? It changes nothing!"
    t "But that's where the biggest inconsistency comes in."
    s "What...?"
    t "If he really died from the fall..."
    t "Then why does he have such a massive head wound on the back of his head!?"
    s "Gyaaah!"
    s "That's, uh... from when he fell...? He cracked his head open...!"
    t "Then the front of his body wouldn't be as bruised as it is. It'd match that wound on the back, his whole body absorbing the impact."
    s "T-Then someone came after he fell, and hit him there...!"
    me "You're just making shit up now. Why the hell would someone come and do that?"
    t "And why hasn't a single person here testified about it?"
    s "U.....uuunngh....!"
    me "Seems to me like there is now more than enough reason to start an investigation."
    me "Obviously, you won't get in the way, right? Mr. Villareal."
    en "N-no, of course not... I can't in good conscience let a murderer roam free..."
    me "Good. Now, follow me, everyone. I need to have a good talk with all of you about your whereabouts."

    tt "The inspector is taking everyone back to the main racetrack. \nWhew, I managed to pull that off somehow..."
    tt "...but this is no time to be resting. I have to find out as much as I can. Who knows what other crap that guy Castillo will try to pull off?"
        
    
    #InvestigationsAreasNow, access from map
    label paddock_inves:
    "You find evidence in the parade ring."
    label racetrack_inves:
    scene placeholder_granstands
    with fade
    "You find evidence in the grandstands."
    label stables_inves:
    scene placeholder_stables
    with fade
    "You find evidence in the stables."
    label lockers_inves:
    scene placeholder_lockers
    with fade
    "You find evidence the lockers."
    label breakroom_inves:
    "You find evidence in the Staff Break Room."
    label inves_complete:
    "You find all the evidence and go back to the Main Race track."
    label ce1:
    "You Cross-Examine to prove its not an accident."
    label ce2:
    "You Cross Examine to defend yourself."
    label ce3:
    "You Cross Examine."
    label ce4:
    "You Cross Examine."
    label ce5:
    "Your last Cross Examination."
    label epilogue:
    "True End."
    label act3_badend:
    "Bad End."
    label act3_badend2:
    "Bad End 2."
return
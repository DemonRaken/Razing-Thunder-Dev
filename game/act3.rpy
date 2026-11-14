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
            with fade
    
    s "He fell down from the grandstands and died when he hit the floor."
    if ce_mode == "object":
        call vs_sebCE_wrong
    if ce_mode:
        $ ce_mode = None
        t "Would a fall from that height actually kill him?"
        s "H-He's dead, isn't he? So obviously it is!"
        with fade

    s "It's obvious! The fall killed him! Those bruises and injuries are exactly what you'd expect from such a fall! There's nothing suspicious here!"
    if ce_mode == "object":
        if ce_object in [de_victimnotes]:
            call vs_sebCE_right
        else:
            call vs_sebCE_wrong
    if ce_mode:
        $ ce_mode = None
        t "And you're sure those injuries were all caused by the fall?"
        s "Of course! What else could've caused them? Stop wasting my time!"
        tt "Hold on... Is that really the case? Something about his injuries doesn't add up."
        with fade


    s "Now, get out of the way so these gentlemen can do their job."
    if ce_mode == "object":
        call vs_sebCE_wrong
    if ce_mode:
        $ ce_mode = None
        t "I think you're jumping the gun a bit, trying to clean up so fast!"
        s "Mr. Villareal here has an event to run. The more time we waste on this, the more things will go off schedule."
        t "Zero thoughts spared for the victim here.."
        with fade

    hide screen ce_ui
    tt "He won't budge from this until I throw some evidence at his face."
    tt "I should open my \"{color=#FF9900}Dossier{/color}\" and \"{color=#FF9900}Present{/color}\" something that counters his claims."
    jump vs_sebCE
    
    label vs_sebCE_wrong:
        $ ce_mode = None
        t "Your testimony contradicts the evidence!!"
        show seb smile
        s "No."
        t "Fuck!"
        # Penalty Damage
        $ ce_rep -= 1
        with fade
        return
    
    label vs_sebCE_right:
        $ ce_mode = None
        $ ce_rep += 2
        call CE_end
        jump act3_continue
 
    label act3_continue:

    t "It's true that, depending on how he landed, a fall from that height could have killed him..."

    s "So you get it! Now, do us all a favor and—"

    t "However! There's something you're overlooking."

    s "Huh?"

    t "Look at his arms. They're just lying at his sides, without any sign of him trying to break his fall."

    s "A-And? Maybe he didn't have time to react!"

    t "Maybe. But there's something else. His face and the front of his body are covered in bruises, as if he took the full impact of the fall face-first."

    s "So what!? He fell face-first! That's what happens when you hit the ground!"

    t "Then explain this: if the Vicente hit the ground face-first..."
    
    t "Why does he have such a large wound on the BACK of his head!?"

    s "G-Gyaaah!"

    t "If he died from the fall, the damage would match how he landed."

    s "T-Then someone hit him AFTER he fell! Yeah! That's what happened!"

    me "You're just making shit up now. Why would someone come along and hit a corpse?" 

    t "And why hasn't a single person here reported seeing anything?"

    s "U.....uuunngh....! Then you explain it, genius! Why does that old crook have that wound!?"

    t "I can think of another possibility. The victim got that wound..." 
    jump fall_choice    
    label fall_choice:
        menu:
            "Before falling.":
                jump b4fall
            "While falling.":
                jump whilefall
            "After falling.":
                jump afterfall

    label afterfall:
        t "He got the wound after hitting the ground."
        s "Ah, so you do agree with me!"
        me "Hold it, isn't this the opposite of what you've been saying?"
        me "Besides, with all the people here, at least one or two would had seen that happen."
        t "Huh? Oh, uh.... yeah! You are right! Ahaha..."
        me "..."
        tt "Ugh, I messed that up big time..."
        tt "Calm down, Tony. Let's try that one more time. If he didn't get injured after the fall, then he got it..."
        jump fall_choice

    label whilefall:
        t "The victim was injured while falling."
        me "...while falling. As in, in the middle of the air?"
        s "I see. Makes sense."
        me "No, it doesn't! How on earth would anyone pull that off!? There is nowhere to stand on! Just air!"
        t "O-Oh, you know! Like, maybe someone was waiting below, suspended with a grappling hook!"
        t "Then the body approached, and they hit him with a well-timed strike! Hard!"
        me "First off, that's insane. Second, you are insane."
        tt "I don't think it's that unlikely... r-right?"
        me "Third, weren't you the one who said he fell face-first, with his arms by his side?"
        me "If the victim got hit during his fall, that would change the trajectory of his fall."
        me "What if the person miscalculated and missed? What if they couldn't muster enough strength due to that awkward position?"
        me "Not to mention, a person hanging from a grappling hook is incredibly suspicious."
        t "A-All very good points...!"
        tt "Shit... I need to re-think this. It is a little crazy to think it happened mid-air. So then, that must mean he got it..."
        jump fall_choice

    label b4fall:
    t "What if he was struck on the back of the head before he ever went over the railing?"

    t "He would've already been dead by then. His body would've fallen limp, unable to protect itself when it hit the ground."

    t "That would explain both the position of his body and the bruises on his front."

    me "Seems to me like there's now more than enough reason to start an investigation."

    me "Obviously, you won't get in the way, right? Mr. Villareal?"

    en "N-no, of course not... I can't in good conscience let a murderer roam free..."

    me "Good. Now, follow me, everyone. I need to have a good talk with all of you about your whereabouts."

    tt "The inspector is taking everyone back to the main racetrack. \nWhew, that was a close one..."
    tt "...but this is no time to be resting. I have to find out as much as I can. Who knows what other crap that guy Castillo will try to pull off?"
    tt "First, I need to make a quick stop to the trainer lockers..."

        
    
    #InvestigationsAreasNow, access from map
    label paddock_inves:
    scene placeholder_paddock
    with fade
    lt "There. Now I'm dressed for the occasion. El Leopardo is on the case...!"

    lt "Huh. The police officers watching over the scene aren't trying to detain me. I guess the inspector gave them a heads-up? Much appreciated!"
    lt "Time to take a good look around and figure out what happened."
    #Points to click: just the body.
    #When done so, zoom in on it.
    lt "I should examine the body more closely... Let's see."
    lt "There's that deep, nasty wound on the back of his head... and the bruises on the front..."
    lt "...Huh? This looks like dirt, but it doesn't match the ground around the parade ring. There's something else mixed in..."
    lt "Is this... bits of hay? Huh."
    lt "Maybe I should check the stables..."

    #Investigation start Sign or animation or something.
    "You find evidence in the parade ring."

    label racetrack_inves:
    scene placeholder_granstands
    with fade
    #Inves point Vip Lunge box
    lt "It's closed off for now, with police officers standing guard."
    lt "If I had to guess, Inspector Medina is questioning people inside."
    lt "I swear... Lorenzo must be fighting like hell to keep anyone from being taken to the police station."
    #railing
    lt "That's a long way down... Judging by the distance between this railing and the ground, I don't think someone could just trip and fall over it. It practically reaches my neck."
    lt "You'd have to deliberately climb over it to jump... or have someone throw you over."
    
    label stables_inves:
    scene placeholder_stables
    with fade
    lt "Hey Chispa. Hope you weren't feeling too lonely without me."
    lt "Wait... this place feels... off. Something's different."
    #click mountain of hay
    lt "Why is there a bunch of hay in the middle of the ground? You'd think the staff would tidy up the place more."
    lt "Hang on, I can see something underneath it..."
    lt "Kneeling over, I begin to brush away all of the hay."
    lt "What the...!? This looks like someone's blood...!"
    lt "...yeah. No doubt about it, this is dried up blood. Moreover, it looks like a few drops lead outside..."
    lt "Huh? The trail suddenly ends before reaching the entrance."
    lt "That's weird. I'll notify one of the officers about it. Better safe than sorry."

    #click shovel
    lt "Why is this poor shovel "

    
    
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
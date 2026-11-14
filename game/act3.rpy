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
    lt "Wait a minute... What's this doing here?"

    lt "A stable shovel. Someone must've left it behind this stall."

    lt "The blade is covered in something dark and flaky. At first, I thought it was dirt..."

    l "...Wait. Is that blood!?"

    lt "And this dent... Looks like it's been damaged pretty badly."

    lt "A dent and blood... some hairs are caught along the edge. Don't tell me this is..."

    lt "...I should have one of the inspector's subordinates run tests on it right away."

    lt "This here... might be the murder weapon!"

    lt "Alright, what's next...?"
    
    label lockers_inves:
    scene placeholder_lockers
    with fade
    l "What's with this locker? It's been left open."
    lt "As I walked over to close it, something in there catches my attention."
    l "A... hawaiin shirt? A pair of sunglasses, too..."
    lt "I guess these must belong to one of the jockeys."
    l "Hm? Hey, that's a notebook on top of the trousers..."
    lt "I do feel bad snooping through someone's belongings, but... it's for the sake of the investigation!"
    l "What do we have here... \n... \n...!?"
    lt "T-This...! The pages here are full with dates from various derby competitions!"
    lt "I recognize some of the horses' names, too..."
    lt "Perla Negra is listed here! That's the one they showed on the news!"
    l "There's something written next to the name... '$7,000'?"
    lt "That's a lot of money... is this a betting record? But ultimately, Perla Negra lost that race..."
    
    lt "...and so did a few of the other listed horses here, now that I think about it."
    
    lt "Their names came up when I first began to look into the incidents."
    
    lt "Hmm... these horses... their names are all crossed out. The only one that isn't is... 'Lucero'."
    l "Lucero... Haven't I heard that name before?"
    lt "...! Oh yeah! That's Lucas' horse! But why is $5,000 written next to it...?"
    lt "Mmmh... I should really find out who this locker belongs to."
    
    l "Does this one have a nameplate? It does. Let's see..."
    
    l "Huh!? Lucas Mendoza?"
    
    lt "The hell? Why does he have a notebook listing his own horse?"
    
    l "This is so weird... I'll have to look into it further. I should get moving for now."

    label breakroom_intro:
    lt "I've never been here before, but during the day, I saw Castillo's underlings coming and going through the hallway that leads here."

    lt "There's no mistaking them. They all wear those ridiculously expensive, flashy golden suits."

    lt "I think most of them have left by now, but... there might still be someone inside."

    lt "What should I do? I definitely need to check this place out. And while I could just kick the door down..."

    lt "...that would only attract unwanted attention. I don't need them calling for backup. I have to be swift."

    l "..."

    menu:
        "Pretend to be room service.":
            jump roomservice
        "Make them think there's a fire.":
            jump fireprank

    label fireprank:
        lt "I take out my phone and search for a 'fire alarm sound effect' video. I crank the volume all the way up and hit play."

        lt "A few seconds later, I hear footsteps rushing toward the door. They're getting closer... Gotta hide!"

        tg "AHHHH! FIRE! FIRE!!!"

        lt "The underling bolts down the hallway, stumbling over his own feet before disappearing from view."

        l "...Whew. Can't believe that actually worked."

        lt "I pull the poncho off my head and wait a few seconds to make sure he isn't coming back. Once I'm certain the coast is clear, I slip into the unattended room."

        lt "Now, let's see what you're hiding in here..."
        jump breakroom_inves
    label roomservice:
        lt "Alright. It's risky, but it just might work."
        l "*coughs* Room service!"
        tg "Finally! I was starving!"
        lt "The voice from inside opens the door."
        tg "..."
        tg "Wait..."

        tg "We don't get room service delivered all the way out here—"

        l "Haah!"

        lt "I toss my poncho over the man's face, catching him completely off guard."

        tg "!?"

        lt "He stumbles around, struggling to pull it off. By the time he manages, I've already stepped in close."

        lt "I drive my palm into his jaw."

        tg "Oof!"

        lt "He crumples to the cold floor, unconscious. I retrieve my poncho and casually sling it back over my shoulder."

        l "Take five."

        lt "Now, let's see what you're hiding in here..."
        jump breakroom_inves
    
    label breakroom_inves:
    lt "This looks like some kind of staff break room."

    lt "A few chairs, a table... Nothing too interesting."

    lt "Hm...? That looks like a trash bin."

    lt "Heh... It may look unimportant, but every good detective knows a crucial piece of evidence could be hiding in one of those!"

    lt "Well, at least I hope that's the case. Now, what have we got here?"

    lt "Rubbish, empty bottles, cigarettes... That's a fire hazard."

    lt "...! Hey, there's a black bag underneath all this. It's been crumpled up, too."

    lt "I dig through the rubbish and pull the bag out. Whoa, this thing is way bigger than I expected..."

    lt "I turn it inside out, and something immediately catches my eye."

    lt "What the...? Why is there so much blood in here!?"

    lt "I take a closer look. It's definitely dried blood..."

    lt "It's stained a large portion of the bag's interior..."

    lt "..."

    lt "Don't tell me... Is this a body bag? How long has this blood been here...?"

    l "Nnh... I need to get this thing analyzed. Pronto."


    #Investigation

    label inves_complete:
    of "Mr. Leopardo, correct?"
    lt "Ah- one of the police officers working for Medina just approached me."
    l "Indeed, that would be me! How may I help you?"
    of "We ran tests of the things you found and have the results. These are copies of them."
    l "Much appreciated, friend! With this, we're one step closer to bringing down the villain behind it!"
    of "R-Right... that was all."
    lt "I watch him leave in a hurry."
    lt "Hmm... I made some solid leeways here. Next, I should check-"
    "*beep!*"
    lt "Who's calling me now? ... \nThe inspector?"
    l "Hello?"
    me "Get your ass over to the main racetrack. Time's up."
    l "Uh. What do you mean time's up-"
    me "It means this stupid event will start in about 30 minutes and I've done all that I can to stop them from leaving."
    l "That's crazy! They can't go ahead with the race with a killer on the loose!"
    l "You're with the police! You have the authority to detain them and-"
    me "Don't tell me what I already know. Just get over here."
    "*beep*"
    l "She hung up..."
    lt "This is messed up. But no matter..."
    l "...for the ally of justice is here to save the truth! Prepare yourselves, villains!"

    label ce1:
    scene placeholder_granstands
    with fade
    lt "I rush all the way over here. The inspector is surrounded by officers, Castillo's underlings, and the jockeys..."

    lt "Time for my dramatic entrance."

    en "Once again, I understand your concerns, Inspector, but I simply cannot afford to cancel the event again."

    me "Then you clearly don't understand the situation."

    en "I promise you, once the race is over, you'll have my full cooperation!"

    me "That's not how this works. You have to—"

    l "—look past your selfish desires and face your responsibilities!"

    me "Exactly—wait, what?"

    lt "With a running leap and a flip, I let my poncho flutter dramatically through the air before striking a pose with my arms."

    l "The nightmare of criminals and fighter for justice..."

    l "El Leopardo is here to assist!"

    me ".............."

    r "Yo. What's this freak's deal?"

    c "...?"

    en "E-Excuse me? Sir, I don't know what kind of game you're playing here, but—"

    l "This is no game. This is a matter of life and death, and you're trying to look the other way!"

    en "Erm... Well, we're already behind schedule, you see..."

    me "Despicable..."

    s "What are you waiting for!? Kick this clown out of my derby—"

    show en neutral
    pause 1.0

    s "I mean... kick him out of your derby already! He's a lunatic!"

    l "Ah, but would you still say the same if I offered you the answers to this case?"

    s "The answers? Don't kid yourself! What would a masked freak like you know?"

    l "Quite a lot, actually, Mr. Castillo. For instance, I know you have a habit of siccing your men on people who inconvenience you."

    s "WHAT!? I, uh... I don't know what he's talking about. I would never..."

    s "More importantly, there's no need to waste any more time on this!"

    s "We already know who the culprit is!"

    lt "If it's coming from this guy, I seriously doubt it..."

    s "It was that suspicious character found near the body: Antonio Ortiz!"

    l "Say whaaaaaat!?"

    s "Yes, yes. Allow me to enlighten you."

    #CE goes here.

    # contra 1: tony killed him at the top of the railings
    # contra 2: tony used the bag to carry the body from the stables

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

label act3:
    $ dossier_enabled = True
    label act3intro:
        scene placeholder_granstands
        with fade
        tl "Razing Thunder Derby.\n Paddock. \n Evening."
        tt "Running at full speed, the gathering crowd immediately gets my attention. Following their gaze, I move past people to see what's got their attention…"
        tt "...and in that moment, the sense of dread that had been building up in my chest as I rushed over washes away, overcome by anger and disbelief."

        #Insert here CG of Vicente dead on the ground.
        scene black
        with dissolve
        play music sad

        tt "On the ground of the parade ring area lay the body of Vicente Ruiz, whom I had just spoken with not long ago, blood seeping from his head."

        t "What the hell…!?"

        tt "I quickly glance around my immediate surroundings, searching for anyone trying to run away." 

        tt "I only see people gasping and muttering among themselves, some even pulling out their phones to snap pictures."

        t "Nnh.."

        tt "Unable to pinpoint the attacker, I rush over, crouching next to where Vicente lies."

        tt "Expecting the worst, I check for a pulse at his neck, hoping to find even the faintest sign of life…!"

        t "......he's dead. He's all bruised up, and his legs are bent in an unnatural way, too."

        $ dossier.add(de_victimnotes)
        scene placeholder_granstands

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

        show en neutral
        hide seb
        hide me
        with dissolve

        en "It is quite regrettable… however, these things can happen. I will take care of it."

        tt "With a snap of his fingers, security staff begin to approach from within the crowd. Oh no, are they already going to dispose of the body…?"
        hide en
        show me sweat2
        with dissolve
        me "Tch, you're pulling that card now?"

        tt "Whatever reinforcements the inspector could call, they'll arrive too late. By then, some evidence might be lost."

        tt "I have to do something, quick! I-"

        menu:
            "Speak up and intervene.":
                call cutin("holdit")
                jump intervene
            "Stay quiet and watch things play out.":
                jump silent

        label silent:
            stop music fadeout 2.5
            scene black
            with fade
            tt "I stay silent, watching things unfold without intervening."
            tt "..."
            tt "Just as feared, the derby staff take away Vicente's body before inspector Medina can properly secure the crime scene."
            tt "The whole thing is dismissed as an accident."
            tt "Was it really just a tragedy? Or was there a perpetrator behind his death?"
            tt "Now I will never know the answer... nor am I really bothered to keep track of what happened at the race next."
            return
label intervene:
    stop music fadeout 2.5
    t det yell "Wait a moment! This is no accident! It's murder."

    show me sweat

    me "Ortiz..."

    hide me
    show seb angry3
    with dissolve
    s "Hah? Wait a moment, y-you...! What are you doing-"
    
    show seb angry
    s "I mean... what are you saying? Didn't you hear what all these people said already?"

    tt what det neutral "Hmph. Surprised I'm still hanging around...?"

    t det neutral "I did. But that doesn't make it an accident."
    
    show seb neutral 
    s "As expected of a country bumpkin, I'll have to explain it nice and slow for you to understand..."

#Tony vs Seb
label vs_seb_Testimony:
    scene placeholder_granstands
    call fx_testimony
    show seb neutral
    with fade
    show seb angry
    s "Get this through your thick skull: this was an accident."
    show seb neutral
    s "He fell down from the grandstands and died when he hit the floor."
    show seb smile2
    s "It's obvious! The fall killed him! Those bruises and injuries are exactly what you'd expect from such a fall! There's nothing suspicious here!"
    show seb grr    
    s "Now, get out of the way so these gentlemen can do their job."
    
    hide screen status_indicator
    stop music fadeout 2.5
    hide seb
    show tony neutral
    with dissolve
    t "So he just... happened to fall off from up there?"

    hide tony
    show seb neutral
    with dissolve
    s "What do you have infront of you? Stop wasting time and let the good inspector do her thing!"

    hide seb
    show tony det neutral
    with dissolve
    t "Right after I ask you a few things..."
    hide tony
    show seb frown
    with dissolve
    s "What is this, some kind of interrogation?"
    
    hide seb
    show tony det neutral right
    with dissolve
    tt "Yes, actually. And I'm going to find the flaw in your words."
    
label vs_sebCE:
    scene placeholder_granstands
    call fx_interrogation
    show seb neutral
    with fade
    call CE_start
    show seb angry
    s "Get this through your thick skull: this was an accident."
    if ce_mode == "object":
        call cutin("objection")
        call vs_sebCE_wrong
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        t neutral "Why are you so sure about that?"
        show seb grr
        s "I'm getting to it, you impatient dolt! Hmph..."
        with fade
    show seb neutral
    s "He fell down from the grandstands and died when he hit the floor."
    if ce_mode == "object":
        call cutin("objection")
        call vs_sebCE_wrong
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        t neutral "Would a fall from that height actually kill him?"
        show seb grr
        s "H-He's dead, isn't he? So obviously it is!"
        with fade
    show seb smile2
    s "It's obvious! The fall killed him! Those bruises and injuries are exactly what you'd expect from such a fall! There's nothing suspicious here!"
    if ce_mode == "object":
        call cutin("objection")
        if ce_object in [de_victimnotes]:
            call vs_sebCE_right
        else:
            call vs_sebCE_wrong
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        t neutral "And you're sure those injuries were all caused by the fall?"
        show seb neutral
        s "Of course! What else could've caused them? Stop wasting my time!"
        play sound se_flash
        tt neutral closed "Hold on... Is that really the case? Something about his injuries doesn't add up." with flash
        with fade

    show seb grr
    s "Now, get out of the way so these gentlemen can do their job."
    if ce_mode == "object":
        call cutin("objection")
        call vs_sebCE_wrong
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        t det yell "I think you're jumping the gun a bit, trying to clean up so fast!"
        show seb angry
        s "Mr. Villareal here has an event to run. The more time we waste on this, the more things will go off schedule."
        tt what aw drop "Zero thoughts spared for the victim here.."
        #with fade

    hide screen ce_ui
    hide screen status_indicator
    hide seb
    show tony neutral right
    # with dissolve
    with fade
    tt "He won't budge from this until I throw some evidence at his face."
    show tony neutral closed
    tt "I should open my \"{color=#FF9900}Dossier{/color}\" and \"{color=#FF9900}Present{/color}\" something that counters his claims."
    jump vs_sebCE
    
    label vs_sebCE_wrong:
        $ ce_mode = None
        t "This part of your testimony doesn't make a lick of sense, Sebastian!"
        show seb smile
        s "Wait a moment, I have to check the time on my watches."
        t "Eh?"
        show seb smile3
        s "I was afraid of this. It does seem like it's 'listen to stupid' o'clock right now."
        t "Gah!!"
        call ce_penalty(1)
        t "Damn. Looks like I was wrong..."
        # Penalty Damage
        with fade
        return
    
    label vs_sebCE_right:
        $ ce_mode = None
        $ ce_rep += 0.5
        call CE_end
        jump act3_continue
 
    label act3_continue:
    hide screen status_indicator
    hide seb
    show tony neutral closed at slightleft
    with dissolve
    t "It's true that, depending on how he landed, a fall from that height could have killed him..."
    
    show seb smile3 at slightright
    with dissolve
    s "So you get it! Now, do us all a favor and—"
    
    show tony det yell
    t "However! There's something you're overlooking."

    show seb frown
    s "Huh?"

    show tony det neutral right
    t "Look at his arms. They're just lying at his sides, without any sign of him trying to break his fall."

    show seb grr
    s "A-And? Maybe he didn't have time to react!"

    show tony det neutral
    t "Maybe. But there's something else. His face and the front of his body are covered in bruises, as if he took the full impact of the fall face-first."

    show seb angry3
    with dissolve
    s "So what!? He fell face-first! That's what happens when you hit the ground!"

    t "Then explain this: if the Vicente hit the ground face-first..."

    play music objection fadein 0.5
    show tony det yell
    with dissolve
    t "Why does he have such a large wound on the BACK of his head!?"

    show seb nervous2 with dissolve
    s "G-Gyaaah!"
    
    show tony det neutral
    t "If he died from the fall, the damage would match how he landed."

    show seb nervous
    s "T-Then someone hit him AFTER he fell! Yeah! That's what happened!"
    
    hide seb
    hide tony
    show me yell
    with dissolve
    me "You're just making shit up now. Why would someone come along and hit a corpse?" 
    
    hide me
    show tony det neutral
    with dissolve
    t "And why hasn't a single person here reported seeing anything?"
    
    hide me
    hide tony
    show seb grr2
    with dissolve
    s "U.....uuunngh....! Then you explain it, genius! Why does that old crook have that wound!?"
    
    hide seb
    show tony det neutral
    with dissolve
    t "I can think of another possibility. The victim got that wound..." 
    jump fall_choice    
    label fall_choice:
        menu:
            "Before falling.":
                call cutin("takethat")
                jump b4fall
            "While falling.":
                jump whilefall
            "After falling.":
                jump afterfall

    label afterfall:
        hide seb
        show tony det yell
        t "He got the wound after hitting the ground."
        
        hide tony
        show seb smile2 at slightleft
        with dissolve
        s "Ah, so you do agree with me!"
        
        show me yell at slightright
        with dissolve
        me "Hold it, isn't this the opposite of what you've been saying?"
        
        show me angry
        me "Besides, with all the people here, at least one or two would had seen that happen."
        
        hide me
        hide seb
        show tony aha
        with dissolve
        t "Huh? Oh, uh.... yeah! You are right! Ahaha..."
        
        show seb smile3 at slightleft
        show me sweat2 at slightright
        hide tony
        with dissolve
        me "..."
        
        hide seb
        hide me
        show tony aw neutral drop
        with dissolve
        tt "Ugh, I messed that up big time..."
        
        show tony neutral drop
        tt "Calm down, Tony. Let's try that one more time. If he didn't get injured after the fall, then he got it..."
        jump fall_choice
    label whilefall:
        hide seb
        hide me
        show tony det yell
        t "The victim was injured while falling."
        
        hide tony
        show me sweat at slightright
        with dissolve
        me "...while falling. As in, in the middle of the air?"
        
        show seb smile2 at slightleft
        with dissolve
        s "I see. Makes sense."
        
        show me yell
        me "No, it doesn't! How on earth would anyone pull that off!? There is nowhere to stand on! Just air!"
        
        hide seb
        hide me
        show tony aw smile drop
        with dissolve
        t "O-Oh, you know! Like, maybe someone was waiting below, suspended with a grappling hook!"
        
        show tony det yell
        t "Then the body approached, and they hit him with a well-timed strike! Hard!"
        
        hide tony
        show seb smile3 at slightleft
        show me angry at slightright
        with dissolve
        me "First off, that's insane. Second, you are insane."
        
        hide seb
        hide me
        show tony neutral drop
        with dissolve
        tt "I don't think it's that unlikely... r-right?"
        
        hide tony
        show seb smile3 at slightleft
        show me sweat at slightright
        me "Third, weren't you the one who said he fell face-first, with his arms by his side?"
        
        show me sweat2
        me "If the victim got hit during his fall, that would change the trajectory of his fall."
        show me neutral
        me "What if the person miscalculated and missed? What if they couldn't muster enough strength due to that awkward position?"
        show me yell
        me "Not to mention, a person hanging from a grappling hook is incredibly suspicious."
        
        hide me
        hide seb
        show tony neutral drop
        with dissolve
        t neutral drop "A-All very good points...!"
        show tony aw neutral drop
        tt "Shit... I need to re-think this. It is a little crazy to think it happened mid-air. So then, that must mean he got it..."
        jump fall_choice

label b4fall:
    hide me
    hide seb
    show tony neutral
    with dissolve
    t "What if he was struck on the back of the head before he ever went over the railing?"
    
    show tony neutral closed
    t "He would've already been dead by then. His body would've fallen limp, unable to protect itself when it hit the ground."

    show tony det yell
    t "That would explain both the position of his body and the bruises on his front."
    
    hide tony
    show me smile
    with dissolve
    me "Seems to me like there's now more than enough reason to start an investigation."
    
    show me smile3
    me "Obviously, you won't get in the way, right? Mr. Villareal?"
    
    hide me
    show en nervous2
    with dissolve
    en "N-no, of course not... I can't in good conscience let a murderer roam free..."

    hide en
    show me neutral
    with dissolve
    me "Good. Now, follow me, everyone. I need to have a good talk with all of you about your whereabouts."

    stop music fadeout 2.5
    hide me
    with dissolve
    
    tt aw neutral drop "The inspector is taking everyone back to the luxury box. \nWhew, that was a close one..."
    tt det neutral "...but this is no time to be resting. I have to find out as much as I can. Who knows what other crap that guy Castillo will try to pull off?"
    tt det smile "First, I need to make a quick stop to the trainer lockers..."
    with fade
    lt smile "There. Now I'm dressed for the occasion. El Leopardo is on the case...!"
    jump act3_main_inves  

    
    #InvestigationsAreasNow, access from map
# label paddock_inves:
#     scene placeholder_paddock
#     with fade
#     lt "There. Now I'm dressed for the occasion. El Leopardo is on the case...!"

#     lt "Huh. The police officers watching over the scene aren't trying to detain me. I guess the inspector gave them a heads-up? Much appreciated!"
#     lt "Time to take a good look around and figure out what happened."
#     play music inves fadein 2.5
#     #Points to click: just the body.
#     #When done so, zoom in on it.
#     lt "I should examine the body more closely... Let's see."
#     lt "There's that deep, nasty wound on the back of his head... and the bruises on the front..."
#     lt "...Huh? This looks like dirt, but it doesn't match the ground around the parade ring. There's something else mixed in..."
#     lt "Is this... bits of hay? Huh."
#     lt "Maybe I should check the stables..."

#     #Investigation start Sign or animation or something.

# label racetrack_inves:
#         scene placeholder_granstands
#         with fade
#         #Inves point Vip Lunge box
#         lt "It's closed off for now, with police officers standing guard."
#         lt "If I had to guess, inspector Medina is questioning people inside."
#         lt "I swear... Lorenzo must be fighting like hell to keep anyone from being taken to the police station."
#         #railing
#         lt "That's a long way down... Judging by the distance between this railing and the ground, I don't think someone could just trip and fall over it. It practically reaches my neck."
#         lt "You'd have to deliberately climb over it to jump... or have someone throw you over."
    
# label stables_inves:
#     scene placeholder_stables
#     with fade
#     lt "Hey Chispa. Hope you weren't feeling too lonely without me."
#     lt "Wait... this place feels... off. Something's different."

#     call screen aai_examine_stables
    
    
#     label lockers_inves:
#         scene placeholder_lockers
#         with fade
#         l "What's with this locker? It's been left open."
#         lt "As I walked over to close it, something in there catches my attention."
#         l "A... hawaiin shirt? A pair of sunglasses, too..."
#         lt "I guess these must belong to one of the jockeys."
#         $ dossier.add(de_casualclothes)

#         l "Hm? Hey, that's a notebook on top of the trousers..."
#         lt "I do feel bad snooping through someone's belongings, but... it's for the sake of the investigation!"
#         l "What do we have here... \n... \n...!?"
#         lt "T-This...! The pages here are full with dates from various derby competitions!"
#         lt "I recognize some of the horses' names, too..."
#         lt "Perla Negra is listed here! That's the one they showed on the news!"
#         l "There's something written next to the name... '$7,000'?"
#         lt "That's a lot of money... is this a betting record? But ultimately, Perla Negra lost that race..."
        
#         lt "...and so did a few of the other listed horses here, now that I think about it."
        
#         lt "Their names came up when I first began to look into the incidents."
        
#         lt "Hmm... these horses... their names are all crossed out. The only one that isn't is... 'Lucero'."
#         l "Lucero... Haven't I heard that name before?"
#         lt "...! Oh yeah! That's Lucas' horse! But why is $5,000 written next to it...?"
#         lt "Mmmh... I should really find out who this locker belongs to."
        
#         l "Does this one have a nameplate? It does. Let's see..."
        
#         l "Huh!? Lucas Mendoza?"
        
#         lt "The hell? Why does he have a notebook listing his own horse?"
        
#         l "This is so weird... I'll have to look into it further. I should get moving for now."
        
#         $ dossier.add(de_notebook)

#     label breakroom_intro:
#         lt "I've never been here before, but during the day, I saw Castillo's underlings coming and going through the hallway that leads here."

#         lt "There's no mistaking them. They all wear those ridiculously expensive, flashy golden suits."

#         lt "I think most of them have left by now, but... there might still be someone inside."

#         lt "What should I do? I definitely need to check this place out. And while I could just kick the door down..."

#         lt "...that would only attract unwanted attention. I don't need them calling for backup. I have to be swift."

#         l "..."

#         menu:
#             "Pretend to be room service.":
#                 jump roomservice
#             "Make them think there's a fire.":
#                 jump fireprank

#         label fireprank:
#             lt "I take out my phone and search for a 'fire alarm sound effect' video. I crank the volume all the way up and hit play."

#             lt "A few seconds later, I hear footsteps rushing toward the door. They're getting closer... Gotta hide!"

#             tg "AHHHH! FIRE! FIRE!!!"

#             lt "The underling bolts down the hallway, stumbling over his own feet before disappearing from view."

#             l "...Whew. Can't believe that actually worked."

#             lt "I pull the poncho off my head and wait a few seconds to make sure he isn't coming back. Once I'm certain the coast is clear, I slip into the unattended room."

#             lt "Now, let's see what you're hiding in here..."
#             jump breakroom_inves
#         label roomservice:
#             lt "Alright. It's risky, but it just might work."
#             l "*coughs* Room service!"
#             tg "Finally! I was starving!"
#             lt "The voice from inside opens the door."
#             tg "..."
#             tg "Wait..."

#             tg "We don't get room service delivered all the way out here—"

#             l "Haah!"

#             lt "I toss my poncho over the man's face, catching him completely off guard."

#             tg "!?"

#             lt "He stumbles around, struggling to pull it off. By the time he manages, I've already stepped in close."

#             lt "I drive my palm into his jaw."

#             tg "Oof!"

#             lt "He crumples to the cold floor, unconscious. I retrieve my poncho and casually sling it back over my shoulder."

#             l "Take five."

#             lt "Now, let's see what you're hiding in here..."
#             jump breakroom_inves
#         label breakroom_inves:
#             lt "This looks like some kind of staff break room."

#             lt "A few chairs, a table... Nothing too interesting."

#             lt "Hm...? That looks like a trash bin."

#             lt "Heh... It may look unimportant, but every good detective knows a crucial piece of evidence could be hiding in one of those!"

#             lt "Well, at least I hope that's the case. Now, what have we got here?"

#             lt "Rubbish, empty bottles, cigarettes... That's a fire hazard."

#             lt "...! Hey, there's a black bag underneath all this. It's been crumpled up, too."

#             lt "I dig through the rubbish and pull the bag out. Whoa, this thing is way bigger than I expected..."

#             lt "I turn it inside out, and something immediately catches my eye."

#             lt "What the...? Why is there so much blood in here!?"

#             lt "I take a closer look. It's definitely dried blood..."

#             lt "It's stained a large portion of the bag's interior..."

#             lt "..."

#             lt "Don't tell me... Is this a body bag? How long has this blood been here...?"

#             l "Nnh... I need to get this thing analyzed. Pronto."
            


#     #Investigation COMPLETE

#     label inves_complete:
#         of "Mr. Leopardo, correct?"
#         lt "Ah- one of the police officers working for Medina just approached me."
#         l "Indeed, that would be me! How may I help you?"
#         of "Here is a copy of the preliminary autopsy report."
#         $ dossier.add(de_autopsy)
#         of "We also ran tests of the things you found and have the results. These are copies of them."
#         $ dossier.add(de_shovel)
#         $ dossier.add(de_blooddrops)
#         $ dossier.add(de_bodybag)
        
#         l "Much appreciated, friend! With this, we're one step closer to bringing down the villain behind it!"
#         of "R-Right... that was all."
#         lt "I watch him leave in a hurry."
#         lt "Hmm... I made some solid leeways here. Next, I should check-"
#         "*beep!*"
#         lt "Who's calling me now? ... \nThe inspector?"
#         l "Hello?"
#         me "Get your ass over to the main racetrack. Time's up."
#         l "Uh. What do you mean time's up-"
#         me "It means this stupid event will start in about 30 minutes and I've done all that I can to stop them from leaving."
#         l "That's crazy! They can't go ahead with the race with a killer on the loose!"
#         l "You're with the police! You have the authority to detain them and-"
#         me "Don't tell me what I already know. Just get over here."
#         "*beep*"
#         l "She hung up..."
#         lt "This is messed up. But no matter..."
#         l "...for the ally of justice is here to save the truth! Prepare yourselves, villains!"

    label ce1:
        scene placeholder_racetrack1
        with fade
        stop music fadeout 2.5
        lt "I rush all the way over here. The inspector is surrounded by officers, Castillo's underlings, and the jockeys..."

        lt "Time for my dramatic entrance."

        show en nervous2 at slightleft
        with dissolve
        en "Once again, I understand your concerns, inspector, but I simply cannot afford to cancel the event again."

        show me angry at slightright
        with dissolve
        me "Then you clearly don't understand the situation."

        show en nervous3
        en "I promise you, once the race is over, you'll have my full cooperation!"

        show me yell2
        me "That's not how this works. You have to—"

        l "—look past your selfish desires and face your responsibilities!"
        
        show me yell
        me "Exactly—wait, what?"
        
        hide me
        hide en
        show leo grin shine
        with vpunch
        with dissolve

        lt "With a running leap and a flip, I let my poncho flutter dramatically through the air before striking a pose with my arms."

        show leo yell

        l "The nightmare of criminals and fighter for justice..."

        show leo think yell
        play sound flash
        play music leo fadein 2.5

        l "El Leopardo is here to assist!" with flash
        
        hide leo
        show me sweat2
        with dissolve
        me ".............."
        
        show rena angry at left
        with dissolve
        r "Yo. What's this freak's deal?"

        show cata surprise at right
        with dissolve
        c "...?"
        
        hide cata
        hide me
        hide rena
        show en yell
        with dissolve
        en "E-Excuse me? Sir, I don't know what kind of game you're playing here, but—"

        l neutral "This is no game. This is a matter of life and death, and you're trying to look the other way!"
        
        show en neutral
        en "Erm... Well, we're already behind schedule, you see..."
        
        hide en
        show me angry at slightright
        with dissolve
        me "Despicable..."
        
        show seb grr2 at slightleft
        with dissolve
        s "What are you waiting for!? Kick this clown out of my derby—"

        hide seb grr2
        hide me
        show en neutral
        with dissolve
        pause 1.0

        hide en
        show seb frown
        with dissolve
        s "I mean... kick him out of your derby already! He's a lunatic!"

        l smile "Ah, but would you still say the same if I offered you the answers to this case?"

        show seb smile2
        s "The answers? Don't kid yourself! What would a masked freak like you know?"

        l neutral "Quite a lot, actually, Mr. Castillo. For instance, I know you have a habit of siccing your men on people who inconvenience you."

        show seb nervous
        s "WHAT!? I, uh... I don't know what he's talking about. I would never..."

        hide seb
        show me angry
        with dissolve
        me "..."

        hide me
        show seb angry
        with dissolve
        s "More importantly, there's no need to waste any more time on this!"
        
        show seb smile
        s "We already know who the culprit is!"

        lt eh neutral "If it's coming from this guy, I seriously doubt it..."
        
        show seb smile3
        s "It was that suspicious character found near the body: Antonio Ortiz!"

        l yell "Say whaaaaaat!?"

        show seb smile2

        s "Yes, yes. Allow me to enlighten you."
        stop music fadeout 2.5

        #CE goes here.

        # contra 1: tony killed him at the top of the railings
        label vs_sebCE2:
            scene placeholder_racetrack1
            show seb neutral
            with fade
            call fx_testimony
            
            s "I overlooked his questionable appearance, given that he's Catalina's trainer..."
            show seb grr
            s "But no more! He's clearly a suspicious person!"
            show seb angry
            s "We all saw him prodding and standing near the body."
            show seb grr
            s "Who does that? A cold blooded murderer!"
            show seb grr2
            s "He attacked that poor old man at the grandstands, then dropped him from high-up!"

            hide screen status_indicator
            stop music fadeout 2.5
            
            show leo think closed at slightleft
            hide seb
            with fade
            l "Mr. Castillo... are you not basing your accusations on prejudice?"
            
            show leo neutral
            l "That may have been just a very curious fellow."
            
            show seb angry2 at slightright
            with dissolve 
            s "How dare you! My words are very well-founded!"
            
            show seb neutral
            s "Now, if you're done parroting, I believe the inspector has a criminal to catch."
            
            show leo grin
            l "Of course. Right as we're done going over your testimony."
            
            show seb frown
            s "Not this again... I'm getting déjà vu."
            
            hide leo
            show seb at center
            with dissolve
            lt "Yeah, and I'm getting déjà vu too. Of a glaring contradiction, that is."
            
            lt "After all the investigating I've done, I know this guy is dead wrong!"
            lt "Now I just have to prove it!"
            with fade
            
        
        #call cutin("cross_examination")
        label vs_sebCE2_loop hide: # Before hide was learned.
            
            call CE_start
            call fx_interrogation
            hide leo
            show seb neutral at center
            s "I overlooked his questionable appearance, given that he's Catalina's trainer..."
            if ce_mode == "object":
                call cutin("objection")
                call vs_sebCE_wrong2
            if ce_mode == "press":
                $ ce_mode = None
                call cutin("holdit")
                l eh neutral drop "My- *cough* what is so questionable about that young man's appearance?"
                
                show seb smile2
                s "That unrefined hair, that nasty scar on his face, the ugly boots... need I go on?"
                
                lt yell "I'm not taking fashion advice from the guy wearing two rolexs on his arm!"
                with fade
            
            show seb grr
            s "But no more! He's clearly a suspicious person!"
            if ce_mode == "object":
                call cutin("objection")
                call vs_sebCE_wrong2
            #p
            if ce_mode == "press":
                $ ce_mode = None
                call cutin("holdit")
                l neutral "What makes you so sure about that?"
                show seb grr
                s "I'm getting there, mask freak! Stop interrupting me."
                with fade
            show seb angry
            s "We all saw him prodding and standing near the body."
            if ce_mode == "object":
                call cutin("objection")
                call vs_sebCE_wrong2
            #p
            if ce_mode == "press":
                $ ce_mode = None
                call cutin("holdit")
                l grin closed "Uh... perhaps he was just trying to help the downed man?"
                
                show seb neutral
                s "Now he's a parademic? Please!"
                
                lt closed drop "I do know some first aid..."
                with fade
            show seb grr
            s "Who does that? A cold blooded murderer!"
            if ce_mode == "object":
                call cutin("objection")
                call vs_sebCE_wrong2
            #p
            if ce_mode == "press":
                $ ce_mode = None
                call cutin("holdit")
                l yell "It's a bit of a stretch to label him a murderer just for that!"
                
                show seb angry
                s "Say what you want, the police should just arrest him and let us run things here!"
                
                lt closed drop "I don't know if I'll be so lucky twice if I end up there again.
                "
                with fade
            show seb grr2
            s "He attacked that poor old man at the grandstands, then dropped him from high-up!"
            #p - contra is here , blood drops
            if ce_mode == "object":
                call cutin("objection")
                if ce_object in [de_blooddrops, de_shovel]:
                    call vs_sebCE_right2
                else:
                    call vs_sebCE_wrong2
            if ce_mode == "press":
                $ ce_mode = None
                call cutin("holdit")
                l neutral "He dropped him right after the attack?"
                show seb angry
                s "Are your ears clogged? Yes!"
                
                l "That would mean Mr. Ruiz was assaulted at the top of the grandstands, yes?"
                show seb frown
                s "Who?"
                
                l eh what "...the victim."
                
                show seb smile2
                s "Oh. Yes. Don't make me repeat the same over and over!"
                
                play sound se_flash
                lt think closed "I will when you stop contradicting yourself over and over." with flash
                #with fade
            
            hide screen ce_ui
            hide screen status_indicator
            scene placeholder_racetrack1
            show leo yell
            with fade
            
            lt "I'm not about to let this guy frame me for murder."
            
            show leo neutral
            lt "Thankfully, he's already made one grave mistake while spewing his falsehoods."
            hide leo 
            with dissolve
            with fade
            
            jump vs_sebCE2_loop

            #continue here
            label vs_sebCE_wrong2:
                $ ce_mode = None
                l yell "Mr. Castillo, you have made a serious mistake in your testimony!"
                
                show seb smile3
                s "The only mistake here is that rag you are carrying around."
                
                l closed drop "Ugh...!"
                
                lt "It's not a rag, it's a poncho..."
                # Penalty Damage
                call ce_penalty(2)
                with fade
                return
            label vs_sebCE_right2:
                $ ce_mode = None
                $ ce_rep += 0.5
                call CE_end
                jump act3_continue2
        label act3_continue2:
            scene placeholder_racetrack1
            hide screen status_indicator
            show seb neutral at slightright
            show leo think closed at slightleft
            with fade
            l "So, you're claiming that Mr. Ortiz attacked the victim at the top of the grandstands... then threw him over the railing..."
            l "...where he landed ultimately on the dirt track below, right where the body was found. Did I get that right?"

            show seb smile

            s "A fine summary! Now that you understand, how about you leave already?"

            play music objection fadein 0.5
            show leo think yell
            with dissolve
            l "Except your explanation is riddled with holes."

            show seb grr3
            with dissolve
            s "H-How dare you!"

            show leo yell
            with dissolve
            l "If Mr. Ortiz threw the victim from that height, how did he manage to show up and \"prod\" at the corpse, as you put it earlier?"

            show seb angry
            s "He ran! All the way down, as fast as he could!"

            show leo neutral right
            l "It's quite a distance to cover. He would've arrived after you, not before you."
            
            show leo neutral
            l "And that's not even the biggest problem."

            show seb frown
            s "There's... more?"

            show leo grin
            l "I'm afraid so. Lots more."

            show leo neutral
            l "For starters, there was a distinct lack of blood at the top of the grandstands."
            
            show seb grr
            s "That's easy! It was cleaned up!"

            call cutin("objection")

            show leo closed
            with dissolve
            play sound se_flash
            l "Luminol test." with flash

            show seb frown
            s "What?"

            show leo neutral 
            l "Forensics examined the area thoroughly. Even if someone wipes away the blood, luminol can still react with the traces left behind, revealing what the naked eye can't see."

            show leo think closed
            l "Yet they found no traces of blood on the railing or the ground beneath the spot where the victim supposedly fell from."

            show leo grin
            l "But there was one place where the victim's blood *was* found. Care to guess where?"
            
            show seb nervous
            s "...Mmmmnngh...."

            call cutin("takethat")
            show leo point
            play sound se_flash
            l "Allow me then: Vicente's blood was discovered at the derby's stables!" with flash

            show seb nervous2
            s "I-Impossible!"

            hide leo
            hide seb
            show me angry
            with dissolve

            me "Forensics confirmed the blood is a match. There's no doubt about it."

            hide me
            show seb angry3
            with dissolve
            s ".....that doesn't change a thing though!"

            hide seb
            show leo neutral
            with dissolve
            l "...? It seems you don't intend on dropping the accusation."

            hide leo
            show seb grr2
            s "Of course not! And you will see why right now!"
            stop music fadeout 2.5
label act3_continue3:
    # contra 2: tony used the bag to carry the body from the stables
    #Leo vs Seb Round 2 CE
    
    default ce_seb_bodybag = False
    label vs_sebCE_3:
    scene placeholder_racetrack1
    show seb angry
    with fade
    call fx_testimony
    s "Fine then, I admit it. That old crook died at the stables."
    show seb grr
    s "That still doesn't clear the country bumpkin's name!"
    show seb grr2
    s "He attacked that trainer, then moved his body away from the stables!"
    
    hide screen status_indicator
    stop music fadeout 2.5
    hide seb
    with fade
    l neutral right "So... you stand by your accusation."
    show seb smile3
    with dissolve
    s "You don't get to where I am by retracting at the slightest error."
    lt eh what "It's been several errors."
    lt neutral right "Hm... nothing in particular seems wrong, but that's because he's skimming over the details."
    lt neutral "I should press him and get a fuller picture of his version of events."
    call cutin("cross_examination")
label vs_sebCE_3_loop hide:
    call CE_start
    call fx_interrogation
    scene placeholder_racetrack1
    hide leo
    show seb angry
    with fade
    s "Fine then, I admit it. That old crook died at the stables."
    #press
    if ce_mode == "object":
        call cutin("objection")
        call vs_sebCE_wrong3
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        l grin closed "Was that so hard?"
        show seb grr3
        s "S-Silence!"
        with fade
    show seb grr
    s "That still doesn't clear the country bumpkin's name!"
    if ce_mode == "object":
        call cutin("objection")
        call vs_sebCE_wrong3
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        l eh neutral "Why do you insist on calling m- on calling him that..?"
        show seb smile3
        s "I have twenty reasons explaining why. Number one..."
        l eh neutral drop "Never mind. Moving on..."
        with fade

    if ce_seb_bodybag:
        show seb grr2
        s "He attacked that trainer, then used some kind of body bag to transport him out from the stables!"
        if ce_mode == "object":
            call cutin("objection")
            $ ce_mode = None
            if ce_object in [de_bodybag]:
                call vs_sebCE_right3
            else:
                call vs_sebCE_wrong3
        if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l neutral"Where did he get the bag from?"
            show seb neutral
            s "How should I know? I am not a criminal! eBay? Drone delivery?"
            lt eh what"Man. If drones started handing out crime tools like candy, we'd all be in big trouble."
            lt neutral right "Speaking of trouble... it doesn't seem Sebastian has realized what it means to have used that method."
            play sound se_flash
            lt smile "At the very least, I know it's impossible for me to have done it. I just gotta prove it now!" with flash
            with fade
    else:
        show seb grr2
        s "He attacked that trainer, then moved his body away from the stables!"
        if ce_mode == "object":
            call cutin("objection")
            call vs_sebCE_wrong3
        if ce_mode == "press":
            $ ce_seb_bodybag = True
            call cutin("holdit")
            $ ce_mode = None
            l neutral "How did he pull that off in a derby full of people?"
            l neutral right "I'd imagine Mr. Ortiz would risk being seen."
            show seb grr
            s "Must I spell it out? That runt didn't drag him by the feet in broad daylight!"
            show seb neutral
            l eh neutral "Then how did he do it?"
            s "Some kind of bag, perhaps? Dark enough so no one can tell!"
            lt closed "...people tend to give themselves away at times. This is one of them."
            l smile "That sounds important. Revise your testimony, Mr. Castillo."
            show seb smile2
            s "Fine, you creep. I'll say it as many times as needed."
            #with fade
    

    hide screen ce_ui
    hide screen status_indicator
    hide seb
    show leo think closed
    with fade
    lt "Parts of his explanation are too vague. I should press for details."
    lt "He's bound to mess up, that will be my chance to counter attack."
    # hide leo
    jump vs_sebCE_3_loop

    label vs_sebCE_wrong3:
        $ ce_mode = None
        l yell "Your testimony contradicts the evidence!"
        show seb smile3
        s "No."
        lt closed drop "Fuck!"
        lt eh neutral drop "Ugh, that didn't go so well..."
        # Penalty Damage
        call ce_penalty (2)
        with fade
        return
    
    label vs_sebCE_right3:
        $ ce_mode = None
        $ ce_rep += 0.5
        call CE_end
        jump act3_continue4
    
label act3_continue4:
    hide screen status_indicator
    stop music fadeout 2.5
    scene placeholder_racetrack1
    show leo think closed at slightleft
    show seb grr2 at slightright
    with fade
    l "Interestingly enough... I agree with what you just said, Mr. Castillo."

    show seb smile2

    s "Even numbskulls like you can listen to reason. There may be hope for you yet."

    show leo think yell
    l "Sorry to disappoint you, but I was referring to the method of transportation."

    show leo think closed
    l "Yes, it's highly likely that a body bag was used to transport the victim's body."
    show leo neutral
    l "But... the person you're accusing couldn't have been the one to use that bag."

    show seb angry3
    s "H-How can you know that!? You can buy a bag like that anywhere!"

    show leo neutral right
    l "True. But you still have to dispose of it afterward."

    show leo neutral
    l "Mr. Castillo. Any idea where the body bag used to transport the victim was found?"

    show seb grr
    s "Hah! How should I know!? Was it dumped in a river?"

    call cutin("takethat")
    play music objection fadein 2.5
    show leo point
    play sound se_flash
    l "It was found inside the staff break room. At the bottom of their trash bin, to be precise." with flash
    show seb nervous2
    s "WHA- How do you-!?"
    
    show leo neutral
    l "The door happened to be open. And an officer happened to check inside."
    show leo closed
    l "What he found was quite damning: a bag stained with the victim's dried blood."

    s "W-Wait, wait, wait! I can explain! This... proves nothing!"

    show seb angry4
    s "That creep just got rid of the bag in that room!"

    show leo yell
    l "That's impossible, and you know it, Mr. Castillo."
    show seb nervous
    s "...!"
    show leo neutral
    l "Mr. Villareal, security has been tightened considerably since the horse collapse incident, correct?"
    
    hide leo
    hide seb
    show en neutral
    with dissolve
    en "Huh? Yes, that's right. We've increased patrols and made sure the public doesn't wander into restricted areas..."

    hide en
    show leo yell
    with dissolve
    l "The staff break room is one of those restricted areas. Unauthorized personnel aren't allowed anywhere near it."
    
    show leo point
    play sound se_flash
    l "Which means only people working behind the scenes could have disposed of the bag there!" with flash

    hide leo
    show seb nervous2
    with dissolve
    s "AAAHHH!"

    hide seb
    show leo grin closed
    with dissolve
    lt "Well, I did manage to get in there relatively easily, but I'm certainly not going to tell him that. Especially when I've got him on the ropes."

    show leo yell
    l "Mr. Castillo! You often boast about having your underlings take care of things for you..."

    show leo grin
    l "How about we give them a call? I'm sure they'll be happy to explain why an area meant for staff to rest..."
    
    show leo neutral
    l "...was being used to hide a piece of evidence connected to the murder."

    show leo point
    with dissolve
    play sound se_flash
    l "I'm sure they'll have something very interesting to share with the rest of us!" with flash

    hide leo
    show seb nervous
    with dissolve
    s "....n...nnnh...."

    show layer master at earthquake(dt=2.0, dist=10)
    show seb nervous2
    with dissolve
    s "Nooooo!"

    pause .5
    stop music fadeout 2.5

    scene placeholder_granstands
    show me smile
    with fade

    #fade here

    me "Got some news. Castillo's men finally 'fessed up. Two of them hid the body bag in the break room. On their boss' orders, of course."

    l neutral "I knew it, so they truly played a part in this."

    l yell "Then this means the culprit behind Vicente's murder is...!"

    #Choose here, but no real consequences, Medina interrupts you. Heck, make a time out choice even.

    default chosen_murderer = _("no idea")

    menu timed_menu_chosen_murderer (screen="timed_choice", timeout=10.0, timeout_label="act3_continue5"):
        "Esteban":
            $ chosen_murderer = _("Esteban")
            jump act3_continue5
        "Catalina":
            $ chosen_murderer = _("Catalina")
            jump act3_continue5
        "El Leopardo":
            $ chosen_murderer = _("El Leopardo")
            jump act3_continue5
        "Sebastian":
            $ chosen_murderer = _("Sebastian")
            jump act3_continue5
        "Renata":
            $ chosen_murderer = _("Renata")
            jump act3_continue5
        "Medina":
            $ chosen_murderer = _("Medina")
            jump act3_continue5
        "Lorenzo":
            $ chosen_murderer = _("Lorenzo")
            jump act3_continue5
        "Lucas":
            $ chosen_murderer = _("Lucas")
            jump act3_continue5
        "Castillo's Underlings":
            $ chosen_murderer = _("Castillo's Underlings")
            jump act3_continue5   

label act3_continue5:
    scene placeholder_granstands
    show me angry
    me "Hold it right there. I know what you're thinking..."
    
    # Breather, Medina finally gets to present people's alibis to Tony.
    show me sweat2
    me "I'm afraid you'll be disappointed if you're planning on pointing the finger at him."

    l neutral "What do you mean, inspector?"

    show me neutral

    me "Alibis. Out of the hundreds of people attending today's derby, we questioned those who had the closest ties to the victim or were seen near the scene."

    me "That leaves us with these suspects."

    l neutral drop "Really? Just them?"

    show me sweat
    
    me "That's what we're left with after ruling out the possibility of a random attack."

    l neutral right "Just to get this out of the way... What about robbery?"

    show me neutral
    me "His wallet was still on him. There wasn't much inside, just some spare change, his ID, and the like."

    l think closed "I see..."

    me "Anyway, we questioned the most likely suspects separately. Going over everyone's whereabouts together might help us uncover something."

    l neutral "Something...? Does that mean you haven't settled on a suspect, inspector?"

    show me smile
    me "I have. But there's no harm in going over the facts, is there?"

    show me smile3
    me "Especially after all those interruptions from Castillo. A proper review of the case might bring something to light."

    l neutral right "Hm. If you say so..."
    show me neutral
    me "Alright. Let's hear it, then. Tell us what you were doing today between 10 and 11 AM."

    hide me
    show rena angry
    with dissolve
    r "Tch. What a waste of time..."


    # Joint Testimony goes here.
label bigCE:
    default ce_rena_phone = False
    default ce_luca_cloth = False
label bigCE_loop:
    scene placeholder_racetrack1
    show en neutral at slightleft
    show me neutral at slightright
    with fade
    call fx_testimony

    en "Around 10 AM, I was supposed to be overseeing the event's proceedings from the comfort of the luxury observatory in the VIP box..."
    
    show en yell
    en "But the inspector here insisted on following me everywhere!"
    
    show en neutral
    en "She even brought Mr. Castillo along! I had the 'pleasure' of being stuck with the two of them until 10:42 AM."
    
    hide en
    hide me
    show rena neutral at slightleft
    show est neutral at slightright
    with dissolve
    r "I was at the café from 10 AM. I was starving, so I figured I'd grab something to eat."
    
    show rena angry
    r "Anyway, I got a phone call from my trainer about twenty minutes later. Give or take."

    show est smile
    e "At 10 AM, I was taking a smoking break by the grandstands before meeting up with Renata."
    
    show rena neutral
    r "The old man showed up a little while after the call, and we headed to the racetrack to do some preparations."
    
    show rena yell
    r "Anyway, shit hit the fan less than 10 minutes later. We both left to see what all the commotion was about."

    hide rena
    hide est
    show lu frown at slightleft
    show cata neutral at slightright
    with dissolve
    lu "...Don Vicente and I spent some time together at the parade ring around 10 AM. We only stayed together for about ten minutes, though..."

    show lu yell2
    lu "...Although, there was this guy wearing a Hawaiian shirt, a hat, and sunglasses. He kept doting on Lucero without asking for permission."

    show lu frown
    lu "Don Vicente said he'd handle it himself, then went after that person towards the stables. I headed over to the observation area by the grandstands."

    show cata neutral
    c "I took Dama de Plata to the racetrack at 10 AM sharp to practice. We stayed there until the body was discovered."
    
    hide screen status_indicator
    stop music fadeout 2.5
    scene placeholder_racetrack1
    
    hide lu
    hide cata
    show leo eh what
    with fade
    lt "Yikes... talk about an overload of information!"
    show leo think closed drop
    lt "This is a lot to take in..."
    lt "I better write some of it down now before I forget."
    #Dossier- add alibis notes to the Dossier!!!!
    $ dossier.add(de_alibi)
    
    hide leo
    show me angry
    with dissolve
    me "Hey, you're gonna ask them something or not?"
    
    hide me
    show leo neutral drop
    with dissolve
    l "Oh, yes! Yes, I will."
    show leo neutral right
    lt "I wonder if there's anything off about these alibis. Let's find out."
    hide leo
    with dissolve
    #call cutin("cross_examination")
label bigCE_loop_ce hide:
    call CE_start
    call fx_interrogation
    scene placeholder_racetrack1
    show en neutral at slightleft
    show me neutral at slightright
    with fade
    en "Around 10 AM, I was supposed to be overseeing the event's proceedings from the comfort of the luxury observatory in the VIP box..."
    if ce_mode == "object":
        call cutin("objection")
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l neutral "Does it really count as overseeing if you're doing it from up there?"
            show en smile
            en "Most certainly! It offers the best view, after all! You can see the entire racetrack!"
            with fade
    show en yell at slightleft
    show me neutral at slightright
    en "But the inspector here insisted on following me everywhere!"
    if ce_mode == "object":
        call cutin("objection")
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l neutral drop "Huh... Is that true, inspector?"
            show me yell
            me "Damn right it is. I needed answers, one way or another."
            lt eh what "Scary."
            with fade
    show en neutral at slightleft
    show me neutral at slightright
    en "She even brought Mr. Castillo along! I had the 'pleasure' of being stuck with the two of them until 10:42 AM."
    if ce_mode == "object":
        call cutin("objection")
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l neutral "I've got two questions. Are you certain about the time? And why was Mr. Castillo there?"
            show en grin
            en "Absolutely! There are several monitors displaying the news and movies, each with a clock."
            show me angry
            me "I can vouch for that. And as for that scumbag, I wanted to keep an eye on him."
            l think closed "Smart thinking, considering everything... Did he do anything in particular while he was with you?"
            show me neutral
            me "Just his usual nonsense. He spent most of the time on his phone."
            with fade
    hide en
    hide me
    show rena neutral at slightleft
    show est neutral at slightright
    with dissolve
    r "I was at the café from 10 AM. I was starving, so I figured I'd grab something to eat."
    if ce_mode == "object":
        call cutin("objection")
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l neutral "What did you have?"
            show rena smile3
            r "What the hell do you care? You gonna write an article about it and post it online?"
            l closed drop "No, that wasn't what I had in mind... Just carry on."
            with fade
    
    show rena angry at slightleft
    show est neutral at slightright
    r "Anyway, I got a phone call from my trainer about twenty minutes later. Give or take."
    if ce_mode == "object":
        call cutin("objection")
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l neutral "Could you be a little more specific about the time...?"
            show rena yell
            r "You really are insufferable, you know that?"
            lt eh neutral drop "I'm just doing my job."
            show rena angry
            r "Ugh, just look at it yourself. See? 10:17 AM. Close enough, isn't it?"
            l neutral right "I suppose..."
            l neutral "Would you mind if we played the recording? Just to be thorough."
            show rena neutral
            r "Knock yourself out. It's pretty boring shit, though."
            scene black
            with fade
            lt "..."
            lt "Most of the call was just Esteban checking in on Renata, asking where she was and telling her he'd meet her at the café."
            lt "The whole thing lasted about four minutes."
            scene placeholder_racetrack1
            with fade
            lt neutral right "I should make a note of this call."
            $ dossier.add(de_callrecords)
            # Dossier updated!!!!
            with fade
    show rena angry at slightleft
    show est smile at slightright
    e "At 10 AM, I was taking a smoking break by the grandstands before meeting up with Renata."
    if ce_mode == "object":
        call cutin("objection")
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l neutral "Did you notice anything unusual while you were there?"
            show est smile2
            e "I'm afraid not. I was simply relaxing and watching the other jockeys and their horses go by."
            l think closed "I see... and how long did you stay there for, again?"
            show est neutral
            e "About 17 minutes, give or take."
            with fade
    show rena neutral at slightleft
    show est smile at slightright
    r "The old man showed up a little while after the call, and we headed to the racetrack to do some preparations."
    if ce_mode == "object":
        call cutin("objection")
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l neutral "So you left together sometime around 10:24 AM... Were you together the entire time after that?"
            show rena angry
            r "Nah. After he showed up at the café, I went to the restroom while he watched my stuff."
            show est smile2
            e "I even had to pay for her meal while waiting for her return. I dare say it was a rather calculated move on her part."
            show rena smile
            r "Buzz off. I let you use my money to pay!"
            with fade
    
    if ce_rena_phone:
        show rena yell2 at slightleft
        show est neutral at slightright
        r "We left at 10:34 AM! That's when all that corpse-related bullshit happened! I'm NOT lying!"
        if ce_mode == "object":
            call cutin("objection")
            call bigCE_wrong
        if ce_mode == "press":
                $ ce_mode = None
                call cutin("holdit")
                    # Press — Nothing new
                l yell "You're absolutely certain about that, even knowing the body was reported at 10:42?"
                show rena yell2
                r "Maybe the report got the time wrong, then! I KNOW I left that café at 10:24, after meeting the old man!"
                with fade
    else:
        show rena yell at slightleft
        show est smile at slightright
        r "Anyway, shit hit the fan less than 10 minutes later. We both left to see what all the commotion was about."
        if ce_mode == "object":
            call cutin("objection")
            # Press — CONTRADICTION! THEY COULDN'T HAVE LEFT AT 10:34 BECAUSE THE BODY WAS REPORTED AT 10:42 AM!
            if ce_object in [de_victimnotes]:
                call bigCE_Renata
            else:
                call bigCE_wrong
       
        if ce_mode == "press":
                $ ce_mode = None
                call cutin("holdit")
                l neutral "And that's when you came across the body?"
                show rena smile2
                r "Yeah. Turns out Enzo's security staff sucks at their jobs, huh? Letting a murderer in."
                hide rena
                hide est
                show en yell2
                with vpunch
                en "Excuse me!? My security personnel are highly trained professionals, fully equipped to handle any situation!"
                hide en
                with dissolve
                lt eh what "Those same professionals somehow managed to miss a bunch of crooks carrying a body around in broad daylight..."
                play sound se_flash
                lt neutral right "...Wait. When exactly did Renata say they left? Something's weird here..." with flash
                with fade
    
    hide rena
    hide en
    hide est
    show lu frown at slightleft
    show cata neutral at slightright
    with dissolve
    lu "...Don Vicente and I spent some time together at the parade ring around 10 AM. We only stayed together for about ten minutes, though..."
    if ce_mode == "object":
        call cutin("objection")
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l neutral "Since that was the last time he was seen alive, I have to ask... Did he seem any different than usual?"
            show lu smile2
            lu "Not really. He was his usual nagging, straightforward self."
            with fade
    
    if ce_luca_cloth:
        show lu nervous2 at slightleft
        show cata at slightright
        lu "I don't know why those clothes and that notebook were in my locker!"
        if ce_mode == "object":
            call cutin("objection")
            call bigCE_wrong
        if ce_mode == "press":
                $ ce_mode = None
                call cutin("holdit")
                # Press — No new contradiction
                l neutral "Are you absolutely certain none of these things belong to you?"
                show lu nervous
                lu "I am! I swear! I have no idea how they got there!"
                l neutral drop "..."
                with fade
    else:
        show lu yell2 at slightleft
        show cata neutral at slightright
        lu "...Although, there was this guy wearing a Hawaiian shirt, a hat, and sunglasses. He kept doting on Lucero without asking for permission."
        # Press — CONTRADICTION! LUCAS HAS THE HAWAIIAN SHIRT IN HIS LOCKER!
        if ce_mode == "object":
            call cutin("objection")
            $ ce_mode = None
            if ce_object in [de_casualclothes, de_notebook]:
                call bigCE_Lucas
            else:
                call bigCE_wrong
        if ce_mode == "press":
                $ ce_mode = None
                call cutin("holdit")
                l neutral right "Can you remember anything distinctive about this man?"
                show lu neutral
                lu "...Just that he was wearing an orange shirt with flowers on it. Sorry."
                l "That's fine. What exactly was he doing with your horse?"
                show lu angry
                lu "He was petting Lucero and letting him lick his hands. We were worried he might be feeding him something he shouldn't."
                l think closed "I see..."
                with fade
    show lu frown at slightleft
    show cata neutral at slightright
    lu "Don Vicente said he'd handle it himself, then went after that person towards the stables. I headed over to the observation area by the grandstands."
    if ce_mode == "object":
        call cutin("objection")
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l neutral "How long did you stay there?"
            show lu neutral
            lu "About 32 minutes. I was still waiting for Don Vicente to come back when I heard the commotion and headed back to the parade ring."
            l closed "I see..."
            with fade
    # Press
    show lu frown at slightleft
    show cata neutral at slightright
    c "I took Dama de Plata to the racetrack at 10 AM sharp to practice. We stayed there until the body was discovered."
    if ce_mode == "object":
        call cutin("objection")
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l eh what "That's it? Can't you tell me a little more about what you were doing?"
            show cata deadpan
            c "Would you like me to recite my entire training routine? I don't see how that's relevant to the investigation."
            hide lu
            hide cata
            show me angry
            with dissolve
            me "It isn't."
            hide me
            show lu frown at slightleft
            show cata deadpan at slightright
            with dissolve
            l neutral drop "Did you speak to any of the other jockeys, perhaps? Or...?"
            show cata neutral
            c "No."
            lt eh neutral drop "Well, that was incredibly unhelpful."
            #with fade
    # BigCE End

    hide screen ce_ui
    hide screen status_indicator
    hide cata
    hide lu
    show leo neutral right
    with fade
    lt "Let's go over everything... Assuming my math hasn't gotten rusty..."
    show leo think closed
    lt "Lorenzo, Sebastian, and the inspector were together at the luxury observatory from 10 AM until 10:42 AM."
    lt "Renata was at the café since 10 AM. She received a call from Esteban at 10:17 AM. They met at 10:24 AM at the cafe before heading off for the racetrack."
    show leo think closed drop
    lt "But they left at 10:34 AM to investigate the big commotion around Vicente's body."
    lt "Esteban was smoking from 10 AM to 10:17 AM by the grandstands."
    lt "Lucas was with Vicente at the parade ring from 10 AM for about ten minutes. Afterwards, he spent roughly 25 minutes at the observation area by the grandstands."
    show leo eh what
    with dissolve
    lt "...my head hurts."

    hide leo
    show me neutral
    with dissolve
    me "Got all that? Only a handful of these accounts can be independently confirmed, but at least we've got a clearer picture of everyone's whereabouts."
    me "Now, do you have any issues with the alibis?"

    hide me
    show leo neutral right
    with dissolve
    lt "That's a good question. After hearing all of that, is there anything about these alibis that bothers me?"


    if ce_rena_phone and ce_luca_cloth:
        jump act3_thoughtroute
    else:
        menu:
            "Something bothers me":
                # Big problems. (Go back to the interrogation.)
                show leo neutral
                l "I do. There are a couple of more of things I'd like to ask about."
                jump bigCE_loop_ce
            "Nothing bothers me":
                # No problems. (End interrogation.)
                show leo neutral
                l "I think we've covered everything, inspector. We can move on."
                jump act3_continue6    

label bigCE_wrong:
    $ ce_mode = None
    l yell "This piece of proof shows the hole in that statement!"
    hide en
    hide rena
    hide me
    hide lu
    hide cata
    hide est
    show me neutral
    with dissolve
    me "...I don't see anything wrong with it."
    l smile "Are you sure? Maybe you have to check again."
    show me angry2
    me "Or maybe you should check if that mask isn't cutting off the oxygen flow to your brain."
    lt closed drop "Ugh... just tell me I was mistaken. So rude..."
    # Penalty Damage
    call ce_penalty(3)
    hide me
    with fade
    return


label bigCE_Renata:
    $ ce_rena_phone = True
    $ ce_mode = None
    $ ce_rep += 0.5
    stop music fadeout 2.5
    # Objection
    hide rena
    hide est
    hide screen ce_ui
    hide screen status_indicator
    show rena neutral at slightright
    show leo neutral at slightleft
    with fade
    l "Just to make sure I've got this straight... You two left sometime around 10:34 AM?"
    show rena yell
    r "Are you deaf? Yeah."
    show leo think closed
    l "And you left because the discovery of the body caused a commotion."
    show rena smile2
    r "That's right, Captain Obvious."
    show leo yell
    l "That's impossible, Ms. Vargas."
    show rena angry2
    r "Huh? Are you calling me a liar?"
    show leo neutral
    l "Do you know what time the body was reported?"
    show rena yell
    r "Like I said! Sometime around 10:34!"
    call cutin("takethat")
    show leo point
    play sound se_flash
    play music objection fadein 2.5
    l "10:42 AM. You're off by eight minutes." with flash
    show rena frown2
    r "What? But that's not—"
    
    hide leo
    hide rena
    show est neutral
    with dissolve
    e "Perhaps Renata simply got confused about the time...?"
    
    show rena yell2
    hide est
    with dissolve
    r "I'm NOT confused! We met at 10:24 AM, and it wasn't even ten minutes before people started screaming and making a scene!"
    show rena angry2
    r "I know because I checked my phone before we left the café!"
    lt closed "Her timing is clearly off, but she insists she's not mistaken..."
    lt neutral right "Does she have a reason to lie? Or is there something else behind this discrepancy...?"
    lt neutral "I'll have to keep this in mind."
    stop music fadeout 2.5
    with fade
    jump bigCE_loop_ce
    #return
label bigCE_Lucas:
    # Counter response here.
    $ ce_luca_cloth = True
    $ ce_mode = None
    $ ce_rep += 0.5
    hide screen ce_ui
    hide screen status_indicator
    stop music fadeout 2.5
    hide cata
    show leo neutral at slightleft
    show lu neutral at slightright
    with fade
    l "Let me ask you something, Mr. Mendoza. Is this the outfit the man was wearing?"
    
    show lu yell2
    lu "Yes! That's exactly what he had on. But... how do you...?"
    
    show leo yell
    l "I'm having a hard time believing you saw someone else wearing these."
    
    show lu frown
    lu "Huh?"
    
    show leo point
    play sound se_flash
    play music objection fadein 2.5
    l "After all, these clothes were found inside your personal locker!" with flash
    
    show lu nervous
    lu "What!?"

    show leo yell
    l "Care to explain that?"

    show lu nervous2
    lu "I... I don't know! I don't own clothes like that! I really did see someone wearing that outfit!"

    hide lu
    hide leo
    show me sweat2
    with dissolve
    me "Damn. Why does a tacky vacation outfit matter, Leopardo? Do you have something against Hawaiian shirts?"
    hide me
    show leo think closed
    with dissolve
    l "I don't have anything against them, inspector..."
    show leo think yell
    l "It's not the clothes themselves that bother me. It's where they were found."
    show leo neutral
    l "Mr. Mendoza claims he saw someone wearing them, yet they were found in his possession..."
    show leo neutral right
    l "And that's not all. They were found alongside another rather peculiar item."

    show me neutral
    hide leo
    with dissolve
    me "A peculiar item?"
    
    call cutin("takethat")
    hide me
    show leo think closed
    with dissolve
    l "This notebook, to be precise. I'm still trying to make heads or tails of it myself..."
    show me frown
    hide leo
    with dissolve
    me "Let me see that..."
    show me yell
    play sound se_flash
    me "...! Aren't these all the horses that collapsed before their races?" with flash
    hide me
    show leo neutral
    l "So you recognize them too. And it looks like each entry has a monetary value attached to it."
    hide leo
    show me sweat2
    with dissolve
    me "A betting ledger? But all these horses ended up losing... And the last entry is for your own horse."
    show me yell
    me "Care to explain this, Mendoza?"
    hide me
    show lu nervous2
    with dissolve
    lu "I-I don't know anything about that! The notebook isn't mine! Neither are the clothes!"
    show me neutral
    hide lu
    with dissolve
    me "Denying everything isn't going to get you very far..."
    hide me
    with fade
    stop music fadeout 0.5
    jump bigCE_loop_ce

# DELETABLE
# #ONLY WHEN YOU SPOT THE TWO EXISTING CONTRAS THIS SHOULD SHOW UP!!
# label bigCE_bigbrain:
#     lt "Lucas doesn't seem to be lying. But then, how did these things end up in his locker...?"
#     lt "And what about Renata getting the time wrong?"
#     lt "Hmm... Should I take another look at the alibis, or call it here?"
#     # Choice.
#     # Take another look: go back to the CE (possibly set a flag indicating the Lucas contradiction has been found).
#     # If ending the interrogation, skip to selecting a culprit.
#     return

default thought_route_complete = False
label act3_thoughtroute:
    scene black
    show leo think closed
    stop music fadeout 2.5
    with fade
    # Found both contradictions
    lt "..."
    show leo think closed drop
    lt "Gaaah, it's as the inspector said! These alibis are difficult to verify..."
    show leo neutral right
    lt "However, two things stand out after all the questions I asked."
    show leo closed
    lt "First: Renata's account is off by about ten minutes. She's adamant that the body was reported earlier than it actually was."
    show leo neutral
    lt "Second: Lucas had in his possession the very clothes worn by someone he claims was feeding his horse."
    show leo neutral right
    lt "Not to mention that notebook listing all the horses that collapsed during previous races..."
    show leo closed drop
    lt "Both of them are sticking to their stories despite the evidence. What am I supposed to make of this...?"
    show leo yell
    lt "Guess it's time to give the ol' noggin a good workout. I'm gonna go over the facts one more time."
    play music thought_route fadein 2.5

    #Thoughtt route!!!
    #make a thought route bg for this part
    #with fade
    label rock_kick_shovel:
        show leo think closed
        with fade
        l "According to Lucas, Vicente left the parade ring to pursue someone wearing an orange Hawaiian shirt."
        l "That would have led him to the stables."
        l "When he caught up with that person, he was attacked with..."

        menu:  
            "A shovel":
                jump tr_shovel
            "A rock":
                jump tr_rock
            "A roundhouse kick":
                jump tr_kick
        label tr_rock:
                show leo think closed drop
                l "Um... no, I don't think a rock was used at all. At least, none has been found so far with the victim's blood."
                l "Focus, me!"
                jump rock_kick_shovel
        label tr_kick:
                show leo think closed drop
                l "If the death blow was a kick to the head, that must have been one hell of a martial artist to pull off such a fatality."
                l "But this isn't a kung fu movie... think! I know I found a likely murder weapon!"
                jump rock_kick_shovel
        label tr_shovel:
            l "The shovel is the most likely weapon. It has a dent in it, and the victim's blood was found on it."
            l "That means blood must have been left behind at the scene."
            jump call4help
            
    label call4help:
        show leo think closed
        l "After killing Vicente, the culprit..."
        menu:
            "Ran away in a panic":
                jump tr_panic
            "Called for help":
                jump tr_help
           
        label tr_panic:
            show leo think closed drop
            l "I mean. I am sure they were feeling panicked and all..."
            l "But if they just ran off, it wouldn't explain why the body wasn't found at the stables."
            jump call4help
    
        label tr_help:
            show leo think closed
            l "Castillo's underlings have already confessed to helping cover up the murder."
            l "They put the body inside that black body bag and threw it from the grandstands."
            l "So the culprit must have called them in to help dispose of the body!"
            l "But that still leaves one question..."
            l "What did the culprit do after leaving the stables?"
            show leo think closed drop
            l "..."
            show leo think closed
            l "...Maybe I need to approach this from another angle."
            l "The murder method itself is more or less established. I should focus on what's still unexplained."
            l "For starters..."
            jump locker_items
    label locker_items:
        show leo think closed
        l "Lucas and that orange Hawaiian shirt."
        l "He insists neither the clothes nor the notebook belong to him."
        l "So the reason those items ended up in his locker must be..."
        menu:
            "He forgot he put them there":
                jump tr_forgot
            "Someone else put them there":
                jump tr_someone_else        
            "He's lying about not putting them there":
                jump tr_lying

    label tr_forgot:
        show leo think closed drop
        l "If he'd simply forgotten about them, he should have recognized them when I brought them up."
        l "Besides, why would he draw attention to something incriminating in his own locker?"
        jump locker_items
    label tr_lying:
        show leo think closed drop
        l "If he were lying, why would he draw attention to the clothes he's trying to conceal in the testimony?"
        l "His story would only make things worse for him."
        jump locker_items

    label tr_someone_else:
        show leo think closed
        l "Someone deliberately planted the orange shirt and the notebook in his locker."
        l "That's certainly possible, assuming Lucas is telling the truth."
        l "But who would have done it?"
        menu:
            "Vicente":
                jump tr_vicente
            "Hawaiian-shirt person":
                jump tr_hawaiia
            "Catalina":           
                jump tr_catalina
    label tr_vicente:
        show leo think closed drop
        l "Wait, wasn't Vicente the one chasing the man with the orange clothes...?"
        l "Why would he just grab those and randomnly drop them in Lucas' locker?"
        l "I might be overthinking this..."
        jump tr_someone_else
    label tr_catalina:
        show leo think closed drop
        l "That doesn't make any sense... Catalina doesn't have any reason to plant those items."
        l "Plus, I'm pretty sure they mentioned it was a man who was wearing them."
        l "Lucas would had immediately recognized it was a blonde woman if it really was Catalina."
        jump tr_someone_else
    label tr_hawaiia:
        show leo think closed
        l "Of course! The man wearing those clothes must have been the one who planted them, along with the notebook."
        l "But why? What did he stand to gain?"
        l "He could have disposed of the evidence almost anywhere..."
        l "...Wait. He could have put them anywhere, but he chose Lucas's locker."
        l "That's because..."
        menu:
            "He wanted them to be found":
                jump tr_found
            "He brought Lucas a change of clothes":
                jump tr_clothes
    label tr_clothes:
        show leo think closed drop
        l "He brought Lucas fresh clothing... that doesn't sound right."
        l "He flee when followed, so that already implies not wanting to run in them."
        l "Plus, if it was just spare clothing, he would had at least told Lucas about it."
        l "But it didn't seem to me like Lucas was expecting any new batch of clothes coming today."
        jump tr_hawaiia
    label tr_found:
        show leo think closed
        l "He wanted them to be found! That's why he left them in Lucas's locker."
        l "Come to think of it, the locker was even left wide open..."
        l "And it wasn't just the clothes. The notebook was planted there too."
        l "Both items would immediately make Lucas look guilty if someone discovered them."
        l "But why would having that notebook and those clothes be so incriminating?"
        l "The notebook lists several racehorses, alongside a series of monetary values."
        l "And almost every entry has been crossed out..."
    label tr_notebook:
        show leo think closed
        l "I should take a closer look at what this notebook actually represents."
        l "What do all the horses listed in this notebook have in common?"
        menu:
            "The horses won":
                jump tr_won
            "The horses are cool":
                jump tr_cool
            "The horses lost":
                jump tr_lost

        label tr_won:
            show leo think closed drop
            l "The horses won.... no, I'm sure that's definitely wrong."
            l "Yes, they might have won some of their races, but these made the headlines because they collapsed and lost the race."
            l "Perla Negra is the one I can remember most vividly."
            jump tr_notebook
        label tr_cool:
            show leo think closed drop
            l "All of the horses are, in fact, very cool, majestic creatures."
            l "..."
            l "But that doesn't help me get any closer to solving things!"
            l "Focus, Tony...!"
            jump tr_notebook
        label tr_lost:
            show leo think closed
            l "Even a quick online check of the race results confirms it. Every horse with a crossed-out entry lost after collapsing during its race."
            l "Except for the last one: Lucero."
            jump tr_losing_horse
    label tr_losing_horse:
        l "If an entry is crossed out, that usually means it's been dealt with..."
        l "Wait. I think I'm onto something."
        l "If every name has been crossed out except one, then that means..."
        menu:
            "Lucero is a winning horse":
                jump tr_winning_horse
            "Lucero is a losing horse":
                jump tr_loser_horse
        label tr_winning_horse:
            show leo think closed
            l "Go, Lucero! You are a winner!"
            show leo think closed drop
            l "...I don't think that's what the notebook is trying to convey..."
            jump tr_losing_horse
    label tr_loser_horse:
            show leo think closed
            l "Lucero is supposed to lose. But I checked the race results, and he hasn't collapsed like the others."
            l "His name hasn't been crossed out yet..."
            l "He's supposed to lose, but his entry is still untouched. That must mean..."
            menu:
                "He'll become a legendary horse":
                    jump tr_legend
                "His loss hasn't happened yet":
                    jump tr_loss
    label tr_legend:
        show leo think closed drop
        l "No... that seems wrong." 
        l "If I believed a horse would become legendary, I would never put them in this notebook."
        jump tr_loser_horse
    label tr_loss:
        show leo think closed
        l "Exactly! His name hasn't been crossed out because his loss hasn't happened yet."
        l "He's being targeted for an upcoming race!"
        l "And that's right... that man was doting on Lucero!"
        l "He wasn't just petting the horse. He was doing something to sabotage him!"
        l "But that still doesn't explain the monetary values..."
        l "Even by clandestine standards, these figures are a little too specific."
        l "And there's a pattern to them, too..."
    label tr_compensation:
        show leo think closed
        l "The amount listed for Perla Negra is considerably higher than the one for Lucero."
        l "Could it have something to do with the horses' reputations?"
        l "The more prestigious the horse, the higher the amount..."
        l "Hmm... these numbers here... what do they represent?"
        menu:
            "How much it will cost to heal them":
                jump tr_heal
            "How much money one gains if they lose":
                jump tr_moneygain
            "How much money one loses if they lose":
                jump tr_moneylose

        label tr_heal:
            show leo think closed drop
            l "I doubt it. A lot. If these were medical expenses, why would someone be recording them alongside horses that collapsed during races?"
            l "Besides, if they were paying for treatment, they'd have to be warning the owners..."
            jump tr_compensation
        label tr_moneylose:
            show leo think closed drop
            l "Why would someone sabotage these horses if they were losing money every time one collapsed!?"
            l "That'd be one hell of a masochistic business model! I should rethink this."
            jump tr_compensation
    label tr_moneygain:
        show leo think closed
        l "Compensation... That's it!"
        l "Someone is being paid every time one of these horses is made to collapse!"
        l "That would explain why the amounts differ. The more prestigious the horse, the higher the compensation for sabotaging it."
        l "And if Lucero is listed here, that means someone is being paid to make him collapse next..."
        l "This isn't just someone tampering with racehorses."
        l "It's an organized operation. {color=#FF0000}Someone is paying people to rig the races{/color}!"
        jump tr_rena1
    label tr_rena1:
        show leo think closed
        l "That leaves the matter of Renata's alibi."
        l "She keeps insisting they left at 10:34, even though the body wasn't reported until 10:42."
        l "That's an eight-minute discrepancy. I don't think I should just dismiss it..."
        l "Why did Renata mistake the time of the body report?"
        menu:
            "She doesn't know how to count":
                jump tr_rena_count
            "She wanted to fabricate an alibi":
                jump tr_rena_alibi
            "Her phone's time was off":
                jump tr_rena_off
        label tr_rena_count:
            show leo think closed drop
            l "Haha... in all seriousness, insulting her in my mind won't give me a real answer."
            l "I should refocus..."
            jump tr_rena1
        label tr_rena_alibi:
            show leo think closed drop
            l "Would she really go through all that trouble to fabricate an alibi?"
            l "She had no way of knowing Esteban would call her, let alone when."
            l "And the call itself would leave a timestamped record..."
            l "No, that doesn't add up. I should refocus..."
            jump tr_rena1
        label tr_rena_off:
            show leo think closed
            l "Her phone's time was off... but in what way?"
            menu:
                "Ten minutes slow":
                    jump tr_rena_slow
                "Ten minutes fast":
                    jump tr_rena_fast
                "The time was correct":
                    jump tr_rena_correct

            label tr_rena_fast:
                show leo think closed drop
                l "No, that doesn't sound right. If her clock were ten minutes fast, she would've found out about the commotion at 10:52 AM."
                l "She definitely didn't say that. Let's think this through again..."
                jump tr_rena_off

            label tr_rena_correct:
                show leo think closed drop
                l "No, no... if the time was correct, then this body discovery discrepancy wouldn't had happened in the first place!"
                l "Think, Tony, think...!"
                jump tr_rena_off
            label tr_rena_slow:
                show leo think closed
                l "If her phone was ten minutes slow, then technically, what she's saying is true."
                l "The discovery at 10:42 would have appeared as 10:32 on her phone."
                jump tr_rena2             
    label tr_rena2:
        show leo think closed
        l "Wait... If she's basing her entire alibi on that clock, then she wasn't at the café at 10:00, but at 10:10 AM!"
        l "Everything shifts forward by ten minutes..."
        l "Her meeting with Esteban would have been at 10:34 instead of 10:24."
        l "And they would have left at 10:42, right when the body was discovered."
        l "That's quite a coincidence..."
        l "But why would her phone be running ten minutes slow in the first place?"
        menu:
            "It was broken":
                jump tr_rena_broken
            "Someone changed its time":
                jump tr_rena_changed
        label tr_rena_broken:
            show leo think closed drop
            l "Nah, if her phone was broken I would had noticed when she showed it to me."
            l "Renata or the inspector would had mentioned it too. I need to re-think this."
            jump tr_rena2
        label tr_rena_changed:
            show leo think closed
            l "Nowadays, phones synchronize their clocks automatically."
            l "You'd have to go out of your way to change the time manually."
            jump tr_rena3
    label tr_rena3:
        show leo think closed
        l "Changing the clock could certainly make someone's alibi look convincing, especially when they're relying on their call history..."
        l "But that wouldn't fool the phone provider. Their records would still show the actual time of the calls."
        l "It's risky, but if the timing is carefully arranged, it could work."
        l "But that leaves one question..."
        l "Who changed Renata's phone clock?"
        menu:
            "Renata herself":
                jump tr_rena_herself
            "Someone else":
                jump tr_rena_someone
        label tr_rena_herself:
            show leo think closed drop
            l "Renata could have changed the clock herself, sure..."
            l "...but that would only make sense if she were the one making the call."
            l "She had no way of knowing when she'd receive a call, if at all."
            l "Which means there's virtually no reason for her to deliberately change her phone's time."
            jump tr_rena3
        label tr_rena_someone:
            show leo think closed
            stop music fadeout 2.5
            play sound se_flash
            l "{color=#FF0000}Someone else tampered with her phone's clock...{/color}! That's it!" with flash
            l "It would explain why she's so adamant that the times are correct, even when they aren't."
            l "Besides, if Renata had done it herself, her account of the meeting wouldn't necessarily match Esteban's."
            l "Hell, she couldn't even have known there WOULD be a meeting to account for!"
            l "She couldn't have known when he'd call her, either."
            l "Their accounts would have to match, down to the minute."
            l "...."
            l "So that's it..."
            l "{color=#FF0000}Someone is being paid to sabotage the horses{/color} listed in the notebook and tried to frame Lucas for it..."
            l "...and the time in {color=#FF0000}Renata's phone was tampered{/color} with without her knowledge!!"
            $ thought_route_complete = True
            jump act3_thoughtrouteComplete
    #THOUGHT ROUTE FINISH!!!!!!
label act3_continue6:
    scene placeholder_racetrack1
    with fade
    # Did not find both contradictions
    lt neutral right "Most of them spent their time alone, so it's certainly difficult to verify or disprove their alibis..."
    lt closed drop "Nothing in particular stands out to me right now."
    label act3_thoughtrouteComplete:
    scene placeholder_racetrack1
    show me neutral at slightright
    with fade
    # Both converge here. Finding the contradictions helps uncover the truth!

    me "Well? Any thoughts you'd like to share?"

    lt think closed "..."

    show en neutral at slightleft
    with dissolve

    en "Ahem. I don't mean to interrupt your diligent efforts to bring this nefarious murderer to justice, inspector, but..."

    show me angry
    me "What is it?"

    show en nervous3
    with dissolve
    en "Well, we're only twenty minutes away from the start of the event! People need to get to their posts and make their final preparations."

    show me yell
    me "You're aware that Castillo was involved in moving the body, correct?"

    show en nervous2
    en "I'm aware of that, yes—"

    show me angry
    me "And you know his underlings were involved as well."

    show en yell3
    en "Yes, I know that too—"

    show me yell2
    me "Those are serious offenses. It's called obstruction of justice."

    show en yell
    en "I understand! But I must insist that this matter be resolved, one way or another, so we can get on with the event!"

    show me angry2
    me "You're in no position to make demands—"

    play sound se_flash
    play music leo fadein 2.5
    l grin shine "It's quite alright, inspector! For I, El Leopardo, have glimpsed the answers we've all been seeking!" with flash

    show me sweat
    me "What?"

    show en grin
    en "Oho! So you've figured out who the culprit is, Mr. Leopardo? Magnificent!"

    hide en
    hide me
    
    show rena angry at left
    show cata neutral at right
    show lu yell1
    with dissolve
    lu "Who is it? Who killed Don Vicente!?"

    l neutral drop "Ah—"

    show rena yell2
    r "Come on! We've got other things to do! Spit it out!"

    l "Yes, I understand, but—"

    c "Despite your rather suspicious appearance, you managed to dismantle Castillo's ridiculous claims without breaking a sweat."

    show cata smile
    c "If you know who's behind this, then you should tell us."

    l closed "..."

    $ renpy.music.set_volume(0.4, delay=1.0, channel="music")

    lt closed drop "What a pickle. All I wanted to do was establish how the murder was carried out..."

    lt neutral right "But now everyone's waiting for an answer, and time is running out. I'll just have to take a shot in the dark and hope for the best."

    lt closed "Based on everything I've gathered, the culprit attacked Vicente in the stables..."

    lt neutral "...then stuffed his body into a bag and had it transported all the way to the top of the grandstands, where it was thrown over the railing."

    lt neutral right "Castillo's underlings were definitely involved, which means the possibility of accomplices can't be ruled out."

    lt "Is there anyone else connected to the Castillos besides Renata...?"

    lt closed "Hmm..."

    lt neutral "The horse collapses, the clandestine betting, the motive for murder..."

    lt "There has to be a connection between all of them...!"

    l yell "The culprit is..."


    menu BigCECulpritChoice:
        "El Leopardo":
            jump choose_leo
        "Catalina":
            stop music fadeout 2.5
            jump choose_cata
        "Lucas":
            jump choose_luc
        "Renata":
            jump choose_rena
        "Esteban":
            jump choose_este
        "Medina":
            jump choose_med
        "Lorenzo":
            jump choose_enzo
        "Sebastian":
            jump choose_seba
        "Sebastian's underlings":
            jump choose_thugs

    label choose_cata:
        scene placeholder_racetrack1
        show leo closed at slightleft
        show cata smile at slightright
        with fade
        play music intense fadein 2.5
        l "..."
        show leo point
        l "Catalina Moreno... you are the murderer!"
        
        hide leo
        hide cata
        show rena frown2
        with dissolve
        r "Holy shit, the Ice Queen is the killer!?"
        
        show cata surprise at slightright
        show leo point at slightleft
        hide rena
        with dissolve
        c "..."
        
        show cata yell
        c "What on earth are you doing?"
        
        hide leo
        hide cata
        show me angry
        with dissolve
        me "I'd like to know too. Why are you accussing her, out of all people?"
        
        show leo neutral right at slightleft
        show cata angry at slightright
        hide me
        with dissolve
        l "As you know, her alibi is shaky at best..."
        
        show leo neutral
        l "But Ms. Moreno's relationship with the victim was already strained, unlike the others."
        
        show cata yell
        c "What are you babbling about now? I don't remember having a single exchange with that man."
        
        show leo yell
        l "Maybe. Or maybe not. He saw you in a poor light due to the rumors. Isn't that right, Mr. Mendoza?"
        
        hide leo
        hide cata
        show lu frown
        with dissolve
        lu "W...We did talk about those rumors, but I don't know how true they are..."
        
        hide lu
        show leo neutral at slightleft
        show cata angry at slightright
        l "That's of little consequence. Wherever they are true or not, what matters is how would Ms. Moreno react to it."
        
        show cata angry2
        c "..."
        
        show leo yell
        l "It must have been infuriating, tolerating all these people besmirch your name."
        
        show leo point
        l "So you finally took it upon yourself to teach one of them a lesson!"
        
        show cata yell2
        c "Are you quite done?"

        show leo neutral drop
        stop music fadeout 2.5
        l "Huh...?"
        
        show cata angry
        c "I can't believe what I have to listen to. I had the faintest of trust placed on you..."
        
        show cata frown
        c "And this is how you repay me?"
        lt "What...? Faith in me?"
        
        show cata yell
        c "Is that all you have to say? Frankly, I don't have time to waste on nonsense."
        
        hide cata
        hide leo
        show me neutral
        with dissolve
        me "So you deny the allegations?"
       
        hide me
        show cata angry2
        with dissolve
        c "I don't even have to. They are so idiotic and lack an actual basis, that it's a waste of breath on my end."
        
        hide cata
        show me angry
        with dissolve
        me "Even so... the fact remains your alibi remains unconfirmed."
        
        hide me
        show cata frown2
        with dissolve
        c "..."
        
        hide cata
        show me frown
        with dissolve
        me "Looks like a standstill to me. Sorry, but I am going to take you in for questioning."
        
        hide me
        show cata nervous
        with dissolve
        c "Hold on, you can't do that. If you do, I am going to miss out on the race."
        
        hide cata
        show me yell
        with dissolve
        me "A man is dead, and all you care about is some puny event-"
        
        hide me
        show cata nervous2
        with dissolve
        c "Be quiet! How is my absence from the race going to tell you who did this!?"
        show cata nervous3
        c "My whereabouts will be the same, no matter how much you ask the same questions over and over!"
        
        hide cata
        show me frown
        with dissolve
        me "..."
        
        hide me
        show rena smile3 at slightleft
        show est neutral at slightright
        with dissolve
        r "Don't take it so personal, Catalina. Poor inspector there is just doing her work."
        show est frown
        e "Easy now, Renata. She's clearly under a lot of stress..."
        
        hide est
        hide rena
        show cata nervous1
        with dissolve
        c "This is revolting, there are far more likely suspects and you'll jeopardize me?"
        
        hide cata
        show me yell
        with dissolve
        me "Alright, that's enough. We'll be standing all day here arguing at this rate. Take her away."
        
        hide me
        show cata nervous2
        with dissolve
        c "Maybe you should instead take in the inconsiderate man in the mask, instead!"
        show cata nervous3
        c "Parading around like that is far more suspicious than anything I have done...!"
        lt think closed drop "D-Damn, I really pushed her buttons this time... multiple police officers manage to take her away, her shouts of complaints fading in the air."
        
        scene black
        with fade
        l "..."
        l "With an unclear suspect, all the people were questioned one by one..."
        l "...but thanks to me, Catalina missed out on the Razing Thunder race."
        l "Obviously, I was fired, so I wasn't exactly allowed to stay at the derby."
        l "The case went cold, and I never found who the culprit was."
        l "Worst of all, sometime later, a couple of police officers came to my work place to arrest me."
        l "It had seem Catalina learned of my true identity, and took it upon herself to let them know."
        l "I denied it, of course, but that didn't help much. The inspector wasn't able to turn a blind eye this time."
        l "Or maybe she didn't intend to after how things ended. Either way..."
        l "With my freedom gone, I won't be able to continue my fight against evil- let alone figure out the killer of this case."
        l "Betraying Catalina spiralled into all of this... what have I done..?"
        call game_over
        return
    label choose_rena:
        scene placeholder_racetrack1
        show leo point at slightleft
        show rena angry2 at slightright
        with fade
        play music intense fadein 2.5
        
        play sound se_flash
        l "Renata Vargas, you are the culprit!" with flash

        show rena yell2
        r "What the fuck did you say!?"

        r "Get real! I'm no damn killer!"

        hide leo
        hide rena
        show me yell
        with dissolve
        me "Leopardo, what are you basing this on?"

        show rena angry2 at slightright
        show leo think closed at slightleft
        hide me
        with dissolve
        l "Ms. Vargas is one of the suspects without a clear alibi..."

        show leo neutral
        l "Not to mention her connection to the Castillos. She's sponsored by them."

        show leo point
        l "It isn't a stretch to say she could have enlisted their help to dispose of the body!"
        
        hide leo
        hide rena
        show me sweat2
        with dissolve
        me "...That is a possibility. Castillo's company has every reason to promote her image and boost its own by having her win."

        show me angry
        me "Eliminating the competition would further that agenda."

        hide me
        show rena yell2 at slightleft
        show est neutral at slightright
        with vpunch
        r "Oh, this is so not happening! I hate those people as much as the next person!"

        show rena angry2
        r "Come on, old man! Tell them! It's not me!"

        show est frown
        e "..."

        show rena frown
        r "Old man...?"

        show est frown2
        e "I'm sorry, Renata. They're right about you being in a favorable position."

        show rena nervous
        r "Not you too...!"

        show est neutral
        e "I can vouch for her not being the kind of person who would resort to murder... but..."

        show est frown
        e "I also know how ambitious she is. How badly she wants to prove herself and establish herself as the very best."

        show rena nervous2
        r "You've got to be kidding me..."

        hide rena
        hide est
        show me neutral
        with dissolve

        me "That's probably cause in my book. You're under arrest, Ms. Vargas."

        show rena nervous3
        hide me
        with dissolve
        r "No! I'm not missing the Derby race over this crap!" 
        
        show rena yell2
        r "This is YOUR fault!"

        # Wham! She punches Leopardo.
        
        hide rena
        show leo closed drop
        play sound se_punch2
        with vpunch
        l "Agh!"

        lt "Medina and several officers step in to restrain Renata as I watch from the ground, holding my bruised face."

        lt "Yeowch... She packs a punch."

        show rena yell2
        hide leo
        with dissolve
        r "I won't forget this, you masked bastard!"

        show me yell
        hide rena
        with dissolve
        me "Take her away!"
        
        hide me
        show rena nervous4
        with dissolve
        r "Let me go! I didn't do it!"
        
        scene black
        stop music fadeout 2.5
        with fade

        # Fade into black.


        l "..."

        l "The race continued as scheduled. All the competitors gave it their very best..."

        l "Lucas was on his way to securing first place, with Catalina close behind in second."

        l "But then, something unexpected happened. His horse collapsed, just like the others in the previous incidents."

        l "The race wasn't stopped or postponed this time, though. Not with Lorenzo's wishes to push forward."

        l "When all was said and done, Catalina seemed utterly disappointed with how things had turned out..."

        l "...and decided against accepting her prize, leaving the Derby altogether."

        l "The police had decided to resume their investigation after the race, and they got to work..."

        l "But despite Lorenzo's now-willing cooperation, with things having finally calmed down..."

        l "They failed to find any conclusive evidence of Renata's guilt."

        l "She was eventually released, but in this kind of elite competition, there are no second chances."

        l "The Castillos cut all ties with her despite the allegations being disproven, closing many doors for her in the industry."

        l "She's a fighter, so she hasn't given up yet, but I hear she's having a pretty rough time."

        l "My accusations had wrongfully sabotaged someone's life. Ironically..."

        l "...they had also allowed the real perpetrator to escape."

        l "Maybe I should consider retiring as a detective if this is the kind of harm I cause..."

        # End the game here
        call game_over
        return
    label choose_seba:
        scene placeholder_racetrack1
        show leo point at slightleft
        show me neutral at slightright
        with fade
        play music intense fadein 2.5
        l "The culprit is none other than Sebastian Castillo!"

        show leo closed think

        l "After having his subordinates dispose of the body and attempting to pass off Vicente's death as nothing more than an accident..."

        show leo think yell
        l "He then tried to pin it on an innocent bystander!"

        show me sweat2
        me "..."

        me "That would be a plausible theory, and everything you've mentioned is true, yes."

        show me neutral
        me "But you're missing one small detail."

        show leo neutral
        l "Huh? What's that?"

        show me yell2
        with vpunch
        me "I was with him. At the time of the murder!"
        
        show leo neutral drop
        l "..."
        stop music fadeout 2.5
        play music eccentric fadein 2.5

        show leo closed drop
        l "Ooohh..."

        show me angry2
        me "Don't 'oh' me! Were you not paying any attention!?"

        hide leo
        hide me
        show en neutral
        with dissolve
        en "My, it must have been quite a traumatic and exhausting ordeal if Mr. Leopardo managed to overlook such an important detail."

        en "Once again, I was also present with the two of them. I assure you, the inspector speaks the truth."

        hide en
        show me yell
        with dissolve
        me "Not that I'd lie about it to begin with. Do you think I enjoy giving that dirtbag an alibi?"

        show leo think smile drop
        hide me
        with dissolve
        l "I-I see. Well, let me give it another try..."
        
        hide leo
        show me angry
        me "No. You're clearly out of your depth. Castillo is definitely involved in some shady business, but Vicente's murder isn't one of them. Not directly, at least."

        hide me
        show leo eh what
        with dissolve
        l "T-Then maybe he sent someone to carry out his orders...?"

        show me yell2
        hide leo
        with dissolve
        me "...Throwing out random guesses isn't going to do you any good. We're done here."
        
        show me angry2
        me "I'm going to resume the investigation after the race. What a waste of my time..."

        hide me
        show leo closed drop
        with dissolve
        l "..."

        stop music fadeout 2.5

        scene black
        with fade

        l "..."

        l "And with that, my involvement in the case came to an end."

        l "I didn't pay much attention to the race results. All I cared about was finding the truth behind Vicente's death."

        l "But I failed to do so."

        l "Days after the Derby, I learned that the search for the culprit had gone nowhere."

        l "By that point, any evidence that could have closed the case had long since disappeared."

        l "Not only had the real culprit gotten away, but Sebastian had managed to exploit a technicality and remain free."

        l "He's been sending his goons after me day after day to 'repay the favor' for our little encounters."

        l "I've fought them off as best I could, but one ambush caught me off guard."

        l "So this is the last thing I'll see, huh...? A bunch of crooked smiles and bright suits."

        l "Damn... it..."
        call game_over
        return
    label choose_leo:
        scene placeholder_racetrack1
        show leo point
        with fade
        play music intense fadein 2.5
        l "Actually, I'm the one who reaped Mr. Ruiz's soul. It was me."

        hide leo
        show en yell3 at left
        show lu angry at right
        show me angry
        with dissolve
        en "What!?"
        
        show lu angry2
        lu "You!?"
        
        show me yell
        stop music fadeout 2.5
        me "Have you gone completely insane!? You just finished proving that it couldn't have been you!"

        hide me
        hide en
        hide lu
        show rena frown at slightleft
        show cata surprise at slightright
        with dissolve
        r "Huh? I thought he just proved that Antonio guy was innocent."
        
        play music eccentric
        show cata deadpan2
        c "…"

        hide cata
        hide rena
        show leo grin closed
        with dissolve
        l "…Oh! I guess you're right! Just a little joke to lighten the mood, haha!"

        hide leo
        show me yell2
        with dissolve
        me "…"

        show me angry2
        me "…"

        show leo grin closed
        hide me
        with dissolve
        lt "The inspector snaps a pair of handcuffs around my wrists while I desperately try to laugh it off."

        show leo grin
        l "Haha… Wait, what-?"

        show me yell
        hide leo
        with dissolve
        me "Play stupid games, win stupid prizes."

        show me angry
        me "You can continue your little joke down at the station."

        show leo neutral drop
        hide me
        with dissolve
        l "Wait, inspector! I'm not done with this case yet!"

        show leo yell
        l "Inspectoooooor!"
        stop music fadeout 2.5

        scene black
        with fade

        l "And just like that, I'm hauled away after my little 'confession'. My identity has been exposed, I'm being charged with murder, and now I'll have to wait for a lawyer before facing trial."

        l "What happened to the race? Who really killed Vicente? I'll never get to know the truth now…"
        call game_over
        return

        #Game over.
    label choose_med:
        scene placeholder_racetrack1
        show leo point
        with fade
        play music intense fadein 2.5
        #Accuse Medina
        play sound se_flash
        l "It was none other than inspector Medina herself!" with flash
        
        hide leo
        show en yell3
        with dissolve
        en "What!? The good inspector has been plotting to sabotage my glorious event through this senseless violence!?"

        show leo point
        hide en
        with dissolve
        stop music fadeout 2.5
        lt "I'm promptly slapped with a pair of handcuffs following my accusation."

        l "Eh?"

        hide leo
        show me angry2
        with dissolve
        me "No. Just... no."

        show leo yell
        hide me
        with dissolve
        l "H-Hey, wait a moment-"

        hide leo
        show me yell2
        with dissolve
        me "First off, I have an alibi! I've been busting my ass investigating this place!"

        show me angry2
        me "Second, I have absolutely no motive to attack that man!"

        show leo neutral drop
        hide me
        with dissolve
        l "Inspector-"

        show me angry
        hide leo
        with dissolve
        me "And third! I. Am. With. The goddamn. POLICE!"

        show leo smile drop
        hide me
        with dissolve
        l "I mean... that doesn't necessarily guarantee-"

        show me yell2
        hide leo
        with dissolve
        me "Oh, you're actually going there!? If you're going to accuse me of being some kind of corrupt cop who also happens to be a serial killer targeting random strangers,"
        me "then you'd better have some damn good evidence!"

        show me angry
        me "Well!?"

        hide me
        show leo closed drop
        with dissolve
        l "…"

        show me yell2
        hide leo
        with dissolve
        me "That's what I thought. Get him the hell out of here."

        scene black
        with fade

        l "And just like that, I'm hauled away by the police."

        l "What happened to the race? Who really killed Vicente? I'll never get to know the truth now…"

        l "The inspector will ensure El Leopardo stays inactive for good now that I've been detained again."

        l "It's all over..."
        call game_over
        return

        # Bad End.
    label choose_enzo:
        #Accuse Villareal
        scene placeholder_racetrack1
        show leo point
        with fade
        play music intense fadein 2.5
        play sound se_flash
        l "It was Villareal! He's the mastermind behind this whole affair!" with flash
        hide leo
        show en yell3
        with dissolve
        en "Whaaaaaat!?"

        hide en
        show me sweat2
        with dissolve
        me "What the hell are you basing that on?"

        show leo yell
        hide me
        with dissolve
        l "Well, the man's greedy as hell. Wouldn't surprise me if Vicente owed him a few bucks, failed to pay up, and ended up on the receiving end of his revenge."

        show me yell
        hide leo
        with dissolve
        me "Being greedy doesn't make someone a murderer. We looked into the victim's affairs, and there's nothing suggesting Vicente owed Villareal any money."

        hide me
        stop music fadeout 2.5
        play music enzo fadein 2.5
        show en yell2
        with dissolve
        en "That's right! I'm not in the debt collection business!"

        show en nervous
        en "I've been hounded by the inspector here practically nonstop! I haven't had a moment to myself, let alone an opportunity to attack anyone!"

        show en yell2
        en "And why, in God's green earth, would I want to murder one of the jockeys or trainers invited to this exclusive event!?"

        show en angry
        en "That would throw the entire competition into chaos and bring everything to a halt! Look at the mess we're in already!"

        hide en
        show leo closed drop
        l "E-Err..."

        show me sweat
        hide leo
        with dissolve
        me "..."
        
        show me sweat2
        me "Guess I got my hopes up a little too much, huh?"
        stop music fadeout 2.5

        show me neutral
        me "I'll take it from here. You're dismissed."
        
        show leo yell
        hide me
        with dissolve
        l "Huh? No, I can still-"

        show me yell2
        hide leo
        with dissolve
        me "You're done. Out."

        show leo think closed drop
        hide me
        with dissolve

        l "..."

        scene black
        hide leo
        with fade
        lt "What happened to the race? Who really killed Vicente? I'll never get to know the truth now…"
        call game_over
        return
    label choose_thugs:
        scene placeholder_racetrack1
        show leo think closed
        with fade
        play music intense fadein 2.5
        l "Castillo's underlings were acting on orders to conceal evidence."
        show leo yell
        l "So it's certainly possible that one of them was also responsible for carrying out the murder."

        hide leo
        show me neutral
        with dissolve
        me "It's possible, but we don't have anything pointing to any one of them in particular..."

        show me angry
        me "Although, I suppose that would technically mean Castillo himself orchestrated the whole thing."

        show me smile
        me "If that's the accusation you're making, then I suppose we can consider the matter settled and investigate things further with that in mind."
        stop music fadeout 2.5
        scene black
        hide me
        with fade
        l "Castillo ordering his men to get rid of someone seemed to make a lot of sense."
        l "Until it didn't. Despite the inspector following that trail, nothing came out from it."
        l "The race continued its course, then tragedy struck at it's peak..."
        l "...but even then, things carried on as usual. And the truth was lost forever."
        call game_over
        return
    label choose_luc:
        #Choose Lucas
        scene placeholder_racetrack1
        show leo neutral at slightleft
        show lu neutral at slightright
        with fade
        l "Out of all the people here, he was the one closest to the victim, with ample opportunity to carry out the attack..."
        show leo point
        play sound se_flash
        play music intense fadein 2.5
        l "That's right, Lucas Mendoza!" with flash

        show lu yell
        lu "What...!?"
        show lu yell1
        lu "M-Me!? You're accusing me!?"

        show lu angry2
        lu "Here I was starting to believe you could actually find out who did it..."
        show lu yell1
        lu "You're wrong! I would never hurt Don Vicente like that!"

        hide leo
        hide lu
        show rena neutral at slightleft
        show cata frown2 at slightright
        with dissolve

        c "That really does sound unlikely. You'd better have a good reason for pointing the finger at him."

        show rena angry
        r "Yeah. What exactly makes you think he's the culprit?"
        hide rena
        hide cata
        show leo think closed
        with dissolve
        l "Well, it's quite simple..."

        l "Given their relationship as trainer and jockey, Lucas could easily have gained Don Vicente's trust and learned where he would be at any given time."
        hide leo
        show me sweat2
        with dissolve
        me "I could somewhat understand if you were accusing one of the other three. After all, they're technically competitors..."

        show me sweat
        me "But his own jockey? Someone he personally trained and mentored?"

        hide me
        show leo neutral
        with dissolve
        l "Things aren't always what they seem. Their seemingly close relationship may have been far more strained than we thought."

        show leo yell
        l "In any case, Mr. Mendoza's alibi is just as shaky as the rest."

        hide leo
        show lu nervous2
        with dissolve
        lu "Hang on a minute...! I'm not the killer!"

        show lu nervous
        lu "I respected Mr. Ruiz! He believed in me and helped me grow as a jockey!"
        
        show lu frown
        lu "Even though I'm one of the lesser-known jockeys, even though I don't have any sponsors backing me..."

        show lu yell1
        lu "He stayed by my side! And you're telling me I killed someone like that!?"

        show leo neutral
        hide lu
        with dissolve
        l "I'm afraid my suspicions have led me to that conclusion, Mr. Mendoza."

        show lu angry2
        hide leo
        with dissolve
        lu "But why!? Do you have any evidence!?"

        if not thought_route_complete:

            # If you didn't do the thought route, continue from here.
            hide lu
            show est neutral
            with dissolve
            e "Excuse me..."

            hide est
            show leo neutral
            with dissolve
            l "Hm?"

            show rena angry
            hide leo
            with dissolve

            r "The hell, old man? Don't interrupt them now. Looks like they caught goody two-shoes here for what he really is."

            hide rena
            show est smile2
            e "Yes, that's not my intention. I just couldn't help but notice something Mr. Mendoza said earlier."

            hide est
            show lu frown
            with dissolve
            lu "What...?"

            show est neutral
            hide lu
            with dissolve
            e "You mentioned that Vicente followed someone wearing peculiar clothes?"

            show lu neutral
            hide est
            with dissolve
            lu "Y-Yeah..."
            
            show lu yell1
            lu "Ah... that must be it! The man Don Vicente followed! He's the one you're looking for!"

            show leo think closed
            hide lu
            with dissolve
            lt "The man in the Hawaiian shirt..."
            show leo think yell
            l "Mr. Mendoza... I'm afraid that's impossible."

        # If you did the thought route, continue from here.

        show leo neutral
        hide lu
        with dissolve
        l "Those clothes you're talking about were found inside your locker."
        
        show lu nervous
        hide leo
        with dissolve
        lu "Ah..."

        show leo point
        hide lu
        play sound se_flash
        l "If anything, I'd say that implicates you even further. You're blaming some non-existent man, and you even disguised yourself in those clothes!" with flash

        show lu nervous2
        hide leo
        with dissolve
        lu "No! This is wrong, I..."
        
        hide lu
        show me yell
        with dissolve
        me "I've heard enough. We'll take it from here. You're coming with us, Mr. Mendoza."

        show lu nervous2
        hide me
        with dissolve
        lu "......"

        show leo neutral drop
        hide lu
        with dissolve
        stop music fadeout 2.5
        lt "Lucas's spirit seems broken as he resigns himself to being taken into police custody. I watch as he leaves the Derby."
        
        show leo neutral right
        lt "He insisted he wasn't the killer until the very end... Did he really kill his own trainer? And why?"
        
        show leo closed drop
        lt "Did I really make the right choice...?"

        lt "..."

        scene black
        hide leo
        with fade

        l "The race continued as scheduled. All the competitors gave it their very best..."

        l "And Renata came in first place, with Catalina finishing as the runner-up."

        l "The police had decided to resume their investigation after the race, and they got to work..."

        l "But despite Lorenzo's now-willing cooperation, with things having finally calmed down..."

        l "They failed to establish any conclusive evidence of Lucas's guilt."

        l "He was eventually released, but in this kind of elite competition, there are no second chances."

        l "Having missed his last chance to revitalize his career, and with sponsors unwilling to back him due to the stigma surrounding his arrest..."

        l "...Lucas was forced to retire as a jockey after the Derby, permanently."

        l "My accusations had put an end to someone's dream."

        l "And, in turn, they had allowed the real perpetrator to escape."

        l "Maybe I should consider retiring as a detective, too, if this is the kind of harm I cause..."

        # End THE GAME HERE
        call game_over
        return
    label choose_este:
        #Accuse Esteban (true end)
        scene placeholder_racetrack1
        show est angry
        with fade
        
        l "..."

        me "...You're unusually quiet."

        r "This masked weirdo... How long are you planning to stand there in silence!?"

        en "Yes, this is no time for naps. We are all exhausted, in one way or another, after this ordeal."

        c "I'm feeling fine."

        r "Always gotta be a fucking contrarian..."

        c "I don't want to hear that from you."

        me "Well? Have you figured anything out? Otherwise, I'm going to proceed with—"

        l "Yes. I've got something, alright."

        lu "...!"

        l "The culprit is...!"

        l "There are two things that have been bothering me. Why did Mr. Mendoza lie about the notebook and the clothes...?"

        l "And why does Ms. Vargas keep insisting on a timeline that's clearly off?"

        r "Like I told you, it's because—"

        l "Your phone, right?"

        r "Y-Yeah... So you get it."

        l "And therein lies the problem."

        me "What do you mean?"

        l "Why does that discrepancy work in Ms. Vargas's favor in the first place? Assuming her phone's clock was accurate, that is."

        me "Why does it work? An alibi establishes that someone was somewhere else at a particular time. If another person can corroborate that, it becomes much harder to dispute."

        me "...!"

        l "Exactly! So why is it that, despite the discrepancy in her timeline..."

        l "...Mr. Rojas hasn't said a word about how his own account is just as inaccurate?"

        e "...!"

        r "Huh? Hold up! Where the hell is this coming from!?"

        l "It's quite simple, Ms. Vargas."

        l "Mr. Rojas hasn't bothered correcting your mistaken timeline of events."

        l "Why is that?"

        e "..."

        l "Because doing so would cost him a rather convenient alibi!"

        r "What!?"

        l "Your call with him was at 10:17 AM, according to your phone."

        r "Y-Yeah...?"

        l "That's when Vicente was murdered. Did it sound like Mr. Rojas was in the middle of, say, a struggle?"

        r "No. He sounded like his usual self..."

        e "And what exactly are you implying, sir?"

        l "Given what we've established, that call couldn't have taken place before 10:27 AM at the earliest."

        l "Yet you never once challenged her account. You were perfectly content to let us believe it happened ten minutes earlier."

        c "In other words, he's using her."

        e "That's a grave accusation. On what grounds are you making it?"

        l "Then answer me a simple question. When did you first go to investigate the commotion surrounding the body?"

        e "Previously, I believed that would have been around 10:32 AM..."

        e "Although I now realize that timeline was mistaken."

        l "Mr. Rojas. Earlier, you claimed you were on a smoking break until 10:17..."

        l "...but that call didn't happen until 10:27."

        l "So what were you actually doing for almost half an hour, Mr. Rojas?"

        e "I can't say I appreciate being put on the spot like this..."

        me "You tied your own noose by failing to come clean earlier."

        e "Yes, I suppose I did... So allow me to clear things up."

        e "That said, if you suspect me simply because my account is off by a few minutes..."

        l "Ten minutes."

        e "If that is the standard we're applying, shouldn't the same logic apply to Ms. Vargas?"

        r "What the fuck, man?"

        menu:
            "Press on.":
                jump press_on
            "You're right.":
                jump reconsider

        label reconsider:

        l "You make a good point. If your whereabouts are unaccounted for, then so are Ms. Vargas's..."

        r "Give me a break! I didn't do shit! I told you I was at the café!"

        scene black
        with fade
        l "The route splits here. Probably a bad ending. Because you hesitated and let the real killer run away!"
        with fade
        return

        label press_on:

        l "You're deflecting, Mr. Rojas. I asked you a question. Answer it."

        e "Hmph. If you insist. But I'll be filing a formal complaint over this slander. With the inspector present, I expect it to be handled swiftly."

        me "Only if you're talking out of your ass."

        me "If I were you, I'd be more concerned about being caught doing just that."

        e "Your concern is noted."

        e "I hesitate to share this, but I suppose I have no choice now that things have come to this..."
label debug:
    label vs_estebanCE:
        scene placeholder_racetrack1
        call fx_testimony
        
        show est smile2
        with fade
        
        show est 
        e "My smoking break really did take that long. A bad habit, I'm well aware."
        show est frown
        e "After I met with Renata at the café, she confessed her guilt to me about what she had done."
        show est frown2
        e "She killed a man in cold blood… and was terrified of the consequences."
        show est angry
        e "Renata even enlisted the help of her sponsors to cover her tracks before eventually turning to me..."
        show est frown
        e "We worked together for a long time as trainer and jockey, so I felt compelled to protect her."
        e "She insisted on changing the times on our phones to provide her with a cover story."
        e "I realize that this was the wrong thing to do. My apologies."
       
        hide screen status_indicator
        stop music fadeout 2.5
        scene placeholder_racetrack1
        show est frown
        with fade

        l "So you are making her take the fall for this…!?"
        
        show est angry
        e "Not at all! This is painful for me too. To think someone I worked closely with would turn out to have done such a thing…"

        r "....."
        
        show est neutral
        e "Well? Was my explanation sufficient?"

        lt "...Painful? This is nothing but convenient for you. Pushing your sins onto others…"

        lt "I'll expose how rotten you really are!"
        
        label vs_esteCE_1:
        scene placeholder_racetrack1
        call fx_interrogation
        show est smile2
        with fade
        #call cutin("cross_examination")
        call CE_start

        show est 
        e "My smoking break really did take that long. A bad habit, I'm well aware."
        if ce_mode == "object":
            call cutin("objection")
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l "A bad habit indeed. Your words are like smoke that will be carried away by the wind."
            e "Heh, give me some credibility, Mr. Leopardo, I just started to explain things..."
            with fade
        
        show est frown
        e "After I met with Renata at the café, she confessed her guilt to me about what she had done."
        if ce_mode == "object":
            call cutin("objection")
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l "And what exactly would drive her to do that?"
            e "I like to believe I am a rather reliable person. It's only natural she would seek support from her trainer."
            lt "Reliable? More like arrogant."
            with fade
        
        show est frown2
        e "She killed a man in cold blood… and was terrified of the consequences."
        if ce_mode == "object":
            call cutin("objection")
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l "Why didn't you immediately alert the police?"
            e "As something of a mentor figure, I didn't want to abandon her like that."
            e "Would you be able to turn someone close to you over to the authorities, Mr. Leopardo?"
            l "Yes."
            e "Oh? Then perhaps you, too, are the cold-blooded type..."
            lt "...I just want justice to be served. That's all."
            with fade
        
        # Objection = Present Renata's Phone (Update evidence description)
        show est angry
        e "Renata even enlisted the help of her sponsors to cover her tracks before eventually turning to me..."
        if ce_mode == "object":
            call cutin("objection")
            if ce_object in [de_callrecords, de_alibi]:
                call vs_esteCE_RIGHT
            else:
                call vs_esteCE_WRONG

        if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            
            l neutral "You mean Castillo's people, yes? Are you saying Ms. Vargas went out of her way to contact them?"
            
            show est frown2
            e "I'm afraid so. The situation must have overwhelmed her. She killed a man, for crying out loud."

            l "When exactly did she contact them?"
            
            show est neutral
            e "A little while after murdering Vicente, or so she told me."

            lt neutral right "That's funny... I happen to think she did no such thing."
        
        show est frown
        e "We worked together for a long time as trainer and jockey, so I felt compelled to protect her."
        if ce_mode == "object":
            call cutin("objection")
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l "You say you've worked together for a long time. Didn't it strike you as strange that she would suddenly murder someone?"
            e "Quite so. But as you may know, Renata tends to have some... explosive outbursts."
            e "I simply chalked it up to that."
            lt "This guy..."
            with fade
        
        e "She insisted on changing the times on our phones to provide her with a cover story."

        if ce_mode == "object":
            call cutin("objection")
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l "So you're saying Renata came up with that on the spot?"
            e "Rather than on the spot, she must have been dreading it ever since I called."
            e "Perhaps she had a guilty conscience, in case the police looked into her phone?"
            lt "Right. Sounds more like someone's trying to shift the blame here."
            with fade
        
        e "I realize that this was the wrong thing to do. My apologies."
        if ce_mode == "object":
            call cutin("objection")
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            call cutin("holdit")
            l "That's it? You're willing to confess to being an accomplice to MURDER, and 'my apologies' is all you can say?"
            e "I deeply regret it, Mr. Leopardo. I assure you. I am ready to accept whatever punishment the law deems fit."
            lt "Oh, the law would've let you slip free if they'd bought your little charade. That's why I'm here."
            with fade

        # CE LOOPS HERE!!!
        hide screen status_indicator
        hide screen ce_ui
        scene placeholder_racetrack1
        show leo think closed
        lt "Renata couldn't have anticipated that Esteban would call her. He knows that, so he's claiming she suggested changing their clocks when they met at the café."

        show leo neutral right
        lt "I can't really dispute that now. Maybe if his fingerprints were on her phone...? But I'm sure he'd find a way to explain those away, too."

        show leo closed
        lt "Hm... If I can't establish Renata's innocence through the tampering with her phone's clock..."
        show leo neutral
        lt "...maybe I should attack one of his other claims instead?"
        jump vs_esteCE_1
    
    label vs_esteCE_WRONG:
        $ ce_mode = None
        l "Mr. Rojas, that statement doesn't hold water!"
        show me neutral
        e "Really? I think it holds up quite well. Maybe you want to give it another try?"
        l "Uh, yes, I think I would like that..."
        lt "I messed that one up..."
        # Penalty Damage
        call ce_penalty(2)
        return
    label vs_esteCE_RIGHT:
        $ ce_mode = None
        $ ce_rep += 0.5
        show leo neutral
        call CE_end
        l "That's fascinating. It is true that the inspector established that Castillo's men were contacted by their boss to dispose of the body..."
        l "...which means the killer must have reached out to either them or Mr. Castillo."
        jump vs_estebanCE2

    label vs_estebanCE2:
    hide screen status_indicator
    #OBJECTION
    hide leo
    show est neutral
    e "We are on the same page, it seems."

    l "Unfortunately for you, it would have been impossible for her to make that call."

    l "Take another look at Ms. Vargas's phone. The only call registered in its history came from none other than you, Mr. Rojas."
    
    show est angry
    e "That's hardly evidence, Mr. Leopardo. She could have simply deleted the call from her history."

    call cutin("objection")
    l "Gotcha now."
    
    show est smile2
    e "C-Come again...?"

    

    l "Certainly, that's entirely possible."

    l "..."

    l "So why didn't she delete YOUR call from her history as well?"

    show est frown
    e "That's...!"

    l "It would have been as simple as asking. You were certainly willing enough to cover for her. I'm sure you would have deleted it on your end in a heartbeat, too."

    show est frown2
    e "Well, I..."

    l "I'll tell you why: because you needed a record of that call to remain."

    l "You needed it to establish your own alibi and frame her once the discrepancy in her timeline came to light..."

    l "...You'd come out on top either way, Mr. Rojas!"

    show est nervous3

    e "Uungh!"

    show est yell

    e "Y-You are just wildly guessing here...! You don't have anything to back up those claims!"

    l "Perhaps we should sprinkle this line of reasoning with some evidence, then."

    show est angry
    e "What...?"

    l "All we have to do is..."

    menu provider_or_log:
        "Reach out to the phone provider":
            call cutin("takethat")
            jump provider
        "Check Esteban's phone call history":
            jump phone_history
    
    label phone_history:
        l "We just have to check Mr. Rojas's call history!"
        show est smile
        e "Go ahead, be my guest."
        l "..."
        lt "I can't find anything here... ack! He must have deleted it!"
        e "Is something wrong?"
        lt "I should try something else..."
        jump provider_or_log

    label provider:

    l "We can check with the phone providers for Ms. Vargas, Mr. Rojas and Mr. Castillo."

    l "Then we'll know for sure who called whom, and when."

    l "Inspector. If you would."

    me "Don't have to tell me twice."

    # Fade
    scene placeholder_racetrack1
    show me smile3
    with fade

    me "I reached out to the phone provider companies. And what do you know? That noose just got an awful lot tighter for you, bud."
    
    show est angry at left
    with dissolve
    e "..."

    l "What did they say?"

    me "First, there aren't any unaccounted calls on Renata's phone from today."

    r "Because I didn't delete anything...!"

    show me smile
    me "...what we did find was one interesting conversation between Rojas and Castillo. Care to listen?"

    # Fade to black, convo replays.

    n "Call at 10:19 AM."

    s "Hello?"

    e "It's me."

    s "Oh, my golden goose! How are things going?"

    e "There's... a situation."

    s "Oh my. Sounds like trouble."

    s "Say no more. Text me the location and I'll take care of it!"

    n "End of the call."

    l "That was certainly insightful."

    show rena angry2 at right
    hide me
    with dissolve

    r "You...! I can't believe it! You told that scum to clean up your mess!? And then you tried to make me take the fall for it?"

    e "It's regrettable that things have spiralled this far..."

    show rena angry
    r "What...?"

    show est frown
    e "Inspector, it seems Renata is willing to pin the crime on me until the very end."

    show rena yell
    r "You...!"

    show me angry
    with dissolve
    me "What do you mean?"

    show est neutral

    e "I know how this looks. Rest assured, I wasn't calling him to 'clean my mess', as Renata put so eloquently."

    e "It was to clean up her mess."

    show rena yell2

    r "This again!?"

    show me yell

    me "You're changing your story again."

    show est yell

    e "Only because I wanted to protect Renata. But in doing so, I became too deeply involved."

    show est angry

    e "Allow me to elaborate."

    lt "Uh-oh. I sense an immense amount of gaslighting coming our way."

    lt "Should I cut him off now?"

    menu:
        "Let him continue":
            jump lethimcook
        "Cut him off now":
            call cutin("holdit")
            jump youcantcook

    label lethimcook:
        lt "I'm a believer that everyone deserves a fair chance to tell their side of the story..."
        lt "...but if I let him keep lying his way out of this, we'll be here all day. I have to stop him now!"
        jump youcantcook
    
    label youcantcook:

        hide me
        hide rena
        show est angry at right
        show leo neutral at left
        with dissolve
        l "I'm afraid there's no need for that."

        show est yell

        e "What...? I have a right to explain myself—"

        show leo neutral right

        l "You stumbled upon her at the stables and contacted Mr. Castillo. Did I get that right?"

        show est smile
        e "Wh... I mean, yes, that is what I was about to say."
        
        show leo closed
        l "Mhm. That's what I thought."

        show rena frown2
        with dissolve
        r "I was never at the stables! I was at the café!"
        
        show est frown
        e "Renata, how long will you keep struggling like this?"

        show rena nervous
        r "..."

        show leo think yell

        l "You're the one struggling in vain, Mr. Rojas."

        l "You speak of illusions that can never become reality."

        show est angry
        e "What...!?"

        show leo neutral

        l "The reason you're wrong is because..."

        menu phone_or_cafe:
            "The phone call":
                jump da_phone_call
            "Renata was at the café":
                jump da_cafe
label da_cafe:
        show leo yell
        l "Ms. Vargas was at the café! You couldn't have stumbled into her at the stables!"
        show est angry
        e "You will just take her word at face value?"
        show est yell
        e "With that reasoning, you should believe what I am telling you just as much."
        show leo think closed drop
        lt "He's right... I need retrace my steps."
        jump phone_or_cafe

label da_phone_call:
    hide screen status_indicator
    hide est
    hide rena
    
    show leo smile at center
    with dissolve
    call cutin("takethat")
    l "Cover the sun with your hand, and the sun will still be there."

    show leo neutral
    l "You called Mr. Castillo to arrange the cover-up. That much is clear."

    l "But then, ten minutes later, you called Renata and arranged to meet her."
    
    hide leo
    show est yell
    e "That was to help her establish an alibi—"
    
    hide est
    show leo think yell
    l "No. It was to establish YOUR alibi."

    show leo think closed
    l "Think about it. If you'd already been helping Renata cover up the murder, why would you need to arrange a meeting with her afterward?"

    l "You could have simply claimed you'd been together the entire time."
    
    show leo neutral with dissolve
    l "But you didn't. You made a separate call, arranged a meeting, and made sure there was a record of it."
    
    show leo yell
    l "Because you needed someone who could corroborate your whereabouts after the murder."

    show leo point with dissolve

    l "You weren't helping Renata hide her crime, Mr. Rojas. You were making sure she could help hide yours!"

    hide leo
    show est nervous4
    with dissolve
    e "Uuunngho!!"

    show est nervous8
    e "Y-You...! Just who do you think you are, accusing me like this!?"

    show est nervous9
    e "I'm no killer! I won't stand for some random guy in a mask spreading lies about me!"

    hide est

    show me angry with dissolve
    me "Do you deny the allegations, then?"
    
    hide me
    show est nervous7
    with dissolve

    e "Of course I do! I deny every last one of them! Besides, what reason would I have to kill a fellow trainer!?"

    show est yell-rerd
    e "None, that's what!"

    lt neutral "So it's finally come to this. Every desperate killer's last line of defense: motive."

    lt neutral right "Until now, I had no idea what could have driven him to kill Vicente..."

    lt closed "But there's no room for doubt anymore."

    l yell "Very well, then. Let us put an end to this dance. The real main event will begin any moment now, after all."

    hide est
    show en yell3
    with dissolve

    en "Eek—! That's right! I've become so engrossed in all this that I nearly forgot about the race...!"
    
    hide en
    show est grit-red
    with dissolve
    e "It will end, alright! With you behind bars for accusing an innocent man!"

    # Last CE
label LastCE:
    scene placeholder_racetrack1
    call fx_testimony
    show est yell
    with fade
    stop music
    play music ce2 fadein 2.5
    
    e "There's no reason for me to kill Vicente!"
    
    show est yell-rerd
    e "I barely spoke to the man! Are you now going to say I hated him!?"

    show est grit-red
    e "We were both trainers! I stand to gain nothing from his death."
    
    show est angry
    e "I was simply going about my duties as a trainer that morning."

    show est yell
    e "I had no reason to interfere with his work, let alone attack him!"

    show est frown2
    e "Why would I throw away my career and life over someone I barely knew?"
    
    show est angry
    e "I had absolutely nothing to gain from his death!"
    
    scene placeholder_racetrack1
    hide screen status_indicator
    stop music fadeout 2.5
    show leo think closed at slightleft
    show est grit-red at slightright
    with fade
    l "So you will insist to the very end that you didn't do it."
    e "Of course I will! You won't get me to admit something I haven't done!"
    show est yell-rerd
    e "If you're that desperate to play detective, then get your act together and find the real culprit!"
    show leo think yell
    l "That's what I'm planning to do once I finish dismantling your web of falsehoods."
    show est grit-red
    e "Nngh..."

    #call cutin("cross_examination")
    label LastCE_Loop:
    scene placeholder_racetrack1
    call fx_interrogation
    show est yell
    with fade
    call CE_start
    stop music
    play music ce2 fadein 1.0 fadeout 1.0
    
    e "There's no reason for me to kill Vicente!"
    if ce_mode == "object":
        call cutin("objection")
        call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        l "I'm not so sure about that. There are a number of reasons one can have to kill a man."
        e "None of them apply to me! And you will see why soon."
        with fade
    
    show est yell-rerd
    e "I barely spoke to the man! Are you now going to say I hated him!?"
    if ce_mode == "object":
        call cutin("objection")
        call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        l "I wouldn't say you have to hate him to have a reason to silence him."
        e "Is that right? Then what reason would that be!?"
        lt "You know damn well what your reason is..."
        with fade

    show est grit-red
    e "We were both trainers! I stand to gain nothing from his death."
    if ce_mode == "object":
        call cutin("objection")
        call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        l "So the idea of having less competition to increase your odds of winning only applies to Ms. Vargas and not you?"
        e "I am not the one getting on the damn horse, Leopardo...!"
        e "My job is to prepare her for the race, not compete against the other trainers."
        l "And yet, her victories reflect on you too, don't they?"
        e "..."
        e "Of course they do. But that hardly makes me responsible for what happened!"
        with fade
    
    show est angry
    e "I was simply going about my duties that morning."
    if ce_mode == "object":
        call cutin("objection")
        call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        l neutral "I thought you were having a break to smoke?"
        show est yell-rerd
        e "That's- ugh! Alright, so I was smoking! Happy!? Are you done tripping me up!?"

        lt yell "Not until you confess your crimes, villain!"
        with fade

    show est yell
    e "I had no reason to interfere with his work, let alone attack him!"
    if ce_mode == "object":
        call cutin("objection")
        call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        l neutral "Someone did interfere with his work that morning, though. He wouldn't be dead otherwise."
        show est angry
        e "It's got nothing to do with me. I have no need to meddle with other trainers."

        lt "Meddle with other trainers..."

        lt think closed "Vicente's work... What was he doing right before he died?"
        menu vicenteb4death:
            "Getting food for the horse":
                jump food4horse
            "Chasing someone":
                jump chasechase
            "Preparing Lucero for the race":
                jump prephorse
        label food4horse:
            lt "Uh, no, I don't think food was mentioned once..."
            lt "Not that it wouldn't be part of his duties as trainer."
            lt "But I don't think they'd kill him over the last bale of hay."
            jump LastCE_Loop
        label prephorse:
            lt "Hmm... is that right?"
            lt "I have the feeling someone told me in their alibi what Vicente was up to..."
            lt "I should check the Dossier."
            jump LastCE_Loop
        label chasechase:
            jump LastCE_RIGHT
        with fade

    show est frown2
    e "Why would I throw away my career and life over someone I barely knew?"
    if ce_mode == "object":
        call cutin("objection")
        call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        l neutral "Why would Renata? She's in the same position as you."
        show est angry
        e "A mistake from youth? A wish to take out a competitor through their trainer?"

        l yell "Those aren't answers, they are guesses at best!"
        show est yell-rerd
        e "Shut up! Ask her if you want to know so badly!"

        lt neutral "No good. He's losing his marbles. This line of questioning isn't going anywhere."

        l neutral "Someone did interfere with his work that morning, though. He wouldn't be dead otherwise."
        show est angry
        e "It's got nothing to do with me. I have no need to meddle with other trainers."
        with fade
    
    show est angry
    e "I had absolutely nothing to gain from his death!"
    if ce_mode == "object":
        call cutin("objection")
        call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
        call cutin("holdit")
        l "People have killed for less. It isn't always about getting something from it."
        e "How rich! So now I am a psycho killer, is that it!?"
        l "I'm saying that a lack of motive doesn't make you innocent."
        e "And I'm saying you have absolutely nothing to support that accusation!"
        lt "He's getting awfully worked up over a simple question..."
        with fade

    #CE LOOPS HERE!
    hide screen status_indicator
    hide screen ce_ui
    scene placeholder_racetrack1
    show leo neutral
    with fade
    lt "This is it. One last push, and he's done for."
    show leo yell
    lt "I have to keep on pressing until I find a weakness!"
    jump LastCE_Loop

label LastCE_WRONG:
    $ ce_mode = None
    l "This proves your testimony wrong, Mr. Rojas!!"
    show e angry
    e "Ahahah! Getting so desperate that you're throwing random evidence around, Leopardo!?"
    l "Guh...!"
    lt "That was the wrong piece of evidence... Calm down, me. Let's try that!"
    # Penalty Damage
    call ce_penalty(3)
    return

label LastCE_RIGHT:
    $ ce_mode = None
    $ ce_rep += 0.5
    call CE_end
    jump LastCE_Continue

label LastCE_Continue:
    scene placeholder_racetrack1
    hide screen status_indicator
    show leo neutral
    with fade


    l "Mr. Rojas. I think I finally understand."

    e "What nonsense will you spout now?"

    l "Mr. Ruiz was following someone who had been petting Lucero without permission."

    l "You know what that means?"

    e "Just get to the point! How does this mystery person count as a reason for me to interfere with Vicente!?"

    

    l "You've got that backwards."

    l "The Hawaiian-shirt man isn't the reason you went after Mr. Ruiz."

    l "He's the reason Mr. Ruiz came after YOU."

    e "WHAT!?"

    r "I-I'm really lost here..."

    lu "Why does the man Don Vicente was following even matter...?"

    l "Because Mr. Rojas is that man."

    e "UOOOOAAAH!?"

    r "That's insane! They would've recognized each other!"

    l "Even with sunglasses, a hat, and a crowd?"

    r "...!"

    l "You put on the disguise, let Lucero lick your hand, then went back to the stables to change."

    l "Vicente followed you, caught you, and discovered exactly what you were doing."

    e "Hold it! That logic is twisted! You still can't prove it was me!"

    l "But I can!"

    e "I-Impossible!?"

    lt "Vicente catching him by surprise at the stables means this wasn't a premeditated murder."

    lt "That means, without a doubt, that he must have failed to conceal something in the evidence that would inevitably point back to him..."

    lt "Just like the blood drops at the stables, the body bag... it was all one big rush job."

    lt "Then it follows that the same applies to the disguise in the locker and the notebook he planted."

    lt "Both of those things... Whatever he couldn't erase in his haste, I should focus on that...!"

    menu FinalStrike:
        "Handwriting":
            jump final_handwriting
        "Fingerprints":
            jump final_prints
        "Names on the list":
            jump final_list
    label final_handwriting:
        l "Your handwriting! If we analyze it, I'm sure it'll match yours!"
        es "Hahaha... knock yourself out! You won't find a thing!"
        lt "He's awfully confident... maybe this approach is a bust. Let's try something else."
        jump FinalStrike
    label final_list:
        l "The names on the list prove it was you!"
        es "How!? They aren't related to me at all! I sure as hell don't see Pícaro on it!"
        lt "Damn it, he's right. Only the names of the collapsing horses are written here."
        lt "I need to calm down and think this through one more time...!"
        jump FinalStrike
    
    label final_prints:
    #play pursuit here
    call cutin("takethat")
    show leo point
    l "Your fingerprints, Mr. Rojas!"

    e "!?"

    l "You tried to get rid of the evidence by stuffing both the clothes and this notebook into Lucas's locker."

    l "This notebook is a hit list. Every horse that collapsed is written here, along with the payment you received for each one. Lucero was today's target."

    l "But there's no way you could have wiped those clean!"

    me "Not to mention, traces of DNA will definitely turn up if you've worn it more than once..."

    e "That's... those aren't..."

    l "We're way past the point where you can claim your clothes were stolen."

    l "You saw an opportunity to get ahead of the others, and exploited it at their expense."

    l "Just like you did to Ms. Vargas and Mr. Mendoza. And to so many other jockeys!"

    e "N-No! None of that is true! IT'S NOT!"
    
    hide est
    show leo yell
    show leo point
    l "Mr. Ruiz caught onto you... and you silenced him by taking his life!"

    l "The killer in this case... is none other than you, Esteban Rojas!"

    # Dramatic pause, panning across every character
    hide leo
    show est nervous7
    e "..."
    show est nervous8
    e "......"
    show est nervous9
    e "T-The clothes... I didn't— no, the collapses don't matter! I'm not behind them—"
    
    show est nervous6
    e "The phone, I didn't call— I mean, I didn't mean to call— the shovel, he got in the way— he wasn't— he wasn't supposed to be there!"
    
    show est nervous5
    e "Ah..."
    show layer master at earthquake(dt=2.0, dist=10)
    show est nervous4
    e "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!"
    
    hide est
    with dissolve
    pause .5

    # Esteban collapses

    
# Epilogue goes here.
label Epilogue:
    scene placeholder_racetrack1
    show me neutral
    with fade
    me "..."
    me "You are now under arrest. You have the right to remain silent. Anything you say can and will be used against you."
    
    hide me
    show est dark
    e "..."

    hide est 
    show rena yell2
    with dissolve
    r "Why...? Why the fuck would you do any of this?"
    r "Drugging other jockeys' horses... and killing someone, what is WRONG with you!?"
    show lu angry2 at slightright
    with dissolve
    lu "I shouldn't have let Don Vicente face you alone, damn it...!"

    show cata angry2 at slightleft
    c "Anyone stooping that low is only trying to make up for their own lack of skill."
    hide cata
    hide rena
    hide lu
    show est nervous7
    with dissolve
    e "H-Haah... how could any of you understand?"

    hide est
    show cata angry2
    with dissolve
    e "You're just some privileged brat whose victories were practically assured, Catalina. You're set for life."
    
    hide cata
    show lu angry2
    with dissolve
    e "Lucas never stood a real chance in this competition. You would've dropped out even if I did nothing..."
    
    hide lu
    show rena nervous
    with dissolve
    e "And you, Renata... you dare ask what's wrong with me? What's wrong with YOU!? Never accepting any of Castillo's help...!"
    
    hide rena
    show est nervous9
    with dissolve
    e "But I'm not like you. I welcomed it wholeheartedly. All I had to do was make a few animals sick enough, and we had ourselves a booming business."
    
    show est dark
    e "Heh, then came the threats. Making the big bucks comes with a price, of course..."
    
    show est nervous6
    e "I wanted to quit, but Sebastian wouldn't let me. So, since I was already knee-deep in that mess, I might as well go all the way and do it at the most prestigious derby! Why not!"

    show est nervous9
    e "It was fine anyway, wasn't it!? No people were getting hurt! Just a few bruises from falling on the racetrack! They can walk it off!"
    
    hide est
    show leo yell
    with dissolve
    l "You... are you so deluded that you think nobody got hurt?"
    
    hide leo
    show est nervous6
    with dissolve
    e "Haha....ha?"
    
    hide est
    show leo yell
    with dissolve
    l "Don't try to excuse your actions by saying no one got hurt. You committed animal abuse time and time again just to satisfy your own greed."
    
    show leo think closed
    l "Those horses are already subjected to plenty of stress just to race at peak capacity."
    
    show leo think yell
    with dissolve
    l "What you did could leave them with lifelong side effects. Maybe even kill them if you got the dosage wrong."

    show leo yell
    with dissolve
    l "And for what? Helping rig the betting odds in your favor?"
    l "You may not have seen it directly, but your dastardly ploys have ruined people's lives, too."
    l "If you're still unable to see the harm you've caused..."
    
    show leo point
    l "If all you can think about is trampling others to win, then you're a failure! Both as a trainer and as a human being!"
    
    hide leo
    show est nervous
    e "..."

    # Another fade. Officers take him away.
    scene placeholder_paddock
    show me smile
    with fade
    
    me "You managed to make that freak go silent. Impressive."
    l "It was not me, but the special effect the words of truth had on his soul, inspector!"
    me "...I'll tolerate your little act since you wrapped up the case nice and tight."
    me "Thank you, El Leopardo."

    lt "Wow. Genuine gratitude from the inspector. That's rare..."

    l "...It is no trouble! I must now depart, for the next case awaits me!"
    l "Farewell!"

    lt "I salute everyone present, then run off until I'm out of sight, before heading back to the trainers' lockers to change into my normal clothes."

    # Fade. Now on the main racetrack again.

    scene placeholder_racetrack1
    with fade
    
    t "Whew... seems like I made it before the race begins."
    show rena smile
    with dissolve
    r "Yo, dumbface! Do you know where that masked guy went off to!?"
    t "Hm? Masked guy? I don't know..."
    r "Damn. Here I was hoping to thank him for helping me out there."
    r "I've always known those bastards from Castillo's organization were using me as a poster girl for their little betting operation..."
    r "But I didn't think they'd take things that far."
    
    show cata smile3 at right
    c "You thought I was the one behind those incidents, right?"
    r "Ugh..."
    
    show lu frown at left
    lu "I also believed the rumors about you. I'm sorry."

    t "How's Lucero doing? Did a vet check him?"
    lu "Yeah. He's stable, but he fell unconscious because of whatever Esteban gave him."
    lu "I don't even want to think about what would've happened if he'd run in the actual race..."
    
    t "Wait... with Vicente gone, aren't you without a trainer?"
    t "Can you still participate?"
    lu "I can, since we technically signed up properly and completed all the paperwork."
    lu "Lorenzo said he could find me another trainer, but... I declined."
    lu "I want it to be just Lucero and me. In honor of Don Vicente's memory."
    t "..."
    c "Normally, that wouldn't be allowed here. It's why I went through the trouble of hiring someone like you."
    c "But Villareal called it an extraordinary circumstance and made an exception."

    r "That greedy bastard seems to have grown a conscience and allowed the race to be delayed for a couple of hours, too."
    lu "Yeah. Lucero and I will be ready by then. Count on it."
    r "Hah, don't think that means you'll be getting past me."

    # Those two leave, only Cata and Tony are left.
    hide rena
    hide lu
    hide cata
    with dissolve

    
    t "It's nice to see everyone getting along."
    show cata neutral at center
    with dissolve
    c "It is certainly more pleasant than the constant bickering Vargas is always causing."
    c "It seems your kind act of believing in her moved her heart."

    t "Yeah..."
    t "..."
    t "Wait, my act? Wasn't, uh... wasn't that the guy you all saw appear out of nowhere and speak funny?"

    c "I stand by what I said."

    t "Catalina, I think you've got the wrong idea... that person wasn't—"

    c "Seriously? Your hairstyle and clothes match."
    c "And you didn't even bother changing your voice that much. All you did was cover your eyes."
    c "Honestly, I'm more shocked nobody else noticed it was you."

    t "......."

    c "...Relax. I'm not going to tell."
    t "Ugh... thanks."

    c "Maybe invest in some glasses, though. Surely that'll fool almost anyone."

    t "Oh, shut it. Don't you have a race to win?"
    c "That, I do."

    tt "I watch her start heading toward the starting gate, but she suddenly turns around to face me."

    c "What are you standing around for? Aren't you going to help me with the final preparations?"
    c "Just because we have a few hours doesn't mean we can take it easy."

    t "...! Help you...? I mean, yes, coming right away!"

    # Fade into black.

label EpilogueNarration:
    $ dossier_enabled = False
    scene black
    with fade
    # Make Enzo say a few words befoer the start of the race
    # Here plays maybe an ending animation of Cata winning the Razing thunder.
    # Have people cheer and what nmot.
    #Ending animation or something. Maybe just narration.
    en "Ladies and gentlemen! The moment you've been waiting for is here!"
    en "The Razing Thunder race will commence... NOW!"
    # Here plays maybe an ending animation of Cata winning the Razing thunder.
    
    #This narration is meant to be faceless. No tony emotes.
    t "And that's how the Razing Thunder case came to an end."
    t "Catalina managed to overtake the competition and finish first, followed by Lucas and Renata."
    t "It does feel a bit weird to be celebrating when someone died just a few hours ago..."
    t "...but justice has been served. I think maybe it's okay, this time."
    t "Some say winning is everything. That success is measured by how far you can climb, how much you can achieve, and how many people you leave behind."
    t "But there's no point in reaching the top if you end up alone, trampling everyone along the way..."
    t "Soon enough, you'll become blinded by those desires and forget what you were fighting for in the first place."
    t "Turning competition into exploitation, and ambition into a free pass to hurt others."
    t "Ultimately, the greatest loss isn't your reputation, your money, or even your freedom... it's yourself."
    t "It's not worth it if you lose sight of who you are on your way to victory."
    t "Those who help you along the way... if you stick together until the end, even if you fall short of your expectations..."
    t "That's still a win in my book. At least, that's what I think."
    t "Oh, right. It's back to business for me. But as for everyone else..."

    label End_Medina:
        scene placeholder_park
        show me sweat2
        with fade
        me "What a goddamn headache of a case. No wonder we never found any signs of intruders. It was someone from the inside all along."
        show me neutral
        me "As unfortunate as this incident has been, it helped us take down the clandestine betting network."
        show me angry
        me "Those people are gonna be facing long sentences."
        show me smile2
        me "...Guess it paid off letting that guy run free around the crime scene."
        show me smile
        me "I'm willing to overlook him showing up there because of that. But next time, the gloves are off."

    label End_Lorenzo:
        scene placeholder_racetrack1
        show en grin
        with fade
        en "Hahaha...! A success! This has been a complete success! Look at everyone's euphoric smiles!"
        show en neutral
        en "Well, if you overlook the fact that someone was been murdered in my derby... my condolences to the family."
        show en yell2
        en "To think there were lowlives seeking to take advantage of my generosity!"
        show en nervous2
        en "W-What? No, of course I had no hand in the clandestine gambling!"
        show en yell
        en "No matter how much the inspector insists, I don't need to partake in the Castillos' schemes to offer everyone a wondrous experience!"
        show en neutral
        en "...That said, I didn't exactly put a stop to it, did I? Even after hearing the rumors. I will ensure there is no repeat of this next year."
        show en smile
        en "Ah, if only that young man had joined our staff! I was certain one of Sebastian's thugs would have made short work of him by the end of all this."
        show en yell
        en "He would have been a promising addition, no doubt. But my offer was turned down!"
        show en neutral
        en "It left me quite perplexed, specially since he mentioned working two jobs already."
        en "I've learned that one of them is at a weird agency, but what could the second one be? He simply wouldn't say..."
    label End_Lucas:
        scene placeholder_lockers
        show lu smile
        with fade
        
        lu "I got second place in the race...! I... I really wouldn't have made it without Don Vicente's help."
        
        show lu smile2
        lu "I... I wish he could've seen it happen."
        
        show lu smile
        lu "...Second place gets half the prize money. I'll be able to keep competing as a jockey with that."
        
        show lu neutral
        lu "Some sponsors reached out after the race, too, though I haven't decided which one I'll go with..."
        
        show lu smile3
        lu "Next time, Lucero and I are crossing the finish line in first place. We'll only get better from here on out."

    label End_Renata:
        scene placeholder_stables
        show rena yell2
        with fade
        
        r "Ugh... it pisses me off that those bastards were using Pícaro and me for so long!"
        show rena angry
        r "Wish I could've clobbered at least one of them. Now none of my wins really count."
        show rena neutral
        r "...Meh, that's fine by me. I don't want them. Not like that, even if it means starting from zero."

        show rena smile
        r "The masked guy did me a huge favor by getting rid of that creep."
        show rena smile3
        r "Now that's someone I could work with!"
        show rena smile2
        r "He disappeared, though... eh. Maybe I'll just steal Cata's trainer, then. He'll do."

    label End_Catalina:
        scene placeholder_parkinglot
        show cata surprise
        with fade
        c "Honestly... what an unfair arrangement."
        
        show cata neutral
        c "I asked for someone to pretend to be my trainer, and to stick around until the end. Nothing more."
        
        c "Instead, I got a guy playing hero who managed to get rid of those poisoning this competition and allowed the race to continue."
        
        c "..."
        
        show cata smile2
        c "Really... I got way more than I was expecting."

        show cata neutral
        c "That's why I tried to even things out by offering him a permanent position."
        
        show cata yell
        c "But he rejected it. What nerve."
        
        show cata smile
        c "...Though I had a feeling that was going to be his response."
        
        show cata smile2
        c "Even after hearing how many zeroes his paycheck would have, he still said no while fighting back tears. How stubborn."

        
    label End_Antonio:
        scene placeholder_office
        show tony smile
        with fade
        t "...and that's a wrap. Whew, I finally finished organizing the files on this case."
        show tony aha
        t "Chispa was so eager to go for a run after watching the race, I barely had a moment to archive these..."
        show tony what drop
        t "I already updated boss on how things went. She gave me an earful for turning down not one, but two offers..."
        show tony det smile
        t "...but it can't be helped. El Leopardo's still got a duty to carry out, and I have to see it through."
        show tony grin
        t "Now then! I wonder what kind of mysteries I'll run into next."
        
        pause 1.0
        scene black
        with fade
        "The end."
        #Why do you loop back to Esteban's CE!? Go back to the main menu!!!!
call ending_sequence
$ MainMenu(confirm=False)()   # Workaround to jump to main menu
return
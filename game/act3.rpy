
label act3:
    $ dossier_enabled = True
    label act3intro:
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
    label vs_seb_Testimony:
        scene placeholder_bodycg
        call fx_testimony
        show seb smile3
        with fade
        
        s "I say my testimony here."
        s "I am done."
        t "Wow that was a long testimony. (not)"
        hide screen status_indicator
    label vs_sebCE:
        scene placeholder_bodycg
        call fx_interrogation
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


    #Investigation COMPLETE

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

        me "..."

        s "More importantly, there's no need to waste any more time on this!"

        s "We already know who the culprit is!"

        lt "If it's coming from this guy, I seriously doubt it..."

        s "It was that suspicious character found near the body: Antonio Ortiz!"

        l "Say whaaaaaat!?"

        s "Yes, yes. Allow me to enlighten you."

        #CE goes here.

        # contra 1: tony killed him at the top of the railings
        label vs_sebCE2:
            scene placeholder_racetrack2
            show seb smile3
            with fade
            call CE_start

            s "I overlooked his questionable appearance, given that he's Catalina's trainer..."
            if ce_mode == "object":
                call vs_sebCE_wrong2
            if ce_mode == "press":
                $ ce_mode = None
                l "My- *cough* what is so questionable about that young man's appearance?"
                s "That unrefined hair, that nasty scar on his face, the ugly boots... need I go on?"
                lt "I'm not taking fashion advice from the guy wearing two rolexs on his arm!"
                with fade
            

            s "But no more! He's clearly a suspicious person!"
            if ce_mode == "object":
                call vs_sebCE_wrong2
            #p
            if ce_mode:
                $ ce_mode = None
                lt "What makes you so sure about that?"
                s "I'm getting there, mask freak! Stop interrupting me."
                with fade
            
            s "We all saw him prodding and standing near the body."
            if ce_mode == "object":
                call vs_sebCE_wrong2
            #p
            if ce_mode:
                $ ce_mode = None
                l "Uh... perhaps he was just trying to help the downed man?"
                s "Now he's a parademic? Please!"
                lt "I do know some first aid..."
                with fade

            s "Who does that? A cold blooded murderer!"
            if ce_mode == "object":
                call vs_sebCE_wrong2
            #p
            if ce_mode:
                $ ce_mode = None
                l "It's a bit of a stretch to label him a murderer just for that!"
                s "Say what you want, the police should just arrest him and let us run things here!"
                lt "I don't know if I'll be so lucky twice if I end up there again.
                "
                with fade
            
            s "He attacked that poor old man at the grandstands, then dropped him from high-up!"
            #p - contra is here , blood drops
            if ce_mode == "object":
                if ce_object in [de_blooddrops]:
                    call vs_sebCE_right2
                else:
                    call vs_sebCE_wrong2
            if ce_mode:
                $ ce_mode = None
                l "He dropped him right after the attack?"
                s "Are your ears clogged? Yes!"
                l "That would mean Mr. Ruiz was assaulted at the top of the grandstands, yes?"
                s "Who?"
                l "...the victim."
                s "Oh. Yes. Don't make me repeat the same over and over!"
                lt "I will when you stop contradicting yourself over and over."
                with fade
            
            hide screen ce_ui
            lt "I'm not about to let this guy frame me for murder."
            lt "Thankfully, he's already made one grave mistake while spewing his falsehoods."
            jump vs_sebCE2

            #continue here
            label vs_sebCE_wrong2:
                $ ce_mode = None
                t "Your testimony contradicts the evidence!!"
                show seb smile
                s "No."
                t "Fuck!"
                # Penalty Damage
                $ ce_rep -= 1
                with fade
                return
            label vs_sebCE_right2:
                $ ce_mode = None
                $ ce_rep += 2
                call CE_end
                jump act3_continue2
        label act3_continue2:
            l "So, you're claiming that Mr. Ortiz attacked the victim at the top of the grandstands... then threw him over the railing..."
            l "...where he landed at the parade ring, right where the body was found. Did I get that right?"

            s "A fine summary! Now that you understand, how about you leave already?"

            l "Except your explanation is riddled with holes."

            s "H-How dare you!"

            l "If Mr. Ortiz threw the victim from that height, how did he manage to show up and \"prod\" at the corpse, as you put it earlier?"

            s "He ran! All the way down, as fast as he could!"

            l "It's quite a distance to cover. He would've arrived after you, not before you."

            l "And that's not even the biggest problem."

            s "There's... more?"

            l "I'm afraid so. Lots more."

            l "For starters, there was a distinct lack of blood at the top of the grandstands."

            s "That's easy! It was cleaned up!"

            l "Luminol test."

            s "What?"

            l "Forensics examined the area thoroughly. Even if someone wipes away the blood, luminol can still react with the traces left behind, revealing what the naked eye can't see."

            l "Yet they found no traces of blood on the railing or the ground beneath the spot where the victim supposedly fell."

            l "But there was one place where the victim's blood *was* found. Care to guess where?"

            s "...Mmmmnngh...."

            l "Allow me then: Vicente's blood was discovered at the derby's stables!"

            s "I-Impossible!"

            me "Forensics confirmed the blood is a match. There's no doubt about it."

            s ".....that doesn't change a thing though!"

            l "...? It seems you don't intend on dropping the accusation."

            s "Of course not! And you will see why right now!"
label act3_continue3:
    # contra 2: tony used the bag to carry the body from the stables
    #Leo vs Seb Round 2 CE
    default ce_seb_bodybag = False
    label vs_sebCE_3:
    scene placeholder_racetrack1
    show seb smile3
    with fade
    call CE_start

    s "Fine then, I will admit. That old crook died at the stables."
    #press
    if ce_mode == "object":
        call vs_sebCE_wrong3
    if ce_mode == "press":
        $ ce_mode = None
        l "Question."
        s "Banter."
        with fade

    s "That still doesn't clear the country bumpkin's name!"
    if ce_mode == "object":
        call vs_sebCE_wrong3
    if ce_mode == "press":
        $ ce_mode = None
        l "Question."
        s "Banter."
        with fade

    if ce_seb_bodybag:
        s "He attacked that trainer, then used some kind of body bag to transport him out from the stables!"
        if ce_mode == "object":
            $ ce_mode = None
            if ce_object in [de_bodybag]:
                call vs_sebCE_right3
            else:
                call vs_sebCE_wrong3
        if ce_mode == "press":
            $ ce_mode = None
            l "Question."
            s "Banter."
            with fade
    else:
        s "He attacked that trainer, then moved his body away from the stables!"
        if ce_mode == "object":
            call vs_sebCE_wrong3
        if ce_mode == "press":
            $ ce_seb_bodybag = True
            $ ce_mode = None
            l "How did he pull that off in a derby full of people?"
            l "I'd imagine Mr. Ortiz would risk being seen."
            s "Must I spell it out? That runt didn't drag him by the feet in broad daylight!"
            l "Then how did he do it?"
            s "Some kind of bag, perhaps? Dark enough so no one can tell!"
            lt "...people tend to give themselves away at times. This is one of them."
            l "That sounds important. Revise your testimony, Mr. Castillo."
            s "Fine, you creep. I'll say it as many times as needed."
            with fade
    

    hide screen ce_ui
    lt "Parts of his explanation are too vague. I should press for details."
    lt "He's bound to mess up, that will be my chance to counter attack."
    jump vs_sebCE_3

    label vs_sebCE_wrong3:
        $ ce_mode = None
        t "Your testimony contradicts the evidence!!"
        show seb smile
        s "No."
        t "Fuck!"
        # Penalty Damage
        $ ce_rep -= 1
        with fade
        return
    
    label vs_sebCE_right3:
    $ ce_mode = None
    $ ce_rep += 2
    call CE_end
    jump act3_continue4
    
label act3_continue4:
    l "Interestingly enough... I agree with what you just said, Mr. Castillo."

    s "Even numbskulls like you can listen to reason. There may be hope for you yet."

    l "Sorry to disappoint you, but I was referring to the method of transportation."

    l "Yes, it's highly likely that a body bag was used to transport the victim's body."

    l "But... the person you're accusing couldn't have been the one to use that bag."

    s "H-How can you know that!? You can buy a bag like that anywhere!"

    l "True. But you still have to dispose of it afterward."

    l "Mr. Castillo. Any idea where the body bag used to transport the victim was found?"

    s "Hah! How should I know!? Was it dumped in a river?"

    l "It was found inside the staff break room. At the bottom of their trash bin, to be precise."

    s "WHA- How do you-!?"

    l "The door happened to be open. And an officer happened to check inside."

    l "What he found was quite damning: a bag stained with the victim's dried blood."

    s "W-Wait, wait, wait! I can explain! This... proves nothing!"

    s "That creep just got rid of the bag in that room!"

    l "That's impossible, and you know it, Mr. Castillo."

    s "...!"

    l "Mr. Villareal, security has been tightened considerably since the horse collapse incident, correct?"

    en "Huh? Yes, that's right. We've increased patrols and made sure the public doesn't wander into restricted areas..."

    l "The staff break room is one of those restricted areas. Unauthorized personnel aren't allowed anywhere near it."

    l "Which means only people working behind the scenes could have disposed of the bag there!"

    s "AAAHHH!"

    lt "Well, I did manage to get in there relatively easily, but I'm certainly not going to tell him that. Especially when I've got him on the ropes."

    l "Mr. Castillo! You often boast about having your underlings take care of things for you..."

    l "How about we give them a call? I'm sure they'll be happy to explain why an area meant for staff to rest..."

    l "...was being used to hide a piece of evidence connected to the murder."

    l "I'm sure they'll have something very interesting to share with the rest of us!"

    s "....n...nnnh...."

    s "Nooooo!"

    scene placeholder_racetrack2
    with fade

    #fade here

    me "Got some news. Castillo's men finally 'fessed up. Two of them hid the body bag in the break room. On their boss' orders, of course."

    l "I knew it, so they truly played a part in this."

    l "Then this means the culprit behind Vicente's murder is...!"

    #Choose here, but no real consequences, Medina interrupts you. Heck, make a time out choice even.

    menu:
        "Esteban":
            jump act3_continue5
        "Catalina":
            jump act3_continue5
        "El Leopardo":
            jump act3_continue5
        "Sebastian":
            jump act3_continue5
        "Renata":
            jump act3_continue5
        "Medina":
            jump act3_continue5
        "Lorenzo":
            jump act3_continue5
        "Lucas":
            jump act3_continue5
        "Castillo's Underlings":
            jump act3_continue5
label act3_continue5:
    me "Hold it right there. I know what you're thinking..."
    
    # Breather, Medina finally gets to present people's alibis to Tony.
    
    me "I'm afraid you'll be disappointed if you're planning on pointing the finger at him."

    l "What do you mean, Inspector?"

    me "Alibis. Out of the hundreds of people attending today's derby, we questioned those who had the closest ties to the victim or were seen near the scene."

    me "That leaves us with these suspects."

    l "Really? Just them?"
    
    me "That's what we're left with after ruling out the possibility of a random attack."

    l "Just to get this out of the way... What about robbery?"

    me "His wallet was still on him. There wasn't much inside, just some spare change, his ID, and the like."

    l "I see..."

    me "Anyway, we questioned the most likely suspects separately. Going over everyone's whereabouts together might help us uncover something."

    l "Something...? Does that mean you haven't settled on a suspect, Inspector?"

    me "I have. But there's no harm in going over the facts, is there?"

    me "Especially after all those interruptions from Castillo. A proper review of the case might bring something to light."

    l "Hm. If you say so..."

    me "Alright. Let's hear it, then. Tell us what you were doing today between 10 and 11 AM."

    r "Tch. What a waste of time..."


    # Joint Testimony goes here.
label bigCE:
    default ce_rena_phone = False
    default ce_luca_cloth = False
label bigCE_loop:
    scene placeholder_racetrack1
    show en neutral
    with fade
    call CE_start

    en "Around 10 AM, I was supposed to be overseeing the event's proceedings from the comfort of the luxury observatory in the VIP box..."
    if ce_mode == "object":
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            l "Does it really count as overseeing if you're doing it from up there?"
            en "Most certainly! It offers the best view, after all! You can see the entire racetrack!"
            with fade
    
    en "But the inspector here insisted on following me everywhere!"
    if ce_mode == "object":
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            l "Huh... Is that true, inspector?"
            me "Damn right it is. I needed answers, one way or another."
            lt "Scary."
            with fade
    
    en "She even brought Mr. Castillo along! I had the 'pleasure' of being stuck with the two of them until 10:42 AM."
    if ce_mode == "object":
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            l "I've got two questions. Are you certain about the time? And why was Mr. Castillo there?"
            en "Absolutely! There are several monitors displaying the news and movies, each with a clock."
            me "I can vouch for that. And as for that scumbag, I wanted to keep an eye on him."
            l "Smart thinking, considering everything... Did he do anything in particular while he was with you?"
            me "Just his usual nonsense. He spent most of the time on his phone."
            with fade

    r "I was at the café from 10 AM. I was starving, so I figured I'd grab something to eat."
    if ce_mode == "object":
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            l "What did you have?"
            r "What the hell do you care? You gonna write an article about it and post it online?"
            l "No, that wasn't what I had in mind... Just carry on."
            with fade

    r "Anyway, I got a phone call from my trainer about twenty minutes later. Give or take."
    if ce_mode == "object":
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            l "Could you be a little more specific about the time...?"
            r "You really are insufferable, you know that?"
            lt "I'm just doing my job."
            r "Ugh, just look at it yourself. See? 10:17 AM. Close enough, isn't it?"
            l "I suppose..."
            l "Would you mind if we played the recording? Just to be thorough."
            r "Knock yourself out. It's pretty boring shit, though."
            lt "..."
            lt "Most of the call was just Esteban checking in on Renata, asking where she was and telling her he'd meet her at the café."
            lt "The whole thing lasted about four minutes."
            lt "I should make a note of that."
            # Dossier updated!!!!
            with fade

    e "At 10 AM, I was taking a smoking break by the grandstands before meeting up with Renata."
    if ce_mode == "object":
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            l "Did you notice anything unusual while you were there?"
            e "I'm afraid not. I was simply relaxing and watching the other jockeys and their horses go by."
            l "I see... and how long did you stay there for, again?"
            e "About 17 minutes, give or take."
            with fade

    r "The old man showed up a little while after the call, and we headed to the racetrack to do some preparations."
    if ce_mode == "object":
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            l "So you left together sometime around 10:24 AM... Were you together the entire time after that?"
            r "Nah. After he showed up at the café, I went to the restroom while he watched my stuff."
            e "I even had to pay for her meal while waiting for her return. I dare say it was a rather calculated move on her part."
            r "Buzz off. I let you use my money to pay!"
            with fade
    
    if ce_rena_phone:
        r "We left at 10:34 AM! That's when all that corpse-related bullshit happened! I'm NOT lying!"
        if ce_mode == "object":
            call bigCE_wrong
        if ce_mode == "press":
                $ ce_mode = None
                    # Press — Nothing new
                l "You're absolutely certain about that, even knowing the body was reported at 10:42?"
                r "Maybe the report got the time wrong, then! I KNOW I left that café at 10:24, after meeting the old man!"
                with fade
    else:
        r "Anyway, shit hit the fan less than 10 minutes later. We both left to see what all the commotion was about."
        if ce_mode == "object":
            # Press — CONTRADICTION! THEY COULDN'T HAVE LEFT AT 10:34 BECAUSE THE BODY WAS REPORTED AT 10:42 AM!
            if ce_object in [de_victimnotes]:
                call bigCE_Renata
            else:
                call bigCE_wrong
       
        if ce_mode == "press":
                $ ce_mode = None
                l "And that's when you came across the body?"
                r "Yeah. Turns out Enzo's security staff sucks at their jobs, huh? Letting a murderer in."
                en "Excuse me!? My security personnel are highly trained professionals, fully equipped to handle any situation!"
                lt "Those same professionals somehow managed to miss a bunch of crooks carrying a body around in broad daylight..."
                lt "...Wait. When exactly did Renata say they left? Something's weird here..."
                with fade
    

    lu "...Don Vicente and I spent some time together at the parade ring around 10 AM. We only stayed together for about ten minutes, though..."
    if ce_mode == "object":
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            l "Since that was the last time he was seen alive, I have to ask... Did he seem any different than usual?"
            lu "Not really. He was his usual nagging, straightforward self."
            with fade
    
    if ce_luca_cloth:
        lu "I don't know why those clothes and that notebook were in my locker!"
        if ce_mode == "object":
            call bigCE_wrong
        if ce_mode == "press":
                $ ce_mode = None
                # Press — No new contradiction
                l "Are you absolutely certain none of these things belong to you?"
                lu "I am! I swear! I have no idea how they got there!"
                l "..."
                with fade
    else:
        lu "...Although, there was this guy wearing a Hawaiian shirt, a hat, and sunglasses. He kept doting on Lucero without asking for permission."
        # Press — CONTRADICTION! LUCAS HAS THE HAWAIIAN SHIRT IN HIS LOCKER!
        if ce_mode == "object":
            $ ce_mode = None
            if ce_object in [de_casualclothes, de_notebook]:
                call bigCE_Lucas
            else:
                call bigCE_wrong
        if ce_mode == "press":
                $ ce_mode = None
                l "Can you remember anything distinctive about this man?"
                lu "...Just that he was wearing an orange shirt with flowers on it. Sorry."
                l "That's fine. What exactly was he doing with your horse?"
                lu "He was petting Lucero and letting him lick his hands. We were worried he might be feeding him something he shouldn't."
                l "I see..."
                with fade

    lu "Don Vicente said he'd handle it himself, then went after that person towards the stables. I headed over to the observation area by the grandstands."
    if ce_mode == "object":
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            l "How long did you stay there?"
            lu "About twenty-five minutes. I was still waiting for Don Vicente to come back when I heard the commotion and headed back to the parade ring."
            l "I see..."
            with fade
    # Press
    

    c "I took Dama de Plata to the racetrack at 10 AM sharp to practice. We stayed there until the body was discovered."
    if ce_mode == "object":
        call bigCE_wrong
    if ce_mode == "press":
            $ ce_mode = None
            l "That's it? Can't you tell me a little more about what you were doing?"
            c "Would you like me to recite my entire training routine? I don't see how that's relevant to the investigation."
            me "It isn't."
            l "Did you speak to any of the other jockeys, perhaps? Or...?"
            c "No."
            lt "Well, that was incredibly helpful."
            with fade
    # BigCE End

    hide screen ce_ui 
    lt "Let's go over everything... Assuming my math hasn't gotten rusty..."
    lt "Lorenzo, Sebastian, and the inspector were together at the luxury observatory from 10 AM until 10:42 AM."
    lt "Renata was at the café since 10 AM. She received a call from Esteban at 10:17 AM.They met at 10:24 AM at the cafe before heading off for the racetrack."
    lt "But they left at 10:34 AM to investigate the big commotion around Vicente's body."
    lt "Esteban was smoking from 10 AM to 10:17 AM by the grandstands."
    lt "Lucas was with Vicente at the parade ring from 10 AM for about ten minutes. Afterwards, he spent roughly 25 minutes at the observation area by the grandstands."
    lt "...my head hurts. I'm going to write all of that down."
    #UPDATE DOSSIER WITH ALIBIS NOTES!!!!

    me "Got all that? Only a handful of these accounts can be independently confirmed, but at least we've got a clearer picture of everyone's whereabouts."
    me "Now, do you have any issues with the alibis?"

    lt "That's a good question. After hearing all of that, is there anything about these alibis that bothers me?"



    if ce_rena_phone and ce_luca_cloth:
        jump act3_thoughtroute
    else:
        menu:
            "Something bothers me":
                # Big problems. (Go back to the interrogation.)
                l "I do. There are a couple of more of things I'd like to ask about."
                jump bigCE_loop
            "Nothing bothers me":
                # No problems. (End interrogation.)
                l "I think we've covered everything, Inspector. We can move on."
                jump act3_continue6    

label bigCE_wrong:
    $ ce_mode = None
    l "Your testimony contradicts the evidence!!"
    show me neutral
    me "No."
    l "Fuck!"
    # Penalty Damage
    $ ce_rep -= 1
    with fade
    return


label bigCE_Renata:
    $ ce_rena_phone = True
    $ ce_mode = None
    $ ce_rep += 2
    # Objection
    l "Just to make sure I've got this straight... You two left sometime around 10:34 AM?"
    r "Are you deaf? Yeah."
    l "And you left because the discovery of the body caused a commotion."
    r "That's right, Captain Obvious."
    l "That's impossible, Ms. Vargas."
    r "Huh? Are you calling me a liar?"
    l "Do you know what time the body was reported?"
    r "Like I said! Sometime around 10:34!"
    l "10:42 AM. You're off by eight minutes."
    r "What? But that's not—"
    e "Perhaps Renata simply got confused about the time...?"
    r "I'm NOT confused! We met at 10:24 AM, and it wasn't even ten minutes before people started screaming and making a scene!"
    r "I know because I checked my phone before we left the café!"
    lt "Her timing is clearly off, but she insists she's not mistaken..."
    lt "Does she have a reason to lie? Or is there something else behind this discrepancy...?"
    lt "I'll have to keep this in mind."
    with fade
    return
label bigCE_Lucas:
    # Counter response here.
    $ ce_luca_cloth = True
    $ ce_mode = None
    $ ce_rep += 2
    l "Let me ask you something, Mr. Mendoza. Is this the outfit the man was wearing?"
    lu "Yes! That's exactly what he had on. But... how do you...?"
    l "I'm having a hard time believing you saw someone else wearing these."
    lu "Huh?"
    l "After all, these clothes were found inside your personal locker!"
    lu "What!?"
    l "Care to explain that?"
    lu "I... I don't know! I don't own clothes like that! I really did see someone wearing that outfit!"

    me "Damn. Why does a tacky vacation outfit matter, Leopardo? Do you have something against Hawaiian shirts?"
    l "I don't have anything against them, Inspector..."
    l "It's not the clothes themselves that bother me. It's where they were found."
    l "Mr. Mendoza claims he saw someone wearing them, yet they were found in his possession..."
    l "And that's not all. They were found alongside another rather peculiar item."

    me "A peculiar item?"
    l "This notebook, to be precise. I'm still trying to make heads or tails of it myself..."
    me "Let me see that..."
    me "...! Aren't these all the horses that collapsed before their races?"
    l "So you recognize them too. And it looks like each entry has a monetary value attached to it."
    me "A betting ledger? But all these horses ended up losing... And the last entry is for your own horse."
    me "Care to explain this, Mendoza?"

    lu "I-I don't know anything about that! The notebook isn't mine! Neither are the clothes!"
    me "Denying everything isn't going to get you very far..."
    with fade
    return

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


label act3_thoughtroute:
    scene black
    show leo think closed
    with fade
    # Found both contradictions
    lt "..."
    lt "Gaaah, it's as the inspector said! These alibis are difficult to verify..."
    lt "However, two things stand out after all the questions I asked."
    lt "First: Renata's account is off by about ten minutes. She's adamant that the body was reported earlier than it actually was."
    lt "Second: Lucas had in his possession the very clothes worn by someone he claims was feeding his horse."
    lt "Not to mention that notebook listing all the horses that collapsed during previous races..."
    lt "Both of them are sticking to their stories despite the evidence. What am I supposed to make of this...?"
    lt "Guess it's time to give the ol' noggin a good workout. I'm gonna go over the facts one more time."

    #Thoughtt route!!!
    #make a thought route bg for this part
    #with fade
    label rock_kick_shovel:
        show leo think closed
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
            l "Even a quick check of the race results confirms it. Every horse with a crossed-out entry lost after collapsing during its race."
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
        l "It's an organized operation. Someone is paying people to rig the races!"
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
            l "Haha... in all seriousness, insulting her in my mind won't give me real answer."
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
            lt "Her phone's time was off... but in what way?"
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
            l "Someone else tampered with her phone's clock...! That's it!"
            l "It would explain why she's so adamant that the times are correct, even when they aren't."
            l "Besides, if Renata had done it herself, her account of the meeting wouldn't necessarily match Esteban's."
            l "Hell, she couldn't even have known there WOULD be a meeting to account for!"
            l "She couldn't have known when he'd call her, either."
            l "Their accounts would have to match, down to the minute."
            l "...."
            l "So that's it..."
            l "Someone is being paid to sabotage the horses listed in the notebook and tried to frame Lucas for it..."
            l "...and the time in Renata's phone was tampered with without her knowledge!!"
            
            jump act3_thoughtrouteComplete
    #THOUGHT ROUTE FINISH!!!!!!
label act3_continue6:
    scene placeholder_racetrack1
    with fade
    # Did not find both contradictions
    lt "Most of them spent their time alone, so it's certainly difficult to verify or disprove their alibis..."
    lt "Nothing in particular stands out to me right now."
    label act3_thoughtrouteComplete:
    scene placeholder_racetrack1
    with fade
    # Both converge here. Finding the contradictions helps uncover the truth!

    me "Well? Any thoughts you'd like to share?"

    lt "..."

    en "Ahem. I don't mean to interrupt your diligent efforts to bring this nefarious murderer to justice, Inspector, but..."

    me "What is it?"

    en "Well, we're only twenty minutes away from the start of the event! People need to get to their posts and make their final preparations."

    me "You're aware that Castillo was involved in moving the body, correct?"

    en "I'm aware of that, yes—"

    me "And you know his underlings were involved as well."

    en "Yes, I know that too—"

    me "Those are serious offenses. Obstruction of justice."

    en "I understand! But I must insist that this matter be resolved, one way or another, so we can get on with the event!"

    me "You're in no position to make demands—"

    l "It's quite alright, Inspector! For I, El Leopardo, have glimpsed the answers we've all been seeking!"

    me "What?"

    en "Oho! So you've figured out who the culprit is, Mr. Leopardo? Magnificent!"

    lu "Who is it? Who killed Don Vicente?"

    l "Ah—"

    r "Come on! We've got other things to do! Spit it out!"

    l "Yes, I understand, but—"

    c "Despite your rather suspicious appearance, you managed to dismantle Castillo's ridiculous claims without breaking a sweat."

    c "If you know who's behind this, then you should tell us."

    l "..."

    lt "What a pickle. All I wanted to do was establish how the murder was carried out..."

    lt "But now everyone's waiting for an answer, and time is running out. I'll just have to take a shot in the dark and hope for the best."

    lt "Based on everything I've gathered, the culprit attacked Vicente in the stables..."

    lt "...then stuffed his body into a bag and had it transported all the way to the grandstands, where it was thrown over the railing."

    lt "Castillo's underlings were definitely involved, which means the possibility of accomplices can't be ruled out."

    lt "Is there anyone else connected to the Castillos besides Sebastian...?"

    lt "Hmm..."

    lt "The horse collapses, the clandestine betting, the motive for murder..."

    lt "There has to be a connection between all of them...!"

    l "The culprit is..."


    menu:
        "El Leopardo":
            jump choose_leo
        "Catalina":
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
        show cata angry2
        l "Catalina did it."
        scene black
        with fade
        l "This is a bad end. Expand on me."
        with fade
        return
    label choose_rena:
        show rena angry2
        l "Renata did it."
        scene black
        with fade
        l "This is a bad end. Expand on me."
        with fade
        return
    label choose_seba:
        l "Sebastian did it."
        scene black
        with fade
        l "This is a bad end. Expand on me."
        with fade
        return
    
    label choose_leo:
        l "Actually, I'm the one who reaped Mr. Ruiz's soul. It was me."

        en "What!?"

        lu "You!?"

        me "Have you gone completely insane!? You just finished proving that it couldn't have been you!"

        r "Huh? I thought he just proved that Antonio guy was innocent."

        c "…"

        l "…Oh! I guess you're right! Just a little joke to lighten the mood, haha!"

        me "…"

        me "…"

        lt "The inspector snaps a pair of handcuffs around my wrists while I desperately try to laugh it off."

        l "Haha… Wait, what-?"

        me "Play stupid games, win stupid prizes."

        me "You can continue your little joke down at the station."

        l "Wait, Inspector! I'm not done with this case yet!"

        l "Inspectoooooor!"

        scene black
        with fade

        lt "And just like that, I'm hauled away after my little 'confession'. My identity has been exposed, I'm being charged with murder, and now I'll have to wait for a lawyer before facing trial."

        lt "What happened to the race? Who really killed Vicente? I'll never get to know the truth now…"

        return

        #Game over.
    label choose_med:
        show me angry2
        #Accuse Medina
        l "It was none other than Inspector Medina herself!"

        en "What!? The good Inspector has been plotting to sabotage my glorious event through this senseless violence!?"

        lt "I'm promptly slapped with a pair of handcuffs following my accusation."

        me "No. Just... no."

        l "H-Hey, wait a moment-"

        me "First off, I have an alibi! I've been busting my ass investigating this place!"

        me "Second, I have absolutely no motive to attack that man!"

        l "Inspector-"

        me "And third! I. Am. With. The goddamn. POLICE!"

        l "I mean... that doesn't necessarily guarantee-"

        me "Oh, you're actually going there!? If you're going to accuse me of being some kind of corrupt cop who also happens to be a serial killer targeting random strangers, then you'd better have some damn good evidence!"

        me "Well!?"

        l "…"

        me "That's what I thought. Get him the hell out of here."

        scene black
        with fade

        lt "And just like that, I'm hauled away after my little 'confession'."

        lt "What happened to the race? Who really killed Vicente? I'll never get to know the truth now…"

        with fade
        return

        # Bad End.
    label choose_enzo:
        #Accuse Villareal
        show en angry
        l "It was Villareal! He's the mastermind behind this whole affair!"

        en "Whaaaaaat!?"

        me "What the hell are you basing that on?"

        l "Well, the man's greedy as hell. Wouldn't surprise me if Vicente owed him a few bucks, failed to pay up, and ended up on the receiving end of his revenge."

        me "Being greedy doesn't make someone a murderer. We looked into the victim's affairs, and there's nothing suggesting Vicente owed Villareal any money."

        en "That's right! I'm not in the debt collection business!"

        en "I've been hounded by the Inspector here practically nonstop! I haven't had a moment to myself, let alone an opportunity to attack anyone!"

        en "And why, in God's green earth, would I want to murder one of the jockeys or trainers invited to this exclusive event!?"

        en "That would throw the entire competition into chaos and bring everything to a halt! Look at the mess we're in already!"

        l "E-Err..."

        me "..."

        me "Guess I got my hopes up a little too much, huh?"

        me "I'll take it from here. You're dismissed."

        l "Huh? No, I can still-"

        me "You're done. Out."

        l "..."

        scene black
        with fade
        lt "What happened to the race? Who really killed Vicente? I'll never get to know the truth now…"
        with fade
        return
    label choose_thugs:
        #Choosing underlings
        show tthug
        l "Castillo's underlings were acting on orders to conceal evidence."

        l "So it's certainly possible that one of them was also responsible for carrying out the murder."

        me "It's possible, but we don't have anything pointing to any one of them in particular..."

        me "Although, I suppose that would technically mean Castillo himself orchestrated the whole thing."

        me "If that's the accusation you're making, then I suppose we can consider the matter settled and investigate things further with that in mind."
        scene black
        with fade
        lt "Hm... Could Castillo really have been behind all this? Did he simply order his men to have Vicente killed?"
        with fade
        return
    label choose_luc:
        #Choose Lucas
        show lu angry2
        l "Out of all the people here, he was the one closest to the victim, with ample opportunity to carry out the attack..."

        l "That's right, Lucas Mendoza!"

        lu "What...!?"

        lu "M-Me!? You're accusing me!?"

        lu "Here I was starting to believe you could actually find out who did it..."

        lu "You're wrong! I would never hurt Don Vicente like that!"

        c "That really does sound unlikely. You'd better have a good reason for pointing the finger at him."

        r "Yeah. What exactly makes you think he's the culprit?"

        l "Well, it's quite simple..."

        l "Given their relationship as trainer and jockey, Lucas could easily have gained Don Vicente's trust and learned where he would be at any given time."

        me "I could somewhat understand if you were accusing one of the other three. After all, they're technically competitors..."

        me "But his own jockey? Someone he personally trained and mentored?"

        l "Things aren't always what they seem. Their seemingly close relationship may have been far more strained than we thought."

        l "In any case, Mr. Mendoza's alibi is just as shaky as the rest."
        scene black
        with fade
        l "Final narration goes here."
        with fade
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

        e "Hmph. If you insist. But I'll be filing a formal complaint over this slander. With the Inspector present, I expect it to be handled swiftly."

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

        call CE_start

        show est 
        e "My smoking break really did take that long. A bad habit, I'm well aware."
        if ce_mode == "object":
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            l "Banter."
            e "Answer."
            with fade
        
        show est frown
        e "After I met with Renata at the café, she confessed her guilt to me about what she had done."
        if ce_mode == "object":
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            l "Banter."
            e "Answer."
            with fade
        
        show est frown2
        e "She killed a man in cold blood… and was terrified of the consequences."
        if ce_mode == "object":
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            l "Banter."
            e "Answer."
            with fade
        
        # Objection = Present Renata's Phone (Update evidence description)
        show est angry
        e "Renata even enlisted the help of her sponsors to cover her tracks before eventually turning to me..."
        if ce_mode == "object":
            if ce_object in [de_callrecords]:
                call vs_esteCE_RIGHT
            else:
                call vs_esteCE_WRONG

        if ce_mode:
            $ ce_mode = None
            
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
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            l "Banter."
            e "Answer."
            with fade
        
        e "She insisted on changing the times on our phones to provide her with a cover story."

        if ce_mode == "object":
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            l "Banter."
            e "Answer."
            with fade
        
        e "I realize that this was the wrong thing to do. My apologies."
        if ce_mode == "object":
            call vs_esteCE_WRONG
        if ce_mode == "press":
            $ ce_mode = None
            l "Banter."
            e "Answer."
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
        l "Your testimony contradicts the evidence!!"
        show me neutral
        e "No."
        l "Fuck!"
        # Penalty Damage
        call ce_penalty(2)
        return
    label vs_esteCE_RIGHT:
        $ ce_mode = None
        $ ce_rep += 2
        t "Actually, I do carry a mate with me. You are terribly wrong!"
        e "Seems like you do."
        call CE_end
        jump vs_estebanCE2

    label vs_estebanCE2:
    hide screen status_indicator
    #OBJECTION

    l "That's fascinating. It is true that the Inspector established that Castillo's men were contacted by their boss to dispose of the body..."

    l "...which means the killer must have reached out to either them or Mr. Castillo."
    
    show est neutral
    e "We are on the same page, it seems."

    l "Unfortunately for you, it would have been impossible for her to make that call."

    l "Take another look at Ms. Vargas's phone. The only call registered in its history came from none other than you, Mr. Rojas."
    
    show est angry
    e "That's hardly evidence, Mr. Leopardo. She could have simply deleted the call from her history."

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

    
    label LastCE_Loop:
    scene placeholder_racetrack1
    call fx_interrogation
    show est yell
    with fade
    call CE_start
    e "There's no reason for me to kill Vicente!"
    
    show est yell-rerd
    e "I barely spoke to the man! Are you now going to say I hated him!?"
    if ce_mode == "object":
            call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
        l "Banter."
        e "Answer."
        with fade

    show est grit-red
    e "We were both trainers! I stand to gain nothing from his death."
    if ce_mode == "object":
            call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
        l "Banter."
        e "Answer."
        with fade
    
    show est angry
    e "I was simply going about my duties that morning."
    if ce_mode == "object":
            call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
        l neutral "I thought you were having a break to smoke?"
        show est yell-rerd
        e "That's- ugh! Alright, so I was smoking! Happy!? Are you done tripping me up!?"

        lt yell "Not until you confess your crimes, villain!"
        with fade

    show est yell
    e "I had no reason to interfere with his work, let alone attack him!"
    if ce_mode == "object":
            call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
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
            lt "Wrong"
            jump LastCE_Loop
        label prephorse:
            lt "Wrong"
            jump LastCE_Loop
        label chasechase:
            jump LastCE_RIGHT
        with fade

    show est frown2
    e "Why would I throw away my career and life over someone I barely knew?"
    if ce_mode == "object":
            call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
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
            call LastCE_WRONG
    if ce_mode == "press":
        $ ce_mode = None
        l "Banter."
        e "Answer."
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
    l "Your testimony contradicts the evidence!!"
    show es angry
    e "No."
    l "Fuck!"
    # Penalty Damage
    call ce_penalty(3)
    return

label LastCE_RIGHT:
    $ ce_mode = None
    $ ce_rep += 2
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
        l "wrong"
        jump FinalStrike
    label final_list:
        l "wrong"
        jump FinalStrike
    
    label final_prints:
    #play pursuit here
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
    l "It was not me, but the special effect the words of truth had on his soul, Inspector!"
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
    lu "Yes. He's stable, but he fell unconscious because of whatever Esteban gave him."
    lu "I don't even want to think about what would've happened if he'd run in the actual race..."

    r "That greedy host seems to have grown a conscience and allowed the race to be delayed for a couple of hours, at least."
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
    c "It is certainly more pleasant than the constant bickering the loud one is always provoking."
    c "It seems your kind act of believing Renata moved her heart."

    t "Yeah..."
    t "..."
    t "Wait, my act? Wasn't, uh... wasn't that the guy you all saw appear out of nowhere and speak funny?"

    c "I stand by what I said."

    t "Catalina, I think you've got the wrong idea... that person wasn't—"

    c "Seriously? Your hairstyle and clothes match for the most part."
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
    scene black
    with fade
    # Make Enzo say a few words befoer the start of the race
    # Here plays maybe an ending animation of Cata winning the Razing thunder.
    # Have people cheer and what nmot.
    t "Ending narration."
    t "Here I am supposed to give you some life changing evidence."
    t "And also I should tell you what becomes of each character."
    t "And of course, I should tell you what me and Chispa did."
    t "We just went back to the agency."
    t "I am yet not at the level of a detective I wanna be."
    t "Some day, I will become a superhero that can save everyone with the truth...!"
    t "The end."
    label End_Medina:
        scene placeholder_park
        show me neutral
        with fade
        me "What a goddamn headache of a case. No wonder we never found signs of any intruders, it was someone from the inside all along."
        me "Unfortunate as it is, it helped us to take down that"
    label End_Lorenzo:
        scene placeholder_racetrack1
        show en grin
        en "Hahaha...! A success! This has been a complete success! Look at everyone's euphoric smiles!"
        show en neutral
        en "Well, if you overlook the fact that someone was been murdered in my derby... my condolences to the family."
        show en yell2
        en "To think there were lowlives seeking to take advantage of my generosity!"
        show en nervous2
        en "W-What? No, of course I had no hand in the clandestine gambling!"
        show en yel
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
        scene placeholder_office
        show luca smile
        with fade
    label End_Renata:
        scene placeholder_office
        show rena smile2
        with fade
    label End_Catalina:
        scene placeholder_office
        show cata smile
        with fade
        
    label End_Antonio:
        scene placeholder_office
        show tony smile
        with fade

    #Ending animation or something. Maybe just narration.
    

    "The end."
return
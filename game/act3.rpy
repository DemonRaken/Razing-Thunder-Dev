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

    me "..."

    s "More importantly, there's no need to waste any more time on this!"

    s "We already know who the culprit is!"

    lt "If it's coming from this guy, I seriously doubt it..."

    s "It was that suspicious character found near the body: Antonio Ortiz!"

    l "Say whaaaaaat!?"

    s "Yes, yes. Allow me to enlighten you."

    #CE goes here.

    # contra 1: tony killed him at the top of the railings
    
    s "I overlooked his questionable appearance, given that he's Catalina's trainer..."
    #p
    l "My- *cough* what is so questionable about that young man's appearance?"
    s "That unrefined hair, that nasty scar on his face, the ugly boots... need I go on?"
    lt "I'm not taking fashion advice from the guy wearing two rolexs on his arm!"

    s "But no more! He's clearly a suspicious person!"
    #p
    lt "What makes you so sure about that?"
    s "I'm getting there, mask freak! Stop interrupting me."
    
    s "We all saw him prodding and standing near the body."
    #p
    l "Uh... perhaps he was just trying to help the downed man?"
    s "Now he's a parademic? Please!"
    lt "I do know some first aid..."

    s "Who does that? A cold blooded murderer!"
    #p
    l "It's a bit of a stretch to label him a murderer just for that!"
    s "Say what you want, the police should just arrest him and let us run things here!"
    lt "I don't know if I'll be so lucky twice if I end up there again.
    "
    s "He attacked that poor old man at the grandstands, then dropped him from high-up!"
    #p - contra is here
    l "He dropped him right after the attack?"
    s "Are your ears clogged? Yes!"
    l "That would mean Mr. Ruiz was assaulted at the top of the grandstands, yes?"
    s "Who?"
    l "...the victim."
    s "Oh. Yes. Don't make me repeat the same over and over!"
    lt "I will when you stop contradicting yourself over and over."
    
    lt "I'm not about to let this guy frame me for murder."
    lt "Thankfully, he's already made one grave mistake while spewing his falsehoods."

    #continue here
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
label debug:
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

    #fade here

    me "Got some news. Castillo's men finally 'fessed up. Two of them hid the body bag in the break room. On their boss' orders, of course."

    l "I knew it, so they truly played a part in this."

    l "Then this means the culprit behind Vicente's murder is...!"

    #Choose here, but no real consequences, Medina interrupts you. Heck, make a time out choice even.

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

    en "Around 10 AM, I was supposed to be overseeing the event's proceedings from the comfort of the luxury observatory in the VIP box..."

    # Press
    l "Does it really count as overseeing if you're doing it from up there?"
    en "Most certainly! It offers the best view, after all! You can see the entire racetrack!"

    en "But the inspector here insisted on following me everywhere!"
    # Press
    l "Huh... Is that true, Inspector?"
    me "Damn right it is. I needed answers, one way or another."
    lt "Scary."

    en "She even brought Mr. Castillo along! I had the 'pleasure' of being stuck with the two of them until 10:42 AM."
    l "I've got two questions. Are you certain about the time? And why was Mr. Castillo there?"
    en "Absolutely! There are several monitors displaying the news and movies, each with a clock."
    me "I can vouch for that. And as for that scumbag, I wanted to keep an eye on him."
    l "Smart thinking, considering everything... Did he do anything in particular while he was with you?"
    me "Just his usual nonsense. He spent most of the time on his phone."

    r "I was at the café from 10 AM. I was starving, so I figured I'd grab something to eat."

    # Press
    l "What did you have?"
    r "What the hell do you care? You gonna write an article about it and post it online?"
    l "No, that wasn't what I had in mind... Just carry on."

    r "Anyway, I got a phone call from my trainer about twenty minutes later. Give or take."

    # Press
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

    # Dossier updated.

    es "At 10 AM, I was taking a smoking break by the grandstands before meeting up with Renata."

    # Press
    l "Did you notice anything unusual while you were there?"
    es "I'm afraid not. I was simply relaxing and watching the other jockeys and their horses go by."

    r "The old man showed up a little while after the call, and we headed to the racetrack to do some preparations."

    # Press
    l "So you left together sometime around 10:24 AM... Were you together the entire time after that?"
    r "Nah. After he showed up at the café, I went to the restroom while he watched my stuff."
    es "I even had to pay for her meal while waiting for her return. I dare say it was a rather calculated move on her part."
    r "Buzz off. I let you use my money to pay!"

    r "Anyway, shit hit the fan less than ten minutes later. We both left to see what all the commotion was about."

    # Press — CONTRADICTION! THEY COULDN'T HAVE LEFT AT 10:34 BECAUSE THE BODY WAS REPORTED AT 10:42 AM!

    l "And that's when you came across the body?"
    r "Yeah. Turns out Enzo's security staff sucks at their jobs, huh?"
    en "Excuse me!? My security personnel are highly trained professionals, fully equipped to handle any situation!"
    lt "Those professionals somehow managed to miss a bunch of crooks carrying a body around in broad daylight..."

    lt "...Wait. When exactly did Renata say they left? Something doesn't add up..."

    # Objection
    l "Just to make sure I've got this straight... You two left sometime around 10:34 AM?"
    r "Are you deaf? Yeah."
    l "And you left because the discovery of the body caused a commotion."
    r "That's right, Captain Obvious."
    l "That's impossible."
    r "Huh? Are you calling me a liar?"
    l "Ms. Vargas, do you know what time the body was reported?"
    r "Like I said! Sometime around 10:34!"
    l "10:42 AM. You're off by eight minutes."
    r "What? But that's not—"
    es "Perhaps Renata simply got confused about the time...?"
    r "I'm NOT confused! We met at 10:24, and it wasn't even ten minutes before people started screaming and making a scene!"
    r "I know because I checked my phone before we left the café!"

    lt "Her timing is clearly off, but she insists she's not mistaken..."
    lt "Does she have a reason to lie? Or is there something else behind this discrepancy...?"
    lt "I'll have to keep this in mind."

    # Another update if the player has already objected to this.

    r "We left at 10:34 AM! That's when all that corpse-related bullshit happened! I'm NOT lying!"

    # Press — Nothing new
    l "You're absolutely certain about that, even knowing the body was reported at 10:42?"
    r "Maybe the report got the time wrong, then! I KNOW I left that café at 10:24, after meeting the old man!"

    lu "...Don Vicente and I spent some time together at the parade ring around 10 AM. We only stayed together for about ten minutes, though..."

    # Press
    l "Since that was the last time he was seen alive, I have to ask... Did he seem any different than usual?"
    lu "Not really. He was his usual nagging, straightforward self."

    lu "...Although, there was this guy wearing a Hawaiian shirt, a hat, and sunglasses. He kept doting on Lucero without even asking permission."

    # Press — CONTRADICTION! LUCAS HAS THE HAWAIIAN SHIRT IN HIS LOCKER!

    l "Can you remember anything distinctive about this man?"
    lu "...Just that he was wearing an orange shirt with flowers on it. Sorry."
    l "That's fine. What exactly was he doing with your horse?"
    lu "He was petting Lucero and letting him lick his hands. We were worried he might be feeding him something."
    l "I see..."

    # Counter response here.

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

    lt "He doesn't seem to be lying. But then, how did these things end up in his locker...?"
    lt "Hmm... Should I take another look at the alibis, or call it here?"

    # Choice.
    # Take another look: go back to the CE (possibly set a flag indicating the Lucas contradiction has been found).
    # If ending the interrogation, skip to selecting a culprit.

    lu "I don't know why those clothes and that notebook were in my locker!"

    # Press — No new contradiction
    l "Are you absolutely certain none of these things belong to you?"
    lu "I am! I swear! I have no idea how they got there!"
    l "..."

    lu "Don Vicente said he'd handle it himself, then went after that person. I headed over to the observation area by the grandstands."

    # Press
    l "How long did you stay there?"
    lu "About twenty-five minutes. I was still waiting for Don Vicente to come back when I heard the commotion and headed back to the parade ring."
    l "I see..."

    c "I took Dama de Plata to the racetrack at 10 AM sharp to practice. We stayed there until the body was discovered."
    l "That's it? Can't you tell me a little more about what you were doing?"
    c "Would you like me to recite my entire training routine? I don't see how that's relevant to the investigation."
    me "It isn't."
    l "Did you speak to any of the other jockeys, perhaps? Or...?"
    c "No."
    lt "Well, that was incredibly helpful."

    # End

    lt "Let's go over everything... Assuming my math hasn't gotten rusty..."

    lt "Villareal, Sebastian, and the Inspector were together at the luxury observatory from 10 AM until 10:42."
    lt "Renata was at the café from 10 AM. She received a call from Esteban at 10:17, met him at 10:24, and then they headed for the racetrack together..."
    lt "According to her, they left around 10:34 to investigate the commotion."
    lt "Before meeting her, Esteban claims he was taking a smoking break by the grandstands from 10 AM."
    lt "Lucas was with Vicente at the parade ring from 10 AM for about ten minutes. Afterwards, he spent roughly twenty-five minutes at the observation area by the grandstands."
    lt "Whew... That's quite a few accounts to keep track of. But I think I've got the picture."

    me "Got all that? Only a handful of these accounts can be independently confirmed, but at least we've got a clearer picture of everyone's whereabouts."
    me "Now, do you have any issues with the alibis?"

    lt "That's a good question. After hearing all of that, is there anything about these alibis that bothers me?"

    # Big problems. (Go back to the interrogation.)
    l "I do. There are a couple of things I'd like to ask about."

    # No problems. (End interrogation.)
    l "I think we've covered everything, Inspector. We can move on."


    
    # Found both contradictions
    lt "As the Inspector pointed out, these alibis are difficult to verify..."
    lt "However, two things stand out."
    lt "Renata's account is off by about ten minutes. She's adamant that the body was reported earlier than it actually was."
    lt "And Lucas had in his possession the very clothes worn by someone he claims was feeding his horse."
    lt "Not to mention that notebook listing all the horses that collapsed during previous races..."
    lt "Both of them are sticking to their stories despite the evidence. What am I supposed to make of this...?"

    # Did not find both contradictions
    lt "Most of them spent their time alone, so it's certainly difficult to verify or disprove their alibis..."
    lt "Nothing in particular stands out to me right now."

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

    lt "The culprit is..."


    menu:
        "Esteban":
            jump haanin_es2
        "Catalina":
            jump haanin_es2
        "El Leopardo":
            jump haanin_es
        "Sebastian":
            jump haanin_es
        "Renata":
            jump haanin_es2
        "Medina":
            jump haanin_es
        "Lorenzo":
            jump haanin_es
        "Lucas":
            jump haanin_es2
        "Castillo's Underlings":
            jump haanin_es

    label haanin_es:

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

    lt "And just like that, I'm hauled away after my little 'confession'. My identity has been exposed, I'm being charged with murder, and now I'll have to wait for a lawyer before facing trial."

    lt "What happened to the race? Who really killed Vicente? I'll never get to know the truth now…"

    #Game over.
    
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

    # Bad End.
    
    #Accuse Villareal
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

    #Bad End.
    #Choosing underlings

    l "Castillo's underlings were acting on orders to conceal evidence."

    l "So it's certainly possible that one of them was also responsible for carrying out the murder."

    me "It's possible, but we don't have anything pointing to any one of them in particular..."

    me "Although, I suppose that would technically mean Castillo himself orchestrated the whole thing."

    me "If that's the accusation you're making, then I suppose we can consider the matter settled and investigate further with that in mind."

    lt "Hm... Could Castillo really have been behind all this? Did he simply order his men to have Vicente killed?"

    #Choose Lucas

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

    label haanin_es2:
    menu:
        "It was him":
            jump itwashim
        "Reconsider":
            jump Reconsider

    label itwashim:
        l "I'm confident this is how things played out!"
        #bad end

    label Reconsider:
        l "On second thought... I don't think it was them."
        me "Then who do you think it was?"
        #jump back to choices

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
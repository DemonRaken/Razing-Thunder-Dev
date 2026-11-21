label act3_main_inves:
    show text _("{size=150}{color=#ff5100}Investigation{/color}{/size}") at truecenter, investigation_text_zoom
    pause 2.0
    hide text
    $ aai_active = True
    $ aai_travel_left = [mp_stables, mp_grandstands, mp_paddock] # add locations to investigate
    jump act3_main_inves_maptravel_mode

label act3_main_inves_end:
    n "This was the end."
    show text _("{size=150}{color=#ff5100}Investigation\nComplete{/color}{/size}")  at truecenter, investigation_text_zoom
    pause 2.0
    hide text
    $ aai_active = False
    lt "I invested everything. Now, I must hurry and confront my first target."
    jump inves_complete

label act3_main_inves_maptravel_mode:
    if len(aai_travel_left) == 0: # done all investigations
        lt "Huh, it seems I investigated everything. I am ready!"
        jump act3_main_inves_end
        
    $ dossier_tab_control = "map"
    call screen dossier_ui
    if aai_travel in aai_travel_done:
        lt "I already went to [aai_travel.name]."
        jump act3_main_inves_maptravel_mode
    if aai_travel not in aai_travel_left:
        lt "I don't have to do anything at [aai_travel.name]"
        jump act3_main_inves_maptravel_mode
    lt "I know! I'll visit [aai_travel.name] next!"
    $ dossier_tab_control = "evidence"
    if aai_travel == mp_stables: # locations jump table
        jump stables_inves
    if aai_travel == mp_grandstands:
        jump racetrack_inves
    if aai_travel == mp_paddock:
        jump paddock_inves


# =================
#    STABLES
# =================


label stables_inves:
    scene placeholder_stables
    with fade
    lt "Hey Chispa. Hope you weren't feeling too lonely without me."
    lt "Wait... this place feels... off. Something's different."

    while aai_active:
        call screen aai_main_menu
        while aai_mode == "talk":
            menu:
                "Ask Chispa: Were you lonely without me?":
                    l "Hey Chispa, you weren't lonely, right?"
                    l "Were you fed well? Do you want something?"
                    l "Don't make that face, I'll come back before you know it!"
                "Ask Chispa: Did you see anything?":
                    l "Hey, Chispa, did you see anything?"
                    ch "Neigh!"
                    l "Thought so."
                "Close":
                    $ aai_mode = None
        if aai_mode == "present":
            $ dossier_tab_control = "evidence"
            call screen dossier_ui
            if ce_object in [dp_leo, de_mate]:
                l "Oh, I really love mate. Mate, oh my love."
                ch "Neigh! Neigh!"
                l "Chispa, you aren't allowed to drink from my Mate."
            elif ce_object in [dp_chispa]:
                l "Chispa, you are so lovely, look at you."
                ch "Neigh! Neeeeigh! Neeeigh!!!"
                l "There there, calm down. I have to focus."
            else:
                l "Chispa what do you think about [ce_object.name]?"
                ch "Neigh! Neigh!"
                l "Thought so."
        elif aai_mode == "examine":
            if mp_stables in aai_travel_left:
                while(mp_stables in aai_travel_left):
                    call screen aai_examine_stables
            else:
                lt "I've already examined this area."
                lt "I better {b}MOVE{/b} somewhere else instead."
        elif aai_mode == "move":
            jump act3_main_inves_maptravel_mode
    return

screen aai_examine_stables():
        imagemap:
            yalign 1.0   # imagemap doesn't show like scene without this.
            idle            "placeholder_stables"
            hover Transform("placeholder_stables", matrixcolor=BrightnessMatrix(0.3))   
            hotspot (1327, 205, 369, 673) action Call("stables_blood")
            hotspot (344, 479, 652, 361) action Call("stables_shovel")


label stables_blood:
    #click mountain of hay
    lt "Why is there a bunch of hay in the middle of the ground? You'd think the staff would tidy up the place more."
    lt "Hang on, I can see something underneath it..."
    lt "Kneeling over, I begin to brush away all of the hay."
    $ renpy.music.set_volume(0.4, delay=1.0, channel="music")
    lt "What the...!? This looks like someone's blood...!"
    lt "...yeah. No doubt about it, this is dried up blood. Moreover, it looks like a few drops lead outside..."
    lt "Huh? The trail suddenly ends before reaching the entrance."
    lt "That's weird. I'll notify one of the officers about it. Better safe than sorry."
    return

label stables_shovel:
#click shovel
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    lt "Wait a minute... What's this doing here?"

    lt "A stable shovel. Someone must've left it behind this stall."

    lt "The blade is covered in something dark and flaky. At first, I thought it was dirt..."

    l "...Wait. Is that blood!?"

    lt "And this dent... Looks like it's been damaged pretty badly."

    lt "A dent and blood... some hairs are caught along the edge. Don't tell me this is..."

    lt "...I should have one of the inspector's subordinates run tests on it right away."

    lt "This here... might be the murder weapon!"

    lt "This is a huge find... but, damn... what a way to go."
    lt "Alright, what's next...?"
    $ aai_investigated(mp_stables)
    return


# =================
#    Paddock and rest
# =================

screen aai_examine_paddock():
        imagemap:
            yalign 1.0   # imagemap doesn't show like scene without this.
            idle            "placeholder_paddock"
            hover Transform("placeholder_paddock", matrixcolor=BrightnessMatrix(0.3))   
            hotspot (141, 377, 874, 316) action Call("aai_paddock_body")

label paddock_inves:
    scene placeholder_paddock
    with fade
    lt "There. Now I'm dressed for the occasion. El Leopardo is on the case...!"

    lt "Huh. The police officers watching over the scene aren't trying to detain me. I guess the inspector gave them a heads-up? Much appreciated!"
    lt "Time to take a good look around and figure out what happened."
    play music inves fadein 2.5
    while aai_active:
        call screen aai_main_menu
        while aai_mode == "talk":
            menu:
                "Talk to Police officers?":
                    lt "No, I should stay away."
                "Close":
                    $ aai_mode = None
        if aai_mode == "present":
            $ dossier_tab_control = "evidence"
            call screen dossier_ui
            lt "I better not show it to the police."
        elif aai_mode == "examine":
            if mp_paddock in aai_travel_left:
                while(mp_paddock in aai_travel_left):
                    call screen aai_examine_paddock
            else:
                lt "I've already examined this area."
                lt "I better {b}MOVE{/b} somewhere else instead."
        elif aai_mode == "move":
            jump act3_main_inves_maptravel_mode

label aai_paddock_body:
    show layer master:
        linear 2.0 zoom 1.5
    #Points to click: just the body.
    #When done so, zoom in on it.
    lt "I should examine the body more closely... Let's see."
    lt "There's that deep, nasty wound on the back of his head... and the bruises on the front..."
    lt "...Huh? This looks like dirt, but it doesn't match the ground around the parade ring. There's something else mixed in..."
    lt "Is this... bits of hay? Huh."
    lt "Maybe I should check the stables..."
    $ aai_investigated(mp_paddock)
    show layer master:
        linear 2.0 zoom 1.0
    return


# =================
#    Racetrack
# =================


screen aai_examine_granstands():
        imagemap:
            yalign 1.0   # imagemap doesn't show like scene without this.
            idle            "placeholder_granstands"
            hover Transform("placeholder_granstands", matrixcolor=BrightnessMatrix(0.3))   
            hotspot (141, 377, 874, 316) action Call("racetrack_inves_vip")
            hotspot (1140, 679, 647, 214) action Call("racetrack_inves_railing")

label racetrack_inves:
        scene placeholder_granstands
        with fade
        
        while aai_active:
            call screen aai_main_menu
            while aai_mode == "talk":
                menu:
                    "Close":
                        $ aai_mode = None
            if aai_mode == "present":
                $ dossier_tab_control = "evidence"
                call screen dossier_ui
                lt "But there is no body to show it to."
            elif aai_mode == "examine":
                if mp_grandstands in aai_travel_left:
                    while(mp_grandstands in aai_travel_left):
                        call screen aai_examine_granstands
                else:
                    lt "I've already examined this area."
                    lt "I better {b}MOVE{/b} somewhere else instead."
            elif aai_mode == "move":
                jump act3_main_inves_maptravel_mode
        return

label racetrack_inves_vip:
        #Inves point Vip Lunge box
        lt "It's closed off for now, with police officers standing guard."
        lt "If I had to guess, Inspector Medina is questioning people inside."
        lt "I swear... Lorenzo must be fighting like hell to keep anyone from being taken to the police station."
        $ aai_investigated(mp_grandstands)
        return

label racetrack_inves_railing:
        #railing
        lt "That's a long way down... Judging by the distance between this railing and the ground, I don't think someone could just trip and fall over it. It practically reaches my neck."
        lt "You'd have to deliberately climb over it to jump... or have someone throw you over."
        return
    
    
# =================
#    Lockers
# =================

    
label lockers_inves:
        scene placeholder_lockers
        with fade
        l "What's with this locker? It's been left open."
        lt "As I walked over to close it, something in there catches my attention."
        l "A... hawaiin shirt? A pair of sunglasses, too..."
        lt "I guess these must belong to one of the jockeys."
        $ dossier.add(de_casualclothes)

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
        
        $ dossier.add(de_notebook)


# =================
#    Breakroom
# =================


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
            

# =================
#    Investigation COMPLETE
# =================

label inves_complete:
        of "Mr. Leopardo, correct?"
        lt "Ah- one of the police officers working for Medina just approached me."
        l "Indeed, that would be me! How may I help you?"
        of "Here is a copy of the preliminary autopsy report."
        $ dossier.add(de_autopsy)
        of "We also ran tests of the things you found and have the results. These are copies of them."
        $ dossier.add(de_shovel)
        $ dossier.add(de_blooddrops)
        $ dossier.add(de_bodybag)
        
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
        jump ce1

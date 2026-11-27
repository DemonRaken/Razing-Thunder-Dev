# =========================== #
#    Act 2 Investigations     #
# =========================== #

init 3 python:
    act2_inves_examine_areas = {
        mp_stables.name: AAI_ExamineArea(mp_stables.name, mp_stables.image + "_act2", [
            AAI_Hotspot((822, 818, 284, 192), "stables_stepladder"),
            #AAI_Hotspot((1375, 818, 232, 240), "stables_"),
        ]),
        # mp_paddock.name: AAI_ExamineArea(mp_paddock.name, mp_paddock.image, [
            
        # ]),
        mp_grandstands.name: AAI_ExamineArea(mp_grandstands.name, mp_grandstands.image, [
            AAI_Hotspot(( 141, 377, 874, 316), "racetrack_inves_vip"),
            AAI_Hotspot((367, 209, 507, 162), "racetrack_inves_railing"),
            AAI_Hotspot((508, 733, 430, 166), "racetrack_inves_body"),
        ]),
        mp_lockers.name: AAI_ExamineArea(mp_lockers.name, mp_lockers.image, [
            AAI_Hotspot((36, 829, 397, 486), "lockers_inves_openlocker"),
            #AAI_Hotspot((109, 329, 327, 502), "lockers_inves_throusers"),
        ]),
        mp_breakroom.name: AAI_ExamineArea(mp_breakroom.name, mp_breakroom.image, [
            AAI_Hotspot((1736, 528, 183, 405), "breakroom_invest_trashbin"),
        ]),
    }
    def act2_area_complete(area_name):
        return all(act2_inves_examined.get((area_name, h.label), False)
                    for h in act2_inves_examine_areas[area_name].hotspots)

    def act2_area_examined_count(area_name):
        return sum(act2_inves_examined.get((area_name, h.label), False)
                    for h in act2_inves_examine_areas[area_name].hotspots)
default act2_inves_examined = {}   # {(area_name, label): True}
#default aai_break = False

# =================
#    Act 2 Control Sections
# =================

label act2_main_inves:
    show text _("{size=150}{color=#ff5100}Investigation{/color}{/size}") at truecenter, investigation_text_zoom
    pause 2.0
    hide text
    $ aai_active = True
    $ aai_travel_left = [mp_stables, mp_grandstands, mp_lockers, mp_paddock] # add locations to map for investigation
    play music inves fadein 2.5
    jump act2_main_inves_maptravel_mode

label act2_main_inves_end:
    #n "This was the end."
    show text _("{size=150}{color=#ff5100}Investigation\nComplete{/color}{/size}")  at truecenter, investigation_text_zoom
    pause 2.0
    hide text
    $ aai_active = False
    lt "I got quite a lot of evidence. I should hurry and have the police officers analyze what they can."
    lt "Who knows when the inspector will finish with the questioning?"
    with fade
    jump act2_inves_complete

label act2_main_inves_maptravel_mode:
    if len(aai_travel_left) == 0: # done all investigations
        lt "Hm... seems like I looked everywhere worth checking. I'm ready now!"
        jump act2_main_inves_end
        
    $ dossier_tab_control = "map"
    call screen dossier_ui
    if aai_travel in aai_travel_done:
        lt "I already went to [aai_travel.name]."
        jump act2_main_inves_maptravel_mode
    if aai_travel not in aai_travel_left:
        lt "I don't have to do anything at [aai_travel.name]"
        jump act2_main_inves_maptravel_mode
    lt "I know! I'll visit [aai_travel.name] next!"
    $ dossier_tab_control = "evidence"
    if aai_travel == mp_stables: # locations jump table
        jump act2_stables_inves
    if aai_travel == mp_grandstands:
        jump act2_racetrack_inves
    if aai_travel == mp_paddock:
        jump act2_paddock_inves
    if aai_travel == mp_lockers:
        jump act2_lockers_inves


label act2_aai_examine(areaname):
    #while(mp_stables in aai_travel_left):
        $ aai_break = False
        $ quick_menu = False
        while not act2_area_complete(areaname.name) and not aai_break:
            call screen aai_examine_allinone(areaname.name, actinvesexarea=act2_inves_examine_areas)
        if act2_area_complete(areaname.name):
            $ aai_investigated(areaname)
        $ quick_menu = True
        return


label act2_generic_present_lucas_vicente:
    # When presenting anyhing other than mate to people [profiles/evidence] (No reaction, basically)
    # Lucas & Vicente
    show vi smile2 at slightright
    show lu neutral at slightleft
    with dissolve
    v "Sorry kid, I don't know what you want me to say about that."
    lu "Me neither..."
    #end
    return

label act2_generic_present_renata_esteban:
    # Renata & Esteban
    show rena smile
    r "What, you're giving that to me?"
    t det neutral "No! I just wanted to ask what you think about it!"
    show rena smile2
    r "Lame."
    #end
    return

label act2_generic_present_catalina:
    # Catalina
    t smile "Catalina, what do you think about this?"
    show cata deadpan
    c "I think I have better things to do than play 20 questions with you."
    tt "Can't say I didn't try..."
    #end
    return

label act2_generic_present_enzo_medina:
    # Enzo & Medina
    show en yell at slightleft
    show me neutral at slightright
    en "Magnificent! Truly, one of it's kind! What an amazing discovery you've made here, my boy!"
    t det yell blush "R-Really?"

    show me sweat2
    me "...you don't have a clue what he just showed you, do you?"

    show en smile
    en "None!"

    t aw neutral drop "..."
    #End
    return

label act2_racetrack_inves:
    scene placeholder_granstands with fade
    stop music
    $ callonce("racetrack1")
    while aai_active:
        call screen aai_main_menu
         
        while aai_mode == "talk":
            menu:
                "Collapsing horses":
                    call racetrack1_topic1
                "Catalina Moreno":
                    call racetrack1_topic2
                "Close":
                    $ aai_mode = None
        if aai_mode == "present":
            $ dossier_tab_control = "evidence"
            call screen dossier_ui
            if ce_object in [dp_leo, de_mate]:
                call racetrack1_presenting_mate
            else:
                show vi smile2
                v "Sorry kid, I don't know what you want me to say about that."
                show lu neutral
                lu "Me neither..."
        elif aai_mode == "examine":
            if mp_stables in aai_travel_left:
                call act2_aai_examine(mp_stables)        
            else:
                lt "I've already examined this area."
                lt "I better {b}MOVE{/b} somewhere else instead."
        elif aai_mode == "move":
            jump act2_main_inves_maptravel_mode
    return
label racetrack1:
    tl "Razing Thunder Derby. \nMain Racetrack."
    tt "I've seen this beauty of a track on my phone before, but…"
    tt "Being here in person is something else! Just looking at this place makes me wanna sign up for the race."

    # Here, the BG should change to Grandstands.

    t "Damn, these rows of seats go really high, huh…? Must be about three… no, four stories tall. The breeze must feel amazing up there."

    tt "Resisting the urge to aura farm on the balcony, I focus on the competitors here. Most of them seem to be taking their horses for a trot, while a handful are having trouble calming down their restless" 
    
    tt "animals."

    x "Stop. I already told you, you're pushing the creature too early in the last stretch of your stride."

    
    t "Hm?"

    # Vincent sprite here.
    show vi angry at slightright
    
    with dissolve
    x "Keep letting your nerves control the reins and you'll burn through the animal's stamina before you reach the halfway point of the track. If you don't fall off first, that is."

    # Lucas sprite here.
    show lu neutral at slightleft
    with dissolve
    x "I know. But I already fell behind in the last race. I can't pull any punches."

    tt "Overhearing their conversation, I hop over the railing and invite myself into their chat."
    
    t aha "Passion is all well and good, but you might wanna wait before hitting the nitro."
    show lu yell2
    lu "Huh? Who are—"

    show vi smile
    v "Hoh. And how long should this guy wait, then?"
    
    t grin "Naturally, the horse will tell him that. It's all about body language! I'm telling you, it'll scream at you when it's time to go all out."

    show vi angry
    v "Talking to his ride? Sounds like a very inconsistent and dangerous thing to rely on. We've already measured when fatigue sets in for Lucero and when his acceleration peaks."

    show lu neutral
    lu "…"

    v "Either way, spectators aren't allowed on this side of the fence, champ. You should get moving before security catches you."
    
    t smile "I'm actually a trainer, just like you. I'm Antonio Ortiz."

    show vi smile
    v "Vicente Ruiz. This boy here is Lucas Mendoza. I don't think I've seen you at the previous races, Antonio. Who's your jockey?"

    t "Catalina Moreno. Got hired for the job today."

    show vi angry
    v "Catalina—"

    show lu angry
    lu "…Moreno?"
    
    tt neutral drop "Yikes. Both their faces just soured."
    
    t aw smile drop "Uh… I take it you two aren't on friendly terms with her?"

    show vi smile2
    v "Find me someone who is. She won't give you the time of day if you're not one of the top contestants."

    show lu yell
    lu "A nepo baby through and through. Having everything served on a silver platter from the get-go… I wouldn't be surprised if this is just a hobby for her."
    
    tt aw neutral right "Well, I can't really blame them for having that kind of impression of her. It's a bit harsh, though. Catalina is as serious about competing as anyone else."

    show vi angry
    v "So what does Moreno's trainer want with us? Shouldn't you be helping her prepare?"

    t aw smile "That's not in her plans, apparently. I just wanted to ask the other competitors a few things about the race and the recent incidents."

    show vi smile
    v "Right, those. If Lucas is feeling up to it, you can go ahead."
    
    show lu smile
    lu "I don't mind. There's still time before the race begins."
    play music happy fadein 2.5

    $ dossier.add(dp_lucas)
    $ dossier.add(dp_vicente)

label racetrack1_investigating:
        # Grandstands
        # Check=Seats
        tt neutral "I read this derby can accommodate about 100,000 people. It'll probably get a lot more crowded in a few hours, once the main event starts."
        # When checking again
        tt aha "If I weren't working on a case, it'd be nice to kick back and just watch the races."

        # Luxury Box
        tt neutral closed "The luxury box. Us mortals who don't want to sell one of our kidneys are forbidden from entering."
        tt aw smile "A café, air conditioning, binoculars, an all-you-can-eat buffet, and an amazing view of the racetrack… Those VIP spectators have everything they could want."

        # When checking again
        tt neutral "While those first-class seats are reserved for VIPs, the café and the buffet aren't off-limits to the public."
        tt aw smile drop "I'm pretty sure whatever prices they're charging over there are way out of my wallet's league, though. I'll pass."

        # Main Racetrack
        # Monitor
        tt neutral "A screen showing recordings of the racers. You can watch the jockeys here once they go out of sight, along with the current standings."
        tt "Given the aerial footage, they probably use a drone to film it."
        # When checking again
        tt grin "Heh. It would be pretty funny if someone filmed everything on horseback, staying ahead of all the other jockeys. No one can keep up with the cameraman."
label racetrack1_presenting_mate:
        show vi angry
        v "Gonna have to turn you down, Antonio. On Lucas' behalf, that is!"
        show vi smile
        v "Can't let the jockey drink something weird before the race. I'll take the hit."
        show lu smile2
        lu "You just want to hog it for yourself."
label racetrack1_topic1:
        t neutral "Know anything about the horses that keep collapsing mid-race?"

        show lu neutral
        lu "A little. Me and the rest were all chasing the lead jockey back then."
        show lu frown
        lu "I remember seeing her horse collapse as we approached the finish line. There wasn't much time to react."

        show vi frown with dissolve
        v "That gal Valentina went down like someone fired a cannonball at her horse. Poor thing."

        show lu angry
        lu "One after another, the best riders keep fumbling right at the end. I don't think it's just a coincidence at this point."
        
        show vi angry
        v "But there's just no way all the pros make the same dumb mistake. It's unnatural."

        t aw neutral right "It's really worrying. What about your horse? Is it doing okay?"

        show lu smile3
        lu "Lucero is ready to deliver. We may be lacking in speed a bit, but we'll pull through."

        show lu smile2
        lu "He's been improving lately, too. I just need to make sure I don't push him beyond his limits."

        show vi smile

        v "And I'm making extra sure this fella is well-fed and doesn't get the hijinks before the big moment."

        t smile "Good to know. Hope you guys don't run into any issues after the race begins."

        show lu angry
        lu "…You're not hoping we'll drop out like Valentina and the others, are you?"

        t neutral drop "N-no? Why would you think that?"

        show lu yell
        lu "You are Moreno's trainer."

        t neutral right "…I see where you're coming from. Fair enough. But I still don't want anyone to drop out."

        t aw neutral right "I mean, what's the point of competing if you can't go all out against your rivals? Training for months, only to be forced to retire like that…"

        t aw smile "These folks who've put in all that effort deserve better, yeah? Even if they don't snatch first place."

        show lu neutral
        lu "…"

        v "This guy gets it. That's how a race should be. If it were novice mistakes or fatigue, it wouldn't be such a big deal."

        show vi smile2

        v "Alas. We can only pray this gets resolved so the kids can ride as they should."
label racetrack1_topic2:
        show vi angry with dissolve
        v "Alright, young man. Spill the beans. Did the Moreno girl send you here to mess with Lucero?"

        t det yell "What—no! I wouldn't do something like that! It's horrible to hurt animals just to get an advantage."

        v "Then what about hurting Lucas here?"

        t aw neutral drop "That's assault. I'm pretty sure security would kick me out if I tried."

        v "Right you are. We already have our hands full preparing as best as we can."
        
        show lu angry
        lu "We really can't afford any mistakes at this stage..."

        t neutral "Why do you need to win that badly?"

        v "This isn't just a hobby, kid. It's a professional career. We can't exactly have Lucas compete in races on goodwill alone."

        show lu frown
        lu "Cash prizes are usually help us keep things going, but..."

        show vi smile
        v "It would be a whole lot story with backing from a proper sponsor. But I say this kid will make it through, without or without one!"

        tt neutral right "Huh... seems like they have it rough. So there jockeys who compete this way too, without any financial support.."

        tt neutral "Wait, I should ask Vicente why he thinks Catalina is some kind mobster leader."

        t aw neutral right "Why do you think Catalina is giving me these kinds of orders? I get that she isn't the most… amicable person, but…"

        show vi frown
        v "It's nothing against you, bud. There are just some unsavory rumors going around."

        t neutral "Rumors? About Catalina?"

        show lu angry
        with dissolve
        lu "Like how she's using her family's wealth to take ownership of the other competitors' horses and force them to quit."
        
        show lu neutral
        lu "I don't know how much of that is true, but I wouldn't be surprised if someone was pulling strings behind the scenes."

        t neutral drop "Wha… So you're saying she's paying her way to win? There's no way that'd go unnoticed."

        v "Hence why they're just rumors. Bribing other trainers to quit their jobs, slipping the officials some cash to overlook doping…"

        tt aw neutral drop "I really hate the idea of working for someone who does all that, but I can't outright deny it's possible."

        t neutral drop "Hang on, is that why her previous trainer quit? Because of the rumors surrounding her, or…?"
        show lu frown
        lu "We don't really know. It's not like he came to tell us before quitting. Some say he got cut off from Moreno's team after being caught red-handed carrying out her orders…"
        show vi angry
        v "Could be the man just didn't agree with her methods and wanted none of it any longer."

        t aw neutral right "Is that so…?"
label racetrack1_complete:
        show vi smile
        show lu neutral
        v "Alright, we should get back to it. Lucero here is getting restless."

        t smile "Right, of course. Thank you two for your time."
        hide lu
        hide vi 
        with dissolve
        
        tt neutral "The duo nods at me before going back to their business."

        tt neutral closed "Alright, where to go next…?"
        return

label stables1_presenting:
    # Dossier > Presenting Mate
    show cata neutral with dissolve
    c "How kind of you. What brand of yerba did you use?"

    t smile "Tarawii."
    
    show cata frown with dissolve
    c "…You might as well have picked some grass off the ground. It wouldn't make a difference."
    
    show cata smile2
    c "Next time, try using Crauz."

    tt aw neutral right "But I like Tarawii..."
    return

label act2_stables_inves:
    scene placeholder_stables with fade
    stop music
    #$ callonce("stables1")
    while aai_active:
        call screen aai_main_menu
         
        while aai_mode == "talk":
            menu:
                "Collapsing horses":
                    call stables1_topic1
                "Catalina Moreno":
                    call stables1_topic2
                "Close":
                    $ aai_mode = None
        if aai_mode == "present":
            $ dossier_tab_control = "evidence"
            call screen dossier_ui
            if ce_object in [dp_leo, de_mate]:
                call stables1_presenting
                
            else:
                call act2_generic_present_catalina
        elif aai_mode == "examine":
            if mp_stables in aai_travel_left:
                call act2_aai_examine(mp_stables)        
            else:
                lt "I've already examined this area."
                lt "I better {b}MOVE{/b} somewhere else instead."
        elif aai_mode == "move":
            jump act2_main_inves_maptravel_mode
    return
# Dossier: Presenting evidence (mate)
label paddock1_presenting:
    show rena smile at slightleft
    show est neutral at slightright
    with dissolve
    r "So you can be useful. I was feeling pretty thirsty."

    show rena angry

    r "This shit better not be lukewarm."

    show est smile

    e "You don't have to drink it if you don't like it, Renata."

    t det yell "It isn't lukewarm! That'd defeat the point of carrying a thermos."

    show rena neutral

    r "We'll see about that… *sip sip sip*"

    show rena smile with dissolve
    r "…Hm. Hah! Not bad. I'll be keeping this."

    t aha "Wha—oh, haha. Good one."

    show rena neutral 
    r "…"

    show est smile2

    e "Renata, I believe that's his…"

    show rena yell
    r "What? He can get another one."

    tt what drop "This was a mistake."
    return
label act2_paddock_inves:
    scene placeholder_paddock with fade
    stop music
    #$ callonce("stables1")
    while aai_active:
        call screen aai_main_menu
         
        while aai_mode == "talk":
            menu:
                "Collapsing horses":
                    call paddock1_topic1
                "Catalina Moreno":
                    call paddock1_topic2
                "Close":
                    $ aai_mode = None
        if aai_mode == "present":
            $ dossier_tab_control = "evidence"
            call screen dossier_ui
            if ce_object in [dp_leo, de_mate]:
                call paddock1_presenting
                
            else:
                call act2_generic_present_renata_esteban
        elif aai_mode == "examine":
            if mp_stables in aai_travel_left:
                call act2_aai_examine(mp_stables)        
            else:
                lt "I've already examined this area."
                lt "I better {b}MOVE{/b} somewhere else instead."
        elif aai_mode == "move":
            jump act2_main_inves_maptravel_mode
    return
label act2_lockers_inves:
    scene placeholder_lockers with fade
    stop music
    #$ callonce("stables1")
    while aai_active:
        call screen aai_main_menu
         
        while aai_mode == "talk":
            menu:
                "Razing Thunder Derby":
                    call lockers1_topic1
                "Close":
                    $ aai_mode = None
        if aai_mode == "present":
            $ dossier_tab_control = "evidence"
            call screen dossier_ui
            if ce_object in [dp_leo, de_mate]:
                call paddock1_presenting
                
            else:
                call act2_generic_present_enzo_medina
        elif aai_mode == "examine":
            if mp_stables in aai_travel_left:
                call act2_aai_examine(mp_stables)        
            else:
                lt "I've already examined this area."
                lt "I better {b}MOVE{/b} somewhere else instead."
        elif aai_mode == "move":
            jump act2_main_inves_maptravel_mode
    return

# The game starts here.
#    $ config.side_image_tag = "leo" # side is only Leo + sticky
#    $ config.side_image_tag = "tony" # side is only tony + sticky
#    $ config.side_image_tag = ""  # side is whoever is talking (default)
#transform slight_jump:
    #easein .15 yoffset -20
    #easeout .15 yoffset 0
# label act2:
    #l neutral "I am here."
    #show leo smile
    #l "I forgot to show myself."
    #l neutral "I forgot what other sprites I got..." with vpunch
    #l smile "It's really dark in here. I need a flashlight."
    #t what drop "something"
    # show leo neutral at left
    # show tony neutral at right
    #pause 2
    # show side tony smile "Tonysception"
    #show leo smile at slight_jump, left
    #show cata neutral
    #c "Can you change emotes while someone else talks?"
    #t what drop ""
    #c "That would be like live reaction to events."
    #t #neutral ""
    #c "And a little neat detail too to react to what happens."
    #c "I only mean Tony's sprites really, so we don't need others."
    #return

label act2:
    scene placeholder_stables
    tl "9:40 AM.\nRazing Thunder Derby.\nStables."

    tt "Whew… we're finally done with all the paperwork. I'm \"{color=#FF9900}Dama de Plata's{/color}\" trainer now, even if only in name."
    show cata neutral with dissolve
    c "Several participants have withdrawn from the competition, so there are plenty of vacant stalls. You can keep Chispa in one of them."

    show side tony neutral at left
    tt "What's this? A rare kind gesture from Miss Ice Queen?"

    show side tony smile normal
    t "Thanks. I'll do just that, then."
    tt "I lead La Chispa to one of the vacant stalls, preparing hay and water for her."

    c "Don't thank me. I'm just stating the obvious. The last thing I need is your horse running around wild and causing a mess."
    
    show side tony det smile
    t "Hmph. Don't underestimate her, La Chispa. Offer her a sweet treat as a reward, and she'll become faster than a lightning bolt. Might even give your horse a run for her money."
    
    show cata angry with dissolve
    c "If that's supposed to be a joke, it isn't amusing. At all."
   
    show cata neutral with dissolve
    show side tony neutral drop with dissolve
    c "If you're done here, I'd appreciate it if you took your leave. I have preparations to make before the race begins."
    
    show side tony neutral
    t "Getting your head in the game? In that case, I could—"
    show cata angry
    c "No."

    show side tony aw neutral drop
    t "…Alright, alright, I'm leaving. Geez."
    
    hide cata with dissolve
    show side tony neutral right with dissolve
    tt "I turn towards La Chispa's stall and approach her."
    
    show side tony smile normal
    t "Keep an eye on 'em for me, will you?"

    ch "…"

    show side tony grin
    t "Too busy stuffing your mouth, eh…?"
    
    hide side tony
    tt "It doesn't seem like Catalina is in a chatty mood. I should look around elsewhere and see what I can find."

    tt "With all these incidents, security is super tight. Not even an ant could sneak into the derby."

    tt "The clandestine gambling, the mystery behind the collapsing horses… There's bound to be a clue out there!"

    label racetrack1:
        scene placeholder_granstands with dissolve
        
        tl "Razing Thunder Derby. \nMain Racetrack."
        tt "I've seen this beauty of a track on my phone before, but…"
        tt "Being here in person is something else! Just looking at this place makes me wanna sign up for the race."

        # Here, the BG should change to Grandstands.

        t "Damn, these rows of seats go really high, huh…? Must be about three… no, four stories tall. The breeze must feel amazing up there."

        tt "Resisting the urge to aura farm on the balcony, I focus on the competitors here. Most of them seem to be taking their horses for a trot, while a handful are having trouble calming down their restless animals."

        x "Stop. I already told you, you're pushing the creature too early in the last stretch of your stride."

       
        t "Hm?"

        # Vincent sprite here.
        show vi test at right with dissolve
        x "Keep letting your nerves control the reins and you'll burn through the animal's stamina before you reach the halfway point of the track. If you don't fall off first, that is."

        # Lucas sprite here.
        show lucas test at left with dissolve
        x "I know. But I already fell behind in the last race. I can't pull any punches."

        tt "Overhearing their conversation, I hop over the railing and invite myself into their chat."
        show side tony aha at left
        t "Passion is all well and good, but you might wanna wait before hitting the nitro."

        lu "Huh? Who are—"

        v "Hoh. And how long should this guy wait, then?"
        show side tony grin
        t "Naturally, the horse will tell him that. It's all about body language! I'm telling you, it'll scream at you when it's time to go all out."

        v "Talking to his ride? Sounds like a very inconsistent and dangerous thing to rely on. We've already measured when fatigue sets in for Lucero and when his acceleration peaks."

        lu "…"

        v "Either way, spectators aren't allowed on this side of the fence, champ. You should get moving before security catches you."
        show side tony smile normal
        t "I'm actually a trainer, just like you. I'm Antonio Ortiz."

        v "Vicente Ruiz. This boy here is Lucas Mendoza. I don't think I've seen you at the previous races, Antonio. Who's your jockey?"

        t "Catalina Moreno. Got hired for the job today."

        v "Catalina—"

        lu "…Moreno?"
        show side tony neutral drop
        tt "Yikes. Both their faces just soured."
        show side tony aw smile drop
        t "Uh… I take it you two aren't on friendly terms with her?"

        v "Find me someone who is. She won't give you the time of day if you're not one of the top contestants."

        lu "A nepo baby through and through. Having everything served on a silver platter from the get-go… I wouldn't be surprised if this is just a hobby for her."
        show side tony aw neutral right
        tt "Well, I can't really blame them for having that kind of impression of her. It's a bit harsh, though. Catalina is as serious about competing as anyone else."

        v "So what does Moreno's trainer want with us? Shouldn't you be helping her prepare?"
        show side tony aw smile
        t "That's not in her plans, apparently. I just wanted to ask the other competitors a few things about the race and the recent incidents."

        v "Right, those. If Lucas is feeling up to it, you can go ahead."

        lu "I don't mind. There's still time before the race begins."

        label racetrack1_topic1:
            t "Know anything about the horses that keep collapsing mid-race?"

            lu "A little. Me and the rest were all chasing the lead jockey back then."

            lu "I remember seeing her horse collapse as we approached the finish line. There wasn't much time to react."

            v "That gal Valentina went down like someone fired a cannonball at her horse. Poor thing."

            lu "One after another, the best riders keep fumbling right at the end. I don't think it's just a coincidence at this point."

            v "But there's just no way all the pros make the same dumb mistake. It's unnatural."

            t "It's really worrying. What about your horse? Is it doing okay?"

            lu "Lucero is ready to deliver. We may be lacking in speed a bit, but we'll pull through."

            lu "He's been improving lately, too. I just need to make sure I don't push him beyond his limits."

            v "And I'm making extra sure this fella is well-fed and doesn't get the hijinks before the big moment."

            t "Good to know. Hope you guys don't run into any issues after the race begins."

            lu "…You're not hoping we'll drop out like Valentina and the others, are you?"

            t "N-no? Why would you think that?"

            lu "You are Moreno's trainer."

            t "…I see where you're coming from. Fair enough. But I still don't want anyone to drop out."

            t "I mean, what's the point of competing if you can't go all out against your rivals? Training for months, only to get injured like that…"

            t "These folks who've put in all that effort deserve better, yeah? Even if they don't snatch first place."

            lu "…"

            v "This guy gets it. That's how a race should be. If it were novice mistakes or fatigue, it wouldn't be such a big deal."

            v "Alas. We can only pray this gets resolved so the kids can ride as they should."
        label racetrack1_topic2:
            v "Alright, young man. Spill the beans. Did the Moreno girl send you here to mess with Lucero?"

            t "What—no! I wouldn't do something like that! It's horrible to hurt animals just to get an advantage."

            v "Then what about hurting Lucas here?"

            t "That's assault. I'm pretty sure security would kick me out if I tried."

            v "Right you are."

            t "Why do you think Catalina is giving me these kinds of orders? I get that she isn't the most… amicable person, but…"

            v "It's nothing against you, bud. There are just some unsavory rumors going around."

            t "Rumors? About Catalina?"

            lu "Like how she's using her family's wealth to take ownership of the other competitors' horses and force them to quit."

            lu "I don't know how much of that is true, but I wouldn't be surprised if someone was pulling strings behind the scenes."

            t "Wha… So you're saying she's paying her way to win? There's no way that'd go unnoticed."

            v "Hence why they're just rumors. Bribing other trainers to quit their jobs, slipping the officials some cash to overlook doping…"

            tt "I really hate the idea of working for someone who does all that, but I can't outright deny it's possible."

            t "Hang on, is that why her previous trainer quit? Because of the rumors surrounding her, or…?"

            lu "We don't really know. It's not like he came to tell us before quitting. Some say he got cut off from Moreno's team after being caught red-handed carrying out her orders…"

            v "Could be the man just didn't agree with her methods and wanted none of it any longer."

            t "Is that so…?"
        label racetrack1_complete:
            v "Alright, we should get back to it. Lucero here is getting restless."

            t "Right, of course. Thank you two for your time."
            hide lucas with dissolve
            hide vi with dissolve
            tt "The duo nods at me before going back to their business."

            tt "Alright, where to go next…?"
                    
    return
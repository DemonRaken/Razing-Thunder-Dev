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
    $ dossier_enabled = True
    scene placeholder_stables
    with fade
    tl "9:40 AM.\nRazing Thunder Derby.\nStables."
    play music happy2 fadein 2.5
    tt "Whew… we're finally done with all the paperwork. I'm \"{color=#FF9900}Dama de Plata's{/color}\" trainer now, even if only in name."
    show cata neutral with dissolve
    c "Several participants have withdrawn from the competition, so there are plenty of vacant stalls. You can keep Chispa in one of them."

    tt neutral "What's this? A rare kind gesture from Miss Ice Queen?"
 
    t smile "Thanks. I'll do just that, then."
    tt "I lead La Chispa to one of the vacant stalls, preparing hay and water for her."

    c "Don't thank me. I'm just stating the obvious. The last thing I need is your horse running around wild and causing a mess."
    
    t det smile "Hmph. Don't underestimate her, La Chispa. Offer her a sweet treat as a reward, and she'll become faster than a lightning bolt. Might even give your horse a run for her money."
    
    show cata angry
    c "If that's supposed to be a joke, it isn't amusing. At all."
   
    show cata neutral
    c "If you're done here, I'd appreciate it if you took your leave. I have preparations to make before the race begins."
    
    t neutral "Getting your head in the game? In that case, I could—"
    
    show cata angry
    c "No."

    t aw neutral drop"…Alright, alright, I'm leaving. Geez."
    
    hide cata with dissolve
    tt neutral right "I turn towards La Chispa's stall and approach her."
    
    t smile "Keep an eye on 'em for me, will you?"

    ch "…"

    t grin "Too busy stuffing your mouth, eh…?"
    
    tt neutral right "It doesn't seem like Catalina is in a chatty mood. I should look around elsewhere and see what I can find."

    tt closed "With all these incidents, security is super tight. Not even an ant could sneak into the derby."

    tt det neutral "The clandestine gambling, the mystery behind the collapsing horses… There's bound to be a clue out there!"

label paddock1:
        scene placeholder_paddock 
        with fade
        stop music
        tl "Razing Thunder Derby. \nPaddock."
        
        tt "This place isn't too far from the stables. Looks like a few racers are getting their horses fitted with equipment and parading them around for the spectators."

        tt "Others seem to be coming and going to the betting booth en masse—"

        x "Hey, you."

        t "…?"

        show rena smile at slightleft 
        with dissolve 

        x "Yes, you, the guy with the dumb face."

        tt what det neutral "The hell?"

        x "I saw you earlier tagging along with Catalina. I'm shocked that girl would spare any time to talk with friends."

        t neutral "Well… she hired me as her trainer."

        show rena smile2
        x "Hah! So you're the new unlucky bastard, huh?"
        
        show est smile at slightright 
        with dissolve 
        
        x "Now, now, you just met the poor guy and you're already giving him a hard time?"

        x "Sorry about that. I know she can be a handful."

        show rena angry
        x "Hey, don't go saying sorry on my behalf!"

        t neutral "It's alright. I'm Antonio Ortiz. From how you're dressed, I'm guessing you two will be competing in the race too?"

        e "That's right. Pleasure to meet you. I'm Esteban Rojas, and this here—"

        show rena smile
        r "Renata Vargas. Burn that into your head, 'cause that name will be making headlines after I get first place."

        e "Technically, you already won the previous race."

        show rena angry with dissolve

        r "Yeah, but those dumbass officials voided the result and made us race again."

        t neutral right "With good reason. If the horses are at risk, that takes precedence over—"

        show rena neutral with dissolve

        r "Who cares? It's just petty excuses. You don't want your ride fainting? Feed it properly, then. You won't see Picaro making a blunder like that."

        show rena smile2
        r "Not like I would expect you to get it."

        tt what det neutral "Why you…! Ugh, I'd better just ask what I need to and get out of here." 
        play music happy2 fadein 2.5
        $ dossier.add(dp_renata)
        $ dossier.add(dp_esteban)
        
        #label paddock1_investigating:
        label paddock1_topic1:
            t neutral "So you said Picaro is in good health, but do you know anything about the other jockeys' horses? Any idea why they keep collapsing…?"
            
            show rena angry with dissolve
            r "How the hell should I know? You think I waste my time following those losers all day, huh?"

            t what det neutral drop "You could have overheard something or noticed something out of the ordinary, I don't know…!"

            show rena yell

            r "You wish. Even if I had, why should I tell you?"

            show est neutral with dissolve

            e "Renata."

            show rena angry

            r "What? For all I know, he's behind it. He might even be trying to find out whether anyone's onto him."

            t det yell "I just want to know what's causing it so I can stop it!"

            show rena smile2 with dissolve

            r "Hah, a puny guy like you? Catalina sent you on an errand to protect her mule?"

            t det "No. I'm doing it for the sake of all the competing horses, not just hers."

            show rena neutral
            r "…Hmph."

            show est neutral

            e "That's very admirable. Unfortunately, there isn't much we can tell you. We double-checked the water supply and the food used here for signs of foul play, but everything seems clean."

            t neutral "You checked this yourselves?"

            show est frown

            e "Yeah. No trainer wants to see another horse collapse, so most of us collaborated to see if we could find anything amiss."

            show rena angry

            r "We started checking crap after that dolt Valentina fell on her ass during the last race."

            t "I see... Then, let me ask you something. Do the horses show any signs of exhaustion before the race? Or exhibit any unusual behavior?"

            show est neutral

            e "Not quite. Every horse is examined and saddled before the race begins. If they were feeling unwell to begin with, they wouldn't be cleared to participate."

            e "If a horse is truly unwell, a professional will spot it immediately. They were perfectly healthy right up until the moment they fell."

            t neutral drop "Zero signs? Are you sure about that?"

            show est angry

            e "I stake my reputation on it, Antonio. A trainer's eye doesn't miss these things."

            tt neutral closed "He sounds incredibly confident. But if the horses were really fine, why did they collapse...?"

            t neutral "Have any collapsed after the race?"

            show rena yell with dissolve

            r "Are you brain-dead? The races have only been stopped because horses fainted during them. What does it matter what happens afterward?"

            show est smile2

            e "It would certainly be concerning if horses were collapsing even after the event was postponed, but I'm not aware of anything like that happening."

            t "I see…"

            tt neutral right "I'd like to be as reassured as Esteban seems to be. But I wonder… Who actually performs these inspections? And how thorough are they, really? If there's room to manipulate the results, then…"
        label paddock1_topic2:
            t neutral "What can you tell me about Catalina?"

            show rena yell2 with dissolve

            r "HER? That ice queen makes Elsa look warm and friendly! I can't stand her."

            tt what aw drop "T-The one from the movie…?"

            show est smile with dissolve

            e "Her riding skills are remarkable, as expected from someone of her lineage. She's among the top contenders, and one we're keeping a close eye on."

            show rena angry

            r "Bah! I already beat her in the previous race, and I'll do it again today!"

            t smile "Bitter rivals to the end, huh?"

            show est smile2

            e "It's only natural. Renata wants to beat the best and stand at the top."

            show rena smile3 with dissolve

            r "It's especially sweet to take down some sheltered girl who's built her career on her parents' money."

            e "That's selling her a little short, don't you think?"

            show rena angry

            r "Whatevs. All the wealth in the world means jack if you can't compete in the race."

            tt aw smile "...She's yelling at me, but she's brushing Pícaro like he's made of glass. Her hands are completely gentle with him."

            t neutral "Why wouldn't she be able to compete?"

            show rena neutral with dissolve

            r "You gotta have a trainer to help prep before the start of the race. The bare minimum legal obligations, you see. I'm certain the host would do without that if he could get away with it."

            tt what drop "He would? That's concerning."

            t neutral "I've been wondering about that. What happened to her previous trainer? Why is it that no one would take the job?"

            show rena yell
            r "Cause no one wants to get involved in shady crap, that's why!"

            t "Meaning…?"

            r "She's behind all those accidents you mentioned, genius. She's been getting rid of anyone who stands in her way!"

            show rena angry

            r "It's pathetic, really. Things should be settled on the racetrack, not by using money, connections, or whatever to take out the competition. It means nothing if you win that way."

            show est neutral with dissolve

            e "Those are just rumors, Antonio. There's no proof that Catalina has anything to do with the incidents."

            show rena neutral

            r "Hmph. Believe what you want. I wouldn't get anywhere near that woman if I were you."

            show rena smile2
            r "Though I guess in your case you can't avoid it. You're shit out of luck."

            tt neutral right "So that's why nobody wanted the job…"

            tt aw neutral drop "I can't say I'm thrilled about being treated like some disposable placeholder."

            tt neutral drop "Still, that's not what I came here for. As long as she leaves me to my own devices, this arrangement works in my favor."
        label paddock1_complete:    
            show est smile     
            e "Oh, look at the time. We'd better wrap things up here, Renata."

            show rena angry with dissolve

            r "Yeah, yeah. The old geezers have had a good look at who's gonna leave everyone else in the dust by now."

            t aha "You wanted the elderly to see Pícaro?"

            show rena yell

            r "Not just them, dumbass! Anyone here, really."

            show est neutral

            e "There are plenty of people who decide who to bet on just by watching the horses move around the parade ring. That's what makes this such an important moment to show off."

            t smile "Oh, that makes sense…"

            r "I wouldn't stick around out here this long if I had a choice, though. Watching me race before should be more than enough."

            show est smile

            e "We have obligations, Renata. You wouldn't want to lose all that support from your sponsors, would you?"

            show rena neutral with dissolve

            r "…"

            e "So, there you have it. Good luck to you, Antonio."

            hide rena
            hide est 
            with dissolve

            tt neutral right "The two of them went back to resume the parade. Sponsors, huh...? Must be some kind of contractual obligation. I wonder how many other jockeys have to put up with that."

            tt aw neutral drop "I can't imagine Catalina being one of them, given what I've heard about her and her family's wealth. Ugh…"
label stables1:
        scene placeholder_stables with fade
        # Only after moving areas once at least.
        stop music
        tl "Razing Thunder Derby.\n Stables."
        
        
        show cata yell at slightright
        with dissolve
        c "I told you already, I've got that matter handled. You can buzz off now."

        t "…?"
        
        show seb smile at slightleft
        with dissolve
        x "Nonsense! I know your situation very well. There's no need to put on a tough act."

        show cata angry
        c "It's not an act. It's reality."

        x "So stubborn. I can get in touch with one of my men in no time, really. All you have to do is—"
        
        show cata smile
        c "…Great timing. Look over there. My trainer is back."

        show seb neutral

        x "What?"

        t grin "…Hey there! How's it going?"

        show seb grr
        x "This chump with the scar? He isn't even dressed for the job!"

        tt det yell "Excuse me!? My clothes are very classy!"

        show cata smile3
        c "It doesn't matter. All the paperwork has been taken care of. You can check with the desk if you don't believe me."

        show seb angry
        x "Tch. That's exactly what I'll do. Then I'll have this country bumpkin out of my Derby!"

        hide seb
        show cata angry
        with dissolve

        c "Since when did it become your Derby…?"

        t aha "Geez. That man almost makes you seem nice in comparison, Catalina."

        show cata at center
        with dissolve
        c "Careful, Ortiz. Just because I can't afford to fire you doesn't mean I won't dock your pay."

        t aw neutral drop "…Yes, ma'am."

        tt "Who was that, anyway? I'd better ask before she starts ignoring me again."
        play music cata fadein 2.5
        
        # label stables1_investigating:
        #     # Investigation
        #     # Stepladder
        #     t neutral right "Looks like a sturdy step ladder. Maybe someone was changing a lightbulb?"
        #     show cata neutral
        #     c "It's just a regular ladder."
        #     t det yell "No, no, see? It folds! That makes it the natural evolution of the standard ladder!"
        #     show cata deadpan with dissolve
        #     c "…"
        label stables1_topic1:
            t neutral "Who were you talking to, Catalina? I could tell from a mile away you couldn't stand the sight of him."
            
            show cata neutral with dissolve
            c "Sebastian Castillo. He's the Sponsorship Director for one of Razing Thunder's main sponsors. They back a handful of jockeys here, including top contenders like Vargas."

            t det yell "Castillo— as in, from THE Castillo family!?"

            c "So you've already heard about them. That saves me time."

            # Check a flag if they answered they know Moreno in ACT 1. If yes:
            if knowcata:
                show cata smile
                c "You hardly look the part, but you're surprisingly well-informed. That is... commendable."

                tt what drop "What kind of backhanded compliment is that…?"

            # If they don't know Moreno:
            else:
                show cata angry2
                c "…How is it that you know about a lowlife like him, but not me? Frankly, I am appalled."

                tt neutral closed "Because it's my JOB to deal with crooks like him…"

            #Back to main branch

            show cata neutral
            c "The sponsorship is merely a front. They do actually back jockeys, however…"

            t neutral "It comes with its own 'perks', right?"

            show cata angry
            c "Yes. You're bombarded with guidelines on how to drive betting activity. How to behave on social media, in public…"

            show cata neutral with dissolve
            c "They even give you 'recommendations' on which races to go all-in on, and which ones to intentionally throw."

            t det neutral "All-in— you mean they're telling competitors when to lose and when to win?"

            t det yell"But that would completely rig the results!"

            c "…And now you know how they build their wealth. Not that they'd ever admit to it. They simply label it 'consulting'."

            t det neutral right "That's despicable… all for the sake of manipulating the betting market, huh?"

            show cata angry
            c "I hear they even run their own off-the-books betting syndicate. It's quite lucrative, especially during events like this. I want no part of it, however."

            tt closed neutral "Clandestine gambling…"

            t neutral "Do you know which jockeys are sponsored by the Castillos?"

            show cata neutral
            c "I don't bother remembering the fodder."

            tt what drop "That's brutal…"

            c "One does come to mind, though. Vargas. She's their top pick for promotion. Renata Vargas."

            t neutral "Interesting…"
            $ dossier.add(dp_sebastian)
        label stables1_topic2:
            t neutral drop "I, uh… I heard some unsavory rumors going around."
            show cata surprise with dissolve
            c "Oh?"

            t neutral right "From the other jockeys, I mean. Mostly about you."

            c "I see. And?"

            t det yell "What do you mean, 'and'!? Don't you care about being slandered? They're saying you're using your money to bribe trainers into quitting. Some even claim you're behind the horses collapsing."
            
            show cata smile3 with dissolve
            c "I have an inkling of who told you about that last one. It's not the first time I've heard those accusations from the likes of her."
            
            show cata neutral
            c "So? Do you believe those rumors?"

            menu:
                "Yes":
                    jump rumors_yes
                "No":
                    jump rumors_no                
            label rumors_yes:
                t aw neutral drop "It's not just one person saying it. Quite a few people seem to believe it. Plus, you're in a rather favorable position to pull it off, so…"

                show cata angry
                c "…If you've already made up your mind, there's not much more for me to say."
                jump stables1_complete
            label rumors_no:
                t neutral right "Rumors are just that. Rumors. I need solid evidence to back those claims. That's why I'm asking you directly."

                show cata surprise with dissolve
                c "…You're acting as if my word alone were indisputable proof."

                t neutral "Well, it might not be, but it's reassuring to hear it from you nonetheless."
                jump stables1_complete
         
        label stables1_complete:
            show cata frown with dissolve

            c "…I suppose now you understand why I hired you, then."

            t "Because no amount of money is worth the risk?"
            
            show cata angry
            c "It ruins the reputation of any self-respecting trainer who wants a future in the industry. Most don't want to be caught up in some blackmail scheme or be told to sabotage the racehorses. Ridiculous…"

            t "So then, the rumors aren't true?"

            show cata neutral
            c "I want to win through my skill, not rely on petty tricks like that."

            tt neutral right "That's a relief to hear, but I wonder how much of that I can really believe."

            show cata smile3 with dissolve
            c "Now, if you aren't planning on quitting after learning all of this, I expect you to be ready on time."

            t smile "You got it. By the way…"

            show cata neutral

            c "What is it?"

            t aha "How come I don't get a matching uniform? You know, a blue tracksuit, maybe?"

            
            show cata smile2 with dissolve
            c "Sorry, I didn't know your size, so I didn't order one."

            t aw smile "Did my boss not tell you…?"

            show cata smile with dissolve
            c "I didn't ask her."

            tt what aw drop "Figures…"

            t aha "It doesn't have to be brand new. Hand-me-downs are fine."

            show cata deadpan2 with dissolve

            c "First off, no trainer of mine would wear recycled clothing. Second, I have no interest in letting you wear the clothes of a coward who quit. They've already been disposed of."

            tt what det drop "So much for that."
label lockers1:
        scene placeholder_lockers
        with fade
        stop music
        x "You can't be serious about going through with this little event."

        x "Oh, but I am! Don't you know? The show must go on!"

        tt "What's with this commotion...? And that voice is—"

        show en grin at left
        with dissolve
        
        show me yell at slightright
        with dissolve
        

        x "There isn't going to be much of a show if all your participants keep dropping like flies!"

        show en smile

        x "Well now! It's your job to prevent that, yes? It's why I made an exception and allowed you in."

        show me angry

        x "Yeah. A job you aren't making any easier for me to carry out."

        show en neutral

        x "Has my magnanimous cooperation not been to your liking, inspector?"
        
        show en yell
        x "If you're not happy, then I am not happy."

        show me angry2
        x "Oh, I'm pretty unhappy, alright, you conniving son of a—"

        t neutral drop "Hey, hey! What's going on here?"

        show en smile

        x "Oh! Howdy, young man. The inspector here and I were having a pleasant chat about the Razing Thunder event."

        show me neutral with dissolve
        x "It's anything but pleasant... What the hell are you doing here, Ortiz? I've got enough crap to deal with as it is, thanks to this guy."

        x "Ah, you two are already acquainted?"

        x "Regrettably."

        t what aw drop "It's nice to see you too, inspector Medina."

        scene black 
        show me neutral at center
        with fade

        tt smile "Police inspector Sofia Medina. We've worked together on cases before."

        tt aha "...well. It's more accurate to say I've crashed into crime scenes that she happened to be in charge of. To help, of course!"

        tt neutral right "The inspector managed to take me in for questioning a while ago, so she knows about me being El Leopardo..."

        tt neutral closed "...but as for how I'm still allowed to walk free? I have no idea."

        tt neutral "Arbitrary exercise of justice will put you in the slammer. We're both aware of that. So why?—"

        scene placeholder_lockers
        show en smile at left        
        show me neutral at slightright
        with fade
        show me yell
        me "…I swear, if I find out you sneaked in here, I'm—"

        show en neutral
        x "Oho, a trespasser? Quite daring. I have security on speed dial for cases like this."

        t det yell "Whoa! Hang on now, I'm here on a job! Catalina Moreno hired me as her trainer! You can check with her if you want."

        show en grin

        x "That's wonderful news! I was worried that Ms. Moreno wouldn't be able to compete after her trainer walked out on her…"
        show me angry
        me "Why did she have to go and get you of all people?"

        t aw smile drop "Apparently, I was the only one willing to take the job…"
        show me neutral
        me "…That checks out."

        tt neutral drop "Phew... she won't send the K9s after me now, at least."

        t neutral "So, who is this you were talking to…?"

        show en smile

        en "Ah, where are my manners? Lorenzo Villarreal. I'm the organizer of the greatest horse-racing event you're ever likely to experience."

        t det yell "Oh…! You're the host of Razing Thunder?"

        $ renpy.notify("Dossier Updated.")

        en "Indeed I am, my boy! How's the place been treating you so far? No doubt the caviar and champagne have sweetened your stay."

        t aw smile "I… haven't had either of those."
        show en neutral
        en "Ah. I see. You're one of *those*. Rest assured, you will still be able to enjoy yourself at my Derby."

        tt what det drop "One of 'those'? What does that even mean…?" 
        tt neutral right "Anyway, this is a perfect chance to ask about the clandestine gambling. There's no way the host himself doesn't know anything about it."
        play music enzo fadein 2.5
        $ dossier.add(dp_lorenzo)
        $ dossier.add(dp_medina)
        label lockers1_investigating:
            # Weighing Scale
            tt neutral "A weighing scale used by the jockeys. They have to meet a specific weight requirement before competing."

            # Recheck
            tt smile "Let me test it out... 168 lbs. Yup, it's working properly."


            # Lockers
            tt neutral "A row of lockers for the jockeys. Do they get assigned one, or can they just pick whichever one is available?"

            # Recheck
            tt det smile "We trainers have a separate locker room elsewhere. If it's empty, I might use it to transform into El Leopardo!"

            tt aw smile"…If the situation calls for it, anyway. But I doubt it."

            # Riding Equipment
            tt neutral right "Helmets, goggles, boots... Everything you'd need to stay safe on the track."

            # Recheck
            tt aha "Personally, I prefer going at it without a helmet. It's more stylish, and you can feel the wind... Such a rush."
        label lockers1_topic1:
            # The Razing Thunder Derby (Single Topic)

            t neutral "What can you tell me about the competition? What makes it so prestigious?"

            show en yell

            en "My boy! Are those eyes of yours just for decoration? Have you not taken a single look around you?"

            tt what drop "This coming from the guy wearing alien sunglasses indoors..."
            show en grin
            en "We have a staggering capacity of over 100,000 spectators! Gourmet meals to feast on before each race…"
            show en yell
            en "Top professional jockeys gathered in one place, carefully selected based on their records and achievements. State-of-the-art facilities! A jaw-dropping prize of SEVEN AND A HALF MILLION" 
            
            en "DOLLARS for the winner!"

            show en grin

            en "I tell you, name me one competition more glamorous than mine, and I'll eat my hat!"

            t aw smile "Uh… the Olympics?"
            show en yell
            en "Those are only held every four years, Mr. Ortiz. Razing Thunder is right at your fingertips every year! It's our very own carnival."

            t neutral drop "How are you able to afford all this?"
            show en smile
            en "Certainly not through my merit alone, I assure you. Though my sheer brilliance accounts for a good chunk of it."

            show en yell

            en "Sponsors, my boy! Everyone makes a generous contribution to get their name out at such a spectacular event as this."

            show en grin

            en "On that note, make sure you place your bets using BETFIGHTER! There's a handsome prize pool waiting to be won."

            t aw smile drop "I-I'm good, thanks. Since you brought up betting, do you know anything about people running clandestine gambling operations based on the race results?"

            show me smile3

            me "Yes, Villarreal. Know anything about that? You love keeping your customers hooked on betting."

            show en neutral

            en "Goodness, no! I assure you, we only work with official betting houses! Admittedly, hosting a private event gives me more freedom to choose which betting houses we affiliate with…"

            show en nervous

            en "…but I'd never stoop so low! What do you take me for?"

            show me angry

            me "A greedy bastard."

            show en grin

            en "Inspector, inspector… If I were as avaricious as you make me out to be, you and that young man would have been charged for entry by now. And not at retail price, mind you!"

            show me yell

            me "Piss off. You know I'm investigating, and you've only allowed a handful of my subordinates into the Derby."

            show en neutral

            en "Those are merely precautions! Would you really have me let a plethora of officers swarm the place and scare away the public?"

            show me angry

            me "I don't give a rat's ass if they get scared. They can leave. They SHOULD leave, before something worse happens."

            show en grin
            en "Evacuate them, you mean? We complied with your demands the previous two times, and you came up empty-handed. I only wish for the event to run its course properly this time."

            show me sweat2

            me "Tch…"
            return
            jump lockers1_complete
        label lockers1_complete:
            show en smile with dissolve
            en "Well now, I'm afraid I have quite a few matters that require my personal attention."

            show en grin

            en "Enjoy your stay, and do look forward to the race!"

            t det yell "Wait! I wanted to ask you about—"

            # He leaves

            hide en with dissolve
            stop music fadeout 2.5
            t aw neutral drop"…The racehorses. *Sigh.*"
            
            show me neutral at center
            with dissolve
            me "Don't bother. You should know better than to expect anything from a guy like him."

            t det yell "But he's the host of this whole operation. He's bound to know something."

            me "Sure. Doesn't mean he'll share a word of it if there's a chance it'll hurt his profits."

            t aw neutral right "Ugh… What about you, inspector? Have the police made any progress?"

            show me frown

            me "…We've got a few leads, but we can't properly investigate them until this whole spectacle is over."

            t neutral "How come? I'd assume you have more than enough authority to get a search warrant."

            show me neutral

            me "Let's just say the orders from the higher-ups are pretty clear: 'Get the hell out of there.'"

            t det neutral "You've got to be kidding me."

            show me sweat2

            me "It's out of my hands. This is all private property, technically. There's only so much we can do without a new incident being reported."

            me "And even then, it'll take time. They've got security crawling all over this place. I swear, not even a mouse could slip past those guards."

            t neutral right "…Thankfully, I'm not nearly as restricted as you are."

            show me angry

            me "If you're thinking of doing something stupid, don't."

            t aha "Haha, I wouldn't dream of it…"

            me "…"
            show me neutral
            me "Here."

            # Receives Medical Report
            #$ renpy.notify("Medical Report obtained!")
            $ dossier.add(de_medicalreport)

            t neutral "Huh? What's this?"

            me "A copy of the examination results for Perla Negra and the other horses that collapsed."

            show me angry

            me "They were examined here after the incidents, but I don't trust a single veterinarian on this payroll."

            me "As far as I'm concerned, that slimeball Villarreal has them all in his pocket."

            t grin "I'll give it a thorough read, then. Thanks, inspector!"

            show me sweat

            me "Don't mention it. Seriously, don't. I don't even know why I'm handing this over to you."

            t det smile "We're on the same side here. We both want to get to the truth—"
            
            show me yell
            me "Pull any stupid crap, and the next place you'll be investigating is a jail cell."

            t neutral drop "G-Got it…!"

            show me neutral

            me "I'm out."

            hide me with dissolve
            t what drop "There she goes…"

            tt neutral closed "I should give this a proper read when I get the chance. For now, I'll add it to my Dossier."
label act2_inves_complete:
        with fade
        # Phone Call / Ringtone / something
        play sound "new_fashion_tone.ogg" fadein 0.5
        show layer master at earthquake(dt=1.0, dist=2)
        n "{i}*RING!*{/i}"
        n "*Bleep!*"
        
        show tony neutral with dissolve

        tt "Huh? I'm getting a phone call. Unknown number… I don't like this. Is it a spam call?"

        n "*Beep.*"

        t "Hello?"

        x "Mr. Ortiz. Ms. Moreno is expecting you in the parking lot. A package of hers is being delivered there."

        show tony det neutral right
        t "A package? Who is this?"

        n "*Beep.*"
        show tony what drop
        t "They hung up…"

        show tony neutral
        tt "I don't like this one bit. Why would she be expecting a package at a time like this?"

        show tony neutral closed
        tt "And why have me pick it up? Strange. I'll try texting her."

        tt "..."
        
        show tony what aw drop
        tt "…And she's ignoring me. Oh well, there's still some time before the race begins. I might as well go see what this is about…"

        show tony neutral at right
        with move
       
        jump parking
label parking:
        scene placeholder_parkinglot
        with fade
        stop music

        tt neutral right "Alright, I'm here now… I guess it makes sense that it's mostly empty, since the race is about to start."

        x "Thank you for making it here so quickly, pal."

        t "It's no—"

        # 3 NPC Thug Sprites go here.
        
        show tthug at center
        show tthug_copy at left
        show tthug_copy2 at right
        with dissolve
        
        t neutral "…problem?"

        tt det neutral "Three men in expensive-looking suits surround me. One holds a baton, another an iron wrench, and the last is sporting a pair of heavy brass knuckles."

        tga "Yeah, the boys and I didn't want to risk you ignoring our call."

        tgb "The boss would've been pretty pissed if you hadn't shown up."

        tgc "He sends his regards, by the way! Real noble of you, helping out that little jockey girl."

        tga "But she's got a new trainer now, so you can hit the road."

        t neutral closed "Is that so? I think I'd like to confirm that with my employer directly, then."

        tgb "Huh? Why? You don't believe us?"

        tgc "You're breaking our hearts here, man."

        t det right "I'm sure you'll survive. If that's all, I'll be leaving—"

        tt det neutral "Just as I turned around, one of them stepped in to block my path."

        tga "Leaving so soon? But we haven't even given you the package."

        t neutral "…And what package would that be?"

        tt "I watch one of them toss an envelope near my feet. I glance back at them, then carefully open it to check the contents."

        t neutral closed "…Money."

        tgb "Consider it compensation for the sudden job termination."

        tgc "You got paid for your time, and then some! Consider yourself lucky."

        t det neutral "Yeah. Really lucky."

        tga "So, move along now. The exit is that way."

        tt neutral right "He gestures with his head toward the parking lot exit. They aren't even gonna let me go get La Chispa?"

        tt det neutral "They really don't want me anywhere near her. In that case, I—"

        menu:
                "Refuse to leave":
                    jump p_refuse
                "Take the money and leave":
                    jump p_givein               

        label p_givein:
                tt aw neutral drop "It's a lot of money, but if I walk away now, not only am I leaving La Chispa behind, I'm losing what might be my only chance to figure out what's actually happening in this derby…!"
                menu:
                    "On second thought...":
                        jump p_refuse
                    "Leave anyway":
                        jump p_badend
                label p_badend:
                    t "Alright. This looks like more than I was going to make from this gig anyway."

                    tga "Take it and go, then. Come on."

                    tt "I begrudgingly take the bribe and leave the derby."
                    
                    scene black
                    with dissolve

                    "Bad ending. The truth was lost. But you can pay rent at least."
                    return        
        label p_refuse:
            play music intense fadein 2.5
            t det yell "Sorry, I won't be accepting this money. You can hand it back to your boss. Or keep it for yourselves."

            tgb "Wow, really? We can keep it—"

            tga "Idiot! Of course we can't take it! Listen here, you little shit. You can leave here walking with the money, or you can leave in an ambulance. What's it gonna be?"

            tt grin "Oh. OH! Dude, this is a golden chance! Okay, don't mess it up, Tony. How did that line go again...?"

            t neutral closed "…Can't be helped, then."

            tt "I take out my phone and call the emergency line, never taking my eyes off the three stooges."
            
            #Bleach Ref
            t neutral right "Hello? Excuse me, I'd like to call an ambulance. Yes, I'm at the Razing Thunder Derby."

            tga "The hell?"

            tgc "We haven't done anything and he's scared shitless already."

            t neutral "The location is the parking lot area."
            t "Number of ambulances..."

            show layer master at cam_move(2.5, 0.2, 0.8,  2.5, 0.2, 0.3)
            t "One..."

            show layer master at cam_move(2.5, 0.8, 0.8,  2.5, 0.8, 0.3)
            t smile "Two..."

            show layer master at cam_move(2.5, 0.5, 0.8,  2.5, 0.5, 0.3)
            t det smile "Three..."

            show layer master at cam_move(2.5, 0.5,  0.3,  1.0, 0.5,  0.5)
            t det grin "Three ambulances!"

            tgabc "Damn you!"

            tt det smile "The three thugs charge at me. I—"

            menu timed_fight (screen="timed_choice", timeout=5.0, timeout_label="p_badend2"):
                "Disarm the man with the baton":
                    jump p_baton
                "Shoulder throw the man with the wrench":
                    jump p_wrench
                "Deflect the brass-knuckle punch":
                    jump p_brass

            label p_badend2:
                # Timeout / Bad Ending Choice (Hesitation)
                play music sad fadein 2.5

                tt neutral drop "I hesitate for a fraction of a second, overthinking my move as all three thugs close in at once. Their combined attack hits me before I can react."

                tga "Got you now, you arrogant punk!"

                tt "One of the thugs swings their baton, catching me across the side of my head."

                with vpunch
                play sound se_punch1

                t det yell "GAH—!"

                tt "My vision flashes white. Before I can regain my balance, a second person drives the heavy wrench into my ribs."

                with vpunch
                play sound se_punch2
                t aw neutral drop "Guh...!"

                tt "I double over, struggling to catch my breath. The one with brass knuckles grabs me by the collar and punches me in the stomach."

                tgc "That's for sticking your nose where it doesn't belong!"

               

                tt "Stumbling backward, I take another blow from the baton across my shoulder, sending me crashing onto the asphalt."

                with vpunch
                play sound se_punch1
                t det "Ngh...! Damn it...!"

                tt "I try to push myself up, only to fall back down after the guy with a wrench kicks me."

                tgb "Stay down!"

                with vpunch
                play sound se_punch2
                with vpunch
                play sound se_punch1
                with vpunch
                play sound se_punch2
                tt aw neutral drop "The three villains surround me, delivering a final series of kicks and blows while I struggle to protect myself."

                tga "What's wrong? Not so tough now, are you?!"

                tt "A sharp kick hits my side. I curl up, barely able to move."

                t "…Can't… get up…"

                tt "My attackers finally step away, leaving me sprawled on the ground."

                tgc "Heh. Should've stayed out of our business."

                hide tthug
                hide tthug_copy
                hide tthug_copy2
                with Dissolve(1.0)
                tt "Their footsteps gradually fade into the distance."

                tt "I try to reach for my phone, but my arm gives out."

                scene black
                with Dissolve(2.0)

                tt "My vision grows increasingly blurry. The sound of approaching sirens becomes distant and muffled."
                
                tt "…Damn it…"
                
                scene black
                with Dissolve(2.0)
                pause 0.5
                return
                
                # Darkness takes over. Bad END.
                # End.
            label p_baton:
                # Option 1 Choice: Deal with tthug A (Baton)

                tt "The one with a baton steps up first, bringing it down in a heavy vertical strike. Muscle memory kicks in..."

                tt det yell "...and I step inside his guard, catching his wrist!"
                
                with vpunch
                tt "I pivot hard, twisting his arm into a lock that forces him to drop the baton right into my hand."

                tt det neutral "Before he can recover, I throw a quick back elbow, knocking him off-balance and sending him crashing right into his buddy. Both of them hit the asphalt in a tangle of limbs."

                hide tthug
                hide tthug_copy
                with dissolve
                show tthug_copy2 at center
                with move

                tt "The one with brass knuckles is the last one standing. He looks at his groaning friends, then at me, and lets out a frustrated roar." 
                
                
                tt "He charges forward, swinging a wild right hook aimed at my jaw."

                with vpunch
                tt det yell "I duck under the swing, grab his wrist, and twist it sharply against his back, forcing him down onto the hood of the nearest car."
                
                play sound se_punch1
                tt det neutral "With his arm pinned and his balance completely broken, I deliver a sharp, controlled strike with the heel of my hand to the side of his neck. His eyes roll back, and he slumps forward onto the hood,"
                
                tt "completely out cold."

                hide tthug_copy2
                with dissolve

                jump parking_complete

                # Go to Fight Aftermath
            label p_wrench:
                # Option 2 Choice: Deal with tthug B (Wrench)

                tt det neutral "The guy with the wrench lunges with a wild, horizontal swing. It's a powerful hit, but way too slow."

                tt det yell "I duck under the blow, grab his extended arm, and use his own momentum to execute a clean shoulder throw."

                with vpunch
                tt det "He flies over my back and lands squarely on top of the man with brass knuckles, both out for the count now."

                hide tthug_copy
                hide tthug_copy2
                with dissolve

                tt "The baton guy is the last one left. He snaps the weapon open, face red with anger. He lunges at me with a quick, aggressive jab."
                play sound se_punch2
                tt det yell "I parry his arm outward, step inside his guard, and deliver a sharp elbow to his ribs."

                with vpunch
                tt "As he doubles over from the impact, I sweep his legs out from under him, sending him crashing onto the concrete."

                hide tthug
                with dissolve

                tt "The baton skitters away, out of reach."

                jump parking_complete
            label p_brass:
                # Option 3 Choice: Deal withtthug C (Brass Knuckles)

                tt det neutral "The man with brass knuckles charges forward with an aggressive right hook, the metal in his hand glinting in the light."

                tt det yell "I parry the strike outward with my forearm, lock his arm, and redirect his forceful punch straight into one of the other men's chest."

                with vpunch
                play sound se_punch2
                tga "Oof! Watch where you're punching, you idiot!"

                tt det neutral "While the two argue, I give the brass knuckle wearer a sharp shove, sending him stumbling backward into the baton holding one. Both lose their footing and crash onto the ground."

                hide tthug
                hide tthug_copy2
                with dissolve

                show tthug_copy at center
                with move

                tt det neutral right "That leaves the one with a wrench. He raises it and charges at me with a wild swing."

                tt det neutral "I sidestep the attack, letting him pass right by me."

                with vpunch
                play sound se_punch1
                tt det yell "Before he can turn around, I grab his shoulder and use his momentum to send him crashing face-first onto the hood of a nearby car."

                hide tthug_copy
                with dissolve

                tt "Lights out for him. I watch him drop the wrench onto the ground as the alarm of the car goes off."
                jump parking_complete
        label parking_complete:
            # Aftermath
            show tony det smile drop with dissolve
            stop music fadeout 2.5
            t "Whew… Their boss is gonna be furious when he sees the dry-cleaning bill for those fancy suits. And the hospital bills, too."

            tt "I kick the envelope containing the bribe money towards one of the groaning thugs."

            show tony det neutral
            t "Keep the change."

            show tony neutral
            tt "Straightening my collar, I turn back towards the stables, only to hear a series of shouts and screams in the distance."

            show tony det yell with dissolve
            t "What's going on now…!? I'd better hurry!"
            show tony det neutral at right
            with move
            # Act 2 End
            jump act3
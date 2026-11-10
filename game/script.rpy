# Ren'Py Built-in Configuration
define config.side_image_only_not_showing = True   # make side image not show when full body is shown.
define config.say_attribute_transition = Dissolve(0.2, alpha=True)   # Always add a dissolve when expression changes

# Default overrides probably shouldn't be here. Edit options.rpy and find the line that sets it to 0 and set it something else
default preferences.text_cps = 30   

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bb = Character(ctc="ctc_horse", ctc_pause="ctc_horse", ctc_position="fixed",
                      window_background="textbox5",
                      callback=blip, cb_blipfile="audio/tick.wav")


define x = Character("???", kind=bb)

define l = Character("El Leopardo", kind=bb, image="leo")
define lt = Character(kind=l, what_color="#4A86E8",  what_outlines=[(0,"#4A86E8", 0, 0)],
what_bold=False, window_background="textbox6")#, cb_blipfile=None)
define t = Character("Antonio Ortiz", kind=l, image="tony")
define tt = Character(kind=t, what_color="#4A86E8", what_outlines=[(1,"#ffd700")])#, cb_blipfile=None)


define c = Character("Catalina Moreno", kind=bb, image="cata")

define e = Character ("Esteban Rojas", kind=bb)
define tv = Character("TV Reporter", kind=bb)
define ch = Character("La Chispa", kind=bb)
define tg = Character("Thug", kind=bb)


# Change narrator to use the bb base
define narrator = Character(kind=bb, callback=blip, cb_blipfile="audio/type.wav", cb_bliploop=True)

# The time and location
define tl = Character(what_color="#38761D", what_bold=True, kind=narrator)



# The game starts here.

image deleteme_flicker_night:
    "neighborhood 2 night light"
    pause 0.1
    "neighborhood 2 night"
    pause 0.05
    "neighborhood 2 night light"
    pause 0.3
    "neighborhood 2 night"
    pause 0.08
    "neighborhood 2 night light"
    pause 0.15
    "neighborhood 2 night"
    pause 0.03
    "neighborhood 2 night light"
    pause 0.2
    repeat   

label deleteme:
    scene deleteme_flicker_night
    tl "9:30 PM\nSome average Argentinian street\nwith poor electrical supply."
    show leo neutral
    $ renpy.notify("Whatever!")
    l "This is me speaking."
    lt "This is me thinking."
    lt smile "...mmm..."
    tl "The time is now\nLocation is here."
    "{color=#38761D}{b}9:45 PM. \nAlleway.{/b}{/color}"
    tl "9:45 PM. \nAlleway."
    "Both location texts look the same! Nice, right?{w}\nOh, I am the narrator, hi!"
    l neutral "hey... maybe I..."
    l smile "Thinking makes me happy."
    hide leo
    l neutral "Time for me to go around."
    l smile "So I walk and walk around.{w} Talking to myself. {w}With no care in the world."
    lt neutral blush "It's late, everyone is at home..."
    lt neutral blush drop "Maybe, I could take this mask off."
    show leo with dissolve
    l "Prepare for my grand reveal!"
    hide leo
    show tony neutral blush
    x "It feels Awesome!"
    x "I am free and no body knows me!"
    show tony at left
    show cata neutral at right
    c "Ortiz! Antonio Ortiz! Come here!"
    t "No! Stay back! Stay away!"
    tt neutral drop "I must run away"
    hide cata
    show tony at center
    tt "And so I ran away from her."
    t "Phew, that was a close one."
    hide tony
    tt "I wonder if there is something here."
    t neutral "Let's explore this area"
    c "Ortiz! Come back here"
    t neutral drop "On no! I must Run!"
    show cata neutral with vpunch
    c "No, you won't. I heard you!"
    t "Yikes! H-Hello!"
    c "You must come with me and investigate the Derby"
    t what det neutral drop "Whaaaa"
    t det neutral right blush drop "You bet I would! Just let me put on my mask."
    lt eh neutral drop "I hate being rushed."
    show leo at left
    show cata at right
    l "I am ready, ma'am. Let's go!"
    c "This way!"

    scene sky night day
    return

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.    

    # These display lines of dialogue.
    call testCE
    call act2
    call deleteme


label act1:

  tl "9:45 PM. \nAlleway."

  lt "The grip on my phone tightens instinctively as I watch the violent fall, shocked."

  tv "—and those are the images moments before the end of the Razing Thunder race, three days ago. While the jockey Valentina Rios suffered only minor bruises from the fall, her horse, Perla Negra, is currently under intense care."

  tv "The race was halted following the incident, marking the third horse collapse at this year's Razing Thunder competition. Officials have once again postponed the event."

  l "What a nasty fall! And she was so close to claiming first place, too…"

  show thug:
    zoom 2

  tg "Bastard! When I get out of these, I'm going to smash that phone on your stupid face!"

  lt "I look at the man I captured, squirming against the ropes and grunting, cussing threats at me. The news reporter's voice fades into background noise as the lowlife distracts me."

  lt "Good luck with that, tough guy. The boys in blue will show up by then to take care of you."

  lt "Time to send them an anonymous tip to get them to come. And… sent."

  tg "Who the hell are you anyway, you mask freak!? When the boss catches wind of this—"

  l "I am glad you asked!"

  tg "Huh?"

  l "The one who strikes fear in the hearts of evildoers…"

  l "The defender of the innocent and eternal ally of justice...!"

  l "I am El Leopardo!"

  tg "…"

  show leo neutral at left

  lt "It seems my grand presentation rendered him speechless, heh."

  l "Now, about this boss of yours… he's connected to the Castillo family, isn't he? You lot have been busy. I can make an educated guess about what task he sent you for tonight."

  tg "Bah! I was just running errands, talking to some peeps. Is that a crime, El Tarado?"

  l "It's {b}EL LEOPARDO{/b}! And last I checked, yes, intimidating people to pay their debts is a form of harassment and a crime!"

  lt "I hold out a handgun in front of the man as I empty out the chambers of its bullets onto the cold ground. He scowls, clicking his tongue as he looks away."

  l "I doubt you need one of these for a normal chat. How much were you owed?"

  tg "More than that last customer could afford, that's for sure. Just 'cause your favorite pick got cold feet when it mattered doesn't mean you get to not pay up!"

  lt "Curious. So his customer bet on a certain horse, and lost so badly they went into debt."

  lt "I wonder if this has something to do with all the incidents at the Razing Thunder..."

  l "'Don't put all your eggs in one basket', huh?"

  lt "I show my phone screen to the criminal with the Razing Thunder coverage news. "
  l "Did your customer bet for this competitor, by any chance?."

  tg "Who knows? I ain't telling you nothing more."

  l "That's quite alright. I'll go ask your customer about it then."

  lt "I drop the gun near him and whistle, waiting for a few moments until my friend arrives."

  lt "The guy continues to squirm against his restraints as I hop on the back of the mare I just called."

  tg "The fuck- hey, you can't just leave me here!"

  l "Feeling lonely? Don't worry, I already gave someone a call to keep you company in my stead."

  tg "Huh?"

  lt "I grip the reins and ride away from the thug. Looking over my shoulder, I can discern the blue light of a patrol car shining on the walls of the alleyway on the other end. Officers begin to shout orders as they approach him."

  tg "Son of a- hey! {size=+6}COME BACK!!!{/size}"

  lt "No thanks. Like I wanna throw in the slammer with you. Once the cops go away, I'll see if I can get into contact with that customer of his."

  l "Let's hurry up, Chispa. With some luck, we'll be done before the clock hits midnight."

  ch "Neigh!"

  hide leo
  hide thug

  tl "{b}8:15 AM. \nName of Tony's Odd Jobs Agency.{/b}"

  

  lt leo neutral "Last night, we came across the person I was looking for shortly after. The guy hadn't run too far away, and it looked like the color drained from his face the moment I brought up the debt collector looking for him."

  lt "Getting him to spill the beans wasn't easy, but his reactions when Castillo's name was brought up said it all."

  lt "Of course, he didn't know who was behind the string of incidents, but he confirmed that debt collectors had been pressuring him ever since the day he bet on Perla Negra and lost."

  lt "There's been more and more victims like him going through the same situation ever since this turf race event started a while ago."

  lt "They'll bet a considerable amount of cash on a promising jockey, only for their pick to mysteriously lose at the last second."

  lt "Since the race itself is a private competition hosted by some bigshot businessman, it makes it difficult for the authorities to get involved."

  lt "On the surface, these are nothing more than a string of unfortunate accidents, after all. Ones that just happen to fill up the pockets of those handling the race bets. The clandestine type, that is."
  
  lt "Limited involvement from the cops gives them more leeway to get away with it. As if regular gambling wasn't enough of a problem, this crap happens…"

  lt "People bet on a horse that ends up losing, which in turn means they're neck deep into debt. And those that can't pay back are visited by guys like the one I came across."

  lt "A tale as old as time. Even so, I can't just stand by and watch it happen. Especially with the kind of foul play going on at the turf race."

  lt "The testimonies I have gathered and the aprietadoresI've fought off all point to the Castillo family being involved somehow."

  lt "They're putting up a front, operating as another sponsor for the Razing Thunder competitors."

  lt "Naturally, just losing a bet doesn't equate to being drowned in debt. I suspect these fiends knowingly allow people to gamble money they don't have, then send their underlings after them when they can't pay. What a wicked scheme."

  lt "I can't help but think that they'd make even bigger bucks if someone knew which horse would drop out next during the races..."

  lt "At any rate, while not unheard of, it's plain unnatural that it has happened three times in a row. Trainers and jockeys are not that neglectful with the horses' health."

  lt "...at least, I hope they aren't."

  lt "Either way, it's clear there is more than meets the eye! That's why today, I am going to talk to other victims of their ploys and gather clues to bring those fiends to justice—"
  show leo
  hide leo
  

# Make screen shake here because phone went off and maybe add photoshpped whatsapp conversation!!!1

  "{i}*RING!*{/i}" with vpunch

  show leo closed

  l "…? Oh, I got a message."

  lt "The notification at the top of the screen immediately lets me know who the sender is. The owner of this agency I work at- my boss, in other words."

  l "You gotta be kidding me… why now of all times? I already cleaned all the windows yesterday!"

  show leo yell

  l "I really don't want to open this, but I'll be in a world of pain later if I ignore it…"

  lt "*Shivers.*"

  lt "Tapping on the notification while letting out a deep sigh, I read what the boss sent me. "
  show leo neutral

  lt "Yup. She's got a new gig for me. A special one at that, considering it's last-minute and happening today."

  lt "I continue reading the job description, resigning myself to putting my plans on hold."

  lt "..."

  l "Wait, I have to do what!?"

  lt "I reread the contents of the message to make sure I am misunderstanding this request."

  lt "T-This… might be the breakthrough I was looking for! I have to hurry and get ready!"

  lt "Wasting no time, I enthusiastically put my phone away into my pocket and rushto get everything I need before heading to meet the person who made the request."

  scene test fence

  tl "{b}9:20 AM. \nPlaza.{/b}"

  lt "This should be the place… Chispa makes it a cinch to get around in no time."
  
  lt "I wait around by a fountain for the client to show up, pulling from the reins to stop Chispa whenever she tries to take a sip."
  
  l "C'mon, you don't know how dirty that water could be."

  ch "..."

  x "Is this your idea of making a good first impression? Frankly, you are overdoing it."

  lt "I turn over to the voice addressing me with disdain."

  show leo neutral at left
  show cata neutral at right

  x "It's useless to show off whatever caretaker abilities you have. You won't be using them."

  l "What? I am not showing off. I came here on horseback from my workplace."

  x "In this day and age? If you can't afford a car, taking the bus is always an option."

  lt "Ouch. Straight to assuming I'm too broke for a car? Not that I can deny it."
  l " I like riding with Chispa here more. Nothing beats the cozy feel of the breeze when this one starts galloping."

  x "It sounds to me like you are asking to get arrested for running into cars."

  l "Hey, the only illegal thing is moving through highways! More importantly, I got your request's details from my boss."

  l "Miss, you are \"{color=#FF9900}Catalina Moreno{/color}\", right? I am—"

  c "{color=#FF9900}Antonio Ortiz. {/color}I know."


  show tony neutral

  tt "…indeed. El Leopardo's secret identity- the man behind the mask is none other than Antonio Ortiz."

  tt "When I am not fighting crime at night, I work at an odd jobs agency, taking on all kinds of gigs that come my way. I'm a jack of all trades, you could say."

  tt "My specialty is offering my services as a private investigator. Sadly, business on that front hasn't picked up lately, so-"

  hide tony
  show cata neutral

  c "—hey. I'm talking to you. Are you even listening?"

  t "Wha- sorry! I zoned out there for a sec."

  hide cata
  show tony what det neutral drop at vpunch, center

  c "Good grief. As I was saying, who you are is inconsequential, and my reputation precedes me, so let's keep introductions short."

  show cata neutral at right
  show tony smile drop at left

  tt "Geez… you sure know how to pick 'em, boss. This is gonna be one hell of a day…"

  

  menu:

        t "Right. Your reputation. I…"

        "I know who you are":

            jump iknow

        "I have no idea who you are.":

            jump idk

label iknow:

    t "Catalina Moreno— you are one of the best professional jockeys hitting the turf races these days."

    t "I think you got second place during the last Razing Thunder race—"

    c "…Those results aren't final. The event was postponed after all, and will be resumed today."

    c "I will be making the most out of it and beat my competition."

    tt "Guh. She is glaring daggers at me now."

    jump act1continues
    
label idk:

    t "To be honest? I never heard of you until my boss reached out to me this morning."

    c "…I said your caretaker abilities didn't matter. But you should be aware of your employer's status, lest your ignorance makes you behave in a way that embarrasses me in public."

    c "For generations, my family has produced some of the finest jockeys in the country. Our name carries weight overseas, too."

    c "However, I have no intention of simply bragging about the achievements of my relatives."

    c "Today, I will show you and everyone what I can do. On the race."

    jump act1continues

label act1continues:
  t "Wait a moment… Did you say today? The event is resuming already? That's way too soon! What about the horse that collapsed a couple of days ago?"

  t "Have the organizers or the police at least figured out what happened?"

  c "No. And I doubt the organizers are interested in doing so. Their main concern is resuming the event."

  t "That's reckless! What if another horse collapses? They can't just—"

  c "If that happens, then the jockey has failed in their duty to protect their horse."

  t "What…? Aren't you afraid the same could happen to you and your horse?"

  c "That is why I hired you, is it not? To play the role of trainer for me."

  c "Don't be mistaken. I am fully capable of looking after Dama de Plata on my own."

  c "It's a requirement that every horse and jockey are accompanied by a trainer when signing up for the race."

  c "I don't need you to control my steed. I only need you because regulations demand it."

  t "So... I am just a legal requirement."

  c "Essentially."

  tt "This woman…! She really doesn't mince words, does she?"

  t "Great... then why hire me at all for this? I am sure someone of your status could get almost anyone to do it."

  c "Usually, yes. But it seems that is not the case this time around. No one would take the job."

  c "No one except for you, that is."

  c "...Let's go. We've wasted enough time."

  tt "With that, Catalina turned around and walked off, leaving me behind."

  tt "That wasn't ominous at all. And it's my boss who accepted this job without consulting me."

  tt "...I don't know whether to feel offended or happy. Sounds like I'll have little to no responsibilities keeping me busy. "

  tt "That gives me plenty of time to investigate. That's a good thing."

  t "It is, but...! It still hurts my pride, damn it! I would make a fine horse trainer! Right, Chispa?!"

  ch "Neigh!"

  t "Thanks, girl. I can always count on you."

  tt "Huffing, I hold onto the reins and hurry to go after my 'delightful' employer."

return

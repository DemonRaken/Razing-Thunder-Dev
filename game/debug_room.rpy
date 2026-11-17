init python:
    def _shake(trans, st, at, dt=3.0, dist=30):
        if st <= dt:
            decay = 1.0 - (st / dt)
            trans.xoffset = int(dist * decay * (renpy.random.random() * 2 - 1))
            trans.yoffset = int(dist * decay * (renpy.random.random() * 2 - 1))
            return 0.01
        return None

transform earthquake(dt=3.0, dist=30):
    function renpy.curry(_shake)(dt=dt, dist=dist)   

define flash = Fade(0.02, 0.0, 0.5, color="#fff")   


label debug_room:
    scene placeholder_breakroom
    show leo smile
    with fade
    l "This is the debug room!"
    show leo smile at left
    show cata smile at right
    c "You bet it is!"
    show layer master:
        linear 4.0 blur 250
        linear 4.0 zoom 2
    menu timed_menu (screen="timed_choice", timeout=4.0, timeout_label="testCataCE"):
        "jump to Debug CutIn Test":
            jump debug_cutins_test
        "Jump to Debug Ambulances":
            jump debug_ambulances
        "Jump to Debug Investigation":
            jump debug_investigation
        "Jump to DeleteMe":
            jump deleteme
    return


label cheat_get_all_evidence:
    $ dossier.add(de_mask)
    $ dossier.add(de_mate)
    $ dossier.add(dp_leo)
    $ dossier.add(de_screen)
    $ dossier.add(de_medicalreport)
    $ dossier.add(de_victimnotes)
    $ dossier.add(de_shovel)
    $ dossier.add(de_blooddrops)
    $ dossier.add(de_bodybag)
    $ dossier.add(de_callrecords)
    $ dossier.add(de_casualclothes)
    $ dossier.add(de_notebook)
    return

label debug_cutins_test:
    scene placeholder_office:
        blur 150
        linear 3.0 blur 0
    "Hello, I am the narration system."
    n "No, I am the real narrator"
    show leo neutral at slightleft
    show cata neutral at slightright
    show layer master at earthquake(dt=2.0, dist=150)
    c "Geez, that was scary."
    show leo grin shine with flash
    l "It's all daijoubuuu!"
    call cutin("objection")
    l "Objection! I am fine!"
    call cutin("holdit")
    c "Hold it! Why do you yell near me?!!"
    call cutin("takethat")
    l "Take That! You are doing it too!"
    call cutin("cross_examination")
    c "Just come and let's do my Cross-Examination and be done with it."



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
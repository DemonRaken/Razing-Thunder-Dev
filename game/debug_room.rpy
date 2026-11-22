init python:
    def _shake(trans, st, at, dt=3.0, dist=30):
        if st <= dt:
            decay = 1.0 - (st / dt)
            trans.xoffset = int(dist * decay * (renpy.random.random() * 2 - 1))
            trans.yoffset = int(dist * decay * (renpy.random.random() * 2 - 1))
            return 0.01
        return None

label fx_testimony:
    show screen status_indicator(_("Testimony"), "#385cff")
    play music ce fadein 2.5
    return
label fx_interrogation:
    show screen status_indicator(_("Interrogation"), "#FF0000")
    play music ce fadein 2.5
    return
transform earthquake(dt=3.0, dist=30):
    function renpy.curry(_shake)(dt=dt, dist=dist)   

define flash = Fade(0.02, 0.0, 0.5, color="#fff")   

transform status_indicator:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 2.0
    linear 1.0 alpha 0.0
    repeat

screen status_indicator(annoucement, colorize):
    text annoucement at status_indicator:
        color colorize
        bold True
        italic True
        size 70
        xpos 20
        ypos 20
        outlines [(2, "#FFFFFF", 0, 0)]

style chosen_style is default:
    color "#888888"
    hover_color "#aaaaaa"   

label debug_room:
    show screen status_indicator("Debug Room", "#FF0000")
    scene placeholder_breakroom
    show leo smile
    with fade
    l "This is the debug room!"
    show leo smile at left
    show cata smile at right
    c "You bet it is! Here, take your dossier!"
    $ dossier_enabled = True
    l "Thanks!"
    show layer master:
        linear 4.0 blur 250
        #linear 4.0 zoom 2
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
    $ dossier.add(de_autopsy)
    $ dossier.add(de_alibi)
    $ dossier.add(dp_tony)
    $ dossier.add(dp_chispa)
    $ dossier.add(dp_catalina)
    $ dossier.add(dp_renata)
    $ dossier.add(dp_lucas)
    $ dossier.add(dp_esteban)
    $ dossier.add(dp_vicente)
    $ dossier.add(dp_medina)
    $ dossier.add(dp_lorenzo)

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

    define audio.embrace = "audio/BGM/Peritune_Last_Embrace.ogg"
    define audio.embrace_offvo = "audio/BGM/Peritune_Last_Embrace_offvo.ogg"
    define audio.thought_route = "audio/BGM/Peritune_Cerebral_Maze.ogg"
    define audio.sad = "audio/BGM/Peritune_Echoed_Art.ogg"
    define audio.ending = "audio/BGM/Peritune_Last_Embrace.ogg"
    define audio.ending2 = "audio/BGM/Peritune_Tender_Gaze.ogg"
    define audio.ce = "audio/BGM/Peritune_Silent_Shadows_loop.ogg"
    define audio.ce2 = "audio/BGM/Peritune_Silent_Witness_loop.ogg"
    define audio.objection = "audio/BGM/PeriTune_Secret_Corridor_loop.ogg"
    define audio.happy = "audio/BGM/PeriTune_Oceanfront_loop.ogg"
    define audio.happy2 = "audio/BGM/Peritune_Sunlit_Cafe_loop.ogg"
    define audio.eccentric = "audio/BGM/PeriTune_Backstreet_Swing_loop.ogg"
    define audio.cata = "audio/BGM/Peritune_Black_Crystal_loop.ogg"
    define audio.enzo = "audio/BGM/PerituneMaterial_Creep_loop.ogg"
    define audio.intense = "audio/BGM/PeriTune_Rituale Machina_loop.ogg"
    define config.main_menu_music = "audio/BGM/Peritune_Tender_Gaze_inst.ogg"
    define audio.inves = "audio/BGM/Peritune_The_City_Breathes_Your_Name_loop.ogg"

style navigation_button:
    properties gui.button_properties("navigation_button")
    hover_sound "sfx/menu/coin2.ogg"
    activate_sound "sfx/menu/shell.ogg"   

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
# The debugging starts here.

# The game starts from label start.
label start:
    menu timed_menu (screen="timed_choice", timeout=4.0, timeout_label="testCataCE"):
      "Jump to Act I":
        jump act1
      "Jump to Act II":
        jump act2
      "Jump to Act III":
        jump act3
      "Jump to DeleteMe":
        jump deleteme

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
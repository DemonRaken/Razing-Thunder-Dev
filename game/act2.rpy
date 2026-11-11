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
    tl "9:40 AM.\nRazing Thunder Derby.\nStables."

    tt "Whew… we're finally done with all the paperwork. I'm Dama de Plata's trainer now, even if only in name."

    c "Several participants have withdrawn from the competition, so there are plenty of vacant stalls. You can keep Chispa in one of them."

    tt "What's this? A rare kind gesture from Miss Ice Queen?"

    t "Thanks. I'll do just that, then."

    tt "I lead La Chispa to one of the vacant stalls, preparing hay and water for her."

    c "Don't thank me. I'm just stating the obvious. The last thing I need is your horse running around wild and causing a mess."

    t "Hmph. Don't underestimate her, La Chispa. Offer her a sweet treat as a reward, and she'll become faster than a lightning bolt. Might even give your horse a run for her money."

    c "If that's supposed to be a joke, it isn't amusing. At all."

    c "If you're done here, I'd appreciate it if you took your leave. I have preparations to make before the race begins."

    t "Getting your head in the game? In that case, I could—"

    c "No."

    t "…Alright, alright, I'm leaving. Geez."

    tt "I turn towards La Chispa's stall and approach her."

    t "Keep an eye on 'em for me, will you?"

    ch "…"

    t "Too busy stuffing your mouth, eh…?"

    tt "It doesn't seem like Catalina is in a chatty mood. I should look around elsewhere and see what I can find."

    tt "With all these incidents, security is super tight. Not even an ant could sneak into the derby."

    tt "The clandestine gambling, the mystery behind the collapsing horses… There's bound to be a clue out there!"
    return
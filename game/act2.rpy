# The game starts here.
#    $ config.side_image_tag = "leo" # side is only Leo + sticky
#    $ config.side_image_tag = "tony" # side is only tony + sticky
#    $ config.side_image_tag = ""  # side is whoever is talking (default)
transform slight_jump:
    easein .15 yoffset -20
    easeout .15 yoffset 0
label act2:
    l neutral "I am here."
    show leo smile
    l "I forgot to show myself."
    l neutral "I forgot what other sprites I got..." with vpunch
    l smile "It's really dark in here. I need a flashlight."
    t what drop "something"
    # show leo neutral at left
    # show tony neutral at right
    pause 2
    # show side tony smile "Tonysception"
    show leo smile at slight_jump, left
    show cata neutral
    c "Can you change emotes while someone else talks?"
    t what drop ""
    c "That would be like live reaction to events."
    t neutral ""
    c "And a little neat detail too to react to what happens."
    c "I only mean Tony's sprites really, so we don't need others."
    return
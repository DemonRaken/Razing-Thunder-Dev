# The game starts from label start.
label start:
    call cheat_get_all_evidence
    scene placeholder_office:
        blur 150
        linear 3.0 blur 0
    menu:
        "Jump to Act I":
            jump act1
        "Jump to Act II":
            jump act2
        "Jump to Act III":
            jump act3
        "Jump to Debug":
            jump debug
        "Jump to Debug Room":
            jump debug_room
        "Jump to bigCE":
            jump bigCE
        "Jump to Ending":
            call ending_sequence
    return
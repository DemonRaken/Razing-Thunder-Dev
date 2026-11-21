# The game starts from label start.
# Define three copies of the same horse image (different tags so they can be on screen at once)

image horse1 = Transform(frame_anim("ctc", [0.03] * 32, prefix="ctc_horse"), zoom=2)
image horse2 = Transform(frame_anim("ctc", [0.03] * 32, prefix="ctc_horse"), zoom=2)
image horse3 = Transform(frame_anim("ctc", [0.03] * 32, prefix="ctc_horse"), zoom=2)
image horse4 = Transform(frame_anim("ctc", [0.03] * 32, prefix="ctc_horse"), zoom=2)
image horse5 = Transform(frame_anim("ctc", [0.03] * 32, prefix="ctc_horse"), zoom=2)

# Horse runs left → right along a gentle arc.
# Tune the ypos values to match the track curve in your photo.
transform horse_run:
    xpos -200 ypos 520-75
    linear 1.0 xpos 400  ypos 470+200-50
    linear 1.0 xpos 960  ypos 450+200
    linear 1.0 xpos 1520 ypos 470+200+50
    linear 1.0 xpos 2120 ypos 520+200+100

label intro_start:
    # Show your racetrack / menu background
    $ dossier_enabled = False
    scene main_menu

    # Stagger three horses, each starting 0.8 s after the last
    show horse1 at horse_run
    $ renpy.pause(0.8, hard=True)
    show horse2 at horse_run
    $ renpy.pause(0.8, hard=True)
    show horse3 at horse_run
    $ renpy.pause(0.8, hard=True)
    show horse4 at horse_run
    $ renpy.pause(0.8, hard=True)
    show horse5 at horse_run

    # Wait for the last horse to finish crossing (4 s total animation)
    $ renpy.pause(4.2, hard=True)

    # Continue into your actual game
    return   

label start:
    #jump start2
    call intro_start
    jump act1
    return

label start2:
    call cheat_get_all_evidence
    scene placeholder_office:
        blur 150
        linear 3.0 blur 0
    menu:
        "Jump to Portal":
            jump paddock_inves
        # "Jump to Act I":
        #     jump act1
        #  "Jump to Act II":
        #     jump act2
        # "Jump to Act III":
        #     jump act3
        "Jump to Debug":
            jump debug
        "Jump to Debug Room":
            jump debug_room
        "Jump to bigCE":
            jump bigCE
        "Jump to Ending":
            call ending_sequence
    return
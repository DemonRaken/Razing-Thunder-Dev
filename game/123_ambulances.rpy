image tthug:
    zoom 1.5
    "thug.png"

image tthug_copy:
    zoom 1.5
    "thug.png"

image tthug_copy2:
    zoom 1.5
    "thug.png"



# ---------------------------------------------------------------------------
# tthug positions in the wide shot.
# xanchor 0.5 puts the sprite's CENTER at px (0..1), which makes the camera
# focus points below predictable regardless of how wide the sprite is.
# ---------------------------------------------------------------------------
transform char_pos(px, py=1.0):
    xpos px xanchor 0.5
    ypos py yanchor 1.0


# ---------------------------------------------------------------------------
# Camera move: interpolate the whole master layer (background + all tthugs)
# from state (fz, fx, fy) to state (tz, tx, ty).
#
#   zoom    z    : 1.0 = wide shot, 2.5 = close-up
#   anchor (x,y) : which point of the SCENE sits at screen center
#
# xpos/ypos are pinned to 0.5 (screen center); the anchor is what selects
# *which* point of the scene we're centered on. So (0.15, 0.6) means "put
# the point 15% across / 60% down the scene at screen center."
#
# Each call MUST start where the previous one ended that's what keeps the
# camera continuous instead of snapping between moves.
# ---------------------------------------------------------------------------
transform cam_move(fz, fx, fy, tz, tx, ty, dur=1.5):
    zoom fz
    xpos 0.5
    ypos 0.5
    xanchor fx
    yanchor fy
    ease dur zoom tz xanchor tx yanchor ty




label debug_ambulances:
    scene placeholder_parkinglot
    show tthug       at char_pos(0.15)
    show tthug_copy  at char_pos(0.50)
    show tthug_copy2 at char_pos(0.85)

    t neutral "The location is the parking lot area."
    t "Number of ambulances&"

    show layer master at cam_move(2.5, 0.2, 0.8,  2.5, 0.2, 0.3)
    t "One..."


    show layer master at cam_move(2.5, 0.8, 0.8,  2.5, 0.8, 0.3)
    t smile "Two..."


    show layer master at cam_move(2.5, 0.5, 0.8,  2.5, 0.5, 0.3)
    t det smile "Three..."

    show layer master at cam_move(2.5, 0.5,  0.3,  1.0, 0.5,  0.5)
    t det grin "Three ambulances!"
    jump start
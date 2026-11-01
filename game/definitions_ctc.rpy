# ============================================================
#  ANIMATED CTC (HORSE) — SIMPLE VERSION
# ============================================================

init python:
    # --- Step 1: Build the animation argument list ---
    # Animation() expects pairs of (image, seconds), so we build a
    # plain list:  [image1, time1, image2, time2, ...]
    anim_parts = []

    for i in range(32):
        filename = "ctc/ctc_horse_%03d.png" % i
        anim_parts.append(filename)   # the picture
        anim_parts.append(0.03)       # how long it shows (seconds)

    # --- Step 2: Create the looping animation ---
    # The * in front of anim_parts "unpacks" the list.
    # Animation(*anim_parts) is the same as writing
    # Animation("frame0.png", 0.03, "frame1.png", 0.03, ...)
    ctc_horse_anim = Animation(*anim_parts)

    # --- Step 3: Put it in the bottom-right corner ---
    ctc_horse_final = Transform(
        ctc_horse_anim,
        xpos=0.83,     # 0.0 = left edge, 1.0 = right edge
        ypos=0.99,     # 0.0 = top edge,  1.0 = bottom edge
        xanchor=1.0,   # anchor the right side of the image
        yanchor=1.0,   # anchor the bottom of the image
    )


# --- Step 4: Give it a name so characters can use it ---
image ctc_horse = ctc_horse_final

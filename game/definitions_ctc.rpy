
init python:
    def frame_anim(folder, timings, prefix="frame"):
        """Build a looping Animation from numbered PNG frames.

        folder  : directory containing the frames (relative to game/)
        timings : list of delays in seconds (len must equal count)
        prefix  : filename prefix -> {prefix}_000.png, {prefix}_001.png, ...
        """
        parts = []
        for i in range(len(timings)):
            parts.append("%s/%s_%03d.png" % (folder, prefix, i))
            parts.append(timings[i])
        return Animation(*parts)

# PNG animations

# Click To Continue Horse
image ctc_horse = Transform(
        frame_anim("ctc", [0.03] * 32, prefix="ctc_horse"),
        xpos=0.82,     # 0.0 = left edge, 1.0 = right edge
        ypos=0.965,     # 0.0 = top edge,  1.0 = bottom edge
        xanchor=1.0,   # anchor the right side of the image
        yanchor=1.0,   # anchor the bottom of the image
    )

# cross-examination
define cross_examination_duration = [0.05, 0.05, 0.05, 0.05, 0.75, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.75, 0.05, 0.05, 0.05, 0.05]
define cross_examination_duration_sum = sum(cross_examination_duration)
image cross_examination:
    Transform(
        frame_anim("cutins/gifs/crossexamination", cross_examination_duration),
        xysize=(config.screen_width, config.screen_height)
        )
    pause cross_examination_duration_sum
    Null()

# holdit
define holdit_duration = [0.04, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.50, 0.02]
define holdit_duration_sum = sum(holdit_duration)
image holdit:
    Transform(
        frame_anim("cutins/gifs/holdit", holdit_duration),
        zoom= 2.0,
        xalign=0.5,
        yalign=0.5
        )
    pause holdit_duration_sum
    Null()


# objection
define objection_duration = [0.04, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.50]
define objection_duration_sum = sum(objection_duration)
image objection:
    Transform(
        frame_anim("cutins/gifs/objection", objection_duration),
        zoom= 2.0,
        xalign=0.5,
        yalign=0.5
        )
    pause objection_duration_sum
    Null()


# takethat
define takethat_duration = [0.04, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.60, 0.04]
define takethat_duration_sum = sum(takethat_duration)
image takethat:
    Transform(
        frame_anim("cutins/gifs/takethat", takethat_duration),
        zoom= 2.0,
        xalign=0.5,
        yalign=0.5
        )
    pause takethat_duration_sum
    Null()

label cutin(name):
    $ dur = getattr(renpy.store, f"{name}_duration_sum")
    $ renpy.show(name)
    pause dur
    $ renpy.hide(name)
    return   

#xysize=(config.screen_width, config.screen_height)
# ============================================================
#  ANIMATED CTC (HORSE) — First VERSION
# ============================================================

# init python:
#     # --- Step 1: Build the animation argument list ---
#     # Animation() expects pairs of (image, seconds), so we build a
#     # plain list:  [image1, time1, image2, time2, ...]
#     anim_parts = []

#     for i in range(32):
#         filename = "ctc/ctc_horse_%03d.png" % i
#         anim_parts.append(filename)   # the picture
#         anim_parts.append(0.03)       # how long it shows (seconds)

#     # --- Step 2: Create the looping animation ---
#     # The * in front of anim_parts "unpacks" the list.
#     # Animation(*anim_parts) is the same as writing
#     # Animation("frame0.png", 0.03, "frame1.png", 0.03, ...)
#     ctc_horse_anim = Animation(*anim_parts)

#     # --- Step 3: Put it in the bottom-right corner ---
#     ctc_horse_final = Transform(
#         ctc_horse_anim,
#         xpos=0.82,     # 0.0 = left edge, 1.0 = right edge
#         ypos=0.965,     # 0.0 = top edge,  1.0 = bottom edge
#         xanchor=1.0,   # anchor the right side of the image
#         yanchor=1.0,   # anchor the bottom of the image
#     )

# --- Step 4: Give it a name so characters can use it ---
# image ctc_horse = ctc_horse_final

define config.overlay_screens += ["dossier_icon"]

screen dossier_ui():
    modal True
    zorder 10
    fixed:
        xalign 0.5
        yalign 0.5
        add "dossier/dossier.png":
            xalign 0.5
            yalign 0.5
        #xpadding 20
        #ypadding 10
        #xsize 880
        #ysize 400
        #modal True

        vpgrid:

            cols 4
            draggable True
            mousewheel True

            text "Top-Left"
            text "Top-Right"
        
            text "Center-Left"
            text "Center-Right"

            text "Bottom-Left"
            text "Bottom-Right"


            xalign 0.25
            yalign 0.3
    
            for i in range(1, 11):

                textbutton "Button [i]":
                    xysize (200, 50)
                    action Return(i)

        vbox:
            xalign 0.94
            yalign 0.4
            text _("Dossier")
            null height 10
            textbutton "Close" action Hide("dossier_ui")   


screen dossier_icon:
    zorder 100
    draggroup:
        drag:
            drag_name "dossier_icon"
            draggable True
            drag_raise True
            xpos 0.9
            ypos 0.65
            clicked ToggleScreen("dossier_ui")
            imagebutton:
                idle "dossier/dossier_icon.png"
                #hover "dossier/dossier_icon_hover.png"
                #focus_mask True



screen timed_choice(items, timeout=5.0, timeout_label=None):
    # Reuse the ren'py normal choice layout
    use choice(items)

    if timeout_label:
        bar:
            value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
            xalign 0.5
            yalign 0.25
            xsize 400
            ysize 10

        timer timeout action Jump(timeout_label)
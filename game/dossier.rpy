define config.overlay_screens += ["dossier_icon"]

#style dossier:

style dossier_text:
    color "#000000"

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

        vbox:
            xalign 0.25
            yalign 0.55
            label "Items":
                xalign 0.5
                yalign 0.5
            vpgrid:

                cols 3
                spacing 5
                draggable True
                mousewheel True
                ysize 650
                xsize 560
                scrollbars "vertical"

                text "Top-Left"
                text "Top-Right"
            
                text "Center-Left"
                text "Center-Right"

                text "Bottom-Left"
                text "Bottom-Right"


        
                for i in range(1, 61):

                    textbutton "Button [i]":
                        xysize (200, 50)
                        action Return(i)
        hbox:
            yalign 0.125
            xalign 0.4
            spacing 30
            imagebutton:
                idle "button-sel"
                idle_foreground Text(_("Evidence"), xalign=0.5, yalign=0.5)
                #hover "button-sel-hover"
                hover_foreground Text(_("Evidence"), xalign=0.5, yalign=0.5)
                action Return()   
            imagebutton:
                idle "button-empty"
                idle_foreground Text(_("Profiles"), xalign=0.5, yalign=0.5)
                #hover "button-empty-hover"
                hover_foreground Text(_("Profiles"), xalign=0.5, yalign=0.5)
                action Return()
            imagebutton:
                idle "button-empty"
                idle_foreground Text(_("Notes"), xalign=0.5, yalign=0.5)
                #hover "button-empty-hover"
                hover_foreground Text(_("Notes"), xalign=0.5, yalign=0.5)
                action Return()
            imagebutton:
                idle "button-empty"
                idle_foreground Text(_("Map"), xalign=0.5, yalign=0.5)
                #hover "button-empty-hover"
                hover_foreground Text(_("Map"), xalign=0.5, yalign=0.5)
                action Return()

        vbox:
            xalign 0.75
            yalign 0.60
            xsize 550
            label "Whatever item Name is maybe":
                xalign 0.5
            frame:
                xpadding 10
                ypadding 10
                xalign 0.5
                add "evidence-mate" xalign 0.5 ysize 200 xsize 200

            fixed:
                xfill True
                ysize 3
                add Solid("#ff0000") 
            text "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vel dolor nunc. Donec ac tempor augue, eget euismod diam. Sed cursus quam id felis blandit.":
                style "dossier_text"
            
            
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
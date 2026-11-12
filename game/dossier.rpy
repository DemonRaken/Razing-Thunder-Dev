define config.overlay_screens += ["dossier_icon"]
define config.keymap['input_next_line'] = ['K_RETURN', 'K_KP_ENTER']   

init python:
    if persistent.dossier_notes_page_left is None:
        persistent.dossier_notes_page_left = ""
    if persistent.dossier_notes_page_right is None:
        persistent.dossier_notes_page_right = ""

transform dossier_fade:
    on show:
        alpha 0
        linear 0.3 alpha 1.0
    on hide:
        linear 0.3 alpha 0.0


#style dossier:

style dossier_text:
    color "#fffb00"

screen dossier_ui():
    modal True
    zorder 10
    tag dossier
    default dossier_tab = "evidence"
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
            xalign 0.92
            yalign 0.58
            text _("Dossier")
            null height 10
            textbutton "Close" action Hide("dossier_ui")   
        imagebutton:
                idle "button-empty"
                idle_foreground Text("Objection!", xalign=0.5, yalign=0.5)
                hover_foreground Text("Objection!", xalign=0.5, yalign=0.5)
                action Return()
                xalign 0.010
                yalign 0.805
        
        imagebutton:
                idle "button-sel"
                idle_foreground Text("Travel!", xalign=0.5, yalign=0.5)
                hover_foreground Text("Travel!", xalign=0.5, yalign=0.5)
                action Return()
                xalign 1-0.01
                yalign 1-0.805+0.11
        
        hbox:
            yalign 0.125
            xalign 0.51
            spacing 30
            for i,j in zip(("evidence", "profiles", "notes", "map"),
                            (_("Evidence"),_("Profiles"),_("Notes"),_("Map"))):
                imagebutton:
                    idle ("button-sel" if dossier_tab == i else "button-empty")
                    idle_foreground Text(j, xalign=0.5, yalign=0.5)
                    #hover "button-sel-hover"
                    hover_foreground Text(j, xalign=0.5, yalign=0.5)
                    action SetScreenVariable("dossier_tab", i)
                

        vbox:
            xalign 0.25
            yalign 0.55
            showif dossier_tab == "profiles":
                label "[dossier_tab] 2":
                    xalign 0.5
                    yalign 0.5
                label "What"
            showif dossier_tab == "notes":
                viewport:
                    ysize 650
                    xsize 560
                    scrollbars "vertical"
                    mousewheel True
                    yinitial 0          # start scrolled to the top
                    input:
                        value VariableInputValue("persistent.dossier_notes_page_left")
                        default persistent.dossier_notes_page_left or ""
                        multiline True
                        xmaximum 400
                        ymaximum 300
                        length 5000
            else: 
                label "[dossier_tab]":
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
                            #action Return(i)

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

            null height 6
            fixed:
                xfill True
                ysize 3
                add Solid("#ff0000") 
            null height 6
            text "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vel dolor nunc. Donec ac tempor augue, eget euismod diam. Sed cursus quam id felis blandit.":
                style "dossier_text"
            
            


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
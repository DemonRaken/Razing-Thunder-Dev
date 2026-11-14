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

screen _dossier_items_chooser:
                label "[dossier_tab]":
                    xalign 0.9
                    yalign 0.5
                vpgrid:

                    cols 4
                    spacing 5
                    draggable True
                    mousewheel True
                    ysize 650
                    xsize 560
                    scrollbars "vertical"

                    default dbtnsize = 125

                    for i in dossier:
                        if not isinstance(i, Evidence if dossier_tab == "evidence" else CharacterProfile):
                            continue

                        imagebutton:
                            idle Transform(i.image, size=(dbtnsize, dbtnsize))
                            idle_background Transform("evidence-empty", size=(dbtnsize, dbtnsize))
                            hover_background Transform("evidence-empty", size=(dbtnsize, dbtnsize))
                            idle_foreground Text(i.name, xalign=0.5, yalign=0.9, size=18)
                            #hover "button-sel-hover"
                            selected dossier_select == i
                            selected_background Transform("evidence-sel", size=(dbtnsize, dbtnsize))
                            hover_foreground Text(i.name, xalign=0.5, yalign=0.9)
                            action SetScreenVariable("dossier_select", i)

screen dossier_ui():
    modal True
    zorder 10
    tag dossier
    default notes_left_value = VariableInputValue("persistent.dossier_notes_page_left", default=False)
    default notes_right_value = VariableInputValue("persistent.dossier_notes_page_right", default=False)
    default dossier_tab = "evidence"
    default dossier_select = None
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
            xalign 0.915
            yalign 0.59
            text _("Dossier")
            null height 5
            textbutton "Close" action Hide("dossier_ui")   

        showif renpy.get_screen("ce", tag_only=True):
            imagebutton:
                    idle "button-empty"
                    idle_foreground Text("Objection!", xalign=0.5, yalign=0.5)
                    hover_foreground Text("Objection!", xalign=0.5, yalign=0.5)
                    action [SetVariable("ce_mode", "object"), SetVariable("ce_object", dossier_select), Hide("dossier_ui"), Return()]
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
                use _dossier_items_chooser
            elif dossier_tab == "map":
                pass
            elif dossier_tab == "notes":

                button:
                    action [notes_left_value.Enable(), notes_right_value.Disable()]
                    viewport:
                        id "notes_page_left"
                        ysize 650
                        xsize 560
                        scrollbars "vertical"
                        mousewheel True
                        yinitial 0          # start scrolled to the top
                        input:
                            value notes_left_value
                            default persistent.dossier_notes_page_left or ""
                            multiline True
                            xmaximum 400
                            ymaximum 300
                            length 5000
            else:
                use _dossier_items_chooser

        vbox:
            xalign 0.75
            ypos 0.2
            xsize 550
            showif dossier_tab in ["evidence", "profiles", "map"]:
                label (dossier_select.name if dossier_select else _("No Item Selected")):
                    xalign 0.5
                fixed:
                    xfill True
                    ysize 3
                    add Solid("#ff0000") 
                null height 5
                frame:
                    xpadding 10
                    ypadding 10
                    xalign 0.5
                    $ page2iconsize = 200
                    frame:
                        xalign 0.5 ysize page2iconsize xsize page2iconsize
                        background Transform("evidence-empty", size=(page2iconsize,page2iconsize))

                        if dossier_select:
                            add Transform(dossier_select.image, size=(page2iconsize,page2iconsize))
                    #add Transform("evidence-empty", size=(50,50))
                    #add (dossier_select.image if dossier_select else "evidence-empty"):
                    #        xalign 0.5 ysize 200 xsize 200
                    

                null height 6
                fixed:
                    xfill True
                    ysize 3
                    add Solid("#ff0000") 
                null height 6

                label (dossier_select.desc_short if dossier_select else _("No Item Selected")):
                    text_size 18
                    xalign 0.5
                fixed:
                    xfill True
                    ysize 3
                    add Solid("#ff0000") 
                    null height 5
                viewport:
                    ysize 365
                    scrollbars "vertical"
                    mousewheel True
                    text (dossier_select.desc_long if dossier_select else _("No Item Selected")):
                        style "dossier_text"
            elif dossier_tab == "notes":
                button:
                    action [notes_left_value.Disable(), notes_right_value.Enable()]
                    viewport:
                        id "notes_page_right"
                        ysize 650
                        xsize 560
                        scrollbars "vertical"
                        mousewheel True
                        yinitial 0          # start scrolled to the top
                        input:
                            value notes_right_value
                            default persistent.dossier_notes_page_right or ""
                            multiline True
                            xmaximum 400
                            ymaximum 300
                            length 5000


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

# screen timed_choice(items, timeout=5.0, timeout_label=None):
#     # Reuse the ren'py normal choice layout
#     use choice(items)

#     if timeout_label:
#         bar:
#             value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
#             xalign 0.5
#             yalign 0.25
#             xsize 400
#             ysize 10

#         timer timeout action Jump(timeout_label)

style choice_bar is bar:
    xalign 0.5
    xsize 400
    ysize 10

screen timed_choice(items, timeout=5.0, timeout_label=None):
    style_prefix "choice"

    vbox:
        if timeout_label:
            bar:
                value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)

        for i in items:
            textbutton i.caption action i.action

    if timeout_label:
        timer timeout action Jump(timeout_label)
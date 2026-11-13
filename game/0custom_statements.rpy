python early:
# react statement
    def _react_execute(attrs):
        tag = _side_image_tag
        if tag:
            renpy.set_tag_attributes(tag + " " + attrs)
            renpy.restart_interaction()

    renpy.register_statement(
        name="react",
        parse=lambda l: l.rest().strip(),
        execute=_react_execute,
    )

# setside statement

    def _setside_execute(tag):
        config.side_image_tag = tag
        _side_image_tag = tag

    renpy.register_statement(
        name="setside",
        parse=lambda l: l.rest().strip(),
        execute=_setside_execute,
    )

transform slightright:
    xalign 0.75
    yalign 1.0
transform slightleft:
    xalign 0.25
    yalign 1.0
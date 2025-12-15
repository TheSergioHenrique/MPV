init offset = -1

################################################################################
## Main and Game Menu Screens
################################################################################

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "touch"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 13

            hbox:

                textbutton _("Controles Touch") action SetScreenVariable("device", "touch")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "touch":
                use touch_help
            elif device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen touch_help():

    hbox:
        label _("Toque simples")
        text _("Avança o diálogo e ativa a interface.")

    hbox:
        label _("Toque longo")
        text _("Abre o menu rápido.")

    hbox:
        label _("Deslizar para cima")
        text _("Acessa o histórico de diálogos.")

    hbox:
        label _("Deslizar para baixo")
        text _("Esconde/mostra a interface.")

    hbox:
        label _("Tocar nas escolhas")
        text _("Seleciona a opção de diálogo.")


screen keyboard_help():

    hbox:
        label _("Toque/Enter")
        text _("Avança o diálogo e ativa a interface.")

    hbox:
        label _("Toque/Space")
        text _("Avança o diálogo sem selecionar escolhas.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Toque/Clique esquerdo")
        text _("Avança o diálogo e ativa a interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 7

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 211
    right_padding 17

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

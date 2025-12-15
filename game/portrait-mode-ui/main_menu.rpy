init offset = -1

################################################################################
## Main Menu - Mobile Friendly (BR)
################################################################################

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    # Container principal centralizado
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 60
        background "#00000000"  # Transparente para focar na logo

        vbox:
            spacing 40
            xalign 0.5

            # LOGO PRINCIPAL - Elemento central do design
            add "backgrounds/MPV.png":
                xalign 0.5
                zoom 1.0

            null height 15

            # Subtítulo elegante abaixo da logo - Estilizado e legível
            text "Uma jornada de aprendizado!":
                size 22
                xalign 0.5
                color "#ffffff"
                bold True
                outlines [(3, "#000000", 0, 0)]

            null height 25

            # Botões principais - Centralizados
            vbox:
                spacing 15
                xalign 0.5

                textbutton "▶ NOVO JOGO" action Start("prologo"):
                    xsize 500
                    ysize 80
                    xalign 0.5
                    text_size 28
                    text_bold True
                    text_xalign 0.5
                    background "#FFD700"
                    hover_background "#FFA000"

                textbutton "💾 CARREGAR JOGO" action ShowMenu("load"):
                    xsize 500
                    ysize 80
                    xalign 0.5
                    text_size 26
                    text_xalign 0.5
                    background "#2ECC71"
                    hover_background "#27AE60"

                textbutton "⚙ CONFIGURAÇÕES" action ShowMenu("preferences"):
                    xsize 500
                    ysize 80
                    xalign 0.5
                    text_size 26
                    text_xalign 0.5
                    background "#3498DB"
                    hover_background "#2980B9"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 237
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -16
    xmaximum 675
    yalign 1.0
    yoffset -16

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

# ================================================
# MOMENTOS PARA VIDA - Game Screens and UI
# ================================================

# ==========================================
# RELATIONSHIP STATUS SCREEN
# ==========================================
screen status_screen():
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 700
        padding (30, 30)
        background "#000000CC"

        vbox:
            spacing 20

            # Title
            text "RELAÇÕES INTERPESSOAIS E SOFT SKILLS" size 28 bold True xalign 0.5

            null height 10

            # Relationships Section
            text "━━━ RELAÇÕES INTERPESSOAIS ━━━" size 24 color "#FFD700"

            null height 10

            # Isabela
            hbox:
                spacing 15
                text "Isabela:" size 20 min_width 150
                for i in range(5):
                    if i < isabela_rel:
                        text "❤️" size 24
                    else:
                        text "🤍" size 24
                text "[get_relation_level('isabela')]" size 18 color "#9B59B6"

            # Lucas
            hbox:
                spacing 15
                text "Lucas:" size 20 min_width 150
                for i in range(5):
                    if i < lucas_rel:
                        text "❤️" size 24
                    else:
                        text "🤍" size 24
                text "[get_relation_level('lucas')]" size 18 color "#3498DB"

            # Camila
            hbox:
                spacing 15
                text "Camila:" size 20 min_width 150
                for i in range(5):
                    if i < camila_rel:
                        text "❤️" size 24
                    else:
                        text "🤍" size 24
                text "[get_relation_level('camila')]" size 18 color "#E74C3C"

            # Paulo
            hbox:
                spacing 15
                text "Paulo:" size 20 min_width 150
                for i in range(5):
                    if i < paulo_rel:
                        text "❤️" size 24
                    else:
                        text "🤍" size 24
                text "[get_relation_level('paulo')]" size 18 color "#F39C12"

            # Rafaela
            hbox:
                spacing 15
                text "Rafaela:" size 20 min_width 150
                for i in range(5):
                    if i < rafaela_rel:
                        text "❤️" size 24
                    else:
                        text "🤍" size 24
                text "[get_relation_level('rafaela')]" size 18 color "#E91E63"

            null height 20

            # Soft Skills Section
            text "━━━ SOFT SKILLS DESENVOLVIDAS ━━━" size 24 color "#FFD700"

            null height 10

            # Skills with progress bars
            vbox:
                spacing 8

                hbox:
                    spacing 10
                    text "Comunicação:" size 18 min_width 200
                    bar value comunicacao range 5 xsize 400 ysize 25
                    text "[comunicacao]/5" size 16

                hbox:
                    spacing 10
                    text "Empatia:" size 18 min_width 200
                    bar value empatia range 5 xsize 400 ysize 25
                    text "[empatia]/5" size 16

                hbox:
                    spacing 10
                    text "Liderança:" size 18 min_width 200
                    bar value lideranca range 5 xsize 400 ysize 25
                    text "[lideranca]/5" size 16

                hbox:
                    spacing 10
                    text "Trabalho em Equipe:" size 18 min_width 200
                    bar value trabalho_equipe range 5 xsize 400 ysize 25
                    text "[trabalho_equipe]/5" size 16

                hbox:
                    spacing 10
                    text "Gestão de Conflitos:" size 18 min_width 200
                    bar value gestao_conflitos range 5 xsize 400 ysize 25
                    text "[gestao_conflitos]/5" size 16

                hbox:
                    spacing 10
                    text "Gestão de Tempo:" size 18 min_width 200
                    bar value gestao_tempo range 5 xsize 400 ysize 25
                    text "[gestao_tempo]/5" size 16

            null height 20

            # Close button
            textbutton "Fechar" action Hide("status_screen") xalign 0.5 xsize 200 ysize 50

# Hotkey to open status screen
init:
    $ config.keymap['status_screen'] = ['r', 'R']
    $ config.underlay.append(renpy.Keymap(status_screen=Show("status_screen")))

# ==========================================
# NOTIFICATION SCREENS
# ==========================================

screen notify_relation(personagem, valor):
    zorder 100

    frame:
        xalign 0.5
        yalign 0.1
        padding (25, 15)
        background "#000000DD"

        hbox:
            spacing 10
            text "✨" size 24
            text "[personagem!c] +[valor]" size 20 color "#00FF00" bold True

    timer 2.5 action Hide("notify_relation")

screen notify_skill(skill, valor):
    zorder 100

    frame:
        xalign 0.5
        yalign 0.15
        padding (25, 15)
        background "#000000DD"

        hbox:
            spacing 10
            text "📈" size 24
            text "[skill!c] +[valor]" size 20 color "#FFD700" bold True

    timer 2.5 action Hide("notify_skill")

screen achievement_popup(ach_name):
    zorder 200

    frame:
        xalign 0.5
        yalign 0.2
        padding (30, 25)
        background "#1A1A1AEE"

        vbox:
            spacing 10
            text "🏆 CONQUISTA DESBLOQUEADA!" size 24 color "#FFD700" bold True xalign 0.5
            text "[achievement_names[ach_name]]" size 20 color "#FFFFFF" xalign 0.5

    timer 4.0 action Hide("achievement_popup")

# ==========================================
# MAIN MENU (UPDATED)
# ==========================================

screen main_menu_custom():
    tag menu

    style_prefix "main_menu"

    add "gui/main_menu.png"

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 20

            text "MOMENTOS PARA VIDA" size 48 bold True xalign 0.5

            null height 30

            # Main Stories
            text "▶ HISTÓRIAS PRINCIPAIS" size 24 color "#FFD700"

            textbutton "Prólogo: Primeiro Dia de Aula" action Start("prologo")
            textbutton "Roteiro 1: O Trabalho em Grupo" action Start("roteiro1") sensitive False
            textbutton "Roteiro 2: A Longa Noite de Estudos" action Start("roteiro2") sensitive False
            textbutton "Roteiro 3: A Prova Surpresa" action Start("roteiro3")

            null height 20

            # Side Content
            text "★ CONHECER OS PERSONAGENS" size 24 color "#FFD700"

            textbutton "☕ Café com Lucas" action Start("side_lucas")
            textbutton "🎨 Arte com Camila" action Start("side_camila")
            textbutton "🎭 Teatro com Rafaela" action Start("side_rafaela")
            textbutton "⚽ Fut com Paulo" action Start("side_paulo")
            textbutton "📚 Biblioteca com Isabela" action Start("side_isabela")

            null height 20

            # System options
            textbutton "❤ Status de Relações" action Show("status_screen")
            textbutton "⚙ Configurações" action ShowMenu("preferences")
            textbutton "❌ Sair" action Quit(confirm=True)

# ==========================================
# EPILOGUE STATISTICS SCREEN
# ==========================================

screen epilogue_stats():
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 700
        padding (30, 30)
        background "#000000F0"

        vbox:
            spacing 15

            text "━━━ ESTATÍSTICAS FINAIS ━━━" size 32 bold True xalign 0.5 color "#FFD700"

            null height 20

            # Relationships
            text "RELAÇÕES FINAIS" size 24 color "#FFFFFF" xalign 0.5

            grid 2 3:
                spacing 20
                xalign 0.5

                # Isabela
                vbox:
                    text "Isabela" size 18 color "#9B59B6"
                    hbox:
                        for i in range(5):
                            if i < isabela_rel:
                                text "❤️" size 20
                            else:
                                text "🤍" size 20
                    text "[get_relation_level('isabela')]" size 14

                # Lucas
                vbox:
                    text "Lucas" size 18 color "#3498DB"
                    hbox:
                        for i in range(5):
                            if i < lucas_rel:
                                text "❤️" size 20
                            else:
                                text "🤍" size 20
                    text "[get_relation_level('lucas')]" size 14

                # Camila
                vbox:
                    text "Camila" size 18 color "#E74C3C"
                    hbox:
                        for i in range(5):
                            if i < camila_rel:
                                text "❤️" size 20
                            else:
                                text "🤍" size 20
                    text "[get_relation_level('camila')]" size 14

                # Paulo
                vbox:
                    text "Paulo" size 18 color "#F39C12"
                    hbox:
                        for i in range(5):
                            if i < paulo_rel:
                                text "❤️" size 20
                            else:
                                text "🤍" size 20
                    text "[get_relation_level('paulo')]" size 14

                # Rafaela
                vbox:
                    text "Rafaela" size 18 color "#E91E63"
                    hbox:
                        for i in range(5):
                            if i < rafaela_rel:
                                text "❤️" size 20
                            else:
                                text "🤍" size 20
                    text "[get_relation_level('rafaela')]" size 14

            null height 20

            # Soft Skills Summary
            text "SOFT SKILLS DESENVOLVIDAS" size 24 color "#FFFFFF" xalign 0.5

            grid 2 4:
                spacing 15
                xalign 0.5

                text "Comunicação: [comunicacao]/5" size 16
                text "Empatia: [empatia]/5" size 16
                text "Liderança: [lideranca]/5" size 16
                text "Trabalho em Equipe: [trabalho_equipe]/5" size 16
                text "Gestão de Conflitos: [gestao_conflitos]/5" size 16
                text "Gestão de Tempo: [gestao_tempo]/5" size 16
                text "Pensamento Crítico: [pensamento_critico]/5" size 16
                text "Resiliência: [resiliencia]/5" size 16

            null height 20

            textbutton "Continuar" action Return() xalign 0.5 xsize 250 ysize 50

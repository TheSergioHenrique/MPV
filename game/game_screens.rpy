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
# MAIN MENU - MOBILE FRIENDLY
# ==========================================

screen main_menu_custom():
    tag menu

    style_prefix "main_menu"

    add "gui/main_menu.png"

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 50
        background "#000000AA"

        vbox:
            spacing 35
            xalign 0.5

            # Logo/Título
            text "MOMENTOS PARA VIDA" size 52 bold True xalign 0.5 color "#FFD700"
            text "Uma jornada de amizades e aprendizado" size 22 xalign 0.5 color "#FFFFFF" italic True

            null height 30

            # Botões principais - Design moderno para mobile
            vbox:
                spacing 20
                xalign 0.5

                textbutton "▶ NOVO JOGO" action Start("prologo"):
                    xsize 600
                    ysize 80
                    text_size 32
                    text_bold True

                textbutton "💾 CARREGAR JOGO" action ShowMenu("load"):
                    xsize 600
                    ysize 80
                    text_size 32
                    text_bold True

                textbutton "🏆 CONQUISTAS" action Show("achievements_screen"):
                    xsize 600
                    ysize 80
                    text_size 32
                    text_bold True

                textbutton "⚙ CONFIGURAÇÕES" action ShowMenu("preferences"):
                    xsize 600
                    ysize 80
                    text_size 32
                    text_bold True

# ==========================================
# ACHIEVEMENTS SCREEN - Tela de Conquistas
# ==========================================

screen achievements_screen():
    modal True
    zorder 100

    # Background escurecido
    add "#000000CC"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 1800
        padding (40, 40)
        background "#1A1A1AEE"

        vbox:
            spacing 25

            # Cabeçalho
            hbox:
                spacing 20
                xalign 0.5

                text "🏆" size 48
                text "CONQUISTAS" size 42 bold True color "#FFD700"

            null height 10

            # Contador de conquistas
            python:
                total_achievements = len(achievements)
                unlocked_count = sum(1 for v in achievements.values() if v)

            text "Desbloqueadas: [unlocked_count]/[total_achievements]" size 28 xalign 0.5 color "#FFFFFF"

            null height 20

            # Lista de conquistas com scroll
            viewport:
                xsize 920
                ysize 1400
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                vbox:
                    spacing 15

                    # Conquistas de Amizade
                    text "━━━ AMIZADES ━━━" size 28 color "#FFD700" bold True

                    $ ach_friendships = [
                        ("primeira_amizade", "👥", "Alcançou nível 3 de amizade com alguém"),
                        ("coracao_grupo", "❤️", "Alcançou nível 4 de amizade com todos"),
                        ("amigo_verdadeiro", "💝", "Alcançou nível 5 de amizade com alguém"),
                    ]

                    for ach_id, icon, desc in ach_friendships:
                        $ is_unlocked = achievements.get(ach_id, False)
                        frame:
                            xsize 880
                            padding (20, 15)
                            background ("#2ECC7188" if is_unlocked else "#333333AA")

                            hbox:
                                spacing 15

                                text icon size 36
                                vbox:
                                    spacing 5
                                    if is_unlocked:
                                        text "[achievement_names[ach_id]]" size 24 bold True color "#FFFFFF"
                                        text desc size 18 color "#CCCCCC"
                                    else:
                                        text "???" size 24 bold True color "#666666"
                                        text "Conquista bloqueada" size 18 color "#666666"

                                if is_unlocked:
                                    text "✓" size 48 color "#2ECC71" xalign 1.0

                    null height 15

                    # Conquistas de Habilidades
                    text "━━━ HABILIDADES ━━━" size 28 color "#FFD700" bold True

                    $ ach_skills = [
                        ("mediador_natural", "🤝", "Resolveu primeiro conflito com diplomacia"),
                        ("mediador_nato", "🕊️", "Alcançou nível 5 em gestão de conflitos"),
                        ("lider_nato", "👑", "Alcançou nível 5 em liderança"),
                        ("estudante_dedicado", "📚", "Completou todos os estudos"),
                        ("mestre_tempo", "⏰", "Alcançou nível 5 em gestão de tempo"),
                    ]

                    for ach_id, icon, desc in ach_skills:
                        $ is_unlocked = achievements.get(ach_id, False)
                        frame:
                            xsize 880
                            padding (20, 15)
                            background ("#3498DB88" if is_unlocked else "#333333AA")

                            hbox:
                                spacing 15

                                text icon size 36
                                vbox:
                                    spacing 5
                                    if is_unlocked:
                                        text "[achievement_names[ach_id]]" size 24 bold True color "#FFFFFF"
                                        text desc size 18 color "#CCCCCC"
                                    else:
                                        text "???" size 24 bold True color "#666666"
                                        text "Conquista bloqueada" size 18 color "#666666"

                                if is_unlocked:
                                    text "✓" size 48 color "#3498DB" xalign 1.0

                    null height 15

                    # Conquistas de Personagens
                    text "━━━ CONHECENDO OS AMIGOS ━━━" size 28 color "#FFD700" bold True

                    $ ach_characters = [
                        ("compreensao_lucas", "☕", "Descobriu a história profunda do Lucas"),
                        ("artista_oculta", "🎨", "Descobriu o talento artístico da Camila"),
                        ("por_tras_mascara", "🎭", "Conheceu o lado vulnerável da Rafaela"),
                        ("pioneiro_familiar", "⚽", "Entendeu os desafios do Paulo"),
                        ("sonhos_maiores", "📚", "Conheceu as ambições da Isabela"),
                    ]

                    for ach_id, icon, desc in ach_characters:
                        $ is_unlocked = achievements.get(ach_id, False)
                        frame:
                            xsize 880
                            padding (20, 15)
                            background ("#9B59B688" if is_unlocked else "#333333AA")

                            hbox:
                                spacing 15

                                text icon size 36
                                vbox:
                                    spacing 5
                                    if is_unlocked:
                                        text "[achievement_names[ach_id]]" size 24 bold True color "#FFFFFF"
                                        text desc size 18 color "#CCCCCC"
                                    else:
                                        text "???" size 24 bold True color "#666666"
                                        text "Conquista bloqueada" size 18 color "#666666"

                                if is_unlocked:
                                    text "✓" size 48 color "#9B59B6" xalign 1.0

                    null height 15

                    # Conquistas de Trabalhos
                    text "━━━ TRABALHOS E PROVAS ━━━" size 28 color "#FFD700" bold True

                    $ ach_work = [
                        ("equipe_unida", "🤝", "Manteve o grupo unido durante o trabalho"),
                        ("trabalho_excelente", "📝", "Tirou nota 8+ no trabalho em grupo"),
                        ("trabalho_perfeito", "💯", "Tirou nota 10 no trabalho em grupo"),
                        ("nota_maxima", "⭐", "Tirou nota 10 em uma prova"),
                    ]

                    for ach_id, icon, desc in ach_work:
                        $ is_unlocked = achievements.get(ach_id, False)
                        frame:
                            xsize 880
                            padding (20, 15)
                            background ("#F39C1288" if is_unlocked else "#333333AA")

                            hbox:
                                spacing 15

                                text icon size 36
                                vbox:
                                    spacing 5
                                    if is_unlocked:
                                        text "[achievement_names[ach_id]]" size 24 bold True color "#FFFFFF"
                                        text desc size 18 color "#CCCCCC"
                                    else:
                                        text "???" size 24 bold True color "#666666"
                                        text "Conquista bloqueada" size 18 color "#666666"

                                if is_unlocked:
                                    text "✓" size 48 color "#F39C12" xalign 1.0

                    null height 15

                    # Conquistas Especiais
                    text "━━━ CONQUISTAS ESPECIAIS ━━━" size 28 color "#FFD700" bold True

                    $ ach_special = [
                        ("final_perfeito", "🌟", "Alcançou o final perfeito do jogo"),
                        ("equilibrio_perfeito", "⚖️", "Manteve equilíbrio entre estudos e vida social"),
                        ("resistencia_mental", "💪", "Superou desafios com resiliência"),
                        ("sabedoria", "🧠", "Desenvolveu todas as soft skills ao máximo"),
                    ]

                    for ach_id, icon, desc in ach_special:
                        $ is_unlocked = achievements.get(ach_id, False)
                        frame:
                            xsize 880
                            padding (20, 15)
                            background ("#E91E6388" if is_unlocked else "#333333AA")

                            hbox:
                                spacing 15

                                text icon size 36
                                vbox:
                                    spacing 5
                                    if is_unlocked:
                                        text "[achievement_names[ach_id]]" size 24 bold True color "#FFFFFF"
                                        text desc size 18 color "#CCCCCC"
                                    else:
                                        text "???" size 24 bold True color "#666666"
                                        text "Conquista bloqueada" size 18 color "#666666"

                                if is_unlocked:
                                    text "✓" size 48 color "#E91E63" xalign 1.0

            null height 20

            # Botão fechar
            textbutton "VOLTAR" action Hide("achievements_screen"):
                xalign 0.5
                xsize 400
                ysize 70
                text_size 28
                text_bold True

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

# ================================================
# MOMENTOS PARA VIDA - Main Script
# Visual Novel Educativa sobre Soft Skills
# ================================================

# ==========================================
# INÍCIO DO JOGO
# ==========================================

label start:

    # Welcome screen
    scene bg_start with fade

    # Show title screen
    show text "{size=40}MOMENTOS PARA VIDA{/size}\n\n{size=20}Uma jornada sobre soft skills e amizades universitárias{/size}\n\n{size=16}Pressione ESPAÇO para continuar{/size}" at truecenter

    pause

    hide text

    # Introduction
    scene black

    narrator "Bem-vinda à universidade."
    narrator "Aqui você não aprenderá apenas fórmulas e teorias."
    narrator "Você aprenderá sobre comunicação, empatia, liderança, trabalho em equipe..."
    narrator "As chamadas 'soft skills'."
    narrator "E mais importante: você fará amizades que durarão para sempre."

    # Player name input
    python:
        povname = renpy.input("Qual é o seu nome?", default="Maria")
        povname = povname.strip()
        if not povname:
            povname = "Maria"

    # Start with prologue
    jump prologo

# ==========================================
# MENU PRINCIPAL CUSTOMIZADO
# (Após completar o prólogo)
# ==========================================

label main_menu_start:

    scene black with fade

    menu:
        "MOMENTOS PARA VIDA\n\nEscolha uma história para jogar:\n"

        "▶ HISTÓRIAS PRINCIPAIS":
            pass

        "Prólogo: Primeiro Dia de Aula":
            jump prologo

        "Roteiro 1: O Trabalho em Grupo":
            jump roteiro1

        "Roteiro 2: A Longa Noite de Estudos":
            jump roteiro2

        "Roteiro 3: A Prova Surpresa":
            jump roteiro3

        "★ CONHECER OS PERSONAGENS":
            pass

        "☕ Café com Lucas":
            call side_lucas
            jump main_menu_start

        "🎨 Arte com Camila":
            call side_camila
            jump main_menu_start

        "🎭 Teatro com Rafaela":
            call side_rafaela
            jump main_menu_start

        "⚽ Fut com Paulo":
            call side_paulo
            jump main_menu_start

        "📚 Biblioteca com Isabela":
            call side_isabela
            jump main_menu_start

        "❤ Ver Status de Relações":
            call screen status_screen
            jump main_menu_start

        "❌ Sair":
            return

# ==========================================
# PLACEHOLDER LABELS FOR FUTURE CONTENT
# ==========================================
# Roteiros 1, 2, and 3 have been implemented in separate files

# ==========================================
# SOFT SKILLS REFERENCE SCREEN
# ==========================================

label soft_skills_info:

    scene black with fade

    narrator "{b}SOFT SKILLS - O QUE SÃO?{/b}"
    narrator ""
    narrator "Soft skills são competências comportamentais que determinam como uma pessoa se relaciona, se comunica e enfrenta desafios."
    narrator ""
    narrator "Neste jogo, você desenvolverá:"
    narrator "• Comunicação"
    narrator "• Empatia"
    narrator "• Liderança"
    narrator "• Trabalho em Equipe"
    narrator "• Gestão de Conflitos"
    narrator "• Gestão de Tempo"
    narrator "• Pensamento Crítico"
    narrator "• Resiliência"
    narrator "E muitas outras!"

    return

# ==========================================
# HELPER LABELS
# ==========================================

label show_relationship_status:
    call screen status_screen
    return

# ==========================================
# CREDITS
# ==========================================

label credits:

    scene black with fade

    show text "{size=32}CRÉDITOS{/size}\n\n{size=20}MOMENTOS PARA VIDA{/size}\n\nDesenvolvido por:\nMatheus Gonçalves\nNathália Bacalhau\nPaulo Massa\nSérgio Henrique\nSócrates F\n\nEscola Politécnica de Pernambuco\n\nEngine: Ren'Py\n\nObrigado por jogar!" at truecenter
    pause
    hide text

    return

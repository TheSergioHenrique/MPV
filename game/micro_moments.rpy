# ================================================
# MOMENTOS PARA VIDA - Micro-Momentos
# Pequenas cenas de transição entre histórias principais
# ================================================

# ==========================================
# MICRO-MOMENTO 1: "WhatsApp - Pós Reunião"
# ==========================================

label micro1:

    if micro1_seen:
        return

    scene black with fade

    show text "{size=24}22h47{/size}" at truecenter
    pause
    hide text

    # Simular tela de WhatsApp
    scene bg_whatsapp  # Placeholder for WhatsApp-style background

    "Grupo: 'Trabalho Cidades Sustentáveis'"

    camila "Gente, obrigada pela reunião de hoje 💙"

    paulo "Tmj! Amanhã eu termino minha parte"

    lucas "Eu já terminei a minha."

    rafaela "mostra-se Lucas 😂"

    isabela "Foco, gente! Mas realmente foi produtivo"

    "..."

    camila "Isabela... obrigada por ter me dado espaço pra falar"

    "O cursor pisca. É sua vez de responder."

    menu micro1_escolha:
        "O que você envia?"

        "Sempre, Camila! Sua opinião é importante 💚":
            $ aumentar_relacao("camila", 2)
            $ aumentar_skill("empatia", 1)

        "Isso aí! Amanhã a gente finaliza tudo":
            $ aumentar_relacao("isabela", 1)

        "😊":
            # Neutro
            pass

        "Não responder":
            $ aumentar_relacao("camila", -1)

    $ micro1_seen = True

    scene black with fade

    return

# ==========================================
# MICRO-MOMENTO 2: "Encontro no RU"
# ==========================================

label micro2:

    if micro2_seen:
        return

    scene bg ru with fade

    "Restaurante Universitário - 12h30"

    "Você está na fila do RU com sua bandeja."

    "O cheiro de comida caseira preenche o ar. Conversas e risadas ecoam pelas mesas lotadas."

    "Você pega seu prato (arroz, feijão, frango e salada) e vai procurar um lugar."

    "Olha para os lados:"

    menu micro2_escolha:
        "Onde você quer sentar?"

        "Com Isabela (ela está lendo sozinha)":
            $ aumentar_relacao("isabela", 2)
            jump micro2_isabela

        "Com Paulo e Rafaela (mesa animada)":
            $ aumentar_relacao("paulo", 1)
            $ aumentar_relacao("rafaela", 2)
            jump micro2_paulo_rafaela

        "Com Camila (ela está sozinha no canto)":
            $ aumentar_relacao("camila", 3)
            jump micro2_camila

        "Comer sozinha e ir estudar":
            # Sem mudança de relação
            pass

    $ micro2_seen = True
    return

label micro2_isabela:
    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela happy at center

    isabela "Oi! Senta aqui!"

    "Vocês conversam sobre ambições acadêmicas."

    isabela "Sabe, eu quero fazer mestrado depois. Talvez até doutorado."

    pov "Nossa, que legal!"

    isabela "E você? Já pensou no futuro?"

    # Brief conversation
    return

label micro2_paulo_rafaela:
    "A mesa explode em risadas."

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo happy at center

    paulo "E aí! Vem se juntar à bagunça!"

    hide paulo
    hide isabela
    hide lucas
    hide camila
    hide professor
    show rafaela happy at center

    rafaela "Paulo tava contando da vez que ele se perdeu no campus!"

    "Vocês riem e relaxam juntos."

    # Stress relief
    return

label micro2_camila:
    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila neutral at center

    camila "Oi! Quer sentar?"

    pov "Claro!"

    "Vocês conversam sobre família e inseguranças."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila sad

    camila "Às vezes eu sinto que não sou boa o suficiente pra estar aqui..."

    pov "Você é incrível, Camila. Não duvide disso."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila happy

    camila "Obrigada..."

    return

# ==========================================
# MICRO-MOMENTO 3: "Biblioteca Fechando"
# ==========================================

label micro3:

    if micro3_seen:
        return

    scene bg library with fade

    "Biblioteca - 21h50"

    "A bibliotecária anuncia: 'A biblioteca fecha em 10 minutos.'"

    "Você ainda tem muito a estudar."

    menu micro3_escolha:
        "O que você faz?"

        "Continuar estudando em casa":
            $ aumentar_skill("gestao_tempo", 1)
            pov "Vou continuar em casa."

        "Ir dormir e descansar":
            $ aumentar_skill("autocuidado", 1)
            pov "Preciso descansar. Amanhã rendo mais."

    $ micro3_seen = True
    return

# ==========================================
# MICRO-MOMENTO 4: "Mensagem de Madrugada"
# ==========================================

label micro4:

    if micro4_seen:
        return

    scene black

    show text "{size=20}02h37 da madrugada{/size}" at truecenter
    pause
    hide text

    "Seu celular vibra."

    "Mensagem de Paulo:"

    paulo "Oi... vc tá acordada? Tô com uma dúvida URGENTE de cálculo 😭"

    menu micro4_escolha:
        "O que você faz?"

        "Responder e ajudar (perde sono)":
            $ aumentar_relacao("paulo", 3)
            $ aumentar_skill("empatia", 1)
            "Você passa 40 minutos ajudando Paulo."

        "Responder: 'Vamos ver isso amanhã, preciso dormir'":
            $ aumentar_skill("limites_saudaveis", 1)
            "Paulo entende."

        "Deixar no visto":
            $ aumentar_relacao("paulo", -1)
            pass

    $ micro4_seen = True
    return

# ==========================================
# MICRO-MOMENTO 5: "Corredor Tenso"
# ==========================================

label micro5:

    if micro5_seen:
        return

    scene bg corridor with fade

    "Você vê Lucas e Camila discutindo no corredor."

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas worried at center

    lucas "Eu só disse que seu método não é eficiente!"

    hide lucas
    hide isabela
    hide paulo
    hide rafaela
    hide professor
    show camila sad at center

    camila "Você sempre faz isso! Invalida o que eu faço!"

    menu micro5_escolha:
        "O que você faz?"

        "Intervir e mediar":
            $ aumentar_skill("gestao_conflitos", 2)
            $ aumentar_skill("lideranca", 1)

            pov "Gente, vamos respirar e conversar com calma?"

            # Mediation scene

        "Apoiar Camila":
            $ aumentar_relacao("camila", 2)
            $ aumentar_relacao("lucas", -1)

            pov "Lucas, você está sendo muito duro."

        "Ficar neutro e não se envolver":
            # Sem mudança
            pass

    $ micro5_seen = True
    return

# ==========================================
# MICRO-MOMENTO 6: "Final de Semana Livre"
# ==========================================

label micro6:

    if micro6_seen:
        return

    scene bg courtyard with fade

    "Sexta-feira - 18h"

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela happy at center

    rafaela "Galera! Vamos pro cinema hoje? Preciso desestressar!"

    "Você tem uma prova segunda-feira e planejava estudar o fim de semana todo."

    menu micro6_escolha:
        "O que você faz?"

        "Ir ao cinema (equilibra vida/estudo)":
            $ aumentar_relacao("rafaela", 2)
            $ aumentar_skill("equilibrio_vida", 1)
            "Você vai e se diverte. Volta renovada."

        "Recusar e estudar":
            $ aumentar_skill("dedicacao", 1)
            "Você estuda. Rende bem."

        "Ir mas sair cedo":
            $ aumentar_relacao("rafaela", 1)
            $ aumentar_skill("gestao_tempo", 1)
            "Equilíbrio perfeito."

    $ micro6_seen = True
    return

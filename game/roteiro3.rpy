# ================================================
# MOMENTOS PARA VIDA - Roteiro 3
# "A Prova Surpresa"
# Soft Skills: Gestão do Tempo, Pensamento Crítico,
#              Resiliência, Tomada de Decisão sob Pressão
# ================================================

label roteiro3:

    # Set character as Isabela for this route
    $ povname = "Isabela"

    # ===================
    # CENA A - "O ANÚNCIO"
    # ===================

    # Play classroom music
    play music classroom fadein 1.0

    scene bg classroom with fade

    "10h05 da manhã"

    "A aula de Termodinâmica acabou de começar."

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide rafaela
    show professor neutral at center

    professor "Bom dia. Antes de começar a matéria de hoje, tenho um aviso."

    "O clima da sala muda instantaneamente. Todos ficam atentos."

    professor "Vocês terão uma avaliação individual hoje às 14h. Quatro horas a partir de agora."

    "Silêncio absoluto."

    professor "A prova cobrirá os três primeiros capítulos que trabalhamos até aqui."

    "A sala explode em sussurros nervosos."

    professor "Isso vale 30%% da nota final. Não haverá reposição exceto com atestado médico. Perguntas?"

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo worried at left

    paulo "Professor... mas... hoje??"

    professor "Sim, hoje. Eu avisei na primeira aula que haveria avaliações surpresa."

    professor "Considerem isso um treino para o mercado de trabalho: nem sempre teremos aviso prévio."

    hide professor with dissolve

    "A aula continua, mas você não consegue prestar atenção."

    hide paulo

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila worried at left
    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas thinking at right
    with dissolve

    "Camila está pálida, as mãos tremendo."

    "Lucas está escrevendo algo furiosamente no caderno."

    hide camila
    hide lucas

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela sad at left
    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo worried at right
    with dissolve

    "Rafaela tem a cabeça abaixada nas mãos."

    "Paulo olha para você com olhos arregalados."

    hide rafaela
    hide paulo
    with dissolve

    pov "Quatro horas. Eu revisei alguma coisa ontem à noite, mas não tudo. O que eu faço?"

    menu roteiro3_cena_a:
        "Como você reage?"

        "Respirar fundo e fazer um plano mental de estudo para as próximas 4 horas":
            $ aumentar_skill("gestao_tempo", 1)
            jump roteiro3_b1

        "Sussurrar para Paulo: 'Calma, a gente estuda junto depois da aula'":
            $ aumentar_skill("empatia", 1)
            $ aumentar_relacao("paulo", 1)
            jump roteiro3_b2

        "Sentir pânico crescendo e pensar em faltar à prova":
            $ resiliencia -= 1
            jump roteiro3_b3

        "Decidir focar totalmente na aula atual para absorver o máximo possível":
            $ aumentar_skill("pensamento_critico", 1)
            jump roteiro3_b4

    # ===================
    # CENA B1 - "ESTRATÉGIA INDIVIDUAL"
    # ===================

label roteiro3_b1:

    scene bg courtyard with fade

    "Fim da aula - 10h50"

    "Você sai da sala e vai direto para um banco do lado de fora. Abre o caderno e começa a mapear o que precisa estudar."

    pov "Capítulo 1: Primeira Lei da Termodinâmica - eu lembro bem"
    pov "Capítulo 2: Entropia - preciso revisar"
    pov "Capítulo 3: Ciclos Termodinâmicos - não entendi direito"

    "Você olha o relógio: 10h52."

    "Você tem até 13h45 (praticamente 3 horas livres)."

    pov "1h para revisar Capítulo 2"
    pov "1h30 para estudar Capítulo 3 do zero"
    pov "30 min para fazer exercícios práticos"
    pov "NENHUM tempo para almoço"

    "Seu estômago ronca."

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo worried at center

    paulo "Isa! Vamos estudar junto? Eu tô pirando aqui."

    "Ao longe, você vê Camila sentada sozinha no degrau, olhando para o nada."

    "Lucas passa rápido em direção à biblioteca."

    "Rafaela está no celular, provavelmente tentando processar o choque."

    menu roteiro3_b1_escolha:
        "O que você faz?"

        "Aceitar estudar com Paulo (perde eficiência, mas ajuda um amigo)":
            $ aumentar_relacao("paulo", 2)
            $ aumentar_skill("trabalho_equipe", 1)
            jump roteiro3_c2

        "Recusar educadamente e seguir seu plano sozinha":
            $ aumentar_skill("gestao_tempo", 2)
            jump roteiro3_c1

        "Propor um estudo em grupo rápido com todos (caótico mas colaborativo)":
            $ aumentar_skill("lideranca", 1)
            $ aumentar_relacao("isabela", 1)
            $ aumentar_relacao("camila", 1)
            $ aumentar_relacao("paulo", 1)
            $ aumentar_relacao("rafaela", 1)
            jump roteiro3_c3

        "Ir até Camila primeiro, depois decidir":
            $ aumentar_skill("empatia", 2)
            $ aumentar_relacao("camila", 2)
            jump roteiro3_c4

    # ===================
    # CENA B2 - Estudo em Dupla
    # ===================

label roteiro3_b2:

    hide paulo
    hide camila
    hide lucas
    hide rafaela
    with dissolve

    show paulo happy at center

    paulo "Sério? Valeu! Eu tô perdidaço."

    pov "Vamos juntos, a gente se ajuda."

    $ aumentar_skill("empatia", 1)

    jump roteiro3_c2

    # ===================
    # CENA B3 - Pânico
    # ===================

label roteiro3_b3:

    scene bg corridor with fade

    "Você sente o pânico crescendo. Seu peito aperta."

    pov "Eu não vou conseguir. São três capítulos... em quatro horas..."

    "Você considera seriamente faltar à prova."

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela worried at center

    isabela "Ei, você está bem? Você está pálida."

    menu:
        "O que você faz?"

        "Desabafar com Isabela":
            $ aumentar_relacao("isabela", 2)

            pov "Eu... eu não sei se vou conseguir. Tá tudo muito rápido."

            isabela "Eu entendo. Mas você consegue. Vem, vamos estudar juntas. Eu te ajudo."

            hide lucas
            hide camila
            hide paulo
            hide rafaela
            hide professor
            show isabela happy

            $ aumentar_skill("resiliencia", 1)

            jump roteiro3_c2

        "Dizer que está tudo bem e se afastar":
            pov "Tá tudo bem, só preciso de um tempo sozinha."

            hide isabela

            jump roteiro3_c1

    # ===================
    # CENA B4 - Foco na Aula
    # ===================

label roteiro3_b4:

    scene bg classroom

    "Você decide focar totalmente na aula que ainda está acontecendo."

    "Cada palavra do professor pode ser crucial."

    "Você anota furiosamente tudo que ele diz."

    $ aumentar_skill("pensamento_critico", 1)

    "Fim da aula - 11h00"

    jump roteiro3_c1

    # ===================
    # CENA C1 - Estudo Solo na Biblioteca
    # ===================

label roteiro3_c1:

    # Play library music for focused study
    play music library fadein 1.5

    scene bg library with fade

    "11h05 - Biblioteca"

    "Você se instala em uma mesa individual, longe de distrações."

    "Abre os livros de Termodinâmica e começa a revisar sistematicamente."

    "Capítulo 1... Capítulo 2... Capítulo 3..."

    "O tempo passa rapidamente."

    "12h30 - Você já revisou tudo. Agora está fazendo exercícios."

    "13h15 - Seu estômago ronca alto, mas você ignora."

    "13h40 - 5 minutos para a prova. Você se sente... preparada. Cansada, com fome, mas preparada."

    $ aumentar_skill("gestao_tempo", 2)

    jump roteiro3_d

    # ===================
    # CENA C2 - Estudo em Dupla/Grupo Pequeno
    # ===================

label roteiro3_c2:

    # Play study music for group work
    play music noite_estudos fadein 1.5

    scene bg library with fade

    "11h10 - Biblioteca"

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo neutral at left
    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela neutral at right

    "Você, Paulo e Isabela encontram uma mesa grande."

    paulo "Ok, por onde a gente começa?"

    isabela "Vamos dividir. Cada um resume um capítulo e explica pros outros?"

    pov "Boa ideia."

    "Vocês trabalham juntos, trocando conhecimento."

    "Paulo entendeu bem o Capítulo 1. Isabela domina o 2. Você ajuda no 3."

    "12h45 - Vocês param para um lanche rápido."

    "13h30 - Retornam para últimas revisões."

    $ aumentar_skill("trabalho_equipe", 2)
    $ aumentar_relacao("paulo", 1)
    $ aumentar_relacao("isabela", 1)

    jump roteiro3_d

    # ===================
    # CENA C3 - Estudo em Grupo Grande
    # ===================

label roteiro3_c3:

    # Play teamwork music for group study
    play music trabalho_grupo fadein 1.5

    scene bg library with fade

    "11h15 - Biblioteca"

    "O grupo inteiro se reúne: você, Isabela, Lucas, Camila, Paulo e Rafaela."

    pov "Gente, vamos estudar juntos. Temos pouco tempo, mas juntos conseguimos."

    lucas "Boa iniciativa. Eu sugiro dividir os capítulos."

    camila "Eu... eu posso fazer um resumo do Capítulo 1?"

    rafaela "Eu ajudo! Vamos nessa!"

    "O grupo trabalha de forma surpreendentemente coordenada."

    "Lucas lidera a organização. Camila ganha confiança. Paulo traz leveza nos momentos tensos."

    "12h00 - Vocês param brevemente para comer alguma coisa."

    "13h35 - Última revisão em grupo."

    $ aumentar_skill("lideranca", 2)
    $ aumentar_skill("trabalho_equipe", 2)
    $ unlock_achievement("equipe_unida")

    jump roteiro3_d

    # ===================
    # CENA C4 - Foco em Camila Primeiro
    # ===================

label roteiro3_c4:

    scene bg courtyard

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila worried at center

    pov "Camila? Você está bem?"

    camila "Eu... eu não sei se vou conseguir. Eu sempre fico nervosa em provas."

    pov "Eu entendo. Mas você não está sozinha. Vem, vamos estudar juntas."

    camila "Você... você faria isso por mim?"

    pov "Claro. Vamos."

    $ aumentar_relacao("camila", 3)

    scene bg library with fade

    "Vocês passam as próximas horas estudando juntas."

    "Você ajuda Camila a se acalmar e focar."

    "Ela, por sua vez, tem anotações excelentes que ajudam você."

    $ aumentar_skill("empatia", 2)

    jump roteiro3_d

    # ===================
    # CENA D - A PROVA
    # ===================

label roteiro3_d:

    # Play decision/test music
    play music decisao fadein 2.0

    scene bg classroom with fade

    "14h00 - Sala de aula"

    "O professor distribui as provas."

    "Você olha as questões. Reconhece a maior parte delas."

    "Seus dedos seguram a caneta firmemente."

    "Você começa a responder."

    scene black with fade

    show text "{size=24}2 horas depois...{/size}" at truecenter
    pause 1.0
    hide text

    scene bg classroom with fade

    "16h00"

    "Você entrega a prova."

    "Não sabe se foi perfeito, mas sabe que deu seu melhor."

    # Calcular resultado baseado em escolhas
    $ prova_resultado = "bom"

    if gestao_tempo >= 3:
        $ prova_resultado = "excelente"
    elif trabalho_equipe >= 3:
        $ prova_resultado = "bom"
    elif empatia >= 3 and camila_rel >= 4:
        $ prova_resultado = "satisfatorio"

    if prova_resultado == "excelente":
        jump roteiro3_final_a
    elif prova_resultado == "bom":
        jump roteiro3_final_b
    else:
        jump roteiro3_final_c

    # ===================
    # FINAIS DO ROTEIRO 3
    # ===================

label roteiro3_final_a:
    # Final Excelente - Preparação Perfeita

    # Play victory/growth music
    play music crescimento fadein 1.5

    scene bg courtyard with fade

    "Uma semana depois..."

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide rafaela
    show professor neutral at center

    professor "Isabela, parabéns. Você tirou a maior nota da turma. 9,8."

    "Você sente uma onda de alívio e orgulho."

    hide professor

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela happy at center

    isabela "Obrigada! Você também foi bem?"

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas happy at center

    lucas "Parabéns, Isabela. Você merece."

    lucas "9,2. Nada mal."

    $ unlock_achievement("nota_maxima")
    $ unlock_achievement("estudante_dedicado")

    narrator "Você aprendeu que gestão de tempo não é sobre fazer tudo,"
    narrator "mas sobre priorizar o que realmente importa."

    jump roteiro3_epilogo

label roteiro3_final_b:
    # Final Bom - Equilíbrio

    # Play calm growth music
    play music crescimento fadein 1.5

    scene bg courtyard with fade

    "Uma semana depois..."

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela happy at center

    isabela "8,5! Não é a maior nota, mas tô feliz!"

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo happy at right

    paulo "Eu tirei 7,5! Passei! Valeu por ter estudado comigo, Isa!"

    pov "Sempre! A gente se ajuda."

    $ unlock_achievement("trabalho_excelente")

    narrator "Você aprendeu que sucesso não precisa vir à custa do isolamento."
    narrator "Ajudar os outros também te fortalece."

    jump roteiro3_epilogo

label roteiro3_final_c:
    # Final Satisfatório - Aprendizado

    scene bg classroom with fade

    "Uma semana depois..."

    "Nota: 7,0"

    pov "Passei... mas poderia ter ido melhor."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila happy at center

    camila "Mas você me ajudou tanto! Eu tirei 7,5 por sua causa!"

    camila "Às vezes, o que importa não é só a nota, sabe?"

    $ aumentar_skill("resiliencia", 2)

    narrator "Nem toda vitória é medida em números."
    narrator "Você aprendeu a importância da empatia e da resiliência."

    jump roteiro3_epilogo

    # ===================
    # EPÍLOGO DO ROTEIRO 3
    # ===================

label roteiro3_epilogo:

    scene black with fade

    show text "{size=32}ROTEIRO 3 COMPLETO{/size}\n\n{size=20}A Prova Surpresa{/size}" at truecenter
    pause
    hide text

    call screen epilogue_stats

    $ roteiro3_completo = True

    return

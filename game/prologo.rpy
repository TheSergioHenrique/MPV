# ================================================
# MOMENTOS PARA VIDA - Prólogo Compartilhado
# "Primeiro Dia de Aula"
# ================================================

label prologo:

    # ===================
    # CENA PRÓLOGO.1 - "A CHEGADA"
    # ===================

    scene bg campus with fade

    "O ônibus para na frente do portão principal. Você desce com a mochila pesada nos ombros, o coração acelerado."

    "O campus é imenso: prédios de concreto, árvores antigas, estudantes apressados caminhando em todas as direções."

    "Há um cheiro de café vindo da cantina próxima."

    pov "Então é aqui... meu primeiro dia como universitária. Engenharia Ambiental. Eu consegui."

    "Um misto de orgulho e medo aperta seu peito."

    "De repente, uma voz animada:"

    show rafaela happy at center

    rafaela "Oi! Oiii! Você é caloura também?"

    "Uma garota de cabelo cacheado e blusa colorida acena empolgada na sua direção."

    "Ela está com outros três estudantes perto da entrada."

    menu prologo_escolha1:
        "Como você reage?"

        "Ir até ela com empolgação e se apresentar":
            $ aumentar_relacao("rafaela", 2)
            $ aumentar_relacao("isabela", 1)
            $ aumentar_skill("comunicacao", 1)
            $ social_score += 1
            jump prologo_2a

        "Acenar timidamente e ir devagar":
            $ aumentar_relacao("camila", 2)
            $ aumentar_relacao("paulo", 1)
            $ cautelosa_score += 1
            jump prologo_2b

        "Apenas acenar e seguir seu caminho":
            $ aumentar_relacao("lucas", 1)
            $ independente_score += 1
            jump prologo_2c

        "Ignorar e procurar a sala sozinha":
            $ isolamento_score += 1
            jump prologo_2d

# ===================
# CENA PRÓLOGO.2A - "O CÍRCULO SE FORMA"
# (Vindo da escolha PRÓLOGO.1 - opção 1)
# ===================

label prologo_2a:

    hide rafaela

    "Você caminha até o grupo com um sorriso."

    show rafaela happy at center

    pov "Oi! Sim, sou caloura. Engenharia Ambiental."

    rafaela "Aaaah! Eu também! Somos da mesma turma! Gente, vem cá!"

    "Ela puxa você para perto dos outros três."

    hide rafaela
    show rafaela happy at pos_4_farleft
    show isabela neutral at pos_4_left
    show lucas thinking at pos_4_right
    with dissolve

    rafaela "Essa é Isabela, Lucas e Paulo. Todos de Ambiental!"

    show isabela happy

    isabela "Prazer! Você já sabe onde é a sala?"

    show lucas neutral

    lucas "A1-203. Cheguei cedo pra conferir."

    show paulo happy at pos_4_farright

    paulo "Esse cara já decorou o campus todo. Eu mal lembro onde desci do busão."

    rafaela "Paulo é da Mecânica, mas a primeira aula é junto."

    "O grupo começa a caminhar junto em direção ao prédio. Isabela caminha ao seu lado."

    hide lucas
    hide paulo
    hide rafaela
    with dissolve

    show isabela happy at pos_3_center

    isabela "Você tá animada? Eu mal dormi essa noite."

    show paulo happy at pos_3_right

    paulo "Eu tô mais é com fome. Alguém sabe se a cantina abre cedo?"

    show lucas thinking at pos_3_left

    lucas "Foco, gente. A primeira impressão conta."

    menu prologo_2a_escolha:
        "Como você responde?"

        "Responder Isabela: 'Sim! Tô nervosa mas animada!'":
            $ aumentar_relacao("isabela", 1)
            $ aumentar_skill("comunicacao", 1)

            pov "Sim! Tô nervosa mas animada!"

            isabela "Eu também! Vamos juntas nessa."

        "Brincar com Paulo: 'Eu também! Vamos na cantina antes?'":
            $ aumentar_relacao("paulo", 2)
            $ aumentar_relacao("rafaela", 1)
            $ descontracao_score += 1

            pov "Eu também! Vamos na cantina antes?"

            paulo "Agora sim! Alguém que me entende!"

            rafaela "Hahaha! Mas a aula começa em 5 minutos, gente!"

        "Concordar com Lucas: 'Ele tem razão, vamos focar'":
            $ aumentar_relacao("lucas", 2)
            $ profissionalismo_score += 1

            pov "Ele tem razão, vamos focar."

            lucas "Exatamente. Obrigado."

        "Apenas ouvir em silêncio, observando todos":
            $ observacao_score += 1

            "Você apenas sorri e observa a dinâmica do grupo."

    jump prologo_3

# ===================
# CENA PRÓLOGO.2B - Caminho Tímido
# ===================

label prologo_2b:

    hide rafaela

    "Você acena timidamente e caminha devagar até o grupo."

    show rafaela happy at center

    rafaela "Oi! Vem, vem! Não precisa ter vergonha!"

    "Ela te puxa gentilmente para perto dos outros."

    hide rafaela
    show rafaela happy at pos_4_farleft
    show isabela neutral at pos_4_left
    show lucas neutral at pos_4_right
    with dissolve

    rafaela "Pessoal, mais uma da nossa turma!"

    isabela "Oi! Seja bem-vinda. Eu sou Isabela."

    lucas "Lucas."

    show paulo happy at pos_4_farright

    paulo "E aí! Paulo aqui. Relaxa, a gente tá tudo perdido igual!"

    "O grupo sorri acolhedor."

    jump prologo_3

# ===================
# CENA PRÓLOGO.2C - Caminho Independente
# ===================

label prologo_2c:

    hide rafaela

    "Você acena brevemente e segue seu caminho sozinha."

    "Ao entrar no prédio, você encontra o mesmo grupo na frente da sala A1-203."

    show rafaela happy at pos_3_left
    show isabela neutral at pos_3_center
    show lucas neutral at pos_3_right

    rafaela "Opa! Você é da nossa sala!"

    "Você acaba entrando junto com eles de qualquer forma."

    jump prologo_3

# ===================
# CENA PRÓLOGO.2D - Caminho Solitário
# ===================

label prologo_2d:

    hide rafaela

    "Você ignora o grupo e procura a sala sozinha."

    "Depois de alguns minutos procurando, você finalmente encontra a sala A1-203."

    "O mesmo grupo que você viu está sentado nas fileiras do meio."

    "Você se senta afastada deles."

    jump prologo_3_alone

# ===================
# CENA PRÓLOGO.3 - "A SALA DE AULA"
# ===================

label prologo_3:

    scene bg classroom with fade

    "A sala está quase cheia. Cadeiras de braço, quadro branco gigante, ar condicionado fazendo barulho."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    with dissolve

    "O grupo encontra lugares juntos nas fileiras do meio."

    "Você senta entre Isabela e Paulo."

    "Rafaela está na frente, já conversando com todo mundo."

    "Lucas está anotando algo no caderno antes mesmo da aula começar."

    "De repente, uma garota de óculos e cabelo preso entra na sala, olhando para os lados com olhar perdido e nervoso."

    show paulo neutral at pos_4_farleft
    show isabela neutral at pos_4_left

    paulo "Ela parece mais perdida que eu."

    "A garota encontra uma cadeira vazia no canto e se senta sozinha, olhando para baixo."

    isabela "Será que a gente devia chamar ela?"

    show lucas thinking at pos_4_right

    lucas "A aula vai começar. Depois a gente vê isso."

    show rafaela happy at pos_4_farright

    rafaela "Gente, vamos chamar! Ninguém merece ficar isolado no primeiro dia."

    menu prologo_3_escolha:
        "O que você faz?"

        "Levantar e chamar a garota para sentar com vocês":
            $ aumentar_relacao("camila", 3)
            $ aumentar_skill("empatia", 2)
            $ aumentar_skill("lideranca", 1)
            jump prologo_4a

        "Concordar com Isabela e esperar o intervalo":
            $ aumentar_relacao("isabela", 1)
            jump prologo_4b

        "Concordar com Lucas e focar na aula":
            $ aumentar_relacao("lucas", 1)
            jump prologo_4c

        "Mandar uma mensagem no grupo perguntando o nome dela":
            $ aumentar_skill("criatividade", 1)
            $ social_score += 1
            jump prologo_4a

# ===================
# CENA PRÓLOGO.3_ALONE - Versão solitária
# ===================

label prologo_3_alone:

    scene bg classroom with fade

    "A sala está quase cheia."

    "Você senta sozinha em uma cadeira de canto."

    "O grupo que você viu lá fora está sentado junto nas fileiras do meio, conversando animadamente."

    "De repente, outra garota de óculos entra nervosa e se senta perto de você."

    show camila worried at center

    "Ela também parece estar sozinha."

    "Vocês trocam um olhar breve."

    camila "Oi... você também é de Ambiental?"

    menu:
        "Como você responde?"

        "Sim, primeiro dia aqui":
            pov "Sim, primeiro dia aqui."

            $ aumentar_relacao("camila", 2)

            camila "Eu também... tô bem nervosa."

            pov "Eu também."

            "Um pequeno sorriso se forma no rosto dela."

        "Sim, e você?":
            pov "Sim, e você?"

            $ aumentar_relacao("camila", 1)

            camila "Também... primeira vez aqui."

    jump prologo_fim_alone

# ===================
# CENA PRÓLOGO.4A - "CAMILA ENTRA NO GRUPO"
# ===================

label prologo_4a:

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    with dissolve

    "Você se levanta e caminha até a garota."

    show camila worried at center

    pov "Oi! A gente tá sentando ali, quer vir junto?"

    "A garota levanta os olhos, surpresa. Parece querer dizer não, mas apenas balança a cabeça timidamente."

    camila "Ah... obrigada. Eu sou Camila."

    pov "Prazer, Camila! Vem, vou te apresentar pro pessoal."

    hide camila with dissolve

    "Camila pega sua mochila e segue você. Ao chegar no grupo, todos dão um sorriso acolhedor."

    show rafaela happy at pos_4_farleft
    show isabela happy at pos_4_left
    show paulo happy at pos_4_right

    rafaela "Oi, Camila! Seja bem-vinda ao caos! Eu sou Rafaela."

    isabela "Oi! Isabela. Fica à vontade."

    paulo "E aí! Paulo. Relaxa, a gente tá tudo perdido igual."

    show lucas neutral at pos_4_farright

    "Lucas apenas acena, voltando ao caderno."

    hide rafaela
    hide isabela
    hide paulo
    hide lucas
    with dissolve

    show camila happy at center

    "Camila senta ao seu lado, com um leve sorriso nos lábios."

    camila "Obrigada... de verdade."

    hide camila with dissolve

    "Você sente que fez a escolha certa."

    narrator "Às vezes, a maior liderança está nos pequenos gestos."
    narrator "Você acabou de formar o grupo que te acompanhará por toda essa jornada."

    $ unlock_achievement("primeira_amizade")
    $ aumentar_skill("empatia", 1)

    jump prologo_fim

# ===================
# CENAS PRÓLOGO.4B e 4C - Versões alternativas
# ===================

label prologo_4b:

    "Você decide esperar o intervalo para falar com a garota."

    "A aula começa logo em seguida."

    jump prologo_fim

label prologo_4c:

    "Você decide focar na aula que está prestes a começar."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    with dissolve

    $ aumentar_skill("pensamento_critico", 1)

    jump prologo_fim

# ===================
# FIM DO PRÓLOGO
# ===================

label prologo_fim:

    scene bg classroom with fade

    "A aula de introdução à Engenharia Ambiental começa."

    "O professor fala sobre sustentabilidade, impacto ambiental, e a importância dos engenheiros ambientais no mundo moderno."

    "Você olha ao redor e vê os rostos dos seus novos colegas."

    "Isabela anotando tudo meticulosamente."

    "Lucas com o olhar focado no professor."

    "Camila tentando acompanhar, ainda um pouco nervosa."

    "Paulo lutando contra o sono."

    "Rafaela tentando não rir de algo no celular."

    narrator "Você não sabe ainda, mas essas pessoas se tornarão parte fundamental da sua jornada universitária."
    narrator "Amizades serão formadas. Desafios serão enfrentados."
    narrator "E você aprenderá que soft skills são tão importantes quanto as hard skills."

    scene black with fade

    show text "{size=32}PRÓLOGO COMPLETO{/size}\n\n{size=20}Pressione 'R' para ver seu status de relações{/size}" at truecenter
    pause
    hide text

    $ prologo_completo = True

    jump roteiro1

# ===================
# FIM DO PRÓLOGO - Versão Solitária
# ===================

label prologo_fim_alone:

    scene bg classroom with fade

    "A aula começa."

    "Você e Camila sentam juntas, formando uma dupla quieta no canto da sala."

    narrator "Nem toda amizade começa com grandes gestos."
    narrator "Às vezes, um simples olhar compartilhado é o suficiente."

    scene black with fade

    show text "{size=32}PRÓLOGO COMPLETO{/size}\n\n{size=20}Você escolheu um caminho mais introspectivo{/size}" at truecenter
    pause
    hide text

    $ prologo_completo = True

    jump roteiro1

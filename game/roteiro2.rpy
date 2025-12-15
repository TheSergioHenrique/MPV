# ================================================
# MOMENTOS PARA VIDA - Roteiro 2
# "A Longa Noite de Estudos"
# Soft Skills: Resiliência, Empatia, Gestão de Tempo,
#              Trabalho em Equipe, Autocuidado
# ================================================

label roteiro2:

    # Player character for this route
    $ povname = "Isabela"

    # ===================
    # CENA A - "SEMANA DE PROVAS"
    # ===================

    # Play campus music
    play music campus fadein 1.0

    scene bg campus with fade

    "Segunda-feira - 17h30"

    "Semana de provas finais."

    "O campus está mais vazio que o normal. Todos estão estudando."

    scene bg courtyard with fade

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela neutral at center

    "Você está no pátio, revisando suas anotações de Cálculo 2."

    "Seu celular vibra."

    # Play WhatsApp sound
    play music whatsapp fadein 0.5

    scene bg whatsapp with fade

    "Grupo: 'Amigos da Ambiental'"

    rafaela "Gente, alguém mais tá em pânico? 😱"

    paulo "Tenho 3 provas essa semana. Vou morrer"

    lucas "Eu sugiro uma sessão de estudos conjunta. Hoje à noite."

    camila "Eu preciso muito de ajuda em Cálculo..."

    rafaela "Bora! Sessão de estudos na biblioteca!"

    "..."

    menu roteiro2_cena_a:
        "Como você responde?"

        "Confirmar presença imediatamente - 'Tô dentro!'":
            $ aumentar_skill("trabalho_equipe", 1)
            $ aumentar_relacao("lucas", 1)
            jump roteiro2_b1

        "Perguntar quem vai e o que vão estudar primeiro":
            $ aumentar_skill("gestao_tempo", 1)
            jump roteiro2_b2

        "Sugerir começar mais cedo - 'Que tal 18h?'":
            $ aumentar_skill("proatividade", 1)
            $ aumentar_skill("gestao_tempo", 1)
            jump roteiro2_b3

        "Hesitar - 'Não sei se consigo, tenho muito pra estudar sozinha'":
            $ independente_score += 1
            jump roteiro2_b4

    # ===================
    # CENA B1 - "CONFIRMAÇÃO IMEDIATA"
    # ===================

label roteiro2_b1:

    scene bg whatsapp

    pov "Tô dentro!"

    isabela "Eu também! A gente se ajuda 💙"

    lucas "Combinado então. 19h na biblioteca, sala de estudos 3."

    rafaela "Levem café! Vai ser longa a noite 😅"

    jump roteiro2_c

    # ===================
    # CENA B2 - "PLANEJAMENTO"
    # ===================

label roteiro2_b2:

    scene bg whatsapp

    pov "Quem vai? E vamos estudar o quê primeiro?"

    lucas "Eu vou. Sugiro começar por Cálculo, é a prova mais difícil."

    camila "Eu preciso MUITO de Cálculo 🙏"

    rafaela "Eu vou! Mas também preciso revisar Química"

    paulo "Eu vou, mas tenho que sair meia-noite. Treino cedo amanhã"

    isabela "Então vamos focar em Cálculo até 22h, depois Química?"

    lucas "Plano sólido."

    $ aumentar_skill("gestao_tempo", 1)

    jump roteiro2_c

    # ===================
    # CENA B3 - "COMEÇAR CEDO"
    # ===================

label roteiro2_b3:

    # Play WhatsApp sound
    play music whatsapp fadein 0.5

    scene bg whatsapp

    pov "Que tal começar 18h? Quanto antes melhor"

    lucas "Boa ideia. Mais tempo para revisar."

    paulo "Mas eu só saio do treino 18h30..."

    rafaela "Eu também só consigo depois das 18h30"

    camila "18h é muito cedo pra mim..."

    lucas "19h então. Compromisso entre eficiência e disponibilidade."

    pov "Ok, 19h!"

    $ aumentar_skill("adaptabilidade", 1)

    jump roteiro2_c

    # ===================
    # CENA B4 - "HESITAÇÃO"
    # ===================

label roteiro2_b4:

    scene bg whatsapp

    pov "Não sei se consigo, tenho muito pra estudar sozinha"

    "..."

    isabela "Mas estudando junto a gente se ajuda!"

    camila "Por favor vem... eu preciso de ajuda 🥺"

    rafaela "Vem! Vai ser mais leve juntos!"

    "Você pensa por um momento."

    menu:
        "O que você decide?"

        "Aceitar ir":
            $ aumentar_relacao("camila", 1)
            $ aumentar_relacao("isabela", 1)
            pov "Ok, vocês convenceram. Vou sim!"
            jump roteiro2_c

        "Recusar":
            pov "Desculpa gente, mas preciso estudar no meu ritmo"
            lucas "Entendo. Boa sorte."
            "Você passa a noite estudando sozinha."
            $ isolamento_score += 2
            jump roteiro2_alone

    # ===================
    # CENA C - "INÍCIO DA SESSÃO"
    # ===================

label roteiro2_c:

    # Play night study music
    play music noite_estudos fadein 2.0

    scene bg library with fade

    "Biblioteca - 19h00"

    "Sala de estudos 3 - uma mesa grande, quadro branco, ar condicionado funcionando."

    "O grupo está reunido. Livros, cadernos, canetas e notebooks espalhados pela mesa."

    "Rafaela chega atrasada com uma sacola."

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela happy at pos_5_farright

    rafaela "Cheguei! E trouxe café, energético e chocolate!"

    paulo "Salvadora da pátria!"

    hide rafaela
    hide paulo
    hide isabela
    with dissolve

    show lucas neutral at center

    lucas "Ok, vamos começar. Cálculo 2, capítulo de integrais."

    "Lucas vai ao quadro branco e começa a explicar."

    "As primeiras horas passam rapidamente."

    scene black with fade

    show text "{size=24}21h30{/size}" at truecenter
    pause 1.0
    hide text

    scene bg library with fade

    "Duas horas e meia depois..."

    "O cansaço começa a aparecer."

    hide isabela
    hide lucas
    hide paulo
    with dissolve

    show camila worried at center

    camila "Eu... eu ainda não entendi essa parte..."

    "Camila está com olheiras, claramente exausta."

    hide camila

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo neutral at center

    paulo "Cara, eu tô morto. Preciso de uma pausa."

    hide paulo

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas thinking at center

    lucas "Pausas são contraproducentes. Temos muito ainda pra revisar."

    hide lucas

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela sad at center

    rafaela "Mas a gente já tá aqui faz horas... Será que não é melhor descansar um pouco?"

    hide rafaela

    menu roteiro2_c_escolha:
        "O que você sugere?"

        "Concordar com Lucas e continuar sem pausa":
            $ aumentar_skill("resiliencia", 1)
            $ aumentar_relacao("lucas", 2)
            jump roteiro2_d1

        "Propor uma pausa de 15 minutos":
            $ aumentar_skill("gestao_tempo", 2)
            $ aumentar_skill("empatia", 1)
            jump roteiro2_d2

        "Sugerir trocar de matéria para refrescar a mente":
            $ aumentar_skill("adaptabilidade", 1)
            $ aumentar_skill("criatividade", 1)
            jump roteiro2_d3

        "Focar em ajudar Camila antes de continuar":
            $ aumentar_skill("empatia", 2)
            $ aumentar_relacao("camila", 2)
            jump roteiro2_d4

    # ===================
    # CENA D1 - "CONTINUAR SEM PAUSA"
    # ===================

label roteiro2_d1:

    scene bg library

    pov "Lucas tem razão. Vamos aproveitar o embalo."

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo worried at center

    paulo "Tá, mas eu preciso de pelo menos um café."

    hide paulo
    hide isabela
    hide lucas
    hide rafaela
    hide professor
    show camila worried at center

    "Paulo se levanta e vai buscar café na máquina."

    "Camila continua lutando com os exercícios, cada vez mais frustrada."

    "A produtividade do grupo cai visivelmente."

    hide paulo
    hide camila

    jump roteiro2_e

    # ===================
    # CENA D2 - "PAUSA DE 15 MINUTOS"
    # ===================

label roteiro2_d2:

    scene bg library

    pov "Vamos fazer uma pausa de 15 minutos. Descansar a mente ajuda a absorver melhor."

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas thinking at center

    lucas "15 minutos apenas. Vamos marcar no celular."

    hide lucas

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela happy at center

    rafaela "Boa! Vamos esticar as pernas!"

    hide rafaela
    hide isabela
    hide lucas
    hide camila
    hide professor
    show paulo happy at center

    "O grupo se dispersa. Alguns vão ao banheiro, outros pegam café."

    "Você aproveita para alongar e respirar fundo."

    scene bg corridor with fade

    "No corredor da biblioteca."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila sad at center

    "Você encontra Camila encostada na parede, olhando para o nada."

    pov "Ei, tudo bem?"

    camila "Eu... eu não sei se vou conseguir passar. Tá tudo tão difícil..."

    menu:
        "Como você responde?"

        "Dar apoio emocional - 'Você consegue, eu acredito em você'":
            $ aumentar_relacao("camila", 2)
            $ aumentar_skill("empatia", 1)
            pov "Você consegue, eu acredito em você. Você já chegou até aqui."
            camila "Obrigada... eu preciso ouvir isso."

        "Dar apoio prático - 'Vamos revisar juntas depois'":
            $ aumentar_relacao("camila", 1)
            $ aumentar_skill("trabalho_equipe", 1)
            pov "Vamos revisar juntas depois, com calma. Eu te ajudo."
            camila "Sério? Obrigada!"

        "Ser honesta - 'É difícil mesmo, mas desistir não vai ajudar'":
            $ aumentar_skill("comunicacao", 1)
            pov "É difícil mesmo, mas desistir não vai ajudar."
            camila "É... você tem razão."

    hide camila

    "Vocês voltam para a sala revigoradas."

    $ aumentar_skill("autocuidado", 1)

    jump roteiro2_e

    # ===================
    # CENA D3 - "TROCAR DE MATÉRIA"
    # ===================

label roteiro2_d3:

    scene bg library

    pov "Que tal mudar para Química? Trocar de assunto ajuda a refrescar a mente."

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela happy at center

    rafaela "Boa ideia! Vamos fazer Química agora!"

    hide rafaela

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas thinking at center

    lucas "Mas ainda não terminamos Cálculo..."

    hide lucas

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela neutral at center

    isabela "A gente volta pra Cálculo depois. Variação ajuda a fixar melhor."

    hide isabela

    "O grupo muda de matéria."

    "A mudança de ritmo realmente ajuda. Todos ficam mais animados."

    $ aumentar_skill("adaptabilidade", 1)

    jump roteiro2_e

    # ===================
    # CENA D4 - "AJUDAR CAMILA"
    # ===================

label roteiro2_d4:

    scene bg library

    pov "Antes de continuar, vamos ajudar a Camila a entender essa parte."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila worried at center

    camila "Eu... vocês não precisam parar por minha causa..."

    hide camila

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela happy at center

    isabela "Claro que precisamos! Estamos juntos nisso."

    hide isabela

    "Você, Isabela e Lucas se reúnem em torno de Camila."

    "Vocês explicam de diferentes formas até ela entender."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila happy at center

    camila "Ahh! Agora eu entendi! Muito obrigada!"

    "Ver Camila finalmente compreendendo traz uma sensação de satisfação ao grupo."

    $ aumentar_skill("empatia", 2)
    $ aumentar_skill("trabalho_equipe", 1)
    $ aumentar_relacao("camila", 3)

    hide camila

    jump roteiro2_e

    # ===================
    # CENA E - "MADRUGADA"
    # ===================

label roteiro2_e:

    scene black with fade

    show text "{size=24}23h45{/size}" at truecenter
    pause 1.0
    hide text

    scene bg library with fade

    "Quase meia-noite."

    "A biblioteca está quase vazia. Apenas alguns estudantes desesperados ainda estão por lá."

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo worried at center

    paulo "Pessoal, eu vou ter que ir. Tenho treino 6h da manhã."

    pov "Vai com cuidado, Paulo!"

    paulo "Valeu pelo estudo! Me salvaram!"

    hide paulo with dissolve

    "Paulo sai."

    "Agora são só quatro: você, Isabela, Lucas e Camila."

    "E Rafaela, que está... dormindo com a cabeça sobre o livro."

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela neutral at center

    "Rafaela ronca suavemente."

    hide rafaela

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas neutral at left
    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela worried at center
    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila worried at right

    lucas "Vamos continuar. Ainda tem Termodinâmica."

    isabela "Lucas... são quase meia-noite. Talvez seja melhor ir dormir."

    lucas "Dormir é perder tempo. A prova é amanhã."

    "Lucas está com olheiras profundas, mas seus olhos estão determinados - quase obsessivos."

    camila "Eu... eu não consigo mais me concentrar..."

    "Camila está praticamente caindo de sono."

    menu roteiro2_e_escolha:
        "O que você faz?"

        "Concordar com Lucas e continuar até de madrugada":
            $ aumentar_skill("resiliencia", 2)
            $ aumentar_relacao("lucas", 2)
            jump roteiro2_f1

        "Sugerir que todos vão dormir e descansem":
            $ aumentar_skill("autocuidado", 2)
            $ aumentar_skill("inteligencia_emocional", 1)
            jump roteiro2_f2

        "Propor que quem quiser vá embora, mas você fica com Lucas":
            $ aumentar_relacao("lucas", 2)
            jump roteiro2_f3

        "Convencer Lucas a ir dormir":
            $ aumentar_skill("empatia", 2)
            $ aumentar_skill("comunicacao", 2)
            jump roteiro2_f4

    # ===================
    # CENA F1 - "CONTINUAR ATÉ DE MADRUGADA"
    # ===================

label roteiro2_f1:

    scene bg library

    pov "Vamos continuar. Estamos quase lá."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila worried at center

    camila "Eu... ok..."

    hide camila

    "O grupo continua estudando."

    scene black with fade

    show text "{size=24}02h30 da madrugada{/size}" at truecenter
    pause 1.0
    hide text

    scene bg library with fade

    "2h30 da madrugada."

    "Todos estão exaustos. Mal conseguem manter os olhos abertos."

    "As palavras nos livros começam a se misturar."

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas worried at center

    lucas "Eu... acho que não tô absorvendo mais nada..."

    "Até Lucas finalmente admite o limite."

    pov "Vamos pra casa. Descansar também é parte do estudo."

    $ aumentar_skill("resiliencia", 1)

    jump roteiro2_g

    # ===================
    # CENA F2 - "IR DORMIR"
    # ===================

label roteiro2_f2:

    scene bg library

    pov "Gente, vamos dormir. Estudar cansado não adianta nada."

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela happy at center

    isabela "Concordo totalmente."

    hide isabela

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila happy at center

    camila "Ai que alívio..."

    hide camila

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas worried at center

    lucas "Mas... a prova é amanhã..."

    pov "E você vai fazer a prova cansado se não dormir. Seu cérebro precisa de descanso."

    "Lucas hesita, mas concorda."

    lucas "Você... tem razão."

    hide lucas

    "O grupo arruma suas coisas."

    $ aumentar_skill("autocuidado", 1)
    $ aumentar_skill("inteligencia_emocional", 1)

    jump roteiro2_g

    # ===================
    # CENA F3 - "FICAR COM LUCAS"
    # ===================

label roteiro2_f3:

    scene bg library

    pov "Quem quiser pode ir. Eu fico aqui com o Lucas."

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela worried at left
    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila worried at right

    isabela "Vocês têm certeza?"

    pov "Sim. Vão descansar."

    "Isabela, Camila e Rafaela vão embora."

    hide isabela
    hide camila
    with dissolve

    "Você e Lucas continuam estudando sozinhos."

    scene black with fade

    show text "{size=24}01h30 da madrugada{/size}" at truecenter
    pause 1.0
    hide text

    scene bg library with fade

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas neutral at center

    "1h30 da madrugada."

    "É só você e Lucas na sala silenciosa."

    lucas "Obrigado por ficar."

    pov "Estamos juntos nisso."

    "Vocês continuam revisando, apoiando um ao outro na exaustão."

    $ aumentar_relacao("lucas", 3)
    $ aumentar_skill("resiliencia", 2)

    jump roteiro2_g

    # ===================
    # CENA F4 - "CONVENCER LUCAS"
    # ===================

label roteiro2_f4:

    scene bg library

    pov "Lucas, olha pra você. Você está exausto."

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas worried at center

    lucas "Eu... eu tenho que estudar. Eu preciso tirar nota máxima."

    pov "Por quê? Por que essa pressão toda?"

    "Lucas para e te olha. Você vê vulnerabilidade em seus olhos."

    lucas "Porque... se eu não for o melhor, eu não sou nada."

    lucas "Meu pai... ele espera perfeição. Sempre esperou."

    "Sua voz quebra um pouco."

    pov "Lucas, você já é incrível. Você não precisa se destruir pra provar isso."

    "Você coloca a mão no ombro dele."

    pov "Vamos pra casa. Você vai se sair bem na prova, descansado ou não. Mas descansado, você vai se sair melhor."

    "Lucas respira fundo."

    lucas "Você... você tem razão."

    "Pela primeira vez, Lucas admite seu limite."

    $ unlock_achievement("amigo_verdadeiro")
    $ aumentar_relacao("lucas", 4)
    $ aumentar_skill("empatia", 3)
    $ aumentar_skill("inteligencia_emocional", 2)

    hide lucas

    jump roteiro2_g

    # ===================
    # CENA G - "DIA DA PROVA"
    # ===================

label roteiro2_g:

    scene black with fade

    show text "{size=24}No dia seguinte...{/size}" at truecenter
    pause 1.0
    hide text

    # Change to decision/test music
    play music decisao fadein 1.5

    scene bg classroom with fade

    "Sala de prova - 8h00"

    "Você chega para a prova de Cálculo 2."

    "O grupo está lá."

    if autocuidado >= 2:
        "Todos parecem descansados e focados."
        $ prova_estado = "descansados"
    elif resiliencia >= 3:
        "Todos parecem cansados, mas determinados."
        $ prova_estado = "determinados"
    else:
        "Todos parecem exaustos."
        $ prova_estado = "exaustos"

    hide isabela
    hide lucas
    hide camila
    hide rafaela

    "A prova começa."

    scene black with fade

    show text "{size=24}2 horas depois...{/size}" at truecenter
    pause 1.0
    hide text

    # Calcular resultado baseado em escolhas
    if prova_estado == "descansados":
        jump roteiro2_final_a
    elif prova_estado == "determinados":
        jump roteiro2_final_b
    else:
        jump roteiro2_final_c

    # ===================
    # FINAIS DO ROTEIRO 2
    # ===================

label roteiro2_final_a:
    # Final Excelente - Equilíbrio Perfeito

    # Play growth/victory music
    play music crescimento fadein 1.5

    scene bg courtyard with fade

    "Uma semana depois - Resultados das provas"

    "O grupo comemora."

    isabela "Galera! Passei com 8,5!"

    lucas "9,2. Não foi perfeito, mas... estou satisfeito."

    camila "Eu... EU PASSEI! 7,0!"

    "Camila está radiante."

    rafaela "8,0 aqui! Viva!"

    pov "Conseguimos! E sem nos destruir no processo!"

    $ unlock_achievement("equilibrio_perfeito")
    $ unlock_achievement("sabedoria")

    narrator "Você aprendeu que sucesso não vem de se sacrificar até o limite,"
    narrator "mas de encontrar equilíbrio entre esforço e autocuidado."

    jump roteiro2_epilogo

label roteiro2_final_b:
    # Final Bom - Resiliência Recompensada

    scene bg courtyard with fade

    "Uma semana depois - Resultados das provas"

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela neutral at left
    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas happy at center
    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila happy at right

    "O grupo se reúne."

    lucas "Tirei 9,5. Valeu a pena continuar estudando."

    pov "Parabéns, Lucas!"

    camila "Eu tirei 7,5! Consegui!"

    isabela "8,0. Bom o suficiente!"

    "Todos estão cansados, mas aliviados."

    $ unlock_achievement("resistencia_mental")

    narrator "A resiliência tem seu valor,"
    narrator "mas é importante saber quando parar."

    jump roteiro2_epilogo

label roteiro2_final_c:
    # Final Satisfatório - Lição Aprendida

    scene bg courtyard with fade

    "Uma semana depois - Resultados das provas"

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila sad at left
    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas worried at center
    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela worried at right

    "O grupo parece abatido."

    camila "7,0... passei raspando."

    lucas "8,5. Esperava mais. A exaustão me atrapalhou."

    pov "Eu também não fui tão bem quanto esperava."

    isabela "Acho que exageramos ontem..."

    "Silêncio pensativo."

    pov "Pelo menos aprendemos algo importante: limites existem por um motivo."

    lucas "É verdade. Na próxima, vou me organizar melhor desde o início."

    $ aumentar_skill("autoconhecimento", 2)

    narrator "Às vezes, as melhores lições vêm dos erros."
    narrator "Você aprendeu sobre seus limites e a importância do autocuidado."

    jump roteiro2_epilogo

    # ===================
    # EPÍLOGO DO ROTEIRO 2
    # ===================

label roteiro2_epilogo:

    scene black with fade

    show text "{size=32}ROTEIRO 2 COMPLETO{/size}\n\n{size=20}A Longa Noite de Estudos{/size}" at truecenter
    pause
    hide text

    call screen epilogue_stats

    $ roteiro2_completo = True

    jump roteiro3

    # ===================
    # ROTA ALTERNATIVA - ESTUDAR SOZINHA
    # ===================

label roteiro2_alone:

    # Play library music for solo study
    play music library fadein 1.5

    scene bg library with fade

    "Você passa a noite inteira estudando sozinha."

    "Sem distrações, você consegue cobrir todo o conteúdo."

    "Mas a solidão pesa. Não tem ninguém para tirar dúvidas. Ninguém para apoiar."

    scene black with fade

    show text "{size=24}Dia da prova{/size}" at truecenter
    pause 1.0
    hide text

    scene bg classroom with fade

    "Você faz a prova."

    "É difícil, mas você se sai razoavelmente bem."

    scene bg courtyard with fade

    "Depois da prova, você vê o grupo reunido, rindo e compartilhando histórias da noite de estudos."

    "Você tirou uma boa nota."

    "Mas perdeu algo mais importante."

    narrator "Às vezes, o valor está mais na jornada compartilhada"
    narrator "do que no destino alcançado sozinho."

    $ aumentar_skill("independencia", 2)
    $ aumentar_skill("solidao", 1)

    jump roteiro2_epilogo

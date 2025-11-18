# ================================================
# MOMENTOS PARA VIDA - Roteiro 1
# "O Trabalho em Grupo"
# Soft Skills: Comunicação, Trabalho em Equipe,
#              Gestão de Conflitos, Liderança
# ================================================

label roteiro1:

    # Set character as Isabela for this route
    $ povname = "Isabela"

    # ===================
    # CENA A - "O ANÚNCIO DO TRABALHO"
    # ===================

    scene bg classroom with fade

    "Quarta-feira - 15h30"

    "Aula de Projeto Integrado."

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide rafaela
    show professor neutral at center

    professor "Pessoal, atenção. Vou anunciar o trabalho final da disciplina."

    "A sala fica em silêncio."

    professor "Vocês vão desenvolver um projeto de Cidade Sustentável em grupos de 5 pessoas."

    professor "O trabalho vale 40%% da nota final e será apresentado daqui a três semanas."

    "Murmúrios começam a preencher a sala."

    professor "Os grupos já foram definidos por mim. Quero que vocês aprendam a trabalhar com pessoas diferentes."

    "O professor começa a ler os grupos."

    professor "Grupo 3: Isabela, Lucas, Camila, Paulo e Rafaela."

    hide professor with dissolve

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo happy at center

    paulo "Opa! Nosso grupo já tá formado!"

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela happy at center

    rafaela "Que legal! A gente vai arrasar!"

    hide paulo
    hide rafaela

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas thinking at center

    lucas "Precisamos começar hoje mesmo. Três semanas passa rápido."

    hide lucas

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila worried at center

    "Camila parece nervosa, olhando para baixo."

    camila "Eu... espero conseguir ajudar direito."

    hide camila

    pov "Vai dar tudo certo. Somos um bom grupo."

    menu roteiro1_cena_a:
        "Como você inicia o planejamento?"

        "Propor uma reunião hoje mesmo após a aula":
            $ aumentar_skill("lideranca", 1)
            $ aumentar_skill("proatividade", 1)
            jump roteiro1_b1

        "Esperar alguém tomar a iniciativa":
            $ aumentar_relacao("lucas", -1)
            jump roteiro1_b2

        "Sugerir criar um grupo no WhatsApp primeiro":
            $ aumentar_skill("comunicacao", 1)
            $ aumentar_relacao("rafaela", 1)
            jump roteiro1_b3

        "Perguntar a opinião de cada um sobre quando começar":
            $ aumentar_skill("empatia", 1)
            $ aumentar_skill("trabalho_equipe", 1)
            jump roteiro1_b4

    # ===================
    # CENA B1 - "LIDERANÇA PROATIVA"
    # ===================

label roteiro1_b1:

    scene bg courtyard with fade

    "16h00 - Pátio da faculdade"

    "O grupo se reúne em uma mesa do pátio."

    pov "Obrigada por virem. Acho importante começarmos hoje."

    lucas "Concordo. Eficiência é fundamental."

    paulo "Então, sobre o que é esse projeto mesmo?"

    rafaela "Cidade sustentável, Paulo! Você não prestou atenção?"

    "Você abre o notebook e projeta os requisitos do trabalho."

    pov "Precisamos dividir as tarefas. O projeto tem cinco partes principais."

    lucas "Eu sugiro dividir por especialidade. Cada um pega uma parte."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila worried at Position(xalign=0.6, yalign=1.0)

    camila "Mas... e se a gente trabalhar junto? Assim ninguém fica perdido..."

    lucas "Isso é ineficiente. Trabalhar separado é mais rápido."

    menu roteiro1_b1_escolha:
        "Como você medeia isso?"

        "Concordar com Lucas - dividir tarefas individualmente":
            $ aumentar_relacao("lucas", 2)
            $ aumentar_relacao("camila", -1)
            jump roteiro1_c1

        "Concordar com Camila - trabalhar juntos":
            $ aumentar_relacao("camila", 2)
            $ aumentar_relacao("lucas", -1)
            $ aumentar_skill("trabalho_equipe", 1)
            jump roteiro1_c2

        "Propor um meio-termo - dividir em duplas":
            $ aumentar_skill("gestao_conflitos", 2)
            $ aumentar_skill("lideranca", 1)
            $ aumentar_relacao("lucas", 1)
            $ aumentar_relacao("camila", 1)
            jump roteiro1_c3

        "Fazer uma votação para decidir":
            $ aumentar_skill("gestao_conflitos", 1)
            jump roteiro1_c4

    # ===================
    # CENA B2 - "ESPERANDO INICIATIVA"
    # ===================

label roteiro1_b2:

    scene bg corridor with fade

    "Fim da aula. Ninguém diz nada sobre o trabalho."

    "Vocês se dispersam."

    scene black with fade

    show text "{size=24}Dois dias depois...{/size}" at truecenter
    pause 1.0
    hide text

    scene bg whatsapp with fade

    "Grupo no WhatsApp: 'Projeto Cidade Sustentável'"

    lucas "Precisamos nos reunir. Já perdemos dois dias."

    lucas "Proponho reunião hoje às 18h na biblioteca."

    rafaela "Opa, eu posso!"

    paulo "Eu também"

    camila "Ok"

    "..."

    menu:
        "Como você responde?"

        "Tô dentro":
            $ aumentar_relacao("lucas", 1)

        "Desculpa, não posso hoje. Amanhã?":
            $ aumentar_relacao("lucas", -1)
            "Lucas fica visivelmente irritado."

    jump roteiro1_c1

    # ===================
    # CENA B3 - "COMUNICAÇÃO PRIMEIRO"
    # ===================

label roteiro1_b3:

    scene bg whatsapp with fade

    "Você cria um grupo no WhatsApp"

    pov "Criei esse grupo pra gente se organizar!"

    rafaela "Aí sim! 🎉"

    paulo "Bora fazer um projeto massa"

    lucas "Quando vamos nos reunir presencialmente?"

    camila "Eu prefiro presencial... tenho dificuldade de me concentrar online"

    pov "Que tal hoje mesmo, 18h na biblioteca?"

    "Todos concordam."

    $ aumentar_skill("comunicacao", 1)

    jump roteiro1_c1

    # ===================
    # CENA B4 - "CONSULTA DEMOCRÁTICA"
    # ===================

label roteiro1_b4:

    scene bg courtyard with fade

    pov "Gente, o que vocês acham? Quando podemos começar?"

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas thinking at pos_4_farleft

    lucas "Quanto antes melhor. Hoje mesmo seria ideal."

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela happy at pos_4_left

    rafaela "Eu posso hoje! Mas amanhã eu tenho teatro..."

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo neutral at pos_4_right

    paulo "Hoje eu tenho treino, mas posso sair mais cedo."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila worried at pos_4_farright

    camila "Eu... eu posso qualquer dia. Vocês decidem."

    pov "Então vamos hoje, 18h30, depois do treino do Paulo?"

    "Todos concordam."

    $ aumentar_skill("empatia", 1)

    jump roteiro1_c1

    # ===================
    # CENA C1 - "DIVISÃO INDIVIDUAL"
    # ===================

label roteiro1_c1:

    scene bg library with fade

    "18h30 - Biblioteca"

    "O grupo está reunido em uma mesa grande."

    lucas "Vamos dividir as tarefas. Eu fico com a parte de gestão de energia renovável."

    rafaela "Eu posso fazer a parte de espaços públicos e áreas verdes!"

    paulo "Eu pego mobilidade urbana, entendo de trânsito."

    "Sobram: Gestão de Resíduos e Habitação Sustentável."

    lucas "Isabela, você fica com qual?"

    menu:
        "Qual parte você escolhe?"

        "Gestão de Resíduos":
            $ parte_isabela = "residuos"
            pov "Eu fico com Gestão de Resíduos."
            camila "Então... eu fico com Habitação."

        "Habitação Sustentável":
            $ parte_isabela = "habitacao"
            pov "Eu pego Habitação Sustentável."
            camila "Então... eu fico com Gestão de Resíduos."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila worried at Position(xalign=0.6, yalign=1.0)

    camila "Eu... eu vou precisar de ajuda. Nunca fiz nada assim."

    lucas "Você tem três semanas. Tem tempo de aprender."

    "O tom de Lucas é frio, técnico."

    "Camila baixa a cabeça."

    jump roteiro1_d

    # ===================
    # CENA C2 - "TRABALHO COLABORATIVO"
    # ===================

label roteiro1_c2:

    scene bg library with fade

    "18h30 - Biblioteca"

    pov "Vamos trabalhar juntos. Assim todo mundo aprende tudo."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila happy at center

    camila "Eu acho ótimo! Me sinto mais segura assim."

    lucas "Mas isso vai levar muito mais tempo..."

    rafaela "Relaxa, Lucas. A qualidade vai ser melhor."

    paulo "E a gente se diverte mais também!"

    lucas "Diversão não garante nota."

    "Você sente a tensão crescendo."

    $ aumentar_skill("gestao_conflitos", 1)

    jump roteiro1_d

    # ===================
    # CENA C3 - "MEIO-TERMO - DUPLAS"
    # ===================

label roteiro1_c3:

    scene bg library with fade

    "18h30 - Biblioteca"

    pov "E se a gente dividir em duplas? Assim é mais eficiente que todos juntos, mas ninguém fica sozinho."

    "Lucas pondera por um momento."

    lucas "Isso... pode funcionar. É um compromisso razoável."

    camila "Eu gosto dessa ideia!"

    rafaela "Perfeito! Quem fica com quem?"

    menu roteiro1_c3_escolha:
        "Como formar as duplas?"

        "Deixar as pessoas escolherem naturalmente":
            $ aumentar_skill("gestao_conflitos", 1)
            "Paulo e Rafaela se juntam naturalmente."
            "Lucas olha para você."
            lucas "Isabela, quer trabalhar comigo? Somos os mais organizados."
            "Camila fica sozinha, olhando para baixo."

            menu:
                "O que você faz?"

                "Aceitar trabalhar com Lucas":
                    $ dupla_isabela = "lucas"
                    $ aumentar_relacao("lucas", 2)
                    $ aumentar_relacao("camila", -2)

                "Sugerir que Lucas trabalhe com Camila":
                    $ dupla_isabela = "paulo_rafaela"
                    $ aumentar_relacao("camila", 2)
                    $ aumentar_skill("empatia", 2)
                    pov "Lucas, que tal você trabalhar com a Camila? Você pode ensinar muito pra ela."
                    lucas "Eu... está bem."

        "Sugerir você mesma as duplas":
            $ aumentar_skill("lideranca", 2)
            pov "Que tal: Lucas e Camila, Paulo e Rafaela, e eu coordeno e ajudo onde precisar?"

            lucas "Por que eu com a Camila?"

            pov "Porque você domina a matéria e ela está aprendendo. Vocês vão se complementar."

            camila "Eu... eu vou me esforçar muito!"

            lucas "Está bem. Vamos trabalhar juntos, Camila."

            $ dupla_isabela = "coordenacao"
            $ aumentar_relacao("lucas", 1)
            $ aumentar_relacao("camila", 2)

    jump roteiro1_d

    # ===================
    # CENA C4 - "VOTAÇÃO"
    # ===================

label roteiro1_c4:

    scene bg library with fade

    "18h30 - Biblioteca"

    pov "Vamos votar. Quem prefere trabalhar individualmente?"

    "Lucas levanta a mão."

    pov "Quem prefere trabalhar em grupo?"

    "Camila, Rafaela e Paulo levantam a mão."

    pov "Maioria venceu. Vamos trabalhar juntos."

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas worried at center

    lucas "Eu discordo, mas vou respeitar a decisão."

    "Lucas está visivelmente frustrado."

    $ aumentar_relacao("lucas", -1)

    jump roteiro1_c2

    # ===================
    # CENA D - "O CONFLITO"
    # ===================

label roteiro1_d:

    scene black with fade

    show text "{size=24}Uma semana depois...{/size}" at truecenter
    pause 1.0
    hide text

    scene bg library with fade

    "Reunião de acompanhamento do projeto."

    "A tensão no ar é palpável."

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas worried at center

    lucas "Camila, você não fez sua parte corretamente. Os dados estão todos errados."

    camila "Eu... eu tentei. Eu pesquisei, mas..."

    lucas "Tentar não basta. Agora eu vou ter que refazer tudo."

    "A voz de Lucas está carregada de frustração."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila sad at right

    camila "Eu não sou burra, Lucas! Eu só preciso de mais tempo!"

    lucas "Tempo é exatamente o que não temos. A apresentação é semana que vem!"

    "Camila está segurando as lágrimas."

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo worried at Position(xalign=0.5, yalign=1.0)

    paulo "Gente, calma..."

    hide paulo

    "Os outros olham para você, esperando que você faça algo."

    menu roteiro1_d_escolha:
        "Como você intervém?"

        "Defender Camila e confrontar Lucas":
            $ aumentar_relacao("camila", 3)
            $ aumentar_relacao("lucas", -2)
            $ aumentar_skill("empatia", 2)
            jump roteiro1_e1

        "Apoiar Lucas e cobrar mais de Camila":
            $ aumentar_relacao("lucas", 2)
            $ aumentar_relacao("camila", -3)
            $ aumentar_skill("lideranca", -1)
            jump roteiro1_e2

        "Mediar o conflito com neutralidade":
            $ aumentar_skill("gestao_conflitos", 3)
            $ aumentar_skill("lideranca", 2)
            $ aumentar_relacao("lucas", 1)
            $ aumentar_relacao("camila", 1)
            jump roteiro1_e3

        "Propor uma solução prática imediata":
            $ aumentar_skill("resolucao_problemas", 2)
            $ aumentar_skill("trabalho_equipe", 2)
            jump roteiro1_e4

    # ===================
    # CENA E1 - "DEFENDER CAMILA"
    # ===================

label roteiro1_e1:

    hide lucas
    hide camila
    with dissolve

    pov "Lucas, você está sendo muito duro. Camila está se esforçando."

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas worried at center

    lucas "Esforço sem resultado não adianta, Isabela."

    pov "Ela precisa de suporte, não de crítica. Nós somos um time."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila happy at right

    camila "Obrigada, Isabela..."

    lucas "Vocês podem ficar com pena dela. Eu vou refazer a parte sozinho."

    "Lucas pega seus materiais e sai."

    hide lucas with dissolve

    "Camila está chorando baixinho."

    pov "Ei, não se culpe. Vamos trabalhar nisso juntas, ok?"

    $ aumentar_skill("empatia", 1)

    jump roteiro1_f

    # ===================
    # CENA E2 - "APOIAR LUCAS"
    # ===================

label roteiro1_e2:

    hide lucas
    hide camila
    with dissolve

    pov "Lucas tem razão, Camila. Você precisa se esforçar mais."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila sad at right

    camila "Eu... eu me esforcei..."

    "Lágrimas começam a escorrer pelo rosto dela."

    camila "Vocês... vocês não entendem como é difícil pra mim..."

    "Camila pega suas coisas e sai correndo."

    hide camila with dissolve

    lucas "Foi duro, mas necessário."

    pov "Será?"

    "Você sente um aperto no peito."

    jump roteiro1_f

    # ===================
    # CENA E3 - "MEDIAR COM NEUTRALIDADE"
    # ===================

label roteiro1_e3:

    hide lucas
    hide camila
    hide paulo
    with dissolve

    pov "Ok, vamos respirar. Gritar não vai resolver nada."

    "Você se posiciona entre os dois."

    pov "Lucas, entendo sua frustração. O prazo está apertado e a qualidade importa."

    lucas "Exatamente."

    pov "Mas Camila também está tentando. Atacar não ajuda ninguém."

    "Você se vira para Camila."

    pov "Camila, você pode me mostrar exatamente onde está com dificuldade?"

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila neutral at Position(xalign=0.7, yalign=1.0)

    camila "Eu... eu não entendi como calcular as emissões de carbono."

    lucas "É só usar a fórmula do slide 15 da aula 3."

    camila "Qual fórmula? Eu não achei isso nas minhas anotações..."

    "Lucas suspira e senta ao lado dela."

    lucas "Me deixa ver suas anotações."

    "Você observa enquanto Lucas, com mais paciência do que antes, explica para Camila."

    "Aos poucos, ela começa a entender."

    camila "Ah! Agora faz sentido!"

    lucas "Viu? Você só precisava entender a lógica."

    "O clima melhora consideravelmente."

    pov "Agora sim. É assim que um time funciona."

    $ unlock_achievement("mediador_nato")
    $ aumentar_skill("gestao_conflitos", 1)

    jump roteiro1_f

    # ===================
    # CENA E4 - "SOLUÇÃO PRÁTICA"
    # ===================

label roteiro1_e4:

    hide lucas
    hide camila
    with dissolve

    pov "Ok, vamos focar na solução. Temos uma semana."

    pov "Lucas, você pode revisar a parte da Camila e marcar o que precisa ser corrigido?"

    pov "Camila, você pode fazer as correções com a ajuda do Lucas?"

    pov "E eu coordeno as outras partes e ajudo onde precisar."

    lucas "Isso parece razoável."

    camila "Eu... eu posso fazer isso."

    pov "Ótimo. Vamos dividir o trabalho agora e marcar reuniões diárias até a apresentação."

    "O grupo se reorganiza com um plano de ação claro."

    rafaela "Gostei! Isabela tá mandando bem como líder!"

    $ aumentar_skill("lideranca", 1)
    $ aumentar_skill("resolucao_problemas", 1)

    jump roteiro1_f

    # ===================
    # CENA F - "A SEMANA FINAL"
    # ===================

label roteiro1_f:

    scene black with fade

    show text "{size=24}Nos dias seguintes...{/size}" at truecenter
    pause 1.0
    hide text

    scene bg library with fade

    "O grupo trabalha intensamente."

    "Reuniões diárias. Noites de estudo. Mensagens constantes no grupo."

    "Aos poucos, o projeto toma forma."

    if lucas_rel >= 3 and camila_rel >= 3:
        "Lucas e Camila começam a se entender melhor."
        hide isabela
        hide camila
        hide paulo
        hide rafaela
        hide professor
        show lucas neutral at center
        lucas "Camila, seu desenho dos espaços verdes ficou muito bom."
        hide lucas
        hide isabela
        hide paulo
        hide rafaela
        hide professor
        show camila happy at center
        camila "Sério? Obrigada, Lucas!"
        hide camila
        "Você sorri, vendo a dinâmica mudar."

    elif lucas_rel < 2:
        "Lucas continua distante, trabalhando principalmente sozinho."
        "O grupo funciona, mas sem muita sinergia."

    elif camila_rel < 2:
        "Camila continua insegura e contribui minimamente."
        "Você sente que poderia ter feito mais por ela."

    jump roteiro1_g

    # ===================
    # CENA G - "A APRESENTAÇÃO"
    # ===================

label roteiro1_g:

    scene bg classroom with fade

    "Dia da apresentação - 14h00"

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide rafaela
    show professor neutral at center

    professor "Grupo 3, vocês estão prontos?"

    hide professor

    "O grupo vai à frente."

    "A apresentação começa."

    "Cada um fala sobre sua parte."

    if trabalho_equipe >= 4 and gestao_conflitos >= 2:
        "A apresentação flui perfeitamente. Todos complementam uns aos outros."
        "As perguntas dos professores são respondidas com segurança."
        $ apresentacao_resultado = "excelente"

    elif trabalho_equipe >= 2:
        "A apresentação é boa, mas há alguns momentos de hesitação."
        $ apresentacao_resultado = "bom"

    else:
        "A apresentação é funcional, mas falta conexão entre as partes."
        $ apresentacao_resultado = "satisfatorio"

    scene black with fade

    "30 minutos depois..."

    # Escolher final baseado em resultado
    if apresentacao_resultado == "excelente":
        jump roteiro1_final_a
    elif apresentacao_resultado == "bom":
        jump roteiro1_final_b
    else:
        jump roteiro1_final_c

    # ===================
    # FINAIS DO ROTEIRO 1
    # ===================

label roteiro1_final_a:
    # Final Excelente - Time Perfeito

    scene bg classroom with fade

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide rafaela
    show professor neutral at center

    professor "Excelente trabalho, grupo 3. Nota: 9,5."

    professor "Vocês demonstraram não apenas conhecimento técnico, mas também excelente trabalho em equipe."

    hide professor

    "O grupo comemora."

    lucas "Isabela, obrigado por ter mediado nossos conflitos. Sem você, não teríamos conseguido."

    camila "É verdade! Você foi uma líder incrível!"

    rafaela "Bora comemorar! Pizza por conta do Paulo!"

    paulo "Opa, espera aí!"

    "Todos riem."

    $ unlock_achievement("trabalho_perfeito")
    $ unlock_achievement("lider_nato")

    narrator "Você aprendeu que um bom líder não é quem manda,"
    narrator "mas quem escuta, medeia e traz o melhor de cada pessoa."

    jump roteiro1_epilogo

label roteiro1_final_b:
    # Final Bom - Trabalho Sólido

    scene bg classroom with fade

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide rafaela
    show professor neutral at center

    professor "Bom trabalho, grupo 3. Nota: 8,5."

    professor "O conteúdo técnico está sólido, mas percebi algumas falhas de integração."

    hide professor

    pov "8,5 não é ruim!"

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas neutral at center

    lucas "Poderia ter sido melhor se tivéssemos nos organizado desde o início."

    camila "Mas a gente conseguiu! Eu aprendi muito!"

    "Você sente que fez um bom trabalho, mas há espaço para melhorar."

    $ unlock_achievement("trabalho_excelente")

    narrator "Nem todo trabalho em grupo é perfeito,"
    narrator "mas o importante é que todos cresçam juntos."

    jump roteiro1_epilogo

label roteiro1_final_c:
    # Final Satisfatório - Aprendizado

    scene bg classroom with fade

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide rafaela
    show professor neutral at center

    professor "Nota: 7,5. O trabalho está correto tecnicamente, mas faltou coesão."

    hide professor

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas worried at center

    lucas "Eu sabia que devíamos ter trabalhado de forma diferente."

    hide lucas
    hide isabela
    hide paulo
    hide rafaela
    hide professor
    show camila sad at center

    camila "Desculpa... foi culpa minha..."

    pov "Não foi culpa de ninguém. Aprendemos muito com esse processo."

    "Você sente que poderia ter gerenciado melhor os conflitos."

    narrator "Às vezes, o aprendizado vem mais dos erros do que dos acertos."
    narrator "Você descobriu que gestão de conflitos é uma habilidade essencial."

    $ aumentar_skill("resiliencia", 2)

    jump roteiro1_epilogo

    # ===================
    # EPÍLOGO DO ROTEIRO 1
    # ===================

label roteiro1_epilogo:

    scene black with fade

    show text "{size=32}ROTEIRO 1 COMPLETO{/size}\n\n{size=20}O Trabalho em Grupo{/size}" at truecenter
    pause
    hide text

    call screen epilogue_stats

    $ roteiro1_completo = True

    jump roteiro2

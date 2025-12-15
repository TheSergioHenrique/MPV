# ================================================
# MOMENTOS PARA VIDA - Side Stories
# Interações Opcionais para conhecer os personagens
# ================================================

# ==========================================
# SIDE STORY 1: ☕ "Café com Lucas"
# ==========================================

label side_lucas:

    if side_lucas_done:
        "Você já teve essa conversa com Lucas."
        return

    # Play cafeteria music
    play music cafeteria fadein 1.5

    scene bg cafeteria with fade

    "Cafeteria do Campus - 16h30 - Fim de tarde"

    "Você encontra Lucas sentado sozinho em uma mesa de canto, com um livro de Física Quântica aberto e uma xícara de café preto fumegando."

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas thinking at center

    "Ele não percebe sua aproximação. Está sublinhando frases com intensidade."

    pov "Posso sentar?"

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas neutral

    lucas "Ah... sim. Claro."

    hide lucas
    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas neutral at right
    with move

    "Você senta. Ele fecha o livro."

    lucas "Você precisa de alguma coisa?"

    pov "Não, só... vi você aqui sozinho."

    "Pausa desconfortável."

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas sad

    "Lucas suspira."

    lucas "Olha... eu sei que às vezes eu sou... difícil. No grupo."

    "Você fica em silêncio, deixando-o falar."

    lucas "Meu pai é engenheiro. Minha mãe é médica. Meu irmão mais velho se formou com honras. Eu sou... o próximo da fila."

    "Ele mexe o café distraidamente."

    lucas "Se eu não for o melhor, eu sou... nada. Entende? Não é sobre ser arrogante. É sobre... sobreviver às expectativas."

    "Você vê, pela primeira vez, a vulnerabilidade por trás da competitividade."

    lucas "Por isso eu pressiono. Por isso eu exijo. Porque se eu relaxar um segundo... eu afundo."

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas worried

    "Ele ri sem humor."

    lucas "Mas eu sei que isso afasta as pessoas. Inclusive vocês."

    "Momento de silêncio compartilhado."

    pov "Você não precisa ser perfeito pra gente gostar de você, Lucas."

    hide isabela
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show lucas neutral

    "Ele te olha, como se essa frase fosse em língua estrangeira."

    lucas "Eu não sei ser de outro jeito."

    narrator "Às vezes, a maior força de alguém é também sua maior fraqueza."
    narrator "Você entendeu Lucas hoje."

    $ unlock_achievement("compreensao_lucas")
    $ aumentar_relacao("lucas", 2)
    $ side_lucas_done = True

    scene black with fade

    "FIM - Café com Lucas"

    return

# ==========================================
# SIDE STORY 2: 🎨 "Arte com Camila"
# ==========================================

label side_camila:

    if side_camila_done:
        "Você já teve essa conversa com Camila."
        return

    # Play campus/outdoor music
    play music campus fadein 1.5

    scene bg courtyard with fade

    "Pátio do Campus - Tarde ensolarada"

    "Você vê Camila sentada debaixo de uma árvore, desenhando algo em um caderno."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila neutral at center

    pov "Oi, Camila! O que você está desenhando?"

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila worried

    "Ela rapidamente fecha o caderno, vermelha."

    camila "Ah! É... é nada. Só uns rabiscos."

    pov "Posso ver?"

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila sad

    camila "Eu... não sei se você vai gostar. Eu desenho mangá."

    pov "Sério? Eu adoro mangá! Por favor, me mostra?"

    "Hesitante, Camila abre o caderno."

    "As páginas revelam desenhos incríveis - personagens, paisagens, quadrinhos completos."

    pov "Camila... isso está INCRÍVEL!"

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila happy

    camila "Você... você acha mesmo?"

    pov "Sério! Você é muito talentosa!"

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila neutral

    camila "Eu uso o desenho pra... pra processar as coisas. Quando fico ansiosa, eu desenho."

    camila "É a única coisa que me acalma de verdade."

    pov "É uma forma linda de se expressar."

    hide isabela
    hide lucas
    hide paulo
    hide rafaela
    hide professor
    show camila happy

    camila "Obrigada... por não achar estranho. Eu nunca mostro pra ninguém."

    narrator "Por trás da timidez, existe um mundo criativo esperando para ser compartilhado."
    narrator "Você descobriu a artista oculta em Camila."

    $ unlock_achievement("artista_oculta")
    $ aumentar_relacao("camila", 3)
    $ side_camila_done = True

    scene black with fade

    "FIM - Arte com Camila"

    return

# ==========================================
# SIDE STORY 3: 🎭 "Teatro com Rafaela"
# ==========================================

label side_rafaela:

    if side_rafaela_done:
        "Você já teve essa conversa com Rafaela."
        return

    # Play side stories music
    play music side_stories fadein 1.5

    scene bg classroom with fade

    "Auditório - Noite"

    "Rafaela te convidou para assistir um ensaio de teatro."

    "O palco está iluminado. Rafaela está no centro, interpretando um monólogo."

    "Você assiste, impressionada. Ela está... diferente. Séria. Intensa. Real."

    scene black

    "Fim do ensaio."

    scene bg classroom

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela neutral at center

    "Rafaela se aproxima, ainda com maquiagem de cena."

    rafaela "E aí? O que achou?"

    pov "Você é incrível, Rafaela! Eu não sabia que você fazia teatro."

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela sad

    rafaela "Eu... eu comecei na terapia, na verdade."

    rafaela "Meu psicólogo sugeriu. Disse que eu escondia muita coisa atrás do humor."

    "Ela senta ao seu lado."

    rafaela "Sabe, todo mundo acha que eu sou essa pessoa super extrovertida e feliz."

    rafaela "Mas às vezes... às vezes eu só quero que levem a sério, sabe?"

    rafaela "As piadas são... uma armadura."

    pov "Eu te levo a sério, Rafaela."

    hide isabela
    hide lucas
    hide camila
    hide paulo
    hide professor
    show rafaela happy

    rafaela "Obrigada. Isso significa muito."

    narrator "Por trás da máscara de alegria, existe uma pessoa complexa e profunda."
    narrator "Você viu a verdadeira Rafaela hoje."

    $ unlock_achievement("por_tras_mascara")
    $ aumentar_relacao("rafaela", 3)
    $ side_rafaela_done = True

    scene black with fade

    "FIM - Teatro com Rafaela"

    return

# ==========================================
# SIDE STORY 4: ⚽ "Fut com Paulo"
# ==========================================

label side_paulo:

    if side_paulo_done:
        "Você já teve essa conversa com Paulo."
        return

    # Play campus/outdoor music
    play music campus fadein 1.5

    scene bg courtyard with fade

    "Quadra de Futsal - Sábado de manhã"

    "Paulo te convidou para jogar futsal com uns amigos."

    "Depois do jogo, vocês sentam na arquibancada, suados e rindo."

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo happy at center

    paulo "Você joga bem! Valeu por vir!"

    pov "Foi divertido! Você é bom mesmo."

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo neutral

    paulo "Meu pai jogou semi-profissional. Eu cresci com bola nos pés."

    "Ele olha para o horizonte."

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo sad

    paulo "Ele queria muito que eu fosse jogador. Mas eu... eu queria fazer engenharia."

    paulo "Sou o primeiro da minha família a entrar na universidade, sabia?"

    pov "Sério?"

    paulo "É. Meus pais não terminaram nem o ensino médio. Eles trabalham muito."

    paulo "Às vezes eu sinto que... que eu não posso falhar, sabe? Tipo, eu TENHO que dar certo."

    paulo "Por eles."

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo worried

    paulo "Por isso eu fico zoando. Pra disfarçar o medo de não ser bom o suficiente academicamente."

    pov "Paulo, você é incrível. E seus pais devem estar muito orgulhosos."

    hide isabela
    hide lucas
    hide camila
    hide rafaela
    hide professor
    show paulo happy

    paulo "Valeu. De verdade."

    narrator "Detrás da descontração, existe o peso de uma responsabilidade familiar."
    narrator "Você entendeu o pioneiro em Paulo."

    $ unlock_achievement("pioneiro_familiar")
    $ aumentar_relacao("paulo", 3)
    $ side_paulo_done = True

    scene black with fade

    "FIM - Fut com Paulo"

    return

# ==========================================
# SIDE STORY 5: 📚 "Biblioteca com Isabela"
# ==========================================

label side_isabela:

    if side_isabela_done:
        "Você já teve essa conversa com Isabela."
        return

    # Play library music
    play music library fadein 1.5

    scene bg library with fade

    "Biblioteca - 22h30 - Véspera de feriado"

    "A biblioteca está quase vazia."

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela thinking at center

    "Isabela está sozinha em uma mesa, cercada de livros."

    pov "Isabela? Você ainda está aqui?"

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela neutral

    isabela "Ah, oi! Sim... estou terminando um projeto pessoal."

    "Você se aproxima e vê plantas de design urbano."

    pov "Isso não é matéria da faculdade, é?"

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela happy

    isabela "Não. É um projeto meu. Estou desenhando um sistema de saneamento sustentável para favelas."

    isabela "Eu cresci em uma. Sei como é não ter acesso a água tratada, esgoto adequado..."

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela sad

    isabela "Por isso eu quero ser engenheira. Não pra ganhar dinheiro. Pra mudar realidades."

    isabela "Pra fazer engenharia social, sabe? De impacto real."

    pov "Isabela... isso é incrível."

    hide lucas
    hide camila
    hide paulo
    hide rafaela
    hide professor
    show isabela happy

    isabela "É meu sonho. Maior que qualquer nota ou diploma."

    narrator "Por trás da organização e ambição, existe um propósito maior."
    narrator "Você descobriu os sonhos de Isabela."

    $ unlock_achievement("sonhos_maiores")
    $ aumentar_relacao("isabela", 3)
    $ side_isabela_done = True

    scene black with fade

    "FIM - Biblioteca com Isabela"

    return

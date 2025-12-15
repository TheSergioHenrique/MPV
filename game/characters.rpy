# ============================================
# MOMENTOS PARA VIDA - Character Definitions
# ============================================

# Character Definitions
# Cores mais vibrantes e distintas para melhor identificação
define isabela = Character("Isabela", color="#BB88FF", image="isabela")  # Roxo claro vibrante
define lucas = Character("Lucas", color="#4DB8FF", image="lucas")  # Azul céu vibrante
define camila = Character("Camila", color="#FF6B6B", image="camila")  # Vermelho coral vibrante
define paulo = Character("Paulo", color="#FFB347", image="paulo")  # Laranja vibrante
define rafaela = Character("Rafaela", color="#FF69B4", image="rafaela")  # Rosa pink vibrante
define professor = Character("Professor", color="#95A5A6", image="professor")  # Cinza claro
# Narrator using ADV style with empty string for portrait-mode compatibility
define narrator = Character("")
define pov = DynamicCharacter("povname", color="#2ECC71")  # Verde (jogador)

# ============================================
# CHARACTER POSITIONS - Evita sobreposição
# ============================================
# Para 2 personagens
transform pos_2_left:
    xalign 0.25
    yalign 1.0

transform pos_2_right:
    xalign 0.75
    yalign 1.0

# Para 3 personagens
transform pos_3_left:
    xalign 0.15
    yalign 1.0

transform pos_3_center:
    xalign 0.5
    yalign 1.0

transform pos_3_right:
    xalign 0.85
    yalign 1.0

# Para 4 personagens
transform pos_4_farleft:
    xalign 0.1
    yalign 1.0

transform pos_4_left:
    xalign 0.35
    yalign 1.0

transform pos_4_right:
    xalign 0.65
    yalign 1.0

transform pos_4_farright:
    xalign 0.9
    yalign 1.0

# Para 5 personagens
transform pos_5_farleft:
    xalign 0.05
    yalign 1.0

transform pos_5_left:
    xalign 0.27
    yalign 1.0

transform pos_5_center:
    xalign 0.5
    yalign 1.0

transform pos_5_right:
    xalign 0.73
    yalign 1.0

transform pos_5_farright:
    xalign 0.95
    yalign 1.0

# Character Image Definitions
# ISABELA - Organizada, prestativa, ambiciosa
image isabela neutral = "characters/isabela_neutral.png"
image isabela happy = "characters/isabela_happy.png"
image isabela sad = "characters/isabela_sad.png"
image isabela worried = "characters/isabela_worried.png"
image isabela thinking = "characters/isabela_thinking.png"

# LUCAS - Competitivo, inteligente, impaciente
image lucas neutral = "characters/lucas_neutral.png"
image lucas happy = "characters/lucas_happy.png"
image lucas sad = "characters/lucas_sad.png"
image lucas worried = "characters/lucas_worried.png"
image lucas thinking = "characters/lucas_thinking.png"

# CAMILA - Tímida, reflexiva, insegura
image camila neutral = "characters/camila_neutral.png"
image camila happy = "characters/camila_happy.png"
image camila sad = "characters/camila_sad.png"
image camila worried = "characters/camila_worried.png"
image camila thinking = "characters/camila_thinking.png"

# PAULO - Desorganizado, bem-humorado, inseguro academicamente
image paulo neutral = "characters/paulo_neutral.png"
image paulo happy = "characters/paulo_happy.png"
image paulo sad = "characters/paulo_sad.png"
image paulo worried = "characters/paulo_worried.png"
image paulo thinking = "characters/paulo_thinking.png"

# RAFAELA - Extrovertida, emocional, dramática
image rafaela neutral = "characters/rafaela_neutral.png"
image rafaela happy = "characters/rafaela_happy.png"
image rafaela sad = "characters/rafaela_sad.png"
image rafaela worried = "characters/rafaela_worried.png"
image rafaela thinking = "characters/rafaela_thinking.png"

# PROFESSOR - Professor da turma
image professor neutral = "characters/Professor_Z.png"

# Background Definitions - Scaled to cover full screen
image bg campus = Transform("backgrounds/bg_campus.png", fit="cover")
image bg classroom = Transform("backgrounds/bg_classroom.jpg", fit="cover")
image bg ru = Transform("backgrounds/bg_ru.png", fit="cover")
image bg library = Transform("backgrounds/bg_library.png", fit="cover")
image bg cafeteria = Transform("backgrounds/bg_cafeteria.jpg", fit="cover")
image bg courtyard = Transform("backgrounds/bg_courtyard.png", fit="cover")
image bg corridor = Transform("backgrounds/bg_corridor.png", fit="cover")

# Special backgrounds
image bg_start = "#fef7e6"  # Tela de início - bege claro
image bg whatsapp = Transform("backgrounds/bg_whatsapp.png", fit="cover")  # WhatsApp

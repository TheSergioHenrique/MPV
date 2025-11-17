# ============================================
# MOMENTOS PARA VIDA - Character Definitions
# ============================================

# Character Definitions
define isabela = Character("Isabela", color="#9B59B6", image="isabela")
define lucas = Character("Lucas", color="#3498DB", image="lucas")
define camila = Character("Camila", color="#E74C3C", image="camila")
define paulo = Character("Paulo", color="#F39C12", image="paulo")
define rafaela = Character("Rafaela", color="#E91E63", image="rafaela")
define professor = Character("Professor", color="#7F8C8D")
# Narrator using ADV style with empty string for portrait-mode compatibility
define narrator = Character("")
define pov = DynamicCharacter("povname", color="#2ECC71")

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
image isabela neutral = Transform("characters/isabela_neutral.png", zoom=5.0)
image isabela happy = Transform("characters/isabela_happy.png", zoom=5.0)
image isabela sad = Transform("characters/isabela_sad.png", zoom=5.0)
image isabela worried = Transform("characters/isabela_worried.png", zoom=5.0)
image isabela thinking = Transform("characters/isabela_thinking.png", zoom=5.0)

# LUCAS - Competitivo, inteligente, impaciente
image lucas neutral = Transform("characters/lucas_neutral.png", zoom=5.0)
image lucas happy = Transform("characters/lucas_happy.png", zoom=5.0)
image lucas sad = Transform("characters/lucas_sad.png", zoom=5.0)
image lucas worried = Transform("characters/lucas_worried.png", zoom=5.0)
image lucas thinking = Transform("characters/lucas_thinking.png", zoom=5.0)

# CAMILA - Tímida, reflexiva, insegura
image camila neutral = Transform("characters/camila_neutral.png", zoom=5.0)
image camila happy = Transform("characters/camila_happy.png", zoom=5.0)
image camila sad = Transform("characters/camila_sad.png", zoom=5.0)
image camila worried = Transform("characters/camila_worried.png", zoom=5.0)
image camila thinking = Transform("characters/camila_thinking.png", zoom=5.0)

# PAULO - Desorganizado, bem-humorado, inseguro academicamente
image paulo neutral = Transform("characters/paulo_neutral.png", zoom=5.0)
image paulo happy = Transform("characters/paulo_happy.png", zoom=5.0)
image paulo sad = Transform("characters/paulo_sad.png", zoom=5.0)
image paulo worried = Transform("characters/paulo_worried.png", zoom=5.0)
image paulo thinking = Transform("characters/paulo_thinking.png", zoom=5.0)

# RAFAELA - Extrovertida, emocional, dramática
image rafaela neutral = Transform("characters/rafaela_neutral.png", zoom=5.0)
image rafaela happy = Transform("characters/rafaela_happy.png", zoom=5.0)
image rafaela sad = Transform("characters/rafaela_sad.png", zoom=5.0)
image rafaela worried = Transform("characters/rafaela_worried.png", zoom=5.0)
image rafaela thinking = Transform("characters/rafaela_thinking.png", zoom=5.0)

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
image bg whatsapp = "#128C7E"  # WhatsApp - verde característico

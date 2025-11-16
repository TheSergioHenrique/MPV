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

# Background Definitions
image bg campus = "backgrounds/bg_campus.jpg"
image bg classroom = "backgrounds/bg_classroom.jpg"
image bg ru = "backgrounds/bg_ru.jpg"
image bg library = "backgrounds/bg_library.jpg"
image bg cafeteria = "backgrounds/bg_cafeteria.jpg"
image bg courtyard = "backgrounds/bg_courtyard.jpg"
image bg corridor = "backgrounds/bg_corridor.jpg"

# WhatsApp background (placeholder - cor verde característica)
image bg whatsapp = "#128C7E"

# ================================================
# MOMENTOS PARA VIDA - Variables and Game State
# ================================================

# Player Name
default povname = "Você"

# ==========================================
# RELATIONSHIP VARIABLES (0-5 hearts scale)
# ==========================================
# 0 = Inexistente
# 1 = Conhecidos
# 2 = Colega
# 3 = Amigo
# 4 = Amigo próximo
# 5 = Melhor amigo / Confiança máxima

default isabela_rel = 3
default lucas_rel = 2
default camila_rel = 3
default paulo_rel = 2
default rafaela_rel = 2

# ==========================================
# SOFT SKILLS VARIABLES (0-5 scale)
# ==========================================
default comunicacao = 0
default empatia = 0
default lideranca = 0
default gestao_conflitos = 0
default trabalho_equipe = 0
default adaptabilidade = 0
default proatividade = 0
default resolucao_problemas = 0
default criatividade = 0
default inteligencia_emocional = 0
default autoconhecimento = 0
default gestao_tempo = 0
default pensamento_critico = 0
default resiliencia = 0
default aprendizado_continuo = 0
default negociacao = 0
default autocuidado = 0

# ==========================================
# ACHIEVEMENT/CONQUISTA FLAGS
# ==========================================
default achievements = {
    "primeira_amizade": False,
    "coracao_grupo": False,
    "mediador_natural": False,
    "mediador_nato": False,
    "estudante_dedicado": False,
    "mestre_tempo": False,
    "lider_nato": False,
    "compreensao_lucas": False,
    "artista_oculta": False,
    "por_tras_mascara": False,
    "pioneiro_familiar": False,
    "sonhos_maiores": False,
    "equipe_unida": False,
    "trabalho_excelente": False,
    "trabalho_perfeito": False,
    "nota_maxima": False,
    "final_perfeito": False,
    "equilibrio_perfeito": False,
    "resistencia_mental": False,
    "sabedoria": False,
    "amigo_verdadeiro": False
}

# ==========================================
# PERSONALITY/TRAIT TRACKERS
# ==========================================
default social_score = 0
default cautelosa_score = 0
default independente_score = 0
default isolamento_score = 0
default descontracao_score = 0
default profissionalismo_score = 0
default observacao_score = 0

# ==========================================
# STORY FLAGS
# ==========================================
default prologo_completo = False
default roteiro1_completo = False
default roteiro2_completo = False
default roteiro3_completo = False

# Side Stories completed
default side_lucas_done = False
default side_camila_done = False
default side_rafaela_done = False
default side_paulo_done = False
default side_isabela_done = False

# Micro-moments seen
default micro1_seen = False
default micro2_seen = False
default micro3_seen = False
default micro4_seen = False
default micro5_seen = False
default micro6_seen = False

# ==========================================
# HELPER FUNCTIONS
# ==========================================

init python:
    def aumentar_relacao(personagem, valor):
        """Aumenta a relação com um personagem (máximo 5)"""
        global isabela_rel, lucas_rel, camila_rel, paulo_rel, rafaela_rel

        if personagem == "isabela":
            isabela_rel = min(5, isabela_rel + valor)
            return isabela_rel
        elif personagem == "lucas":
            lucas_rel = min(5, lucas_rel + valor)
            return lucas_rel
        elif personagem == "camila":
            camila_rel = min(5, camila_rel + valor)
            return camila_rel
        elif personagem == "paulo":
            paulo_rel = min(5, paulo_rel + valor)
            return paulo_rel
        elif personagem == "rafaela":
            rafaela_rel = min(5, rafaela_rel + valor)
            return rafaela_rel

    def aumentar_skill(skill, valor):
        """Aumenta uma soft skill (máximo 5)"""
        if skill == "comunicacao":
            store.comunicacao = min(5, store.comunicacao + valor)
        elif skill == "empatia":
            store.empatia = min(5, store.empatia + valor)
        elif skill == "lideranca":
            store.lideranca = min(5, store.lideranca + valor)
        elif skill == "gestao_conflitos":
            store.gestao_conflitos = min(5, store.gestao_conflitos + valor)
        elif skill == "trabalho_equipe":
            store.trabalho_equipe = min(5, store.trabalho_equipe + valor)
        elif skill == "gestao_tempo":
            store.gestao_tempo = min(5, store.gestao_tempo + valor)
        elif skill == "pensamento_critico":
            store.pensamento_critico = min(5, store.pensamento_critico + valor)
        elif skill == "resiliencia":
            store.resiliencia = min(5, store.resiliencia + valor)
        elif skill == "autocuidado":
            store.autocuidado = min(5, store.autocuidado + valor)
        elif skill == "criatividade":
            store.criatividade = min(5, store.criatividade + valor)

    def get_relation_level(personagem):
        """Retorna o nível de relacionamento com descrição"""
        if personagem == "isabela":
            rel = isabela_rel
        elif personagem == "lucas":
            rel = lucas_rel
        elif personagem == "camila":
            rel = camila_rel
        elif personagem == "paulo":
            rel = paulo_rel
        elif personagem == "rafaela":
            rel = rafaela_rel
        else:
            return "Desconhecido"

        if rel == 0:
            return "Relação inexistente"
        elif rel == 1:
            return "Conhecidos"
        elif rel == 2:
            return "Colega"
        elif rel == 3:
            return "Amigo"
        elif rel == 4:
            return "Amigo próximo"
        elif rel == 5:
            return "Melhor amigo"

    def unlock_achievement(ach_name):
        """Desbloqueia uma conquista"""
        if not achievements[ach_name]:
            achievements[ach_name] = True
            renpy.show_screen("achievement_popup", ach_name)

    def get_skill_description(skill_name, level):
        """Retorna descrição do nível de habilidade"""
        if level == 0:
            return "Não praticado"
        elif level == 1:
            return "Iniciante"
        elif level == 2:
            return "Básico"
        elif level == 3:
            return "Intermediário"
        elif level == 4:
            return "Avançado"
        elif level == 5:
            return "Mestre"

# Achievement Names
define achievement_names = {
    "primeira_amizade": "Primeira Amizade",
    "coracao_grupo": "Coração do Grupo",
    "mediador_natural": "Mediador Natural",
    "mediador_nato": "Mediador Nato",
    "estudante_dedicado": "Estudante Dedicado",
    "mestre_tempo": "Mestre do Tempo",
    "lider_nato": "Líder Nato",
    "compreensao_lucas": "Compreensão Profunda - Lucas",
    "artista_oculta": "Artista Oculta - Camila",
    "por_tras_mascara": "Por Trás da Máscara - Rafaela",
    "pioneiro_familiar": "Pioneiro Familiar - Paulo",
    "sonhos_maiores": "Sonhos Maiores - Isabela",
    "equipe_unida": "Equipe Unida",
    "trabalho_excelente": "Trabalho Excelente",
    "trabalho_perfeito": "Trabalho Perfeito",
    "nota_maxima": "Nota Máxima",
    "final_perfeito": "Final Perfeito",
    "equilibrio_perfeito": "Equilíbrio Perfeito",
    "resistencia_mental": "Resistência Mental",
    "sabedoria": "Sabedoria",
    "amigo_verdadeiro": "Amigo Verdadeiro"
}

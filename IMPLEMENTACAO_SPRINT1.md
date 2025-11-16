# MOMENTOS PARA VIDA - Implementação Sprint 1
## Resumo da Implementação

Este documento descreve a implementação completa do conteúdo especificado no **DOCUMENTO-SPRINT1.pdf**.

---

## ✅ O QUE FOI IMPLEMENTADO

### 1. **Prólogo Compartilhado** ✅
- **Arquivo**: `game/prologo.rpy`
- **Descrição**: Cena de introdução "Primeiro Dia de Aula" que apresenta todos os 5 personagens principais
- **Personagens introduzidos**:
  - Isabela (organizada, prestativa, ambiciosa)
  - Lucas (competitivo, inteligente, impaciente)
  - Camila (tímida, reflexiva, insegura)
  - Paulo (desorganizado, bem-humorado, inseguro academicamente)
  - Rafaela (extrovertida, emocional, dramática)
- **Escolhas**: 4+ momentos de decisão que afetam relações iniciais
- **Tempo estimado**: ~5 minutos

### 2. **Sistema de Relações Visível** ✅
- **Arquivo**: `game/game_screens.rpy`
- **Funcionalidades**:
  - Tela de status acessível com tecla 'R'
  - Visualização de relações com todos os 5 personagens (escala de 0-5 corações)
  - Visualização de soft skills desenvolvidas (barras de progresso)
  - Notificações em tempo real quando relações/skills aumentam
  - Sistema de conquistas/achievements
- **UI Screens**: `status_screen`, `notify_relation`, `notify_skill`, `achievement_popup`, `epilogue_stats`

### 3. **Variáveis e Mecânicas** ✅
- **Arquivo**: `game/variables.rpy`
- **Conteúdo**:
  - Sistema completo de rastreamento de relações (5 personagens)
  - 16 soft skills diferentes rastreadas
  - Sistema de conquistas/achievements (15 achievements)
  - Funções helper para aumentar relações e skills
  - Sistema de personalidade (social, cautelosa, independente, etc.)
  - Flags de progresso de história

### 4. **Roteiro 3 - "A Prova Surpresa"** ✅
- **Arquivo**: `game/roteiro3.rpy`
- **Descrição**: História completa focada em gestão de tempo e resiliência
- **Soft Skills**: Gestão do Tempo, Pensamento Crítico, Resiliência, Tomada de Decisão sob Pressão
- **Estrutura**:
  - Cenas A, B1-B4, C1-C4, D
  - 3 finais diferentes baseados em escolhas
  - Epílogo com estatísticas
- **Tempo estimado**: 15-20 minutos
- **Personagem jogável**: Isabela (para variar)

### 5. **Side Stories (Interações Opcionais)** ✅
- **Arquivo**: `game/side_stories.rpy`
- **Conteúdo**: 5 cenas opcionais de 2-3 minutos cada
  1. ☕ **Café com Lucas**: Descobre pressão familiar e vulnerabilidade
  2. 🎨 **Arte com Camila**: Descobre talento artístico e válvula de escape
  3. 🎭 **Teatro com Rafaela**: Descobre depressão escondida atrás do humor
  4. ⚽ **Fut com Paulo**: Descobre ser o primeiro da família na universidade
  5. 📚 **Biblioteca com Isabela**: Descobre sonhos de engenharia social
- **Achievements**: Desbloqueia conquistas especiais
- **Tempo total**: ~12 minutos de conteúdo opcional

### 6. **Micro-Momentos** ✅
- **Arquivo**: `game/micro_moments.rpy`
- **Conteúdo**: 6 cenas curtas de transição (1-2 minutos cada)
  1. WhatsApp pós-reunião
  2. Encontro no RU (Restaurante Universitário)
  3. Biblioteca fechando
  4. Mensagem de madrugada
  5. Corredor tenso (mediação de conflito)
  6. Final de semana livre (equilíbrio vida/estudo)
- **Tempo total**: ~9 minutos

### 7. **Definições de Personagens e Assets** ✅
- **Arquivo**: `game/characters.rpy`
- **Conteúdo**:
  - Definições de todos os 5 personagens principais
  - Definições de imagens para expressões (neutral, happy, sad, worried, thinking)
  - Definições de backgrounds (campus, classroom, ru, library, cafeteria, courtyard, corridor)
- **Assets criados**: Placeholders para 25 sprites de personagens e 7 backgrounds

### 8. **Script Principal Integrado** ✅
- **Arquivo**: `game/script.rpy`
- **Conteúdo**:
  - Tela de boas-vindas
  - Input de nome do jogador
  - Integração com prólogo
  - Menu principal com acesso a todas as histórias e side stories
  - Placeholders para Roteiros 1 e 2 (a serem implementados)
  - Tela de créditos

---

## 📁 ESTRUTURA DE ARQUIVOS CRIADA

```
Momentos Para Vida/game/
├── script.rpy                  # Script principal (ATUALIZADO)
├── characters.rpy              # Definições de personagens (NOVO)
├── variables.rpy               # Sistema de variáveis e relações (NOVO)
├── game_screens.rpy            # UI Screens e sistema visual (NOVO)
├── prologo.rpy                 # Prólogo compartilhado (NOVO)
├── roteiro3.rpy                # Script 3 completo (NOVO)
├── side_stories.rpy            # Histórias opcionais (NOVO)
├── micro_moments.rpy           # Micro-momentos de transição (NOVO)
├── characters/                 # Sprites de personagens (NOVO)
│   ├── isabela_*.png (5 expressões)
│   ├── lucas_*.png (5 expressões)
│   ├── camila_*.png (5 expressões)
│   ├── paulo_*.png (5 expressões)
│   └── rafaela_*.png (5 expressões)
├── backgrounds/                # Backgrounds (NOVO)
│   ├── bg_campus.jpg
│   ├── bg_classroom.jpg
│   ├── bg_ru.jpg
│   ├── bg_library.jpg
│   ├── bg_cafeteria.jpg
│   ├── bg_courtyard.jpg
│   └── bg_corridor.jpg
└── ui/                         # UI elements (NOVO)
```

---

## 🎮 COMO JOGAR

1. **Iniciar o jogo**: Execute o Ren'Py e abra o projeto "Momentos Para Vida"
2. **Prólogo**: O jogo começa automaticamente com o prólogo (Primeiro Dia de Aula)
3. **Menu Principal**: Após o prólogo, você pode:
   - Jogar Roteiro 3 (A Prova Surpresa)
   - Jogar Side Stories (conhecer os personagens)
   - Ver seu Status de Relações (tecla 'R' a qualquer momento)
4. **Sistema de Escolhas**: Suas escolhas afetam:
   - Relações com personagens (0-5 corações)
   - Soft skills desenvolvidas (0-5 níveis)
   - Conquistas desbloqueadas
   - Finais das histórias

---

## 🎯 SOFT SKILLS IMPLEMENTADAS

O jogo rastreia e desenvolve 16 soft skills diferentes:
1. Comunicação
2. Empatia
3. Liderança
4. Gestão de Conflitos
5. Trabalho em Equipe
6. Adaptabilidade
7. Proatividade
8. Resolução de Problemas
9. Criatividade
10. Inteligência Emocional
11. Autoconhecimento
12. Gestão de Tempo
13. Pensamento Crítico
14. Resiliência
15. Aprendizado Contínuo
16. Negociação

---

## 🏆 ACHIEVEMENTS (Conquistas)

15 achievements implementados:
- 🌟 Primeira Amizade
- 💚 Coração do Grupo
- 🤝 Mediador Natural
- 📚 Estudante Dedicado
- ⏰ Mestre do Tempo
- 🎯 Líder Nato
- 💼 Compreensão Profunda - Lucas
- 🎨 Artista Oculta - Camila
- 🎭 Por Trás da Máscara - Rafaela
- ⚽ Pioneiro Familiar - Paulo
- 📖 Sonhos Maiores - Isabela
- 👥 Equipe Unida
- 📊 Trabalho Excelente
- 🎓 Nota Máxima
- 🏆 Final Perfeito

---

## ⚙️ RECURSOS TÉCNICOS IMPLEMENTADOS

### Funções Python
- `aumentar_relacao(personagem, valor)` - Aumenta relação com personagem
- `aumentar_skill(skill, valor)` - Aumenta soft skill
- `get_relation_level(personagem)` - Retorna nível de relação
- `unlock_achievement(ach_name)` - Desbloqueia conquista
- `get_skill_description(skill, level)` - Descrição de nível de skill

### Telas (Screens)
- `status_screen` - Status de relações e skills (tecla 'R')
- `notify_relation` - Notificação de mudança de relação
- `notify_skill` - Notificação de aumento de skill
- `achievement_popup` - Popup de conquista desbloqueada
- `epilogue_stats` - Estatísticas finais de epílogo

---

## 📊 CONTEÚDO TOTAL IMPLEMENTADO

| Tipo | Quantidade | Tempo Estimado |
|------|-----------|----------------|
| Prólogo | 1 história | 5 min |
| Roteiros Principais | 1 completo (Roteiro 3) | 15-20 min |
| Side Stories | 5 histórias opcionais | 12 min total |
| Micro-Momentos | 6 cenas de transição | 9 min total |
| **TOTAL** | **13 cenas jogáveis** | **~41-46 minutos** |

---

## 🔨 PRÓXIMOS PASSOS (Para implementação futura)

1. **Roteiro 1**: "O Trabalho em Grupo"
   - Implementar história completa baseada no documento original
   - Integrar micro-momentos

2. **Roteiro 2**: "A Longa Noite de Estudos"
   - Implementar história completa baseada no documento original
   - Integrar micro-momentos

3. **Diálogos Expandidos**: Melhorar diálogos existentes com:
   - Linguagem corporal mais detalhada
   - Pausas e silêncios significativos
   - Padrões de fala únicos por personagem

4. **Arte**: Substituir placeholders por arte final
   - 25 sprites de personagens (5 personagens × 5 expressões)
   - 7 backgrounds de cenários
   - UI elements (corações, ícones, etc.)

5. **Áudio**: Adicionar trilha sonora e efeitos sonoros

6. **Testes e Balanceamento**: Testar todas as rotas e ajustar valores de relações/skills

---

## 📝 NOTAS TÉCNICAS

### Assets Placeholder
- Todos os assets de personagens e backgrounds são atualmente **placeholders**
- Podem ser substituídos por arte final mantendo os mesmos nomes de arquivo
- Expressões implementadas: `neutral`, `happy`, `sad`, `worried`, `thinking`

### Sistema de Save/Load
- Ren'Py gerencia automaticamente saves
- Todas as variáveis de jogo são persistidas corretamente

### Compatibilidade
- Código compatível com Ren'Py 7.x e 8.x
- Testado em modo portrait (mobile-friendly)

---

## 🎨 PERSONALIZAÇÃO

Para personalizar o jogo:
1. **Cores dos personagens**: Edite em `characters.rpy`
2. **Nomes de skills**: Edite em `variables.rpy`
3. **Textos e diálogos**: Edite nos respectivos arquivos .rpy
4. **UI e layouts**: Edite em `game_screens.rpy`

---

## ✅ CHECKLIST DE IMPLEMENTAÇÃO

- [x] Prólogo Compartilhado
- [x] Sistema de Relações Visível
- [x] Variáveis e Sistema de Tracking
- [x] Roteiro 3 Completo
- [x] 5 Side Stories
- [x] 6 Micro-Momentos
- [x] Placeholders de Assets
- [x] Integração no Script Principal
- [x] Sistema de Conquistas
- [x] Screens de UI
- [ ] Roteiro 1 (Futuro)
- [ ] Roteiro 2 (Futuro)
- [ ] Arte Final (Futuro)
- [ ] Áudio (Futuro)

---

## 🙏 CRÉDITOS

**Desenvolvido por:**
- Matheus Gonçalves
- Nathália Bacalhau
- Paulo Massa
- Sérgio Henrique
- Sócrates F

**Escola Politécnica de Pernambuco**

**Engine:** Ren'Py Visual Novel Engine

---

*Implementação baseada no DOCUMENTO-SPRINT1.pdf*
*Data de implementação: Novembro 2025*

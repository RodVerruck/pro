#!/usr/bin/env python3
"""
Deep cleanup - Remove all dead code from Pai, RPG, and Músico modes
"""

import re

def cleanup_deep(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_lines = len(content.splitlines())
    
    # ═══ STEP 1: Remove CSS for dead modes ═══
    
    # Remove entire Modo Pai CSS block (lines ~1846-2478)
    pai_css_pattern = r'/\* =========================================\s+MODO PAI: O CAOS CRIATIVO DA ISIS\s+========================================= \*/\s+body\.pai-mode \{[^}]+\}.*?/\* Esconder toast e hints no modo pai \*/\s+body\.pai-mode #toast,\s+body\.pai-mode #hint-box \{\s+display: none !important;\s+\}'
    content = re.sub(pai_css_pattern, '', content, flags=re.DOTALL)
    
    # Remove hero eyebrow por modo block
    hero_eyebrow_pattern = r'/\* Hero eyebrow por modo \*/\s+body\.pai-mode \.hero-eyebrow,\s+body\.rpg-mode \.hero-eyebrow,\s+body\.musico-mode \.hero-eyebrow \{[^}]+\}.*?body\.musico-mode \.hero-eyebrow::before \{[^}]+\}'
    content = re.sub(hero_eyebrow_pattern, '', content, flags=re.DOTALL)
    
    # Remove contact card por modo
    contact_pattern = r'/\* Contact card por modo \*/\s+body\.pai-mode \.contact-title,\s+body\.rpg-mode \.contact-title,\s+body\.musico-mode \.contact-title \{[^}]+\}.*?body\.musico-mode \.contact-title::before \{[^}]+\}'
    content = re.sub(contact_pattern, '', content, flags=re.DOTALL)
    
    # Remove about card por modo
    about_pattern = r'/\* About card por modo \*/\s+body\.rpg-mode \.about-hello,\s+body\.musico-mode \.about-hello \{[^}]+\}.*?body\.musico-mode \.about-bio::before \{[^}]+\}'
    content = re.sub(about_pattern, '', content, flags=re.DOTALL)
    
    # Remove toast styles for pai mode
    toast_pai_pattern = r'/\* Estilos do Modo Pai para o toast - MAIOR ESPECIFICIDADE \*/\s+body\.pai-mode #toast \{[^}]+\}'
    content = re.sub(toast_pai_pattern, '', content, flags=re.DOTALL)
    
    # Remove hint-box styles
    hint_box_pattern = r'#hint-box \{[^}]+\}\s+#hint-box\.show \{[^}]+\}\s+#hint-box span \{[^}]+\}'
    content = re.sub(hint_box_pattern, '', content, flags=re.DOTALL)
    
    # Remove RPG snow styles
    rpg_snow_pattern = r'/\* Modo RPG - Atmosfera Skyrim \*/\s+#rpg-snow \{[^}]+\}.*?body\.rpg-mode \.proj-title \{[^}]+\}'
    content = re.sub(rpg_snow_pattern, '', content, flags=re.DOTALL)
    
    # Remove tool-pill-pai styles
    tool_pill_pattern = r'/\* Controle de visibilidade das ferramentas \*/\s+\.tool-pill-pai \{[^}]+\}.*?body\.pai-mode \.tool-pill-pai \{[^}]+\}'
    content = re.sub(tool_pill_pattern, '', content, flags=re.DOTALL)
    
    # Remove about-text-pai styles
    about_text_pai_pattern = r'/\* Mostrar/ocultar blocos de texto por modo no card Sobre \*/\s+\.about-text-pai \{[^}]+\}.*?body\.pai-mode \.about-text-pai \.about-bio \{[^}]+\}'
    content = re.sub(about_text_pai_pattern, '', content, flags=re.DOTALL)
    
    # Remove media query hint-box
    media_hint_pattern = r'#hint-box \{\s+display: none;\s+\}'
    content = re.sub(media_hint_pattern, '', content)
    
    # ═══ STEP 2: Remove HTML elements ═══
    
    # Remove rpg-snow div
    content = re.sub(r'\s*<div id="rpg-snow"></div>', '', content)
    
    # Remove portal-flash div
    content = re.sub(r'\s*<div id="portal-flash"></div>', '', content)
    
    # Remove toast div
    content = re.sub(r'\s*<div id="toast"></div>', '', content)
    
    # Remove hint-box div
    content = re.sub(r'\s*<div id="hint-box"></div>', '', content)
    
    # Remove about-text-pai block
    about_text_pai_html = r'<div class="about-text-pai">.*?</div>\s*</div>'
    content = re.sub(about_text_pai_html, '</div>', content, flags=re.DOTALL)
    
    # Remove tool-pill-pai elements
    tool_pill_pai_html = r'\s*<div class="tool-pill tool-pill-pai"[^>]*>.*?</div>'
    content = re.sub(tool_pill_pai_html, '', content, flags=re.DOTALL)
    
    # ═══ STEP 3: Remove JS dead code ═══
    
    # Remove toast function
    toast_func_pattern = r'function toast\(msg\) \{[^}]+\}'
    content = re.sub(toast_func_pattern, '', content, flags=re.DOTALL)
    
    # Remove // toast removed comments
    content = re.sub(r'\s*// toast removed', '', content)
    
    # Remove hints system
    hints_pattern = r'// ═══ SISTEMA DE DICAS \(HINTS\) IRRERENTES ═══\s+const hints = \[.*?\];.*?function startHints\(\) \{.*?\}\s+\}'
    content = re.sub(hints_pattern, '', content, flags=re.DOTALL)
    
    # Remove hintIdx variable
    content = re.sub(r'\s*let hintIdx = 0;', '', content)
    
    # Remove enginePai
    engine_pai_pattern = r'// Engines específicos\s+function enginePai\(\) \{.*?musicTimers\.push\(setTimeout\(enginePai, tick\)\);\s+\}'
    content = re.sub(engine_pai_pattern, '// Engines específicos', content, flags=re.DOTALL)
    
    # Remove engineRpg
    engine_rpg_pattern = r'function engineRpg\(\) \{.*?musicTimers\.push\(setTimeout\(engineRpg, tick\)\);\s+\}'
    content = re.sub(engine_rpg_pattern, '', content, flags=re.DOTALL)
    
    # Remove engineMusico
    engine_musico_pattern = r'function engineMusico\(\) \{.*?musicTimers\.push\(setTimeout\(engineMusico, tick\)\);\s+\}'
    content = re.sub(engine_musico_pattern, '', content, flags=re.DOTALL)
    
    # Remove logsPaiMode array
    logs_pai_pattern = r'const logsPaiMode = \[.*?\];'
    content = re.sub(logs_pai_pattern, '', content, flags=re.DOTALL)
    
    # Remove logsRPGMode array
    logs_rpg_pattern = r'// Logs do modo RPG - Skyrim e jogos medievais\s+const logsRPGMode = \[.*?\];'
    content = re.sub(logs_rpg_pattern, '', content, flags=re.DOTALL)
    
    # Remove logsMusicoMode array
    logs_musico_pattern = r'// Logs do modo Músico - Rock, estúdio e música\s+const logsMusicoMode = \[.*?\];'
    content = re.sub(logs_musico_pattern, '', content, flags=re.DOTALL)
    
    # ═══ STEP 4: Simplify JS functions ═══
    
    # Simplify startMusicEngine - remove pai/rpg/musico branches
    start_music_old = r"if \(currentMode === 'trabalho'\) engineTrabalho\(\);\s+else if \(currentMode === 'pai'\) enginePai\(\);\s+else if \(currentMode === 'rpg'\) engineRpg\(\);\s+else if \(currentMode === 'musico'\) engineMusico\(\);\s+else if \(currentMode === 'interstellar'\) engineInterstellar\(\);"
    start_music_new = "if (currentMode === 'trabalho') engineTrabalho();\n      else if (currentMode === 'interstellar') engineInterstellar();"
    content = re.sub(start_music_old, start_music_new, content)
    
    # Simplify animVinylLoop - remove isMusico, isRpg
    content = re.sub(r'\s+const isMusico = currentMode === \'musico\';', '', content)
    content = re.sub(r'\s+const isRpg = currentMode === \'rpg\';', '', content)
    
    # Simplify atualizarLogTerminal - remove dead conditionals
    log_terminal_old = r"let logsAtuais;\s+if \(document\.body\.classList\.contains\('pai-mode'\)\) \{\s+logsAtuais = logsPaiMode;\s+\} else if \(document\.body\.classList\.contains\('interstellar-mode'\)\) \{\s+logsAtuais = logsInterstellar;\s+\} else if \(document\.body\.classList\.contains\('rpg-mode'\)\) \{\s+logsAtuais = logsRPGMode;\s+\} else if \(document\.body\.classList\.contains\('musico-mode'\)\) \{\s+logsAtuais = logsMusicoMode;\s+\} else \{\s+logsAtuais = logsDivertidos;\s+\}"
    log_terminal_new = "let logsAtuais;\n      if (document.body.classList.contains('interstellar-mode')) {\n        logsAtuais = logsInterstellar;\n      } else {\n        logsAtuais = logsDivertidos;\n      }"
    content = re.sub(log_terminal_old, log_terminal_new, content)
    
    # Remove startHints() call from dismissIntro
    content = re.sub(r'; startHints\(\);', ';', content)
    
    # Simplify setMode - remove pai/rpg/musico classList operations
    content = re.sub(r"document\.body\.classList\.remove\('pai-mode', 'rpg-mode', 'musico-mode'\);", '', content)
    
    # Save file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    final_lines = len(content.splitlines())
    
    print(f"✓ Deep cleanup concluído!")
    print(f"  Linhas: {original_lines} → {final_lines}")
    print(f"  Removidas: {original_lines - final_lines} linhas")
    print(f"  Redução: {((original_lines - final_lines) / original_lines * 100):.1f}%")

if __name__ == '__main__':
    cleanup_deep('portfolio-rod.html')

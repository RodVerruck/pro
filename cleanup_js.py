#!/usr/bin/env python3
"""
Remove dead JS code (engines, logs, toast, hints)
"""

import re

def cleanup_js(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_lines = len(content.splitlines())
    
    # Remove toast function
    content = re.sub(
        r'function toast\(msg\) \{\s+const t = document\.getElementById\(\'toast\'\);\s+if \(!t\) return;\s+t\.textContent = msg;\s+t\.classList\.add\(\'show\'\);\s+setTimeout\(\(\) => t\.classList\.remove\(\'show\'\), 3000\);\s+\}',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove hints system
    content = re.sub(
        r'// ═══ SISTEMA DE DICAS \(HINTS\) IRRERENTES ═══\s+const hints = \[[^\]]+\];\s+let hintIdx = 0;\s+function startHints\(\) \{[^}]+\}\s+\}',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove startHints() call
    content = re.sub(r'; startHints\(\)', '', content)
    
    # Remove enginePai function
    content = re.sub(
        r'// Engines específicos\s+function enginePai\(\) \{.*?musicTimers\.push\(setTimeout\(enginePai, tick\)\);\s+\}',
        '// Engines específicos',
        content,
        flags=re.DOTALL
    )
    
    # Remove engineRpg function
    content = re.sub(
        r'function engineRpg\(\) \{.*?musicTimers\.push\(setTimeout\(engineRpg, tick\)\);\s+\}',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove engineMusico function
    content = re.sub(
        r'function engineMusico\(\) \{.*?musicTimers\.push\(setTimeout\(engineMusico, tick\)\);\s+\}',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove logsPaiMode array
    content = re.sub(
        r'const logsPaiMode = \[.*?\];',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove logsRPGMode array
    content = re.sub(
        r'// Logs do modo RPG - Skyrim e jogos medievais\s+const logsRPGMode = \[.*?\];',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove logsMusicoMode array
    content = re.sub(
        r'// Logs do modo Músico - Rock, estúdio e música\s+const logsMusicoMode = \[.*?\];',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Simplify startMusicEngine
    content = re.sub(
        r"if \(currentMode === 'trabalho'\) engineTrabalho\(\);\s+else if \(currentMode === 'pai'\) enginePai\(\);\s+else if \(currentMode === 'rpg'\) engineRpg\(\);\s+else if \(currentMode === 'musico'\) engineMusico\(\);\s+else if \(currentMode === 'interstellar'\) engineInterstellar\(\);",
        "if (currentMode === 'trabalho') engineTrabalho();\n      else if (currentMode === 'interstellar') engineInterstellar();",
        content
    )
    
    # Simplify animVinylLoop - remove isMusico, isRpg
    content = re.sub(r'\s+const isMusico = currentMode === \'musico\';', '', content)
    content = re.sub(r'\s+const isRpg = currentMode === \'rpg\';', '', content)
    
    # Simplify atualizarLogTerminal
    content = re.sub(
        r"let logsAtuais;\s+if \(document\.body\.classList\.contains\('pai-mode'\)\) \{\s+logsAtuais = logsPaiMode;\s+\} else if \(document\.body\.classList\.contains\('interstellar-mode'\)\) \{\s+logsAtuais = logsInterstellar;\s+\} else if \(document\.body\.classList\.contains\('rpg-mode'\)\) \{\s+logsAtuais = logsRPGMode;\s+\} else if \(document\.body\.classList\.contains\('musico-mode'\)\) \{\s+logsAtuais = logsMusicoMode;\s+\} else \{\s+logsAtuais = logsDivertidos;\s+\}",
        "let logsAtuais;\n      if (document.body.classList.contains('interstellar-mode')) {\n        logsAtuais = logsInterstellar;\n      } else {\n        logsAtuais = logsDivertidos;\n      }",
        content
    )
    
    # Save
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    final_lines = len(content.splitlines())
    
    print(f"✓ JS cleanup concluído!")
    print(f"  Linhas: {original_lines} → {final_lines}")
    print(f"  Removidas: {original_lines - final_lines} linhas")

if __name__ == '__main__':
    cleanup_js('portfolio-rod.html')

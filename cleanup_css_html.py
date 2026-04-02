#!/usr/bin/env python3
"""
Remove CSS and HTML for dead modes (Pai, RPG, Músico)
"""

import re

def cleanup_css_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    original_count = len(lines)
    result = []
    skip_until = None
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Skip CSS blocks for dead modes
        if '/* Hero eyebrow por modo */' in line:
            # Skip until we find the closing brace for musico-mode eyebrow
            skip_until = 'body.musico-mode .hero-eyebrow::before'
            i += 1
            continue
        
        if skip_until and skip_until in line:
            # Skip this line and the next closing brace
            while i < len(lines) and '}' not in lines[i]:
                i += 1
            i += 1  # Skip the closing brace
            skip_until = None
            continue
        
        if skip_until:
            i += 1
            continue
        
        # Skip Contact card por modo
        if '/* Contact card por modo */' in line:
            skip_until = 'body.musico-mode .contact-title::before'
            i += 1
            continue
        
        # Skip About card por modo
        if '/* About card por modo */' in line:
            skip_until = 'body.musico-mode .about-bio::before'
            i += 1
            continue
        
        # Skip entire RPG mode block
        if 'MODO RPG: O DOVAHKIIN DO FRONT-END' in line:
            skip_until = 'body.rpg-mode .c-proj-calc .proj-title::before'
            i += 1
            continue
        
        # Skip entire Músico mode block
        if 'MODO MÚSICO: ROCK & CODE' in line:
            skip_until = 'body.musico-mode .c-proj-calc .proj-title::before'
            i += 1
            continue
        
        # Skip project visibility rules for dead modes
        if 'PROJETOS VISÍVEIS APENAS NO MODO TRABALHO' in line:
            # Skip until we find the closing brace for skills
            while i < len(lines) and 'body.musico-mode .c-skills' not in lines[i]:
                i += 1
            while i < len(lines) and '}' not in lines[i]:
                i += 1
            i += 1  # Skip closing brace
            continue
        
        # Remove HTML elements
        if '<div id="rpg-snow"></div>' in line:
            i += 1
            continue
        
        if '<div id="portal-flash"></div>' in line:
            i += 1
            continue
        
        if '<div id="toast"></div>' in line:
            i += 1
            continue
        
        if '<div id="hint-box"></div>' in line:
            i += 1
            continue
        
        # Skip about-text-pai block
        if '<div class="about-text-pai">' in line:
            depth = 1
            i += 1
            while i < len(lines) and depth > 0:
                if '<div' in lines[i]:
                    depth += 1
                if '</div>' in lines[i]:
                    depth -= 1
                i += 1
            continue
        
        # Skip tool-pill-pai elements
        if 'class="tool-pill tool-pill-pai"' in line:
            # Skip until closing div
            if '</div>' in line:
                i += 1
                continue
            else:
                while i < len(lines) and '</div>' not in lines[i]:
                    i += 1
                i += 1
                continue
        
        result.append(line)
        i += 1
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(result)
    
    final_count = len(result)
    print(f"✓ CSS/HTML cleanup concluído!")
    print(f"  Linhas: {original_count} → {final_count}")
    print(f"  Removidas: {original_count - final_count} linhas")

if __name__ == '__main__':
    cleanup_css_html('portfolio-rod.html')

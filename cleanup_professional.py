#!/usr/bin/env python3
"""
Script para remover toasts e simplificar MODOS object para versão profissional
"""

import re

def cleanup_professional(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_lines = len(content.splitlines())
    
    # 1. Remove todas as chamadas toast()
    content = re.sub(r'\s*toast\([^)]+\);', '  // toast removed', content)
    
    # 2. Simplifica o objeto MODOS para apenas trabalho
    modos_pattern = r'const MODOS = \{[^}]+pai: \{[^}]+\},[^}]+rpg: \{[^}]+\},[^}]+musico: \{[^}]+\},[^}]+\'interstellar\': \{[^}]+\},[^}]+\};'
    modos_replacement = '''const MODOS = {
      trabalho: {
        emoji: '💼', title: 'Modo Trabalho', color: '#4a90e2', bg: '#1a2332',
        desc: 'Sessão de foco extremo. Café, headset e problemas complexos. Nada interrompe o flow.'
      }
    };'''
    
    content = re.sub(modos_pattern, modos_replacement, content, flags=re.DOTALL)
    
    # Salva o arquivo
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    final_lines = len(content.splitlines())
    
    print(f"✓ Cleanup profissional concluído!")
    print(f"  Linhas: {original_lines} → {final_lines}")
    print(f"  Removidas: {original_lines - final_lines} linhas")

if __name__ == '__main__':
    cleanup_professional('portfolio-rod.html')

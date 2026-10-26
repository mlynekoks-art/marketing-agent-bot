#!/usr/bin/env bash
# Instaluje narzędzia CLI, których potrzebują skille z .claude/skills.
# Uruchom ręcznie: bash scripts/install-tools.sh
set -euo pipefail

# agent-browser: sterowanie przeglądarką przez agenta (skill: agent-browser)
npm install -g agent-browser@latest
agent-browser install

# REA: reverse engineering aplikacji (skill: reverse-engineer-anything, MCP: rea)
npm install -g rea-agents@6.8.0

# GSD: workflow Omów → Zaplanuj → Wykonaj → Sprawdź → Wyślij (komendy /gsd-*)
npx -y @opengsd/gsd-core@latest --claude --local

# Zależności bota
pip install -r requirements.txt

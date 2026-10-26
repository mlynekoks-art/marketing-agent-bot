# Zainstalowane skille

Skille w tym folderze Claude Code ładuje automatycznie dla tego projektu.

| Skill(e) | Źródło | Commit |
|---|---|---|
| algorithmic-art, brand-guidelines, canvas-design, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx, academy-guide, discernment-nudge | https://github.com/anthropics/skills (oficjalne Anthropic) | dbd4588 |
| taste-skill (design-taste-frontend) | https://github.com/Leonxlnx/taste-skill | 12af471 |
| make-interfaces-feel-better | https://github.com/jakubkrehel/make-interfaces-feel-better | 35545ea |
| ui-ux-pro-max, design, design-system, brand, banner-design, slides, ui-styling | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | 1f88579 |
| impeccable | https://github.com/pbakaus/impeccable | 3671d50 |
| interface-design | https://github.com/Dammyjay93/interface-design | 2f9be32 |
| emil-design-eng, animate, animate-expo, animation-performance, animation-vocabulary, apple-design, ask-sonner, break-ui, find-animation-opportunities, improve-animations, mobile-native, pick-ui-library, prototype, review-animations, write-swift | https://github.com/emilkowalski/skills (Emil Kowalski) | 2d22863 |
| brainstorming, writing-plans, executing-plans, verification-before-completion, systematic-debugging, subagent-driven-development, dispatching-parallel-agents, requesting-code-review, receiving-code-review, using-git-worktrees, finishing-a-development-branch, writing-skills, using-superpowers, diagnosing-superpowers | https://github.com/obra/superpowers | 2ce8aa1 |
| find-skills | https://github.com/vercel-labs/skills | a80e4c9 |
| agent-browser (wymaga CLI: scripts/install-tools.sh) | https://github.com/vercel-labs/agent-browser | 04ba526 |
| reverse-engineer-anything (MCP w .mcp.json) | https://github.com/morluto/rea | 8a65787 |
| gamedev-router + 76 skilli do gier (Godot, Unity, Unreal, Roblox, Phaser, PixiJS, three.js, Bevy, Defold, LÖVE, pygame, Ebitengine, gatunki, dyscypliny, wydawanie) | https://github.com/gamedev-skills/awesome-gamedev-agent-skills (Apache-2.0) | 184b72b |
| 33 oficjalne skille Android (Jetpack Compose, Gradle, profiler, bezpieczeństwo, Wear, TV, XR) | https://github.com/android/skills (Apache-2.0) | 4ebabf2 |
| 31 oficjalnych skilli Flutter / Dart | https://github.com/flutter/skills (BSD-3) | f813a46 |
| 24 oficjalne skille Expo / EAS (React Native) | https://github.com/expo/skills (MIT) | d5caf7f |
| caveman, ultracave, megacave, caveman-compress, caveman-commit (oszczędzanie tokenów) | https://github.com/JuliusBrussee/caveman (Apache-2.0 / MIT) | 9b68f7e |
| context-mode, ctx-stats, ctx-search, ctx-doctor (+ MCP w .mcp.json) | https://github.com/mksglu/context-mode (Elastic License 2.0) | 8b74cbb |

Router gier oryginalnie nazywa się `router`, tu przemianowany na `gamedev-router`. Skille leżą płasko, więc ścieżki `skills/<silnik>/...` w routerze oznaczają `.claude/skills/<nazwa-skilla>/`.
Pełne teksty licencji: `.claude/licenses/`.

GSD (https://github.com/open-gsd/gsd-core) instaluje się tylko własnym instalatorem: patrz scripts/install-tools.sh.

Pominięte: `claude-api` z anthropics/skills, bo Claude Code ma nowszą wbudowaną wersję.
Licencje: każdy skill zawiera własny plik LICENSE (o ile repo go dostarcza).

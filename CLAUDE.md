# marketing-agent-bot

Bot marketingowy na Telegramie (python-telegram-bot 20.7 + Gemini). Kod w `bot.py`, klucze w `.env` (wzór: `.env.example`).
Użytkownik pisze po polsku: odpowiadaj po polsku, krótko i konkretnie.

## Zasada nr 1: zawsze dobieraj skille sam

Użytkownik nie będzie mówił, którego skilla użyć. Przed każdym zadaniem:

1. Dopasuj zadanie do tabeli poniżej i wywołaj pasujące skille narzędziem Skill, zanim zaczniesz pracę.
2. Przy grach zacznij od `gamedev-router`: wykrywa silnik i wskazuje właściwe skille.
3. Gdy nic nie pasuje, użyj `find-skills` (wyszukuje i instaluje skille z GitHuba). Jeśli nic nie ma, stwórz skill przez `skill-creator`.
4. Nie pytaj użytkownika o wybór skilla. Wspomnij jednym zdaniem, którego używasz.

Skille projektu leżą płasko w `.claude/skills/<nazwa>/`. Źródła i licencje: `.claude/skills/SOURCES.md`.

## Mapa: zadanie → skill

### Gry
| Zadanie | Skille |
|---|---|
| Dowolna gra, nie wiadomo od czego zacząć | `gamedev-router` |
| Roblox Studio (Luau) | `roblox-studio-workflow`, `roblox-luau`, `roblox-ui`, `roblox-datastores`, `roblox-networking`, `roblox-physics`, `roblox-characters` + wtyczka `roblox-dev:*` (architektura, bezpieczeństwo, wydajność, testy; agent `roblox-dev:roblox-reviewer` do audytu) |
| Godot | skille `godot-*` |
| Unity | skille `unity-*` |
| Unreal | skille `unreal-*` |
| Gry w przeglądarce | `phaser-*`, `pixijs-*`, `threejs-*` + `anthropic-skills:threejs-viewer` |
| Inne silniki | `bevy-ecs`, `defold-core`, `love2d-core`, `pygame-core`, `ebitengine-game` |
| Gatunki, mechaniki, game feel, audio, AI, zapis, multiplayer, wydanie (Steam/itch) | skille gatunków i dyscyplin wskazane przez `gamedev-router` |

### Aplikacje mobilne
| Zadanie | Skille |
|---|---|
| Android natywnie (Kotlin, Jetpack Compose, Gradle) | oficjalne skille Google: `jetpack-compose-*`, `adaptive`, `android-cli`, `android-profiler`, `migrate-xml-views-to-jetpack-compose` i reszta z `android/skills` + `anthropic-skills:android-*` |
| Flutter / Dart | oficjalne skille `flutter-*`, `dart-*` |
| React Native / Expo (Android i iOS z jednego kodu) | oficjalne skille `expo-*`, `eas-*` + `animate-expo` |
| iOS / Swift | `write-swift`, `apple-design` |
| Aplikacja webowa „jak natywna” (PWA) | `mobile-native`, `anthropic-skills:pwa-offline-cache` |

### Aplikacje na komputer i web
| Zadanie | Skille |
|---|---|
| Strona, landing, UI | `frontend-design` → `taste-skill` → `impeccable` / `make-interfaces-feel-better` |
| Animacje | `emil-design-eng` → `animate`, `review-animations`, `animation-performance` |
| Panele, dashboardy, narzędzia | `interface-design`, `ui-ux-pro-max`, `ui-styling` |
| Electron / aplikacje desktopowe | `agent-browser` (sterowanie Electronem), `anthropic-skills:react-ui`, `anthropic-skills:node-backend` |
| CLI | `anthropic-skills:cli-design` |
| Testy w przeglądarce | `webapp-testing` (Playwright jest zainstalowany) lub `agent-browser` |
| Odtworzenie funkcji z innej aplikacji | `reverse-engineer-anything` (MCP `rea`) |

### Proces pracy (każdy większy projekt)
| Etap | Skille |
|---|---|
| Pomysł → plan | `brainstorming` → `writing-plans` |
| Wykonanie | `executing-plans` lub `subagent-driven-development`, `test-driven-development` |
| Błąd | `systematic-debugging` |
| Przed „gotowe” | `verification-before-completion`, `requesting-code-review` |

### Marketing, dokumenty, grafika
| Zadanie | Skille |
|---|---|
| Teksty, kampanie, SEO, social media | wtyczki `marketing:*`, `searchfit-seo:*`, `small-business:social-content-engine`, `humanizer:humanizer` |
| Banery, grafiki, posty | `banner-design`, `design`, `canvas-design` |
| Marka i design system | `brand`, `design-system`, `theme-factory` |
| Prezentacje | `slides` (HTML) lub `pptx` |
| Dokumenty | `docx`, `xlsx`, `pdf`, `doc-coauthoring` |
| Serwer MCP / integracja API | `mcp-builder` |

## Oszczędzanie limitów i kontekstu

- Odpowiedzi krótkie: najpierw wynik, bez wstępów i powtórzeń. Na prośbę „krócej” / „caveman” włącz `caveman`.
- Duże wyniki komend, logi, strony www i długie pliki przepuszczaj przez MCP `context-mode`, gdy jest dostępne (`context-mode`, `ctx-search`). Pliki czytaj fragmentami (offset/limit, grep), nie w całości.
- Nie uruchamiaj subagentów bez potrzeby: każdy startuje od zera i zużywa limit.
- Długa sesja: zapisz stan w `STATE.md` i zaproponuj `/compact` albo nową sesję.
- Do commitów: `caveman-commit`. Do skracania dużych plików instrukcji: `caveman-compress` (najpierw zrób kopię).
- Zużycie kontekstu i oszczędności: `ctx-stats`. Problemy z context-mode: `ctx-doctor`.

## Zasady pracy

- Duże zadania: stan pracy zapisuj w `STATE.md` (co zrobione, co dalej). Nie polegaj na pamięci rozmowy.
- Przed oddaniem UI zrób zrzut ekranu (Playwright) i oceń go według wybranego skilla.
- Ta chmurowa sesja nie ma Roblox Studio, Unity, Godota ani emulatora Androida. Kod piszę i sprawdzam tutaj, a uruchomienie w edytorze należy do użytkownika na jego komputerze.
- Sprawdź składnię przed commitem: `python -m py_compile bot.py`.

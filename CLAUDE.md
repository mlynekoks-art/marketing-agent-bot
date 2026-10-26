# marketing-agent-bot

Bot marketingowy na Telegramie (python-telegram-bot 20.7 + Gemini). Kod w `bot.py`, klucze w `.env` (wzór: `.env.example`).
Użytkownik pisze po polsku: odpowiadaj po polsku, krótko i konkretnie.

## Skille: kiedy którego używać

Skille projektu są w `.claude/skills/`. Źródła: `.claude/skills/SOURCES.md`. Zanim zaczniesz zadanie, dobierz skill z tabeli i wywołaj go narzędziem Skill.

| Zadanie | Skill |
|---|---|
| Nowa strona, landing, UI. Zawsze zaczynaj od kierunku wizualnego | `frontend-design`, potem `taste-skill` (anty-„AI slop”) |
| Dopracowanie wyglądu, coś „wygląda słabo” | `impeccable`, `make-interfaces-feel-better` |
| Animacje, mikrointerakcje, ruch (Emil Kowalski) | `emil-design-eng` najpierw, potem `animate`, `review-animations`, `improve-animations`, `animation-performance` |
| Styl Apple, aplikacje mobilne | `apple-design`, `mobile-native`, `animate-expo`, `write-swift` |
| Panele, dashboardy, narzędzia | `interface-design`, `ui-ux-pro-max`, `ui-styling` |
| Szybki prototyp / test odporności UI | `prototype`, `break-ui` |
| Wybór biblioteki komponentów | `pick-ui-library` |
| Design system, tokeny, marka | `design-system`, `brand`, `theme-factory`, `brand-guidelines` |
| Grafiki marketingowe, banery, posty | `banner-design`, `design`, `canvas-design` |
| Prezentacje | `slides` (HTML) lub `pptx` (plik) |
| Dokumenty i arkusze | `docx`, `xlsx`, `pdf`, `doc-coauthoring` |
| Testowanie strony w przeglądarce | `webapp-testing` (Playwright jest zainstalowany) lub `agent-browser` (wymaga CLI, patrz niżej) |
| Odtworzenie funkcji z innej aplikacji | `reverse-engineer-anything` (REA, MCP `rea` w `.mcp.json`) |
| Brakuje skilla do zadania | `find-skills` |
| Większa funkcja: przemyśl → zaplanuj → wykonaj → sprawdź | `brainstorming` → `writing-plans` → `executing-plans` → `verification-before-completion` |
| Błąd do znalezienia | `systematic-debugging` |
| Nowy własny skill | `skill-creator` lub `writing-skills` |
| Serwer MCP / integracja z API | `mcp-builder` |

Teksty marketingowe, SEO i social media obsługują wbudowane wtyczki (`marketing:*`, `searchfit-seo:*`, `small-business:social-content-engine`, `humanizer:humanizer`). Nie dubluj ich.

## Zasady pracy

- Duże zadania: zapisuj stan pracy w `STATE.md` (co zrobione, co dalej). Nie polegaj na pamięci rozmowy.
- Przed oddaniem UI zrób zrzut ekranu (Playwright) i oceń go względem wybranego skilla.
- Sprawdź składnię przed commitem: `python -m py_compile bot.py`.

# Settings Spec

> User preferences, auth status, and system health. Minimal for V1; extensible for future.
> Reference: `fixtures/settings.json`

---

## Purpose

Show and manage:
- **Current user** (hardcoded as `anant` for V1, only human identity that can approve/promote)
- **UI preferences** (dark mode, refresh intervals, sidebar behavior)
- **API key status** (are they valid? when last checked?)
- **System health** (secrets redaction passing? any warnings?)

---

## Layout

```
┌──────────────────────────────────────────────────────────┐
│ research_data | Dashboard | ... Settings     [⚙ Settings] │
├──────────────────────────────────────────────────────────┤
│                                                            │
│ Settings                                                 │
│                                                            │
│ ▼ ACCOUNT                                                │
│ ┌──────────────────────────────────────────────────────┐│
│ │ Identity: anant (research desk owner)                ││
│ │ Role: Human approver (only identity that can promote)││
│ │ Last login: 2026-07-20 14:30 UTC                     ││
│ │                                                      ││
│ │ This is locked for V1. Multi-user auth deferred.    ││
│ └──────────────────────────────────────────────────────┘│
│                                                            │
│ ▼ UI PREFERENCES                                         │
│ ┌──────────────────────────────────────────────────────┐│
│ │ Dark mode: [ON ▼] (default for trading desk)         ││
│ │                                                      ││
│ │ Auto-refresh intervals:                              ││
│ │ • Live panels (prices, portfolio): [5 min ▼]        ││
│ │ • AI content (evidence, logs): [5 min ▼]            ││
│ │ • Static content (tests, journal): [Manual only ▼]   ││
│ │                                                      ││
│ │ Sidebar behavior:                                    ││
│ │ • Default state: [Collapsed ▼]                      ││
│ │ • Memory: [Remember last state ▼]                   ││
│ │                                                      ││
│ │ [Save preferences]                                  ││
│ └──────────────────────────────────────────────────────┘│
│                                                            │
│ ▼ API & SECRETS                                          │
│ ┌──────────────────────────────────────────────────────┐│
│ │ API Key Status:                                      ││
│ │ • Polygon:     ✓ Valid (checked 2h ago)             ││
│ │ • Tiingo:      ✓ Valid (checked 2h ago)             ││
│ │ • FMP:         ✓ Valid (checked 2h ago)             ││
│ │ • LLM keys:    ✓ Valid (Gemini, Groq)               ││
│ │                                                      ││
│ │ Secrets redaction: ✓ Passing                        ││
│ │ Last check: 2026-07-20 14:00 UTC                     ││
│ │                                                      ││
│ │ All keys are stored in .env (never in source/logs). ││
│ │ [Check now] [View docs on key setup →]              ││
│ │                                                      ││
│ │ ⚠️ Note: API key validity is checked on page load.   ││
│ │    If keys are invalid, ingest will fail silently   ││
│ │    (shown as error in Bots-Hub logs).               ││
│ └──────────────────────────────────────────────────────┘│
│                                                            │
│ ▼ SYSTEM HEALTH                                          │
│ ┌──────────────────────────────────────────────────────┐│
│ │ Database: ✓ DuckDB connected                         ││
│ │ Database size: 47 MB (14 symbols, 2+ years history) ││
│ │ Last backup: 2026-07-20 06:00 UTC (auto, daily)     ││
│ │                                                      ││
│ │ Python backend: ✓ Responsive (<500ms latency)       ││
│ │ LLM provider: ✓ Gemini (primary), Groq (fallback)   ││
│ │                                                      ││
│ │ Storage: 120 GB free on disk                        ││
│ │ No warnings or errors.                               ││
│ │                                                      ││
│ │ [Run diagnostics] [View system log →]               ││
│ └──────────────────────────────────────────────────────┘│
│                                                            │
│ ▼ ABOUT                                                  │
│ ┌──────────────────────────────────────────────────────┐│
│ │ research_data v1.0 (2026-07-20)                      ││
│ │ A personal US stocks/ETFs research desk.             ││
│ │                                                      ││
│ │ Built by: Anant Gupta                               ││
│ │ Repository: github.com/gupta-builds/TradingView      ││
│ │ Docs: /Docs/ folder                                 ││
│ │ License: Personal use only                          ││
│ │                                                      ││
│ │ [View changelog] [Report issue → GitHub]            ││
│ │                                                      ││
│ │ Not affiliated with TradingView.com                 ││
│ │ Not financial advice; for research/learning only.  ││
│ └──────────────────────────────────────────────────────┘│
│                                                            │
└──────────────────────────────────────────────────────────┘
```

---

## Component Tree

```
SettingsPage
├── Header (global)
├── PageTitle: "Settings"
├── Section: Account
│   ├── IdentityDisplay (hardcoded "anant")
│   ├── RoleDisplay ("Human approver")
│   ├── LastLoginDisplay
│   └── Note (locked for V1)
├── Section: UIPreferences
│   ├── DarkModeToggle
│   ├── AutoRefreshIntervalInputs × 3 (live/AI/static)
│   ├── SidebarBehaviorDropdowns
│   └── SaveButton
├── Section: APISecrets
│   ├── APIKeyStatusList × 4 (Polygon, Tiingo, FMP, LLM)
│   │   └── StatusBadge + LastCheckedTimestamp
│   ├── SecretsRedactionStatus
│   ├── CheckNowButton
│   └── LinkToDocsButton
├── Section: SystemHealth
│   ├── DatabaseStatus
│   ├── BackendStatus
│   ├── DiskSpaceStatus
│   ├── WarningsDisplay (if any)
│   ├── RunDiagnosticsButton
│   └── LinkToSystemLogButton
└── Section: About
    ├── VersionDisplay
    ├── Description
    ├── BuildInfo
    ├── License
    └── Links (changelog, GitHub issue, docs)
```

---

## Data Shape (Fixture Excerpt)

```json
{
  "settings": {
    "as_of": "2026-07-20T14:30:00Z",
    "account": {
      "identity": "anant",
      "role": "human_approver",
      "last_login": "2026-07-20T14:30:00Z"
    },
    "ui_preferences": {
      "dark_mode": true,
      "auto_refresh_live_panels_min": 5,
      "auto_refresh_ai_content_min": 5,
      "auto_refresh_static_min": null,
      "sidebar_default_state": "collapsed",
      "sidebar_remember_last": true
    },
    "api_secrets": {
      "keys": [
        {
          "provider": "Polygon",
          "status": "valid",
          "last_checked": "2026-07-20T12:30:00Z",
          "error_message": null
        },
        {
          "provider": "Tiingo",
          "status": "valid",
          "last_checked": "2026-07-20T12:30:00Z",
          "error_message": null
        },
        {
          "provider": "FMP",
          "status": "valid",
          "last_checked": "2026-07-20T12:30:00Z",
          "error_message": null
        },
        {
          "provider": "LLM (Gemini/Groq)",
          "status": "valid",
          "last_checked": "2026-07-20T12:30:00Z",
          "error_message": null
        }
      ],
      "secrets_redaction_passing": true,
      "secrets_last_checked": "2026-07-20T14:00:00Z"
    },
    "system_health": {
      "database": {
        "status": "connected",
        "type": "DuckDB",
        "size_mb": 47,
        "symbols_count": 14,
        "history_years": 2.5
      },
      "backend": {
        "status": "responsive",
        "latency_ms": 250,
        "last_response": "2026-07-20T14:28:00Z"
      },
      "llm_provider": {
        "primary": "Gemini",
        "fallback": "Groq",
        "status": "operational"
      },
      "disk": {
        "free_gb": 120,
        "status": "healthy"
      },
      "warnings": [],
      "last_diagnostics": "2026-07-20T12:00:00Z"
    },
    "about": {
      "app_name": "research_data",
      "version": "1.0",
      "release_date": "2026-07-20",
      "description": "A personal US stocks/ETFs research desk.",
      "author": "Anant Gupta",
      "repository": "github.com/gupta-builds/TradingView",
      "license": "Personal use only",
      "not_affiliated": "Not affiliated with TradingView.com",
      "disclaimer": "Not financial advice; for research/learning only."
    }
  }
}
```

---

## Interactions

### Account Section

**Identity display:**
- Read-only (hardcoded for V1)
- Shows: "anant (research desk owner)"
- Note: "This is locked for V1. Multi-user auth deferred."

### UI Preferences

**Dark mode toggle:**
- ON | OFF
- Toggles site-wide theme immediately

**Auto-refresh interval inputs:**
- Dropdowns: 1 min | 5 min | 10 min | 15 min | 30 min | Manual only
- Applies to dashboard and live panels
- AI content (evidence, logs) typically slower refresh
- Static content (tests, journal) often manual-only

**Sidebar behavior:**
- Default state: [Collapsed | Expanded]
- Remember last state: [ON | OFF]

**[Save preferences]:**
- Saves to browser localStorage (prototype)
- Production: POST to backend, persist in DB

### API Secrets

**Key status list:**
- Shows each provider with status badge (✓ Valid | ⚠ Expired | ✗ Invalid)
- Last checked timestamp

**[Check now]:**
- Re-validates all keys immediately
- Shows results after 2–5 second check

**[View docs]:**
- Link to setup guide (e.g., `/docs/api-keys`)

### System Health

**Status badges:**
- Database: ✓ Connected
- Backend: ✓ Responsive
- LLM provider: ✓ Operational
- Disk: ✓ Healthy

**[Run diagnostics]:**
- Launches a system check (async)
- Shows progress spinner
- Populates warnings if any
- Results cached for 1 hour

**[View system log]:**
- Link to detailed system logs (may be a separate page or modal)

### About

**Links:**
- "[View changelog →]" – link to `/changelog` or release notes
- "[Report issue → GitHub]" – link to GitHub issues

---

## Refresh Strategy

- **Settings page**: Load on page enter, no auto-refresh
- **API key status**: Manual refresh via [Check now] button
- **System health**: Cached (refreshed on [Run diagnostics] or on page load if >1 hour old)
- **Dark mode / UI prefs**: Immediate (no server round-trip)

---

## Edge Cases

### API key is invalid
- Status shows ✗ Invalid
- Error message: "Polygon API key not authorized. Check .env file."
- [Check now] button still available

### No disk space
- Disk status shows ⚠ Low
- Warning added to system health: "Only 5 GB free. Archiving old data recommended."

### Multiple warnings present
- Display all warnings at top of System Health section
- Each warning has an action (e.g., "[Archive old data]")

### Backend latency is slow
- Backend status shows: ✓ Responsive (but slow)
- Message: "Latency: 5000ms (typically <500ms). Check server logs."

### LLM provider down
- LLM provider shows: ✗ Offline
- Message: "Gemini offline. Using Groq fallback."
- Or: "All LLM providers offline. Analysis paused."

---

## Accessibility & Mobile

- **Tab order**: Account → UI Prefs → API Secrets → System Health → About
- **Keyboard**: Tab to move between sections, Enter to toggle switches, arrow keys for dropdowns
- **Mobile (<640px)**:
  - Sections stack vertically
  - Inputs scale to full width
  - Status badges stack inline-block (wrap if needed)
- **Screen reader**: 
  - "Account section: Identity anant, role human approver"
  - "API key status: Polygon valid, checked 2 hours ago"

---

## Prototype Acceptance Criteria

- [ ] Account section displays with identity and role
- [ ] Dark mode toggle works (immediate visual change)
- [ ] UI preference dropdowns are functional (no save needed in prototype)
- [ ] [Save preferences] button is clickable (can be no-op in prototype)
- [ ] API key status shows for all 4 providers
- [ ] [Check now] button is clickable (can be no-op in prototype)
- [ ] System health shows database, backend, LLM, and disk status
- [ ] [Run diagnostics] button is clickable (can be no-op in prototype)
- [ ] About section shows version, description, author, license, links
- [ ] Links to docs/GitHub are valid (may be placeholder in prototype)
- [ ] All sections render correctly and are readable
- [ ] Responsive down to 375px

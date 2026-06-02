-- Jarvis memory registry schema.
-- The machine-readable index of the vault: notes, structure, links, chunks,
-- conversations, enrichment events, and the answer benchmark. This is the
-- substrate the three-month plan builds retrieval, answering, and learning on.
-- Safe to re-run: every table uses IF NOT EXISTS.

CREATE TABLE IF NOT EXISTS notes (
    id          INTEGER PRIMARY KEY,
    path        TEXT UNIQUE NOT NULL,   -- vault-relative posix path
    title       TEXT,
    type        TEXT,                   -- frontmatter type
    status      TEXT,                   -- frontmatter status (seed/sprout/tree/...)
    track       TEXT,                   -- ai|systems|algorithms|career|trading
    enrichment_status TEXT,
    source_status     TEXT,
    word_count  INTEGER,
    hash        TEXT,                   -- sha256 of file text
    updated     TEXT,                   -- frontmatter updated date
    indexed_at  TEXT                    -- ISO timestamp of last index
);

CREATE TABLE IF NOT EXISTS headings (
    id        INTEGER PRIMARY KEY,
    note_id   INTEGER NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
    heading   TEXT,
    level     INTEGER,
    position  INTEGER
);

CREATE TABLE IF NOT EXISTS links (
    id             INTEGER PRIMARY KEY,
    source_note_id INTEGER NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
    target         TEXT,                -- raw wikilink target
    target_note_id INTEGER REFERENCES notes(id),
    link_type      TEXT,                -- wikilink|embed|frontmatter
    status         TEXT                 -- resolved|broken|ambiguous
);

CREATE TABLE IF NOT EXISTS chunks (
    id            INTEGER PRIMARY KEY,
    note_id       INTEGER NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
    heading_path  TEXT,
    text          TEXT,
    hash          TEXT,
    token_estimate INTEGER
);

CREATE TABLE IF NOT EXISTS conversations (
    id           INTEGER PRIMARY KEY,
    conversation_id TEXT UNIQUE,        -- stable external id
    source_app   TEXT,                  -- claude-code|codex|cursor|kiro|chatgpt|claude-web|ollama|other
    title        TEXT,
    started_at   TEXT,
    ended_at     TEXT,
    project      TEXT,
    raw_path     TEXT,                  -- 60_Claude/05_Clippings/AI Conversations/...
    summary_path TEXT,                  -- 60_Claude/10_Source_Summaries/...
    status       TEXT,                  -- raw|distilled|promoted|archived
    checksum     TEXT
);

CREATE TABLE IF NOT EXISTS enrichment_events (
    id        INTEGER PRIMARY KEY,
    note_id   INTEGER REFERENCES notes(id) ON DELETE CASCADE,
    level     TEXT,                     -- light|standard|deep
    created   TEXT,
    summary   TEXT
);

CREATE TABLE IF NOT EXISTS benchmarks (
    id            INTEGER PRIMARY KEY,
    question      TEXT,
    category      TEXT,                 -- definition|comparison|course|project|research
    expected_notes TEXT,               -- json array of paths
    status        TEXT,                 -- open|passing|failing
    last_score    REAL,
    last_run      TEXT
);

CREATE INDEX IF NOT EXISTS idx_notes_type   ON notes(type);
CREATE INDEX IF NOT EXISTS idx_notes_track  ON notes(track);
CREATE INDEX IF NOT EXISTS idx_notes_status ON notes(status);
CREATE INDEX IF NOT EXISTS idx_links_source ON links(source_note_id);
CREATE INDEX IF NOT EXISTS idx_headings_note ON headings(note_id);
CREATE INDEX IF NOT EXISTS idx_chunks_note  ON chunks(note_id);

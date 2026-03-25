# Knowledge Store Inventory Template

## Instructions

Copy this template into your workspace and fill it in.
Knowing where your knowledge lives is the first step to retrieving it.

---

# My Knowledge Stores

## Unstructured Memory (prose, narrative, searchable by meaning)

| Store | Location | Access Method | Notes |
|-------|----------|---------------|-------|
| Daily notes | `memory/YYYY-MM-DD.md` | File read, semantic search | Raw session logs |
| Long-term memory | `MEMORY.md` | Loaded at boot + searchable | Curated, consolidated |
| Research threads | `memory/research-*.md` | Semantic search | Deep dives on topics |
| Letters/correspondence | `~/mail/cur/` | File search | External communication |
| | | | |

## Structured Data (databases, APIs, queryable by field)

| Store | Location | Access Method | Notes |
|-------|----------|---------------|-------|
| Example: contacts | `contacts.json` | JSON read | Names, addresses, relationships |
| Example: calendar | Google Calendar API | API call | Events, schedules |
| Example: database | `localhost:8080/api/` | REST query | Domain-specific records |
| | | | |

## Archives (historical, rarely consulted, but searchable)

| Store | Location | Access Method | Notes |
|-------|----------|---------------|-------|
| Chat transcripts | Platform-specific | Search/export | Past conversations |
| Old session logs | Compacted sessions | May not be accessible | Pre-compaction content |
| Email history | `~/mail/cur/` | File grep | All received mail |
| | | | |

## Reference Data (functional, not narrative — contacts, configs, skills)

| Store | Location | Access Method | Notes |
|-------|----------|---------------|-------|
| People/contacts | `memory/people/` | File read | Names, relationships, context |
| Tool config | `TOOLS.md` | Loaded at boot | Environment-specific notes |
| Skills | Skill directories | Read on demand | How to use specific tools |
| | | | |

## Topic Index

| Item | Value |
|------|-------|
| Index file | `memory/topic-index.md` |
| Last rebuilt | YYYY-MM-DD |
| Keyword count | (run build-index.py to populate) |
| Rebuild command | `python tools/build-index.py` |

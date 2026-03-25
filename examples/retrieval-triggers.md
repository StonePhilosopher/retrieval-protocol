# Retrieval Trigger Examples

## For AGENTS.md / Session Instructions

Drop this into your agent's AGENTS.md or equivalent boot instructions,
customized for your domain.

---

### 🔍 Retrieval Protocol — Search Before You Speak

When conversation references something outside your current context:

1. **Identifiers** (ticket numbers, specimen IDs, order numbers, etc.):
   Query your structured store AND search memory for prior notes.

2. **Names/people**: Check your topic index for file locations,
   then pull the relevant sections.

3. **Domain terms**: Search memory with the term. If nothing comes back,
   check the topic index for alternate locations.

4. **Events/dates**: Search daily files with the date or event description.

5. **"Remember when..."**: ALWAYS search. Never guess from what you
   loaded at session start.

**Rule: If you're about to say "I don't recall" or "I'm not sure about that" — search first. The answer is probably in a file you didn't load.**

---

## Domain-Specific Trigger Tables

### General Agent
| Trigger | Action |
|---------|--------|
| A person's name you recognize but can't place | Index lookup → pull their history |
| Reference to a past conversation | Semantic search on the topic |
| A date or time reference | Check calendar + search dailies |
| You're about to hedge or disclaim | Stop. Search. Then respond. |

### Knowledge Base Agent
| Trigger | Action |
|---------|--------|
| A product or project name | Query KB + search memory for context |
| A customer or stakeholder name | Pull interaction history |
| "Last time we discussed..." | Search conversation archives |
| A technical term from your domain | Pull definition + prior usage |

### Personal Assistant Agent
| Trigger | Action |
|---------|--------|
| Any name from contacts | Pull relationship context |
| Schedule/calendar references | Query calendar API |
| "That thing I mentioned" | Search recent dailies for topics |
| Recurring topics (health, projects, hobbies) | Pull the relevant shelf/theme file |

### Creative Agent
| Trigger | Action |
|---------|--------|
| Reference to prior creative work | Pull the work + notes about it |
| Themes or motifs from past sessions | Search for the theme across files |
| Collaborator names | Pull collaboration history |
| "Like that other one we did" | Search by technique/medium/style |

# Project: Social Deduction Game

## Overview
A social deduction game (Jackbox style) with a Python (FastAPI) backend and a React frontend. Players use phones/headphones for audio-based instructions.

## Tech Stack
- **Backend:** FastAPI, Uvicorn, `websockets` library.
- **Frontend:** React (Vite), Tailwind CSS, WebSockets API.

## System Architecture

### Views
1. **Display View (`/display`):** Shows room code, player list, voting results, and point totals.
2. **Player View (`/`):** Join screen, Lobby (with host controls), Splash screen, Round/Audio screen, Voting screen, Results screen.

### WebSocket Protocol
| Message Type | Description |
| :--- | :--- |
| `SERVER_INFO` | Initial connection and room join confirmation |
| `PLAYER_UPDATE` | Updates the list of players in the lobby |
| `GAME_START` | Transitions from Lobby to Splash screen |
| `PRELOAD_ASSETS` | Sends URLs for audio files to be pre-downloaded |
| `ROUND_START` | Triggers playback of pre-downloaded audio |
| `VOTING_START` | Transitions to the voting interface |
| `VOTE_REVEAL` | Sends votes and results for display/results view |
| `GAME_OVER` | Ends the session |

## Audio Strategy
To ensure synchronization:
1. Server sends `PRELOAD_ASSETS` with audio URLs.
2. Client pre-downloads and buffers audio files.
3. Server sends `ROUND_START` to trigger simultaneous playback.

## Roadmap
- [ ] Phase 1: Scaffolding (React + Tailwind + Vite)
- [ ] Phase 2: Connectivity (Join Flow $\rightarrow$ Lobby via WebSockets)
- [ ] Phase 3: Display Logic (Lobby & Results views)
- [ ] Phase 4: Game Loop with Preloading (Pre-download $\rightarrow$ Sync trigger)
- [ ] Phase 5: UI/UX & Polish (Transitions, animations, and voting UI)

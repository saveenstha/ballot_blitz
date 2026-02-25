# 🗳️ Ballot Box Blitz

A fast-paced arcade game built with Django + HTML Canvas.

Catch valid ballots, dodge the duds, and save democracy — one paper at a time!

## 🎮 How to Play

| Item | Effect |
|------|--------|
| ✅ Valid Ballot | Catch it → **+10 points** |
| ⭐ Golden Ballot | Catch it → **+30 points** |
| ❌ Spoiled Ballot | Avoid it → **-1 Life** |
| 💣 Ballot Bomb | Avoid it → **-20 points** |

- Move the ballot box with your **mouse** or **arrow keys / WASD**
- Every **100 points** → Level Up (faster, more chaotic!)
- You have **3 lives** — don't let spoiled ballots in!
- Press **P or ESC** to pause

## 🚀 Setup

```bash
# 1. Clone / copy this folder
cd ballot_blitz

# 2. Install Django (already in your env from your Election project)
pip install -r requirements.txt

# 3. Collect static files (for production) or just run dev server
python manage.py runserver

# 4. Open http://127.0.0.1:8000
```

No database setup needed — this game is completely stateless!
Best score is saved in the browser's localStorage.

#  The Steady Hand Election — स्थिर हात निर्वाचन

A bilingual (Nepali + English) browser-based election stamping game.
Built with Django 4.2.8 + HTML5 Canvas + Vanilla JS. No database required.

## 🎮 Game Modes

| Mode | Timer | Challenge |
|------|-------|-----------|
| ⚡ Precinct Rush | 60s | Find and stamp 5 ballots fast |
| 🕯️ Dimly Lit Booth | 45s | Blurred, wobbly, dark — Hard mode |
| 📚 Practice | None | Unlimited tries with precision feedback |

## 🏆 Scoring
- Valid ballot (stamp fully inside border): **+20 points**
- Spoiled ballot (any edge touches line): **0 points**
- Time bonus: **remaining seconds × 2**


No `migrate` needed — zero database.


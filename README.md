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

## 📁 Structure

```
ballot_blitz/
├── ballot_blitz/          # Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── game/                  # Game app
│   ├── templates/game/
│   │   └── index.html     # Game UI & layout
│   ├── static/game/
│   │   ├── css/style.css  # All styles
│   │   └── js/steady_hand_game.js     # Full game engine
│   ├── views.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

## 🔧 Integrating into your existing Election project

If you want to add this as an app to your existing Election Django project:

1. Copy the `game/` folder into your Election project
2. Add `'game'` to `INSTALLED_APPS` in your settings
3. Include game URLs: `path('game/', include('game.urls'))` in your main urls.py
4. Run `python manage.py collectstatic`
"# ballot_blitz" 
"# ballot_blitz" 

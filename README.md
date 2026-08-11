# 🎴 UNO Live
 game-link-to-play  - https://uno-game-lake.vercel.app/
> A modern web-based UNO game powered by Python and Flask, with a responsive interactive interface and AI opponents.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge\&logo=flask\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-Deployed-000000?style=for-the-badge\&logo=vercel\&logoColor=white)

---

##  About

**UNO Live** is a browser-based implementation of a custom UNO-style card game originally developed as a Python terminal game and later transformed into an interactive web application.

The game combines a **Flask backend** for game logic with a custom **HTML, CSS and JavaScript frontend** to create a responsive tabletop-style experience.

The project supports playing against **1–4 system opponents**, special cards, penalty stacking, reverse/skip mechanics, wild-card color selection, live game events and win detection.

---

##  Features

*  Interactive UNO-style card interface
*  Play against **1–4 AI opponents**
*  7-card starting hand
*  Four card colors — Red, Blue, Green and Yellow
*  Wild card color selection
   +1 penalty stacking
*  +4 penalty stacking
   Reverse card
*  Skip card
*  Draw cards
*  Automatic AI turns
*  Live game activity feed
*  Automatic win detection
*  Built-in rules panel
*  Delayed system actions so gameplay is easier to follow
*  Responsive interface for desktop and mobile
*  Vercel deployment support

---

##  How To Play

### 1. Match a Card

A card can normally be played when it matches either:

* The **color** of the current card
* The **value/action** of the current card

For example:

```text
Current: 🔴 7

You can play:
🔴 3
🔴 Skip
🔴 Reverse
🔵 7
🟢 7
```

---

### 2. Draw

If you don't want to play a card, use the **DRAW** pile.

A card is added to your hand and your turn moves on.

---

### 3. Wild

The **WILD** card can be played regardless of the current color.

You then choose:

```text
🔴 RED
🔵 BLUE
🟢 GREEN
🟡 YELLOW
```

---

### 4. +1

Playing a **+1** adds one card to the current penalty.

Example:

```text
Player +1
    ↓
Penalty = 1

System +1
    ↓
Penalty = 2

Next player must:
Stack another +1
OR
Take 2 cards
```

---

### 5. +4

The **+4** card adds four cards to the penalty and allows the player to choose a new color.

+4 cards can also be stacked according to the game's custom rules.

---

### 6. Reverse

The **Reverse** card changes the direction of the game.

```text
Clockwise ↻
     ↓
Reverse ↶
```

---

### 7. Skip

The **Skip** card skips the next player.

---

### 8. Winning

The first player to empty their hand wins the game.

```text
7 cards
 ↓
5 cards
 ↓
3 cards
 ↓
1 card
 ↓
 WIN
```

---

##  Game Logic

The original game logic was designed in Python and then adapted for the web.

The backend maintains the game state, including:

```text
Player hands
System hands
Current card
Current player
Direction
Penalty
Winner
Game events
```

The browser communicates with the Flask API to perform actions while the frontend handles the visual presentation and interaction.

---

##  Project Structure

```text
uno-live/
│
├── api/
│   └── index.py          # Flask API and game engine
│
├── static/
│   ├── index.html        # Main interface
│   ├── style.css         # UI and animations
│   └── app.js            # Frontend game interaction
│
├── requirements.txt      # Python dependencies
├── vercel.json            # Vercel configuration
└── README.md
```

---

##  Tech Stack

### Backend

* Python
* Flask
* REST-style API
* Randomized AI card selection

### Frontend

* HTML5
* CSS3
* Vanilla JavaScript
* Responsive design
* CSS animations

### Deployment

* GitHub
* Vercel

---

##  Run Locally

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/uno-live.git
cd uno-live
```

### Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the server

```bash
python api/index.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## ☁️ Deployment

The project includes a `vercel.json` configuration for deployment on Vercel.

### Deploy using Vercel

1. Push the repository to GitHub.
2. Open Vercel.
3. Import the GitHub repository.
4. Keep the framework preset as **Other**.
5. Deploy.

The Flask API is exposed through the Vercel serverless Python function.

---

##  Project Highlights

This project demonstrates practical experience with:

* Python game logic
* Object/state-based thinking
* Backend API development
* Frontend-backend communication
* JavaScript DOM manipulation
* Responsive UI development
* Git and GitHub
* Vercel deployment
* Translating a terminal application into a web application

---

##  Future Improvements

Possible future additions include:

*  Real-time multiplayer
*  Private game rooms
*  User accounts
*  Leaderboards
*  Card sound effects
*  Background music
*  More UNO card types
*  Game statistics and  Custom card themes
*  In-game chat

---

##  Author

**K. Charan**
https://github.com/cherry5231
Built as a personal web development project while experimenting with Python, Flask, frontend development and deployment.

---

##  Support

If you like the project, consider giving the repository a ⭐ on GitHub.

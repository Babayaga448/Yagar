# Yagar - Web3 Multiplayer Game

A multiplayer browser-based game inspired by agar.io, featuring Web3 integration and blockchain interactions on the Monad testnet.

## Project Structure
```
├── contracts/
│   └── YagarSplit.sol       # Smart contract for cell splitting
├── static/
│   ├── css/
│   │   └── style.css        # Game styles
│   └── js/
│       ├── audio.js         # Game audio effects
│       ├── game.js          # Main game logic
│       ├── monad_relayer.js # Blockchain interaction
│       └── web3mock.js      # Web3 wallet connection
├── templates/
│   └── index.html           # Main game page
├── app.py                   # Flask application
└── main.py                  # Entry point
```

## Dependencies
- Python 3.11
- Flask
- Gunicorn
- Eventlet
- Web3.js
- Ethers.js

## Smart Contract (Monad Testnet)
- Address: 0xA4A1c7A60E45708662aD528482a031Ee97e973b7
- RPC URL: https://testnet-rpc.monad.xyz/

## Features
1. Multiplayer real-time gameplay
2. Web3 wallet integration
3. Blockchain-based cell splitting
4. Dynamic score tracking
5. Audio feedback
6. 3-minute game rounds

## How to Play
1. Connect your Web3 wallet
2. Move your cell with the mouse
3. Press spacebar to split (requires connected wallet)
4. Eat other players to grow
5. The largest player after 3 minutes wins!

## Running Locally
1. Install dependencies:
```bash
pip install flask gunicorn eventlet flask-socketio
```

2. Run the server:
```bash
python main.py
```

## Deployment
Deploy using Replit's deployment feature for instant hosting and SSL.
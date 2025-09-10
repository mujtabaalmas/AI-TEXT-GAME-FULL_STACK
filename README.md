# AI_TEXT_GAME

An interactive AI-powered adventure game with a full-stack architecture. The backend is built with Python (FastAPI), and the frontend uses React with Vite.

## Features

- AI-generated storylines and prompts
- Save and load game progress
- Dynamic theme input for custom adventures
- Responsive and modern UI

## Project Structure

```
AI_TEXT_GAME/
├── backend/   # FastAPI backend, database, models, routers, schemas
└── frontend/  # React frontend, Vite config, components, assets
```

### Backend

- **Tech:** Python, FastAPI, SQLite
- **Main files:** `main.py`, `core/`, `db/`, `models/`, `routers/`, `schemas/`
- **Database:** `database.db`
- **Config:** `requirements.txt`, `pyproject.toml`

#### Running the Backend

1. Install dependencies:
	```
	pip install -r requirements.txt
	```
2. Start the server:
	```
	uvicorn main:app --reload
	```

### Frontend

- **Tech:** React, Vite
- **Main files:** `src/`, `components/`, `public/`
- **Config:** `package.json`, `vite.config.js`

#### Running the Frontend

1. Install dependencies:
	```
	npm install
	```
2. Start the development server:
	```
	npm run dev
	```

## How to Play

1. Start the backend server.
2. Start the frontend server.
3. Open your browser at `http://localhost:5173` (or the port shown in the terminal).
4. Enter a theme and begin your AI-generated adventure!

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Connect

Find me on LinkedIn: [Mujtaba Almas](https://www.linkedin.com/in/mujtabaalmas)

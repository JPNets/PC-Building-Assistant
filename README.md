# AI-powered PC Builder Assistant

A Streamlit app that helps users design optimized PC builds based on budget, usage, preferences, and compatibility rules. This project is database-first: all hardware specifications, prices and compatibility are stored in the `data/` JSON files which are the single source of truth.

Features:
- Component database (JSON)
- Compatibility engine
- Build optimizer (Balanced, Value, Maximum Performance)
- AI explanations using OpenAI (only sees final builds)
- Interactive Streamlit UI with visualizer and Plotly charts
- Save/load/export builds (JSON, PDF)

Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and set `OPENAI_API_KEY`.

3. Run the app:

```bash
streamlit run app.py
```

Notes

- The `data/` folder contains curated component entries. The app does not invent specs or prices; edit those JSON files to update the database.

# AIna AI Agent

A minimal Python AI agent with both a command-line interface and a small web app you can publish to GitHub.

## What it does

- Runs a simple command-line AI assistant
- Includes a Streamlit web chat interface
- Uses the OpenAI API
- Keeps short in-memory conversation history during each session
- Reads configuration from environment variables

## Project structure

```text
.
├── agent.py
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file or export your environment variables:

```bash
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_MODEL="gpt-4.1-mini"
```

## Run the agent

Command line:

```bash
python agent.py
```

Type `exit` to quit.

Web app:

```bash
streamlit run app.py
```

Then open the local URL Streamlit prints in your terminal.

## Publish to GitHub

If this repo is not the one you want to publish, point it to your own GitHub repository:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/aina-ai-agent.git
git add .
git commit -m "Create initial AI agent"
git push -u origin main
```

If you want to create a brand new GitHub repository first:

1. Go to GitHub and create a new empty repository.
2. Copy its HTTPS URL.
3. Run:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git add .
git commit -m "Create initial AI agent"
git push -u origin main
```

## Next improvements

- Add memory backed by a database or file
- Add tools like web search or file actions
- Add authentication and usage logging
- Deploy the Streamlit app online

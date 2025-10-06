## LangChain Notes

A collection of notebooks and examples exploring LangChain, prompt engineering, and LLM tooling.

### Project Structure
- `Lecture Notes/`: Jupyter notebooks with step-by-step tutorials
- `requirements.txt`: Python dependencies
- `.gitignore`: ignores `venv/`, `.venv/`, `.env`, and other local artifacts

### Setup

1) Clone and enter the project
```powershell
git clone <your-repo-url>
cd "E:\Extra Learning Resources\Extra Learning Resources\NLP\Langchain"
```

2) Create/activate a virtual environment (or use the existing `venv`)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3) Environment variables
- Create a `.env` file in the project root:
```env
GROQ_API_KEY=gsk_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
- Ensure `.env` is ignored by Git (already in `.gitignore`).

4) Launch notebooks
```powershell
jupyter notebook
```
Open notebooks in `Lecture Notes/` and select the `venv` kernel if needed.
```

### Requirements

Install all dependencies:
```powershell
pip install -r requirements.txt
```

### License

Add your preferred license here.
##🩺 RAG4HealthQA – Healthcare Q&A Assistant
RAG4HealthQA is an AI-powered healthcare assistant that uses Retrieval-Augmented Generation (RAG) to provide trustworthy, explainable answers to health-related questions. Built with LangChain, FAISS, Cohere LLMs, and a curated public health knowledge base (WHO, NIH, CDC), it supports digital health education, public outreach, and personalized learning.

## Live demo powered by Streamlit + FAISS + LangChain + Cohere
- Knowledge grounded in official medical content
- Designed to serve public interest — EB2-NIW ready

📌 Features
- ** RAG-based architecture with real-time retrieva
- ** Clean UI using Streamlit for patient-friendly Q&A
- ** Uses FAISS (no SQLite issues) for efficient local vector search
- ** Knowledge base sourced from WHO, NIH, Nutrition.gov
- ** Dynamically refreshable .md/.txt content for new updates
- ** Modular backend (retriever, embedder, LLM, pipeline)
🧠 Example Questions
- What are the symptoms of hypertension?
- How does CBT help with PTSD?
- Is vegetarian diet safe for athletes?
- How much water should adults drink daily?
🗂️ Project Structure
```
RAG4HealthQA/
├── main.py                   # Streamlit frontend
├── requirements.txt
├── .env                      # API keys (Cohere)
├── app/
│   ├── rag_pipeline.py       # Main RAG logic
│   ├── embedding_config.py   # Embedding model config
│   ├── vector_store.py       # FAISS-based document store
│   └── utils.py              # Load and clean docs
├── data/                     # Markdown/txt knowledge base
│   ├── hypertension_who.txt
│   ├── mental_health_nih.md
│   ├── diabetes_nih.txt
│   └── nutrition_basics.txt
├── scripts/
│   └── generate_health_kb.py # Scraper for public sources
├── docs/
│   └── architecture.md       # Design explanation
├── tests/                    # Pytest unit tests
└── .streamlit/config.toml
```
🚀 Quickstart
1. Clone this repository
```bash
git clone https://github.com/Sankarraj-Subramani/RAG4HealthQA
cd RAG4HealthQA
```
```bash
2. Install dependencies
pip install -r requirements.txt
```
```bash
3. Set up environment variables
Create a .env file in the root:
COHERE_API_KEY=your-cohere-api-key
```
```bash
4. Run the app
streamlit run main.py
```
🔁 Updating the Knowledge Base
```bash
Run the included scraper to dynamically download and clean WHO/NIH/CDC data:
python scripts/generate_health_kb.py
Then restart the app to use the updated data.
```
📖 Documentation
```bash
See docs/architecture.md for a visual diagram and explanation of: - Chunking & embedding - Retrieval flow - LangChain integration - LLM pipeline (Cohere)
```

🔒 License and Data Use
```bash
This project uses public-domain or openly licensed health c>WHO - NIH/NIMH - Nutrition.gov

Data is processed solely for educational and informational use.
```
## ✨ Author

**Sankarraj Subramani**  
QA Automation Lead | AI/ML Enthusiast | EB2-NIW/EB1A Aspirant  
[GitHub](https://github.com/Sankarraj-Subramani) • [LinkedIn](https://www.linkedin.com/in/sankarraj-subramani-34254757)

> ⭐ If you like this project, kindly star the repo and share with the QA + AI community!

## Why This Matters
> RAG4HealthQA supports the U.S. national interest by improving public access to verified medical knowledge, aiding patient understanding, and aligning with priorities in health equity, AI transparency, and digital well-being.

> This repository is included as evidence in a U.S. EB2-NIW petition for permanent residency, demonstrating national relevance and technical merit.

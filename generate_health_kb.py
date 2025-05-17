import os
import requests
from bs4 import BeautifulSoup

# Create data directory if not exists
os.makedirs("data", exist_ok=True)

def clean_text(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove unwanted tags
    for script in soup(["script", "style", "footer", "nav", "aside"]):
        script.decompose()

    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines()]
    text = "\n".join(line for line in lines if line)
    return text

def fetch_and_save(url, filename):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        cleaned = clean_text(response.text)

        # Save with source attribution
        with open(f"data/{filename}", "w", encoding="utf-8") as f:
            f.write(f"# Source: {url}\n\n")
            f.write(cleaned[:10000])  # truncate to 10k chars for clean vectorizing
        print(f"✅ Saved {filename}")
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")

# Example: Official public health sources
sources = {
    "hypertension_who.txt": "https://www.who.int/news-room/fact-sheets/detail/hypertension",
    "diabetes_nih.txt": "https://medlineplus.gov/diabetes.html",  # ✅ Replaces CDC source
    "mental_health_nih.md": "https://www.nimh.nih.gov/health/topics",
    "nutrition_basics.txt": "https://www.nutrition.gov/topics/basic-nutrition"
}




for filename, url in sources.items():
    fetch_and_save(url, filename)

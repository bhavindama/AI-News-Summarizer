import requests
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os

# 1. SETUP
model_name = "sshleifer/distilbart-cnn-12-6"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("="*60)
print(" 🤖 AI NEWS BOT")
print("="*60)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def get_full_page_content(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        paragraphs = soup.find_all('p')
        full_text = " ".join([p.get_text() for p in paragraphs if len(p.get_text()) > 50])
        return full_text
    except Exception as e:
        return f"ERROR: {e}"

def generate_summary(text):
    # This function handles the actual "thinking"
    inputs = tokenizer("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs["input_ids"], 
        max_length=150, 
        min_length=50, 
        num_beams=4, 
        early_stopping=True
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# 2. THE MAIN LOOP
if __name__ == "__main__":
    clear_screen()
    while True:
        print("\n" + "╔" + "═"*58 + "╗")
        print("║" + "🚀  AI SUMMARIZER  🚀".center(58) + "║")
        print("╚" + "═"*58 + "╝")
        
        user_link = input("\n🔗 PASTE URL: ").strip()
        if user_link.lower() == 'exit': break
        
        print("\n⏳ READING FULL ARTICLE AND GENERATING SUMMARY...")
        article_text = get_full_page_content(user_link)
        
        if "ERROR" in article_text or len(article_text) < 200:
            print("\n❌ Content too short or site blocked.")
        else:
            # If the article is very long, we split it in two and summarize both halves
            if len(article_text) > 3000:
                mid = len(article_text) // 2
                part1 = generate_summary(article_text[:mid])
                part2 = generate_summary(article_text[mid:])
                final_result = part1 + " " + part2
            else:
                final_result = generate_summary(article_text)
            
            print("\n" + "✨" + " FULL ARTICLE SUMMARY ".center(56, "-") + "✨")
            print(f"\n{final_result}")
            print("\n" + "-"*60)
        
        input("\n✅ Press ENTER to continue...")
        clear_screen()
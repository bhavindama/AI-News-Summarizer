# 🤖 AI News Summarizer

Hi! This is my Python project that uses Artificial Intelligence to read long news articles and give you a short, 2-line summary. It helps you save time by getting the main points of any news story instantly.

## 🌟 What this project does
- **Reads Any News:** You paste a link (from BBC, Times of India, etc.), and the bot "reads" the page.
- **Cleans the Mess:** It automatically ignores ads, menus, and pop-ups to find the real story.
- **Smart AI Summary:** It uses a "Transformer" model (AI) to understand the text and write a summary in its own words.
- **Handles Long Text:** If an article is very long, my code splits it into parts so the AI doesn't get confused.

## 🛠️ Tools I Used
- **Python:** The main language used for coding.
- **BeautifulSoup:** For "scraping" or pulling text from websites.
- **Hugging Face:** For the AI model that does the actual summarizing.
- **Requests:** To connect the script to the internet.

## 🚀 How to use it
1. **Download the code** to your computer.
2. **Install the requirements** (open your terminal and type):
   ```bash
3.  pip install requests beautifulsoup4 transformers torch
Run the script:

Bash
python main.py
4.  Paste a URL from a news site and press Enter!

📈 Example
Input URL: A long article about a Space Mission.
Output: "NASA successfully tested its new rocket fuel today in Florida. The mission aims to send humans back to the moon by 2026."

📚 What I learned
How to extract data from websites (Web Scraping).

How to use pre-trained AI models to process human language (NLP).

How to handle errors like "Page Not Found" or "Connection Timeout."

Developed by: BHAVIN DAMA
Contact: https://linkedin.com/in/bhavin-dama-23bd

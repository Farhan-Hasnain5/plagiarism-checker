import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Replace with your Bing Search API key
BING_API_KEY = '794dd43999bc4d3c80f7261aa79399cc'
BING_SEARCH_URL = 'https://api.bing.microsoft.com/v7.0/search'

def fetch_web_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    return cosine_sim[0][1]

def search_bing(query):
    headers = {'Ocp-Apim-Subscription-Key': BING_API_KEY}
    params = {'q': query, 'textDecorations': True, 'textFormat': 'HTML'}
    response = requests.get(BING_SEARCH_URL, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    return [result['url'] for result in search_results['webPages']['value']]

def check_plagiarism(input_text):
    urls = search_bing(input_text)
    similarities = []
    for url in urls:
        web_content = fetch_web_content(url)
        similarity = calculate_similarity(input_text, web_content)
        similarities.append(similarity)
    return max(similarities) * 100

def on_check_plagiarism():
    input_text = text_area.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text to check for plagiarism.")
        return
    plagiarism_percentage = check_plagiarism(input_text)
    result_label.config(text=f"Plagiarism Percentage: {plagiarism_percentage:.2f}%")

# Set up the GUI
root = tk.Tk()
root.title("Plagiarism Checker")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=20)
text_area.pack(padx=10, pady=10)

check_button = tk.Button(frame, text="Check Plagiarism", command=on_check_plagiarism)
check_button.pack(pady=10)

result_label = tk.Label(frame, text="Plagiarism Percentage: N/A")
result_label.pack(pady=10)

root.mainloop()
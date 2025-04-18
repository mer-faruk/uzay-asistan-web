import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"


def gpt_cevap_al(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/omerfarukkocakaya",
        "X-Title": "GPT CLI Asistan"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "Cevap verirken kullanıcının dilinde cevap ver. Girdi Türkçe ise Türkçe yanıtla, İngilizce ise İngilizce."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Hata oluştu: {response.status_code} - {response.text}"
    

def main():
    print(" 👀 GPT Komut Satırı Asistanı (çıkmak için 'q' yaz)")
    while True:
        mesaj = input("Sen: ")
        if mesaj.lower() == 'q':
            break
        cevap = gpt_cevap_al(mesaj)
        print("Asistan:", cevap)

if __name__ == "__main__":
    main()
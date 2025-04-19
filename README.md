 👀 Uzay Asistan Web

GPT destekli komut satırı asistanı projesinin Flask ile web arayüzü halidir. Kullanıcılar basit bir web arayüzüyle OpenRouter API aracılığıyla LLM (Large Language Model) tabanlı cevaplar alabilir.

  Özellikler
- Flask tabanlı backend
- HTML (Jinja2) destekli frontend
- .env ile güvenli API anahtarı yönetimi
- OpenRouter üzerinden ücretsiz model desteği (örnek: `mistralai/mistral-7b-instruct`)

  Kurulum
bash
git clone https://github.com/mer-faruk/uzay-asistan-web.git
cd uzay-asistan-web
python -m venv venv
venv\Scripts\activate  # macOS/Linux icin: source venv/bin/activate
pip install -r requirements.txt


 API Anahtarı
.env dosyasına şu satırı eklemeyi unutma:
OPENROUTER_API_KEY=sk-xxxxxx...


 Çalıştırma
bash
python app.py

Tarayıcında `http://127.0.0.1:5000/` adresini açarak kullanabilirsin.

📂 Proje Yapısı

├── app.py
├── cli_asistan.py
├── config.py
├── .env
├── templates
│   └── index.html
├── static
│   └── style.css
└── requirements.txt


Demo
(Ekran görüntüsü veya gif buraya eklenecek)

👤 Geliştirici
Ömer Faruk Kocakaya
GitHub: [@mer-faruk](https://github.com/mer-faruk)


⭐ Eğer projeyi faydalı bulduysan repo'ya yıldız bırakmayı unutma!


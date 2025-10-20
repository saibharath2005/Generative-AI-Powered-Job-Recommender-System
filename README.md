📄 AI Job Recommender App

This project is an AI-powered Job Recommendation System built with Streamlit. It analyzes your uploaded resume (PDF), summarizes your profile, identifies skill gaps, provides a career roadmap, and recommends relevant jobs from LinkedIn and Naukri — all powered by **Groq AI using the `openai/gpt-oss-20b` model**, with **job scraping via Apify** and **automation using MCP**.

---

🚀 Features

* Upload a PDF resume.
* Extract and summarize experience, education, and skills using `openai/gpt-oss-20b` via Groq.
* Detect missing skills or certifications (skill gap analysis).
* Generate a personalized career roadmap.
* Extract job search keywords from resume summary.
* Fetch job listings from LinkedIn and Naukri via Apify actors or MCP automation.
* Clean Streamlit interface with loading spinners for smooth user experience.

---

🧩 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI Model:** `openai/gpt-oss-20b` via Groq
* **Automation & Scraping:** MCP, Apify
* **Libraries:**

  * `openai`
  * `apify-client`
  * `streamlit`
  * `pymupdf`
  * `python-dotenv`

---

⚙️ Setup Instructions

1. Clone the repository:

```
git clone https://github.com/your-username/AI-Job-Recommender.git
cd AI-Job-Recommender
```

2. Create a virtual environment and activate it:

```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Add your API keys in `.env`:

```
GROQ_API_KEY=your_groq_api_key_here
APIFY_API_KEY=your_apify_api_key_here
```

> MCP may require local configuration depending on the automation scripts.

---

▶️ Run the App

```
streamlit run app.py
```

Then open the URL displayed in the terminal (usually [http://localhost:8501](http://localhost:8501)).

---

🧠 How It Works

1. Upload your resume (PDF).
2. Extract text using **PyMuPDF (`fitz`)**.
3. **GPT-OSS-20B via Groq** summarizes the resume, identifies skill gaps, and generates a career roadmap.
4. Job keywords are extracted from the summary.
5. **Apify** or **MCP automation** fetches jobs from LinkedIn and Naukri.
6. Streamlit displays the results with **loading spinners** for a smooth UX.

---

🧾 Example Prompts

* Summarization: `Summarize this resume highlighting the skills, education, and experience.`
* Skill Gaps: `Analyze this resume and highlight missing skills or certifications.`
* Roadmap: `Suggest a future career roadmap.`
* Job Keywords: `Suggest top job titles and keywords (comma-separated only).`

---

🛡️ Security Notes

* Keep **API keys private** — do not commit `.env` files.
* Use environment variables in production.
* Rotate keys regularly.

---

✅ Requirements (`requirements.txt`)

```
openai
apify-client
streamlit
pymupdf
python-dotenv
requests
```

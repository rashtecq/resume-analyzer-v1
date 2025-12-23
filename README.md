## Resume Analyzer & Skill Gap Advisor (Local AI)

A **privacy-first, local GenAI application** that analyzes a resume against a job description to identify **skill match percentage, gaps, strengths, and improvement suggestions** — running entirely on your local machine using **Ollama + Llama 3.1** .

## 🚀 Features

* 📤 Upload resume (PDF / DOCX)
* 📋 Paste job description
* 🧠 AI-powered analysis:
  * Skill match percentage
  * Matched skills
  * Missing skills
  * Resume improvement suggestions
* 🔒 Fully local execution (no cloud APIs)
* ⚡ Optimized for Apple Silicon (M1/M2)

## 🛠️ Tech Stack


| Component      | Tool                   |
| ---------------- | ------------------------ |
| LLM            | Llama 3.1 (via Ollama) |
| Framework      | LangChain-community    |
| UI             | Streamlit              |
| Resume Parsing | PyPDF, python-docx     |
| Runtime        | Python 3.10+           |

## Architecture (v1)

<pre class="overflow-visible! px-0!" data-start="1684" data-end="1816"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="@w-xl/main:top-9 sticky top-[calc(--spacing(9)+var(--header-height))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span><span class="hljs-keyword">Resume</span></span><span> + Job Description
        ↓
   </span><span><span class="hljs-keyword">Text</span></span><span> Extraction
        ↓
 Prompt-based LLM Analysis
        ↓
 Structured AI Insights</span></span></code></div></div></pre>

**Note:** v1 intentionally avoids vector databases to keep the system simple and transparent.

## ⚙️ Prerequisites

* macOS (Apple Silicon recommended)
* Python 3.10+
* Ollama installed

### Install Ollama

<pre class="overflow-visible! px-0!" data-start="2031" data-end="2083"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="@w-xl/main:top-9 sticky top-[calc(--spacing(9)+var(--header-height))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>brew install ollama
ollama pull llama3.1</span></span></code></div></div></pre>

## 🧪 Setup & Run

### 1️⃣ Clone the Repository

<pre class="overflow-visible! px-0!" data-start="2138" data-end="2233"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="@w-xl/main:top-9 sticky top-[calc(--spacing(9)+var(--header-height))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span><span class="hljs-built_in">clone</span></span><span> https://github.com/rashtecq/resume-analyzer-v1.git
</span><span><span class="hljs-built_in">cd</span></span><span> resume-analyzer-v1
</span></span></code></div></div></pre>

### 2️⃣ Create Virtual Environment

<pre class="overflow-visible! px-0!" data-start="2270" data-end="2327"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="@w-xl/main:top-9 sticky top-[calc(--spacing(9)+var(--header-height))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python3 -m venv venv
</span><span><span class="hljs-built_in">source</span></span><span> venv/bin/activate
</span></span></code></div></div></pre>

### 3️⃣ Upgrade pip (recommended)

<pre class="overflow-visible! px-0!" data-start="2363" data-end="2410"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="@w-xl/main:top-9 sticky top-[calc(--spacing(9)+var(--header-height))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m pip install --upgrade pip
</span></span></code></div></div></pre>

### 4️⃣ Install Dependencies

<pre class="overflow-visible! px-0!" data-start="2441" data-end="2484"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="@w-xl/main:top-9 sticky top-[calc(--spacing(9)+var(--header-height))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
</span></span></code></div></div></pre>

### 5️⃣ Run the App

<pre class="overflow-visible! px-0!" data-start="2506" data-end="2538"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="@w-xl/main:top-9 sticky top-[calc(--spacing(9)+var(--header-height))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>streamlit run app.py
</span></span></code></div></div></pre>

---

## 📊 Sample Output

* ✅ Skill Match: **72%**
* ✔️ Matched Skills: Python, Docker, CI/CD
* ❌ Missing Skills: Kubernetes, MLOps
* ✍️ Resume Suggestions:
  * Add measurable achievements
  * Highlight cloud-native experience

---

## 🧩 Project Motivation

This project demonstrates:

* Practical **Generative AI usage**
* Prompt engineering
* Local LLM orchestration
* Privacy-aware AI design

It is ideal for:

* AI portfolio projects
* Career transition into AI / GenAI
* Demonstrating real-world LLM applications

---

## 🚧 Roadmap

* [ ] Skill match scoring with progress bars
* [ ] Embedding-based semantic skill matching
* [ ] Resume bullet point rewriter
* [ ] Multiple job description comparison
* [ ] Export improved resume (PDF/DOCX)
* [ ] RAG-based version (v2)

---

## 📜 License

MIT License

---

## 🙌 Author

**Rajesh Sharma**

DevOps Engineer | GenAI Enthusiast

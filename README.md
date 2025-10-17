# 🧬 Bio-Trends: Journey to Fight Aging with AI

My learning journey from zero to using artificial intelligence for anti-aging research

## 📖 What is this repo?

A structured, project-based learning path for:
- Learning Machine Learning and Deep Learning
- Working with biological and medical data
- Conducting research in longevity and anti-aging
## 🎯 Where am I right now?


→ **see:** [`00-ROADMAP/current-phase.md`](00-ROADMAP/current-phase.md)

## 📋 What’s the next step?


→ **see:** [`00-ROADMAP/next-steps.md`](00-ROADMAP/next-steps.md)

## 📚 Guides


- [How do I start?](01-GUIDES/how-to-start.md)
- [I’m having trouble!](01-GUIDES/debugging-guide.md)

## 📊 My progress


→ **see:** [`02-LOGS/week-01.md`](02-LOGS/week-01.md)

## 🗂️ Repo Structure

```
bio-trends/
├── 00-ROADMAP/        # نقشه کلی و وضعیت فعلی
├── 01-GUIDES/         # راهنماهای قدم‌به‌قدم
├── 02-LOGS/           # گزارش روزانه/هفتگی
├── 03-CONTEXT-FOR-AI.md  # برای وقتی که چت لیمیت می‌خوره
└── projects/          # پروژه‌های واقعی (به زودی)
```

## 🚀 Planned Projects

1. **Health Data Analyzer** – Personal health data analysis
2. **Disease Classifier** – Classification of age-related diseases
3. **Biological Age Predictor** – Biological age prediction
4. **Cell Image Analysis** – Microscopic image analysis
5. **Longevity Predictor** – Lifespan prediction model
6. **Anti-Aging Recommender** – Intervention recommendation system

## 💡 Philosophy of this Repo

* **Self-Documenting:** Everything is documented, even when I’m not around
* **Progressive:** Step-by-step, from simple to complex
* **Practical:** All project-based and hands-on
* **Open:** Everyone can view and learn

---

## ✅ Step 3: Create a .gitignore file

Edit or create the .gitignore file:```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv

# Jupyter
.ipynb_checkpoints
*.ipynb

# Data
*.csv
*.xlsx
*.h5
*.pkl
data/raw/
data/processed/

# Models
models/*.pt
models/*.h5
*.pth

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Personal
TODO_personal.md
secrets/ 

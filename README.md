<div align="center">

# 🚀 Resume Analyzer Pro
### *AI-powered resume analysis tool that gives you instant scores and improvement suggestions!*

<img src="https://github.com/sonall99/AI-Resume-Analyzer/blob/main/Screenshot%202025-08-24%20194339.png" alt="Resume Analyzer Pro Banner" width="700"/>

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://python.org)
[![AI Powered](https://img.shields.io/badge/AI-Powered-green.svg)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/sonall99/AI-Resume-Analyzer?style=social)](https://github.com/sonall99/AI-Resume-Analyzer)

**📊 ANALYZE • 🎯 OPTIMIZE • 🚀 SUCCEED**

</div>

## ✨ Features

- 📊 **Resume Scoring** - ML-powered analysis with TF-IDF + XGBoost
- 🤖 **AI Suggestions** - GPT-generated improvement tips
- 📄 **PDF Upload** - Easy drag-and-drop interface
- 📱 **Responsive Design** - Works on all devices
- ⚡ **Fast Results** - Get insights in seconds

## 🛠 Tech Stack

- **Frontend**: HTML, CSS, Tailwind, JavaScript
- **Backend**: FastAPI(Python)
- **ML**: scikit-learn, TF-IDF, XGBoost
- **AI**: Google Gemini API
- **Deployment**: Vercel+Render

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables
```bash
# Create .env file
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run Backend
```bash
uvicorn main:app --reload
```

### 5. Run Frontend
```bash
cd frontend
python -m http.server 8080
# OR open index.html in browser
```

Visit `http://localhost:8080` to start analyzing resumes!

## 📁 Project Structure

```
Resume-Analyzer/
│
├── Backend/                     # Backend (API + ML Model)
│   ├── Backend.py                # Main backend application (Flask/FastAPI)
│   ├── Final.ipynb               # Model training & experiments notebook
│   ├── final_model.joblib        # Trained ML model (XGBoost / Classifier)
│   ├── final_vectorizer.joblib   # TF-IDF vectorizer
│   ├── requirements.txt          # Backend dependencies
│   └── __pycache__/              # Compiled python cache (ignored)
│
├── Frontend/                    # Frontend (React + Vite + Tailwind)
│   ├── index.html                # Entry point
│   ├── package.json              # Node dependencies
│   ├── vite.config.ts            # Vite config
│   ├── tailwind.config.js        # Tailwind config
│   ├── src/                      # React source files
│   │   ├── app.jsx               # Main app logic
│   │   ├── main.jsx              # React DOM render
│   │   ├── App.css               # App styles
│   │   ├── index.css             # Global styles
│   │   └── assets/               # Static assets (icons, images)
│   └── public/                   # Public static files
│
├── Data/                        # Dataset & Model JSON
│   ├── resume_job_matching_dataset.csv
│   └── resume_model.json
│
├── Screenshots/                 # App demo screenshots
│   ├── upload_resume.png
│   ├── score_result.png
│   ├── suggestions.png
│   └── mobile_view.png
│
├── README.md                    # Project documentation
└── .gitignore                   # Git ignore rules

```

## 🎯 How to Use

1. **Upload** your resume (PDF format)
2. **Click** "Analyze Resume" button
3. **Get** your score (0-100) and AI suggestions
4. **Improve** your resume based on feedback


### 🎬 **User Journey Flow**

| Step 1: Upload | Step 2: Analysis | Step 3: Suggestions | Step 4: Results |
|:---:|:---:|:---:|:---:|
| ![Upload](https://github.com/sonall99/AI-Resume-Analyzer/blob/main/Screenshot%202025-08-24%20194339.png) | ![Analysis](https://github.com/sonall99/AI-Resume-Analyzer/blob/main/Screenshot%202025-08-24%20194434.png) | ![Suggestions](https://github.com/sonall99/AI-Resume-Analyzer/blob/main/Screenshot%202025-08-24%20194503.png) | ![Results](https://github.com/sonall99/AI-Resume-Analyzer/blob/main/Screenshot%202025-08-24%20195001.png) |
| *Easy drag & drop* | *ML-powered scoring* | *AI recommendations* | *Track improvements* |

---

## ✨ **Key Features Showcase**

<table>
<tr>
<td width="50%">
<h3>🎨 Beautiful UI/UX</h3>
<img src="https://github.com/sonall99/AI-Resume-Analyzer/blob/main/Screenshot%202025-08-24%20194339.png" alt="UI Design" width="100%"/>
<ul>
<li>✅ Clean, modern interface</li>
<li>✅ Responsive design</li>
<li>✅ Intuitive navigation</li>
<li>✅ Professional aesthetics</li>
</ul>
</td>
<td width="50%">
<h3>🧠 Smart Analytics</h3>
<img src="https://github.com/sonall99/AI-Resume-Analyzer/blob/main/Screenshot%202025-08-24%20194434.png" alt="Analytics" width="100%"/>
<ul>
<li>✅ ML-powered scoring</li>
<li>✅ Detailed breakdowns</li>
<li>✅ Performance metrics</li>
<li>✅ Visual indicators</li>
</ul>
</td>
</tr>
<tr>
<td width="50%">
<h3>🤖 AI Recommendations</h3>
<img src="https://github.com/sonall99/AI-Resume-Analyzer/blob/main/Screenshot%202025-08-24%20194503.png" alt="AI Features" width="100%"/>
<ul>
<li>✅ GPT-powered insights</li>
<li>✅ Personalized tips</li>
<li>✅ Actionable advice</li>
<li>✅ Industry-specific suggestions</li>
</ul>
</td>
<td width="50%">
<h3>📈 Progress Tracking</h3>
<img src="https://github.com/sonall99/AI-Resume-Analyzer/blob/main/Screenshot%202025-08-24%20195001.png" alt="Progress Tracking" width="100%"/>
<ul>
<li>✅ Success metrics</li>
<li>✅ Improvement tracking</li>
<li>✅ Goal achievement</li>
<li>✅ Performance history</li>
</ul>
</td>
</tr>
</table>

## 🎬 **Live Demo**

<div align="center">

### 🌟 **See It In Action!**

[![Demo](https://img.shields.io/badge/🚀%20LIVE%20DEMO-Try%20It%20Now!-success?style=for-the-badge&logo=rocket)](https://ai-resume-analyze-rose.vercel.app/)

*Experience the power of AI-driven resume analysis*

---

### 📱 **Mobile & Desktop Ready**

| 💻 Desktop View | 📱 Mobile Responsive |
|:---:|:---:|
| ![Desktop](https://github.com/sonall99/AI-Resume-Analyzer/blob/main/Screenshot%202025-08-24%20194339.png) | Perfect for all screen sizes! |

</div>

## 🤝 Contributing

1. Fork the repo
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## 📝 Requirements

### Backend Dependencies
- FastAPI for web framework
- scikit-learn for machine learning
- pandas and numpy for data processing
- XGBoost for advanced ML models
- Gemini for AI suggestions
- PyPDF2 for PDF processing
- python-dotenv for environment variables



## 📄 License

MIT License - feel free to use this project for learning and development!


---

**⭐ Star this repo if it helped you!**

Made with ❤️ by [Sonal Singh](https://github.com/sonall99)

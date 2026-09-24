# Noted! 📝 — AI-Powered Note Taking Web Application

Noted! is an intelligent note-taking web application that allows users to create, edit, format, enhance, and download notes with the power of AI. Built for simplicity, productivity, and a seamless cloud experience.

## 🎯 Aim

To develop an AI-powered note-taking web application that allows users to create, edit, enhance, and download their notes intelligently using artificial intelligence.

## 🚀 Features

- ✍️ Create, edit, and organize notes effortlessly
- 🤖 AI-powered note enhancement (grammar correction, clarity improvement, better phrasing) via **Gemini AI API**
- 🎨 Rich text formatting — Bold, Italic, Underline
- 🗑️ Delete or clear notes anytime
- 📄 Download notes as `.docx` documents

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML, CSS, Bootstrap, JavaScript |
| **Backend** | Python (Flask) |
| **AI Integration** | Gemini AI API |
| **IDE** | Visual Studio Code |


## 📐 Project Workflow

The application is structured into four main layers:

1. **Frontend (UI)** — Built with HTML, CSS & Bootstrap; provides an interface for writing and formatting notes.
2. **Backend (Flask)** — Manages routes for creating, deleting, enhancing, and downloading notes.
3. **AI Integration (Gemini API)** — Processes note content to improve grammar, clarity, and phrasing.

---

## ⚙️ Core Functionalities

| Feature | Description |
|---|---|
| **Create New Note** | Initializes a new text area for writing |
| **Delete Note** | Removes the selected note from the backend |
| **Clear Note** | Clears note content without deleting it |
| **Enhance Note (AI)** | Sends note text to Gemini API and returns an enhanced version |
| **Formatting Tools** | JavaScript-powered Bold, Italic, Underline |
| **Download Note** | Exports the note as a `.docx` file |

## 📂 Project Structure

```
Noted/
├── templates/
│   └── index.html
├── .gitignore
├── LICENSE
├── README.md
├── main.py
└── requirements.txt
```

## 🖥️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/soorya-prakash-r/Noted-AI-powered-Notes-Taking-app.git
   cd Noted-AI-powered-Notes-Taking-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. Open `http://localhost:5000` in your browser.

## 📄 License

This project is licensed under the terms of the [LICENSE](./LICENSE) file included in this repository.

## 👤 Author

**Soorya Prakash R**

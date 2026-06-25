# 🚀 Social Media Content Generator

Generate engaging, platform-optimized social media content directly from your terminal using Google Gemini AI.

## ✨ Features

- 🎯 Generate content for a single platform or multiple platforms at once
- 🤖 Powered by Google Gemini AI
- 🎨 Multiple tone options:
  - Professional
  - Casual
  - Humorous
  - Inspirational
- #️⃣ Custom hashtag support
- 📣 Optional call-to-actions (CTAs)
- 😀 Emoji control
- 📊 Content statistics and history tracking
- 💾 Export content as TXT or JSON
- 🖥️ Fully terminal-based workflow

## 📱 Supported Platforms

- Twitter/X
- Instagram
- LinkedIn
- TikTok
- Facebook
- YouTube
- Pinterest
- Threads
- Bluesky
- Mastodon

---

## 🏗️ Project Structure

```text
social-media-generator/
├── social_media_generator.py
├── content_generator.py
├── config.py
├── utils.py
├── requirements.txt
├── README.md
└── generated_content/
```

---

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API Key
- Internet connection

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/social-media-generator.git
cd social-media-generator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API Key

**Windows (CMD)**

```bash
set GEMINI_API_KEY=your_api_key_here
```

**Windows (PowerShell)**

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

**macOS/Linux**

```bash
export GEMINI_API_KEY="your_api_key_here"
```

Get your API key from: https://ai.google.dev

---

## 🚀 Usage

Start the application:

```bash
python social_media_generator.py
```

### Main Menu

1. Generate content for a specific platform
2. Generate content for multiple platforms
3. View content history
4. Save content to file
5. Settings
6. Exit

---

## 📝 Example

### Input

```text
Topic: Product Launch Announcement
Tone: Professional
Platforms: Twitter, LinkedIn, Instagram
Hashtags: Enabled
CTA: Enabled
Emojis: Enabled
```

### Output

The application generates platform-specific content optimized for audience expectations, character limits, and engagement patterns.

---

## 📊 Platform Configuration

| Platform | Max Length |
|----------|-----------:|
| Twitter/X | 280 |
| Instagram | 2200 |
| LinkedIn | 3000 |
| TikTok | 1500 |
| Facebook | 5000 |

---

## 💡 Best Practices

- Use specific topics for better results.
- Match the tone to your target audience.
- Keep hashtag counts platform appropriate.
- Review generated content before publishing.
- Test multiple variations for higher engagement.

---

## 📂 Output Options

Generated content can be:

- Saved as `.txt` files
- Exported as `.json`
- Stored in generation history
- Organized by timestamp

---

## 🛠️ Troubleshooting

### API Key Not Found

Verify that `GEMINI_API_KEY` is correctly configured.

### Module Not Found

Install dependencies:

```bash
pip install -r requirements.txt
```

### Content Generation Errors

- Check internet connectivity
- Verify API key validity
- Retry the request

---

## 🔮 Roadmap

- [ ] Image generation support
- [ ] Post scheduling
- [ ] Analytics integration
- [ ] Content calendar
- [ ] A/B testing suggestions
- [ ] Multi-language support

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 📜 License

This project uses the Google Gemini API.

Review the Google AI Terms of Service before deployment.

---

## ⭐ Support

If you find this project useful, consider giving it a star on GitHub.

Happy content creation! 🎉

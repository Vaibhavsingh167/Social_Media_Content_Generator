# 🚀 Social Media Content Generator

A powerful, terminal-based social media content generation system using Google's Gemini AI API. Generate engaging, platform-optimized content for Twitter, Instagram, LinkedIn, TikTok, Facebook, YouTube, Pinterest, Threads, Bluesky, and Mastodon—all from your terminal!

---

## ✨ Features

### 🎯 Core Functionality
- **Single Platform Generation**: Create content for one platform at a time
- **Multi-Platform Generation**: Generate optimized content for multiple platforms simultaneously
- **Smart Content Customization**:
  - Adjustable tone (Professional, Casual, Humorous, Inspirational)
  - Optional hashtags with custom counts
  - Call-to-action (CTA) options
  - Emoji inclusion control
  
### 📱 Supported Platforms
1. **Twitter/X** - 280 character limit, real-time engagement
2. **Instagram** - Visual storytelling, up to 2,200 characters
3. **LinkedIn** - Professional content, industry insights
4. **TikTok** - Trendy, casual short-form captions
5. **Facebook** - Community engagement, longer posts
6. **YouTube** - Detailed descriptions and tags
7. **Pinterest** - Visual discovery, inspirational content
8. **Threads** - Text-based social networking
9. **Bluesky** - Decentralized social network
10. **Mastodon** - Federated social network

### 🛠️ Advanced Features
- **Content History**: Track all generated content with timestamps
- **File Management**: Save content to organized files
- **Content Statistics**: Character count, word count, hashtag analysis
- **Batch Processing**: Generate variations and optimize content
- **Multi-format Output**: Save as text files or JSON

---

## 📋 Prerequisites

- **Python 3.8 or higher**
- **Google Gemini API Key** (free tier available at [https://ai.google.dev](https://ai.google.dev))
- **Internet Connection**

---

## 🔧 Installation

### Step 1: Clone or Download the Project
```bash
# Navigate to your desired directory
cd your-project-directory
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Key
#### Option A: Environment Variable
```bash
# On Windows (Command Prompt):
set GEMINI_API_KEY=your_api_key_here

# On Windows (PowerShell):
$env:GEMINI_API_KEY='your_api_key_here'

# On macOS/Linux:
export GEMINI_API_KEY='your_api_key_here'
```

## 🚀 How to Run

### Start the Application
```bash
python social_media_generator.py
```

### First Run Experience
1. Application initializes and connects to Gemini API
2. Main menu displays with 6 options
3. Follow prompts to generate content

---

## 📖 Usage Guide

### Main Menu Options

#### 1️⃣ Generate Content for a Specific Platform
- Select one platform from the list
- Enter your topic/theme
- Choose tone (Professional, Casual, Humorous, Inspirational)
- Configure optional features:
  - Include hashtags? (Yes/No + count)
  - Include call-to-action? (Yes/No)
  - Include emojis? (Yes/No)
- Content is generated and displayed
- Option to save to file

**Example Workflow:**
```
Select an option: 1
Available platforms:
  1. Twitter
  2. Instagram
  3. LinkedIn
  ...
Select platform (number): 2
Enter the topic/theme for content: Summer travel tips
Enter tone (professional/casual/humorous/inspirational) [professional]: casual
Include hashtags? (y/n) [y]: y
Number of hashtags (1-10) [5]: 8
Add call-to-action? (y/n) [y]: y
Include emojis? (y/n) [y]: y
```

#### 2️⃣ Generate Multi-Platform Content
- Select multiple platforms (comma-separated)
- Provide topic and configuration once
- Content is generated for all selected platforms
- Preview all content with platform separators
- Save all at once

**Example Workflow:**
```
Select an option: 2
Select platforms: 1,2,3
Enter the topic/theme for content: Product launch announcement
Enter tone: professional
Include hashtags? (y/n) [y]: y
```

#### 3️⃣ View Generation History
- See all previously generated content
- Timestamps and platform info included
- View full content of any previous generation
- Review multiple items in one session

#### 4️⃣ Save Content to File
- Export entire history as JSON
- Organized by date and time
- Stored in `generated_content/` directory
- Easy backup and reference

#### 5️⃣ Settings
- **View API Status**: Confirm API connection
- **View Platform Configurations**: See details for each platform
- **Clear History**: Reset content history (with confirmation)

#### 6️⃣ Exit
- Gracefully close the application
- History is preserved for current session

---

## 💡 Best Practices

### Tips for Better Content

1. **Be Specific with Topics**
   - ✅ "Budget-friendly home office setup tips"
   - ❌ "Work from home"

2. **Choose Appropriate Tone**
   - **Professional**: B2B, business updates, corporate communications
   - **Casual**: Lifestyle, entertainment, personal brands
   - **Humorous**: Entertainment, tech, young audiences
   - **Inspirational**: Self-help, motivation, wellness

3. **Hashtag Strategy**
   - Twitter: 2-3 hashtags
   - Instagram: 8-10 hashtags
   - LinkedIn: 3-5 hashtags
   - TikTok: 8-12 hashtags

4. **Call-to-Action Examples**
   - "Learn more below 👇"
   - "Tag someone who needs this!"
   - "Share your thoughts in the comments"
   - "Click the link in bio"

5. **Platform Optimization**
   - Twitter: Keep it punchy and timely
   - Instagram: Tell a story, use line breaks
   - LinkedIn: Professional insights and value
   - TikTok: Trend-focused and entertaining

---

## 📁 Project Structure

```
social-media-generator/
├── social_media_generator.py  # Main application entry point
├── content_generator.py        # Gemini API integration
├── config.py                   # Platform configurations
├── utils.py                    # Utility functions
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── generated_content/          # Output folder (created automatically)
    ├── twitter_2024-01-15_10-30-45.txt
    ├── instagram_2024-01-15_10-32-12.txt
    └── ...
```

---

## 🔑 API Key Management

### Getting Your Google Gemini API Key

1. Visit [https://ai.google.dev](https://ai.google.dev)
2. Click "Get API Key" or "Gemini API"
3. Create a new API key (free tier available)
4. Copy your API key
5. Set it as environment variable or use the embedded key

### Security Best Practices
- ✅ Use environment variables in production
- ✅ Never commit API keys to version control
- ✅ Regenerate keys periodically
- ⚠️ The embedded key is for demonstration only

---

## 📊 Output Examples

### Generated Content Samples

#### Twitter Content
```
Just launched our new blog on digital marketing trends! 📱
Discover why video content is dominating 2024 and how to 
leverage it for your brand. Read the full insights here 👇
#Marketing #ContentStrategy #DigitalTrends
```

#### Instagram Content
```
Summer Goals ☀️✨

Ready to transform your fitness journey this season? 

Our new workout program is designed specifically for outdoor 
enthusiasts who want to stay active while enjoying the weather.

🏃‍♀️ Flexible scheduling
💪 Beginner-friendly
🌿 Nature-inspired routines

Link in bio to get started! 

#FitnessCommunity #SummerWorkout #HealthyLifestyle
```

#### LinkedIn Content
```
The Future of Remote Work

After analyzing 5000+ companies, we've identified key trends 
shaping the workplace in 2024:

• Hybrid models are here to stay
• Well-being initiatives are non-negotiable
• Async communication is becoming essential

Companies prioritizing these elements see 40% higher retention 
rates. Ready to adapt?

#FutureOfWork #RemoteWork #WorkplaceTrends
```

---

## ⚙️ Configuration Details

### Platform Configurations

Each platform has unique settings:

| Platform | Max Length | Tone | Features |
|----------|-----------|------|----------|
| Twitter | 280 chars | Concise | Real-time engagement |
| Instagram | 2,200 chars | Narrative | Visual storytelling |
| LinkedIn | 3,000 chars | Professional | Thought leadership |
| TikTok | 1,500 chars | Casual | Trendy content |
| Facebook | 5,000 chars | Conversational | Community building |

### Customization

Modify `config.py` to adjust:
- Platform character limits
- Recommended hashtag counts
- Default tones
- Content features

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "API Key not found"**
- Solution: Set GEMINI_API_KEY environment variable or ensure the embedded key is present
- Command: `export GEMINI_API_KEY='your-key-here'`

**Issue: "Error generating content"**
- Solution: Check internet connection, verify API key validity
- Retry the generation

**Issue: "Permission denied when saving files"**
- Solution: Ensure you have write permissions in the directory
- Try running from a different folder

**Issue: "Module not found"**
- Solution: Install dependencies: `pip install -r requirements.txt`
- Verify Python version: `python --version` (should be 3.8+)

**Issue: "Content too short/long"**
- Solution: Different tones and platforms produce varying lengths
- Regenerate to get different output

---

## 🔄 Workflow Example

### Scenario: Launch a Product

1. **Start Application**
   ```bash
   python social_media_generator.py
   ```

2. **Select Multi-Platform Generation**
   - Option 2: Generate multi-platform content

3. **Configure**
   - Platforms: Twitter, Instagram, LinkedIn, TikTok
   - Topic: "Launching AI-powered task management tool"
   - Tone: Professional
   - Include: Hashtags, CTA, Emojis

4. **Review**
   - See all 4 platform-specific versions
   - Each optimized for platform norms

5. **Save**
   - Save all content to files
   - Each saved separately by platform

6. **Use**
   - Copy content to respective platforms
   - Schedule posts as needed
   - Track engagement

---

## 📈 Advanced Features

### Content Statistics

After generation, you can:
- Check character count vs. platform limits
- Count hashtags and emojis
- Analyze word count
- View line-by-line breakdown

### Content Variations

Request multiple versions:
- Different tones for same topic
- Platform-specific angles
- A/B testing variants
- Seasonal variations

### Export Options

- **Text Files**: Individual `.txt` files per platform
- **JSON Export**: Batch export for integration
- **History Tracking**: Timestamp all generations

---

## 🤝 Contributing & Support

### Reporting Issues
- Note platform, topic, and tone used
- Include error messages
- Describe expected vs. actual behavior

### Feature Requests
- Suggest new platforms
- Propose content types
- Recommend improvements

---

## 📜 License

This project uses the Google Gemini API (free tier).
See [Google AI Terms of Service](https://ai.google.dev/terms) for API usage terms.

---

## 🎓 Learning Resources

### Content Strategy
- [HubSpot Blog](https://blog.hubspot.com/marketing/social-media-content-strategy)
- [Buffer Social Media Guide](https://buffer.com/library/social-media-marketing/)

### Platform Best Practices
- [Twitter/X Best Practices](https://help.twitter.com/en/using-twitter/best-practices)
- [Instagram Creator Guidelines](https://creators.instagram.com/guidelines)
- [LinkedIn Content Tips](https://business.linkedin.com/marketing-solutions/content-marketing)

### Google Gemini API
- [Official Documentation](https://ai.google.dev/docs)
- [API Reference](https://ai.google.dev/api)

---

## 🎉 Quick Start Cheat Sheet

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set API key
export GEMINI_API_KEY='your-key-here'

# 3. Run application
python social_media_generator.py

# 4. Generate content
# Follow the interactive prompts in the terminal

# 5. Find saved content
# Check the 'generated_content/' folder
```

---

## ✅ What's Included

- ✅ 10 popular social media platforms
- ✅ 4 content tones (Professional, Casual, Humorous, Inspirational)
- ✅ Customizable hashtags, CTAs, and emojis
- ✅ Content history and tracking
- ✅ File export functionality
- ✅ Color-coded terminal UI
- ✅ Comprehensive error handling
- ✅ Content statistics
- ✅ Multi-platform batch processing
- ✅ Fully terminal-based (no frontend required)

---

## 🚀 Future Enhancements

Potential features for future versions:
- [ ] Image generation for social content
- [ ] Scheduling capability
- [ ] Analytics integration
- [ ] Content calendar view
- [ ] A/B testing suggestions
- [ ] Hashtag trend analysis
- [ ] Competitor analysis
- [ ] Multi-language support

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review example workflows
3. Verify API key configuration
4. Check internet connection
5. Review Google Gemini API documentation

---

**Happy Content Creation! 🎉**

Generate amazing social media content with the power of Google Gemini AI. Your brand's voice, amplified. 📱✨

---

*Last Updated: January 2024*
*Version: 1.0.0*
*Built with ❤️ using Python and Google Gemini API*
#   S o c i a l _ M e d i a _ C o n t e n t _ G e n e r a t o r  
 
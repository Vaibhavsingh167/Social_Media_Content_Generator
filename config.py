"""
Configuration file for Social Media Content Generator
Defines platform-specific settings and default configurations
"""

# Platform configurations
PLATFORM_CONFIGS = {
    "twitter": {
        "name": "Twitter/X",
        "max_length": 280,
        "description": "Short, punchy posts with character limits",
        "hashtags": "#trending #viral #socialmedia",
        "features": [
            "Character limit enforced",
            "Threaded tweets",
            "Real-time engagement",
        ],
        "content_style": "concise",
        "recommended_hashtags": 2,
    },
    "instagram": {
        "name": "Instagram",
        "max_length": 2200,
        "description": "Visual-focused content with detailed captions",
        "hashtags": "#instadaily #instaprimer #instagram",
        "features": [
            "Visual storytelling",
            "Story format",
            "Carousel posts",
            "Reels",
        ],
        "content_style": "narrative",
        "recommended_hashtags": 10,
    },
    "linkedin": {
        "name": "LinkedIn",
        "max_length": 3000,
        "description": "Professional and industry-focused content",
        "hashtags": "#linkedin #business #professional",
        "features": [
            "Professional networking",
            "Thought leadership",
            "Industry insights",
        ],
        "content_style": "professional",
        "recommended_hashtags": 5,
    },
    "tiktok": {
        "name": "TikTok",
        "max_length": 1500,
        "description": "Trendy, entertaining short-form video captions",
        "hashtags": "#foryou #fyp #viral #trending",
        "features": [
            "Video-first platform",
            "Trending sounds",
            "Viral challenges",
            "Duets and stitches",
        ],
        "content_style": "casual",
        "recommended_hashtags": 8,
    },
    "facebook": {
        "name": "Facebook",
        "max_length": 5000,
        "description": "Community-focused content with engagement hooks",
        "hashtags": "#facebook #community #social",
        "features": [
            "Community building",
            "Longer form posts",
            "Event promotion",
            "Group discussions",
        ],
        "content_style": "conversational",
        "recommended_hashtags": 3,
    },
    "youtube": {
        "name": "YouTube",
        "max_length": 5000,
        "description": "Detailed descriptions and tags for video content",
        "hashtags": "#youtube #videos #content",
        "features": [
            "Long-form video",
            "Playlists",
            "Community posts",
            "Shorts",
        ],
        "content_style": "descriptive",
        "recommended_hashtags": 5,
    },
    "pinterest": {
        "name": "Pinterest",
        "max_length": 500,
        "description": "Visual discovery-focused descriptions",
        "hashtags": "#pinterest #pinworthy #inspiration",
        "features": [
            "Visual discovery",
            "DIY and inspiration",
            "Lifestyle content",
            "Pins and boards",
        ],
        "content_style": "inspirational",
        "recommended_hashtags": 4,
    },
    "threads": {
        "name": "Threads",
        "max_length": 500,
        "description": "Text-based social networking",
        "hashtags": "#threads #socialmedia #textfirst",
        "features": [
            "Text-based conversation",
            "Threading",
            "Real-time discussion",
        ],
        "content_style": "conversational",
        "recommended_hashtags": 2,
    },
    "bluesky": {
        "name": "Bluesky",
        "max_length": 300,
        "description": "Decentralized social network posts",
        "hashtags": "#bluesky #decentralized #social",
        "features": [
            "Decentralized platform",
            "Open protocol",
            "Custom feeds",
        ],
        "content_style": "authentic",
        "recommended_hashtags": 3,
    },
    "mastodon": {
        "name": "Mastodon",
        "max_length": 500,
        "description": "Federated social network posts",
        "hashtags": "#mastodon #fediverse #social",
        "features": [
            "Federated network",
            "Open source",
            "Community-run servers",
        ],
        "content_style": "thoughtful",
        "recommended_hashtags": 3,
    },
}

# Default configuration
DEFAULT_CONFIG = {
    "tone_options": ["professional", "casual", "humorous", "inspirational"],
    "engagement_styles": ["viral", "conversational", "educational"],
    "default_tone": "professional",
    "default_hashtag_count": 5,
    "default_include_cta": True,
    "default_include_emojis": True,
    "default_include_hashtags": True,
}

# Tone descriptions for guidance
TONE_DESCRIPTIONS = {
    "professional": "Formal, business-appropriate, expert-level insights",
    "casual": "Friendly, conversational, relatable to everyday audiences",
    "humorous": "Witty, funny, entertaining with clever wordplay",
    "inspirational": "Motivational, uplifting, encouraging action and change",
}

# Output settings
OUTPUT_SETTINGS = {
    "save_directory": "generated_content",
    "timestamp_format": "%Y-%m-%d_%H-%M-%S",
    "file_format": "txt",
}

# API settings
API_SETTINGS = {
    "model": "gemini-pro",
    "temperature": 0.7,
    "max_output_tokens": 1024,
}

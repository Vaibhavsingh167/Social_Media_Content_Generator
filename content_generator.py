"""
Content Generator Module
Handles content generation using Google Gemini API
"""

import google.generativeai as genai
from config import PLATFORM_CONFIGS, DEFAULT_CONFIG
from typing import Optional, Dict


class SocialMediaContentGenerator:
    """Generate social media content using Gemini API"""

    def __init__(self, api_key: str):
        """
        Initialize the content generator
        
        Args:
            api_key: Google Gemini API key
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def generate_content(
        self,
        platform: str,
        topic: str,
        tone: str = "professional",
        include_hashtags: bool = True,
        hashtag_count: int = 5,
        include_cta: bool = True,
        include_emojis: bool = True,
    ) -> str:
        """
        Generate content for a specific social media platform
        
        Args:
            platform: Target platform (twitter, instagram, linkedin, etc.)
            topic: Content topic/theme
            tone: Writing tone (professional, casual, humorous, inspirational)
            include_hashtags: Whether to include hashtags
            hashtag_count: Number of hashtags to include
            include_cta: Whether to include call-to-action
            include_emojis: Whether to include emojis
            
        Returns:
            Generated content string
        """
        platform = platform.lower()

        if platform not in PLATFORM_CONFIGS:
            raise ValueError(f"Unknown platform: {platform}")

        config = PLATFORM_CONFIGS[platform]
        prompt = self._build_prompt(
            platform=platform,
            topic=topic,
            tone=tone,
            config=config,
            include_hashtags=include_hashtags,
            hashtag_count=hashtag_count,
            include_cta=include_cta,
            include_emojis=include_emojis,
        )

        try:
            response = self.model.generate_content(prompt)
            content = response.text.strip()
            return content
        except Exception as e:
            raise Exception(f"Error generating content: {str(e)}")

    def _build_prompt(
        self,
        platform: str,
        topic: str,
        tone: str,
        config: Dict,
        include_hashtags: bool,
        hashtag_count: int,
        include_cta: bool,
        include_emojis: bool,
    ) -> str:
        """
        Build the prompt for content generation
        
        Args:
            platform: Social media platform
            topic: Content topic
            tone: Writing tone
            config: Platform configuration
            include_hashtags: Whether to include hashtags
            hashtag_count: Number of hashtags
            include_cta: Whether to include CTA
            include_emojis: Whether to include emojis
            
        Returns:
            Generated prompt string
        """
        max_length = config["max_length"]

        prompt = f"""Create engaging {platform} content for the following:

Topic: {topic}
Tone: {tone}
Platform: {platform}
Max Length: {max_length} characters

Requirements:
1. Keep it within {max_length} characters
2. Use a {tone} tone
3. Make it engaging and relevant to {platform}
4. Write for {platform}'s unique audience and format
5. The content should be original and creative
"""

        if include_cta:
            prompt += "6. Include a clear call-to-action (CTA)\n"

        if include_emojis:
            prompt += f"7. Include relevant emojis to make it more engaging\n"
        else:
            prompt += "7. Do not include emojis\n"

        if include_hashtags:
            prompt += f"8. Add {hashtag_count} relevant hashtags at the end\n"
        else:
            prompt += "8. Do not include hashtags\n"

        prompt += f"""
Platform-specific guidelines for {platform}:
- Format: {config['description']}
- Recommended hashtags: {config['hashtags']}
- Key features: {', '.join(config['features'])}

Generate the content now. Only output the content, no explanations or preamble:"""

        return prompt

    def generate_variations(
        self, platform: str, topic: str, count: int = 3, tone: str = "professional"
    ) -> list:
        """
        Generate multiple variations of content
        
        Args:
            platform: Target platform
            topic: Content topic
            count: Number of variations to generate
            tone: Writing tone
            
        Returns:
            List of generated content variations
        """
        variations = []

        for i in range(count):
            try:
                content = self.generate_content(
                    platform=platform,
                    topic=topic,
                    tone=tone,
                    include_hashtags=True,
                    include_cta=True,
                    include_emojis=True,
                )
                variations.append(content)
            except Exception as e:
                print(f"Error generating variation {i + 1}: {str(e)}")
                continue

        return variations

    def generate_content_batch(
        self, platforms: list, topic: str, tone: str = "professional"
    ) -> Dict[str, str]:
        """
        Generate content for multiple platforms at once
        
        Args:
            platforms: List of platform names
            topic: Content topic
            tone: Writing tone
            
        Returns:
            Dictionary with platform names as keys and content as values
        """
        content_batch = {}

        for platform in platforms:
            try:
                content = self.generate_content(
                    platform=platform,
                    topic=topic,
                    tone=tone,
                    include_hashtags=True,
                    include_cta=True,
                    include_emojis=True,
                )
                content_batch[platform] = content
            except Exception as e:
                print(f"Error generating for {platform}: {str(e)}")
                content_batch[platform] = None

        return content_batch

    def optimize_for_engagement(
        self, platform: str, content: str, engagement_style: str = "viral"
    ) -> str:
        """
        Optimize existing content for better engagement
        
        Args:
            platform: Target platform
            content: Original content
            engagement_style: Style optimization (viral, conversational, educational)
            
        Returns:
            Optimized content
        """
        prompt = f"""You are a social media expert. Optimize the following {platform} content for {engagement_style} engagement:

Original content:
{content}

Rewrite it to be more {engagement_style} while keeping the core message. Focus on:
- Increasing shareability
- Better call-to-action
- More engaging opening
- Optimal hashtag placement
- Better emoji usage

Output only the optimized content:"""

        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Error optimizing content: {str(e)}")

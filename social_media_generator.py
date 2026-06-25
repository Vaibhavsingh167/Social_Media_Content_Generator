#!/usr/bin/env python3
"""
Social Media Content Generator using Google Gemini API
Main application entry point with terminal-based UI
"""

import os
import sys
import json
from datetime import datetime
from typing import Optional, Dict, List
import google.generativeai as genai
from colorama import init, Fore, Style
from content_generator import SocialMediaContentGenerator
from config import DEFAULT_CONFIG, PLATFORM_CONFIGS
from utils import (
    print_header,
    print_success,
    print_error,
    print_info,
    print_warning,
    get_user_input,
    get_multiline_input,
    save_content_to_file,
    display_content,
    get_yes_no_input,
)

# Initialize colorama for cross-platform colored output
init(autoreset=True)


class SocialMediaApp:
    """Main application class for social media content generation"""

    def __init__(self, api_key: str):
        """
        Initialize the application
        
        Args:
            api_key: Google Gemini API key
        """
        self.api_key = api_key
        self.generator = None
        self.content_history = []
        self.init_generator()

    def init_generator(self):
        """Initialize the content generator with API key"""
        try:
            genai.configure(api_key=self.api_key)
            self.generator = SocialMediaContentGenerator(api_key=self.api_key)
            print_success("✓ API initialized successfully!")
        except Exception as e:
            print_error(f"Failed to initialize API: {str(e)}")
            sys.exit(1)

    def display_main_menu(self):
        """Display the main menu"""
        print("\n")
        print_header("=" * 60)
        print_header("  SOCIAL MEDIA CONTENT GENERATOR")
        print_header("=" * 60)
        print_info("Select an option:")
        print("  1. Generate content for a specific platform")
        print("  2. Generate multi-platform content")
        print("  3. View generation history")
        print("  4. Save content to file")
        print("  5. Settings")
        print("  6. Exit")
        print_header("-" * 60)

    def generate_single_platform(self):
        """Generate content for a single platform"""
        print("\n")
        print_info("Available platforms:")
        platforms = list(PLATFORM_CONFIGS.keys())
        for i, platform in enumerate(platforms, 1):
            print(f"  {i}. {platform.title()}")

        platform_choice = get_user_input("Select platform (number): ").strip()

        try:
            platform_idx = int(platform_choice) - 1
            if 0 <= platform_idx < len(platforms):
                selected_platform = platforms[platform_idx]
            else:
                print_error("Invalid selection!")
                return
        except ValueError:
            print_error("Please enter a valid number!")
            return

        # Get topic/theme
        topic = get_user_input("Enter the topic/theme for content: ").strip()
        if not topic:
            print_warning("Topic cannot be empty!")
            return

        # Get optional parameters
        tone = get_user_input(
            "Enter tone (professional/casual/humorous/inspirational) [professional]: "
        ).strip() or "professional"

        hashtags = get_user_input(
            "Include hashtags? (y/n) [y]: "
        ).strip().lower()
        include_hashtags = hashtags != "n"

        hashtag_count = 5
        if include_hashtags:
            try:
                count = get_user_input("Number of hashtags (1-10) [5]: ").strip()
                hashtag_count = int(count) if count else 5
            except ValueError:
                hashtag_count = 5

        call_to_action = get_user_input(
            "Add call-to-action? (y/n) [y]: "
        ).strip().lower()
        include_cta = call_to_action != "n"

        emojis = get_user_input(
            "Include emojis? (y/n) [y]: "
        ).strip().lower()
        include_emojis = emojis != "n"

        # Generate content
        print_info("\n🔄 Generating content...")

        try:
            content = self.generator.generate_content(
                platform=selected_platform,
                topic=topic,
                tone=tone,
                include_hashtags=include_hashtags,
                hashtag_count=hashtag_count,
                include_cta=include_cta,
                include_emojis=include_emojis,
            )

            self.content_history.append(
                {
                    "platform": selected_platform,
                    "topic": topic,
                    "content": content,
                    "timestamp": datetime.now().isoformat(),
                }
            )

            display_content(content, selected_platform)

            # Ask if user wants to save
            if get_yes_no_input("\nSave this content? (y/n): "):
                filename = save_content_to_file(content, selected_platform)
                print_success(f"Content saved to {filename}")

        except Exception as e:
            print_error(f"Error generating content: {str(e)}")

    def generate_multi_platform(self):
        """Generate content for multiple platforms at once"""
        print("\n")
        print_info("Available platforms:")
        platforms = list(PLATFORM_CONFIGS.keys())
        for i, platform in enumerate(platforms, 1):
            print(f"  {i}. {platform.title()}")

        print("\nEnter platform numbers separated by commas (e.g., 1,2,3)")
        platform_input = get_user_input("Select platforms: ").strip()

        try:
            selected_indices = [int(x.strip()) - 1 for x in platform_input.split(",")]
            selected_platforms = [
                platforms[i] for i in selected_indices if 0 <= i < len(platforms)
            ]

            if not selected_platforms:
                print_error("Invalid platform selection!")
                return
        except ValueError:
            print_error("Please enter valid numbers separated by commas!")
            return

        # Get topic
        topic = get_user_input("Enter the topic/theme for content: ").strip()
        if not topic:
            print_warning("Topic cannot be empty!")
            return

        tone = get_user_input(
            "Enter tone (professional/casual/humorous/inspirational) [professional]: "
        ).strip() or "professional"

        include_hashtags = (
            get_user_input("Include hashtags? (y/n) [y]: ").strip().lower() != "n"
        )
        include_cta = (
            get_user_input("Include call-to-action? (y/n) [y]: ").strip().lower() != "n"
        )
        include_emojis = (
            get_user_input("Include emojis? (y/n) [y]: ").strip().lower() != "n"
        )

        print_info(f"\n🔄 Generating content for {len(selected_platforms)} platforms...")

        all_content = {}
        for platform in selected_platforms:
            try:
                content = self.generator.generate_content(
                    platform=platform,
                    topic=topic,
                    tone=tone,
                    include_hashtags=include_hashtags,
                    hashtag_count=5,
                    include_cta=include_cta,
                    include_emojis=include_emojis,
                )
                all_content[platform] = content

                self.content_history.append(
                    {
                        "platform": platform,
                        "topic": topic,
                        "content": content,
                        "timestamp": datetime.now().isoformat(),
                    }
                )

                print_success(f"✓ Generated for {platform.title()}")
            except Exception as e:
                print_error(f"Error generating for {platform}: {str(e)}")

        # Display all content
        print_header("\n" + "=" * 60)
        for platform, content in all_content.items():
            display_content(content, platform)
            print_header("-" * 60)

        # Ask to save
        if get_yes_no_input("\nSave all content to files? (y/n): "):
            for platform, content in all_content.items():
                filename = save_content_to_file(content, platform)
                print_success(f"Saved {platform}: {filename}")

    def view_history(self):
        """Display content generation history"""
        if not self.content_history:
            print_warning("\nNo content history yet!")
            return

        print_header("\n" + "=" * 60)
        print_header("  GENERATION HISTORY")
        print_header("=" * 60)

        for i, item in enumerate(self.content_history, 1):
            timestamp = datetime.fromisoformat(item["timestamp"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            print(f"\n{i}. Platform: {Fore.CYAN}{item['platform'].upper()}{Style.RESET_ALL}")
            print(f"   Topic: {item['topic']}")
            print(f"   Time: {timestamp}")

        view_choice = get_user_input("\nView content? (number or 'n'): ").strip()
        if view_choice.lower() != "n":
            try:
                idx = int(view_choice) - 1
                if 0 <= idx < len(self.content_history):
                    item = self.content_history[idx]
                    display_content(item["content"], item["platform"])
                else:
                    print_error("Invalid selection!")
            except ValueError:
                print_error("Please enter a valid number!")

    def save_history_to_file(self):
        """Save all content history to a JSON file"""
        if not self.content_history:
            print_warning("\nNo content to save!")
            return

        filename = f"content_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join("generated_content", filename)

        os.makedirs("generated_content", exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.content_history, f, indent=2, ensure_ascii=False)

        print_success(f"History saved to {filepath}")

    def display_settings(self):
        """Display settings menu"""
        print("\n")
        print_info("Settings:")
        print("  1. View API status")
        print("  2. View platform configurations")
        print("  3. Clear history")
        print("  4. Back to main menu")

        choice = get_user_input("Select option: ").strip()

        if choice == "1":
            print_info("\n✓ API is connected and ready")
            print_info(f"  API Key: {self.api_key[:10]}...{self.api_key[-10:]}")

        elif choice == "2":
            print_header("\n" + "=" * 60)
            for platform, config in PLATFORM_CONFIGS.items():
                print(f"\n{Fore.CYAN}{platform.upper()}{Style.RESET_ALL}")
                print(f"  Max Length: {config['max_length']} characters")
                print(f"  Recommended Hashtags: {config['hashtags']}")
                print(f"  Features: {', '.join(config['features'])}")

        elif choice == "3":
            if get_yes_no_input("Clear all history? (y/n): "):
                self.content_history = []
                print_success("History cleared!")

    def run(self):
        """Main application loop"""
        while True:
            self.display_main_menu()

            choice = get_user_input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.generate_single_platform()
            elif choice == "2":
                self.generate_multi_platform()
            elif choice == "3":
                self.view_history()
            elif choice == "4":
                self.save_history_to_file()
            elif choice == "5":
                self.display_settings()
            elif choice == "6":
                print_info("\nThank you for using Social Media Content Generator!")
                print_info("Goodbye! 👋\n")
                break
            else:
                print_error("Invalid choice! Please try again.")


def main():
    """Main entry point"""
    # Check for API key
    api_key = os.getenv("GEMINI_API_KEY") or "Ab8RN6IbJ9nZ1N18eT9BdIQ_1321v6iYDZvp_d_ulfUQPo7GYA"

    if not api_key:
        print_error("GEMINI_API_KEY not found!")
        print_info("Please set the GEMINI_API_KEY environment variable or pass it as argument")
        sys.exit(1)

    # Initialize and run app
    print_header("\n" + "=" * 60)
    print_header("  Initializing Social Media Content Generator...")
    print_header("=" * 60)

    app = SocialMediaApp(api_key)

    print("\n")
    print_success("✓ Application initialized successfully!")
    print_info("Use arrow keys to navigate, Enter to select\n")

    # Run the main application loop
    app.run()


if __name__ == "__main__":
    main()

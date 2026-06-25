"""
Utility functions for Social Media Content Generator
Includes UI helpers, file operations, and utility functions
"""

import os
import json
from datetime import datetime
from colorama import Fore, Style
from config import OUTPUT_SETTINGS


def print_header(text: str):
    """Print formatted header text"""
    print(f"{Fore.CYAN}{Style.BRIGHT}{text}{Style.RESET_ALL}")


def print_success(text: str):
    """Print success message"""
    print(f"{Fore.GREEN}{text}{Style.RESET_ALL}")


def print_error(text: str):
    """Print error message"""
    print(f"{Fore.RED}{Style.BRIGHT}{text}{Style.RESET_ALL}")


def print_info(text: str):
    """Print info message"""
    print(f"{Fore.BLUE}{text}{Style.RESET_ALL}")


def print_warning(text: str):
    """Print warning message"""
    print(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")


def get_user_input(prompt: str) -> str:
    """
    Get user input with formatted prompt
    
    Args:
        prompt: Input prompt text
        
    Returns:
        User input string
    """
    return input(f"{Fore.CYAN}{Style.BRIGHT}→ {prompt}{Style.RESET_ALL}")


def get_multiline_input(prompt: str) -> str:
    """
    Get multiline input from user
    
    Args:
        prompt: Input prompt text
        
    Returns:
        Multiline user input string
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}{prompt}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}(Enter an empty line to finish){Style.RESET_ALL}")

    lines = []
    while True:
        try:
            line = input()
            if not line:
                break
            lines.append(line)
        except EOFError:
            break

    return "\n".join(lines)


def get_yes_no_input(prompt: str) -> bool:
    """
    Get yes/no input from user
    
    Args:
        prompt: Input prompt text
        
    Returns:
        True for yes, False for no
    """
    response = get_user_input(prompt).strip().lower()
    return response in ["y", "yes"]


def save_content_to_file(content: str, platform: str) -> str:
    """
    Save generated content to a file
    
    Args:
        content: Content to save
        platform: Social media platform name
        
    Returns:
        Path to saved file
    """
    # Create output directory if it doesn't exist
    output_dir = OUTPUT_SETTINGS["save_directory"]
    os.makedirs(output_dir, exist_ok=True)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime(OUTPUT_SETTINGS["timestamp_format"])
    filename = f"{platform}_{timestamp}.{OUTPUT_SETTINGS['file_format']}"
    filepath = os.path.join(output_dir, filename)

    # Save content to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Platform: {platform.upper()}\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        f.write(content)

    return filepath


def display_content(content: str, platform: str):
    """
    Display generated content in a formatted way
    
    Args:
        content: Content to display
        platform: Social media platform name
    """
    print_header("\n" + "=" * 60)
    print_header(f"  {platform.upper()} CONTENT")
    print_header("=" * 60)
    print(f"\n{content}\n")
    print_header("=" * 60)


def format_content_for_platform(content: str, platform: str) -> str:
    """
    Format content according to platform-specific requirements
    
    Args:
        content: Raw content string
        platform: Platform name
        
    Returns:
        Formatted content
    """
    platform = platform.lower()

    # Platform-specific formatting rules
    if platform == "twitter":
        # Ensure it's under 280 characters
        if len(content) > 280:
            content = content[:277] + "..."

    elif platform == "instagram":
        # Add line breaks for readability
        content = content.replace(". ", ".\n\n")

    elif platform == "linkedin":
        # Add professional formatting
        if not content.startswith("\n"):
            content = "\n" + content

    elif platform == "tiktok":
        # Add trendy formatting
        lines = content.split("\n")
        if lines:
            lines[0] = f"✨ {lines[0]}"
            content = "\n".join(lines)

    return content


def get_character_count(content: str) -> int:
    """
    Get character count of content
    
    Args:
        content: Content string
        
    Returns:
        Character count
    """
    return len(content)


def get_word_count(content: str) -> int:
    """
    Get word count of content
    
    Args:
        content: Content string
        
    Returns:
        Word count
    """
    return len(content.split())


def get_hashtag_count(content: str) -> int:
    """
    Get hashtag count in content
    
    Args:
        content: Content string
        
    Returns:
        Hashtag count
    """
    return content.count("#")


def get_emoji_count(content: str) -> int:
    """
    Get emoji count in content
    
    Args:
        content: Content string
        
    Returns:
        Emoji count (approximate)
    """
    # Simple emoji detection by checking for common emoji character ranges
    emoji_count = 0
    for char in content:
        # Unicode ranges for emojis
        if (
            "\U0001F300" <= char <= "\U0001F9FF"
            or "\U0001F600" <= char <= "\U0001F64F"
            or "\U0001F680" <= char <= "\U0001F6FF"
            or "\U0001F700" <= char <= "\U0001F77F"
            or "\U0001F780" <= char <= "\U0001F7FF"
            or "\U0001F800" <= char <= "\U0001F8FF"
            or "\U0001F900" <= char <= "\U0001F9FF"
        ):
            emoji_count += 1

    return emoji_count


def get_content_stats(content: str) -> dict:
    """
    Get comprehensive statistics about content
    
    Args:
        content: Content string
        
    Returns:
        Dictionary with content statistics
    """
    return {
        "characters": get_character_count(content),
        "words": get_word_count(content),
        "hashtags": get_hashtag_count(content),
        "emojis": get_emoji_count(content),
        "lines": len(content.split("\n")),
    }


def display_content_stats(content: str):
    """
    Display statistics about generated content
    
    Args:
        content: Content string
    """
    stats = get_content_stats(content)

    print_header("\n" + "-" * 60)
    print_header("  CONTENT STATISTICS")
    print_header("-" * 60)
    print(f"Characters: {stats['characters']}")
    print(f"Words: {stats['words']}")
    print(f"Hashtags: {stats['hashtags']}")
    print(f"Emojis: {stats['emojis']}")
    print(f"Lines: {stats['lines']}")


def export_content_as_json(content_dict: dict, filename: str) -> str:
    """
    Export content as JSON file
    
    Args:
        content_dict: Dictionary of content
        filename: Output filename
        
    Returns:
        Path to saved file
    """
    output_dir = OUTPUT_SETTINGS["save_directory"]
    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(content_dict, f, indent=2, ensure_ascii=False)

    return filepath


def validate_api_key(api_key: str) -> bool:
    """
    Validate API key format
    
    Args:
        api_key: API key to validate
        
    Returns:
        True if valid format, False otherwise
    """
    return api_key is not None and len(api_key) > 10


def clear_screen():
    """Clear terminal screen"""
    os.system("clear" if os.name == "posix" else "cls")


def print_separator(char: str = "-", length: int = 60):
    """Print a separator line"""
    print(f"{Fore.CYAN}{char * length}{Style.RESET_ALL}")

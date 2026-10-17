"""
Finance YouTube Automation
Initial version: 0.1
Purpose: Generate and manage educational finance Shorts.
"""

from datetime import datetime


def generate_video_idea():
    """Return a sample educational finance video idea."""

    return {
        "topic": "How Compound Interest Works",
        "audience": "Indian beginners",
        "format": "YouTube Short",
        "duration_seconds": 45,
        "hook": (
            "What if your money could earn money "
            "without you working extra hours?"
        ),
        "key_points": [
            "Understand compound interest.",
            "Learn how reinvested returns can grow.",
            "Remember that actual investment returns vary."
        ]
    }


def display_video_idea(idea):
    """Display the video idea in a readable format."""

    print("\n=== FINANCE YOUTUBE AUTOMATION ===")
    print(f"Generated: {datetime.now():%Y-%m-%d %H:%M}")
    print(f"Topic: {idea['topic']}")
    print(f"Audience: {idea['audience']}")
    print(f"Format: {idea['format']}")
    print(f"Duration: {idea['duration_seconds']} seconds")
    print(f"\nHook: {idea['hook']}")

    print("\nKey points:")
    for number, point in enumerate(idea["key_points"], start=1):
        print(f"{number}. {point}")


def main():
    idea = generate_video_idea()
    display_video_idea(idea)


if __name__ == "__main__":
    main()
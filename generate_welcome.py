#!/usr/bin/env python3
"""
Playbook: Generate a Welcome HTML file.

This script prompts the user for their first name, last name, and country,
then generates an HTML file (welcome.html) in the repository with a
personalized welcome message.
"""

import os


def get_user_input():
    """Prompt the user for first name, last name, and country."""
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    country = input("Enter your country: ").strip()
    return first_name, last_name, country


def generate_html(first_name, last_name, country):
    """Generate an HTML welcome page with the provided user details."""
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f0f4f8;
        }}
        .welcome-container {{
            text-align: center;
            padding: 40px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }}
        h1 {{
            color: #2c3e50;
        }}
    </style>
</head>
<body>
    <div class="welcome-container">
        <h1>Welcome to the project {first_name} {last_name} and {country}!</h1>
    </div>
</body>
</html>
"""
    return html_content


def main():
    """Main entry point for the playbook."""
    print("=== Welcome Page Generator ===\n")

    first_name, last_name, country = get_user_input()

    if not first_name or not last_name or not country:
        print("Error: All fields (first name, last name, country) are required.")
        return

    html_content = generate_html(first_name, last_name, country)

    # Write the HTML file in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "welcome.html")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"\nWelcome page generated successfully!")
    print(f"File saved to: {output_path}")


if __name__ == "__main__":
    main()

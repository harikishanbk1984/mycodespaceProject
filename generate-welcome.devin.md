# Generate Welcome Page Playbook

## Description
This playbook collects the user's first name, last name, and country, then generates a styled HTML welcome page (`welcome.html`) in the repository.

## Inputs
Prompt the user for the following inputs before proceeding:

1. **First Name** — The user's first name
2. **Last Name** — The user's last name
3. **Country** — The user's country

## Steps

1. Ask the user for their **first name**, **last name**, and **country**.
2. Validate that all three values are non-empty. If any value is missing, ask the user again.
3. Run the welcome page generator script with the collected inputs:
   ```
   printf '%s\n' "<first_name>" "<last_name>" "<country>" | python3 generate_welcome.py
   ```
4. Verify that `welcome.html` was created successfully in the repository root.
5. Open `welcome.html` and confirm it contains the text:
   ```
   Welcome to the project <first_name> <last_name> and <country>!
   ```
6. Commit `welcome.html` to the repository with the message:
   ```
   Generated welcome page for <first_name> <last_name> from <country>
   ```
7. Push the commit and inform the user that the welcome page has been generated.

## Notes
- The script `generate_welcome.py` must exist in the repository root.
- The generated `welcome.html` will overwrite any existing `welcome.html` file.
- You can also trigger this process via the **GitHub Actions** workflow: go to **Actions → Generate Welcome Page → Run workflow** and fill in the input fields.

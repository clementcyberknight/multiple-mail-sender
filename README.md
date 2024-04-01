# Email Sender

This Python script allows you to send emails to multiple recipients using Gmail SMTP. It reads recipient emails from a CSV file, composes an email with a subject and body text, and sends it to the specified recipients.

## Prerequisites

Before using this script, ensure you have the following:

- Python installed on your machine.
- Access to a Gmail account from which you want to send emails.
- A CSV file containing the list of recipient emails.

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/email-sender.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd email-sender
    ```

3. **Install Dependencies:**

    This script requires no external dependencies.

4. **Update Script Parameters:**

    - Open the script `email_sender.py` in a text editor.
    - Replace the following variables with your own information:
        - `sender_email`: Your Gmail email address.
        - `sender_password`: Your Gmail account password. **Note:** For better security, consider using App Passwords if you have 2-Step Verification enabled.
        - `subject`: The subject line of your email.
        - `body_text`: The body text of your email.
        - `csv_file`: Path to your CSV file containing recipient emails.

5. **Run the Script:**

    ```bash
    python email_sender.py
    ```

    This will execute the script, read the recipient emails from the CSV file, and send the email to the specified recipients.

## CSV File Format

The CSV file should contain a list of recipient emails, with each email address in a separate row. Example:


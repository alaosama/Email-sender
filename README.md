# Email Sender

This Python script allows you to send an email using your Gmail account. It uses the `smtplib` library to connect to Gmail's SMTP server and send the email.

## Prerequisites

Before using this script, make sure you have the following prerequisites in place:

1. Python installed on your system.
2. A Gmail account from which you want to send emails.
3. [Less secure apps](https://myaccount.google.com/lesssecureapps) enabled for your Gmail account. Note that enabling this option makes your account less secure, so use it with caution.

## Usage

1. Clone or download this repository to your local machine.

2. Open the terminal/command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:


4. You will be prompted to enter the recipient's email address and the content of the email.

5. The script will use your Gmail account (specified in the `server.login()` function) to send the email to the recipient.

6. After successfully sending the email, the script will close the SMTP server connection.

**Note:** Make sure to replace the Gmail account credentials (`server.login()`) with your own email address and password.

## Security Considerations

- Be cautious about storing or sharing your email account password in the script. It's not recommended to hardcode your password directly in the script for security reasons. Consider using environment variables or a more secure method to manage your credentials.

- Enabling "Less secure apps" for your Gmail account is not recommended for long-term use, as it reduces the security of your account. You should explore other methods like OAuth2 authentication for a more secure email sending solution.

## Disclaimer

This script is for educational purposes and should be used responsibly and in compliance with Gmail's terms of service. Always consider security best practices when handling email credentials.

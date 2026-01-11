import os

from dotenv import load_dotenv

load_dotenv()


EMAIL_FROM = os.environ.get("EMAIL_FROM")
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER", "a@a.com")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "password")

import smtplib
from abc import ABC, abstractmethod
from email.message import EmailMessage
from email.mime.text import MIMEText

from src.config import EMAIL_FROM, SMTP_HOST, SMTP_PASSWORD, SMTP_PORT, SMTP_USER


class Notification(ABC):
    @abstractmethod
    def notify(self) -> None:
        pass


class EmailNotification(Notification):
    def __init__(self, to_address: str, title: str, message: str) -> None:
        self.to_address = to_address
        self.title = title
        self.message = message
        super().__init__()

    def notify(self) -> None:
        msg = EmailMessage()
        msg["From"] = EMAIL_FROM
        msg["To"] = self.to_address
        msg["Subject"] = self.title
        # msg.set_content(self.message)
        msg.set_content(MIMEText(self._create_html_message(), "html"))

        try:
            with smtplib.SMTP(
                SMTP_HOST,
                SMTP_PORT,
            ) as server:
                server.starttls()
                server.login(
                    SMTP_USER,
                    SMTP_PASSWORD,
                )
                server.send_message(msg)

            print("Mail sent successfully")

        except Exception as e:
            print(f"Mail send failed: {e}")

    def _create_html_message(self) -> str:
        return f"""\
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="utf-8">
                    <title>{self.title}</title>
                </head>
                <body style="font-family: Arial, Helvetica, sans-serif; line-height: 1.6;">
                    <h2 style="margin-bottom: 12px;">{self.title}</h2>

                    <ul style="list-style: none; padding: 0; margin: 0;">
                    {self.message}
                    </ul>

                    <hr style="margin-top: 24px; border: none; border-top: 1px solid #ddd;">

                    <p style="font-size: 12px; color: #777;">
                    This is an automated message.
                    </p>
                </body>
                </html>
                """

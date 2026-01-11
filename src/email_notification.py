import smtplib
from abc import ABC, abstractmethod
from email.message import EmailMessage

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
        msg.set_content(self.message)

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

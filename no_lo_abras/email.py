from email.mime.base import MIMEBase
import ssl
from smtplib import SMTP_SSL
from ssl import SSLContext
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from typing import Literal


class Email:

    def __init__(self, address: str, password: str) -> None:
        self.address = address
        self.password = password
        self.context: SSLContext = ssl.create_default_context()
        self.server: SMTP_SSL

    def send_massive_email(self, subject: str, receivers: list[str], text: str, html: str, uploads: list[str], priority: Literal["1", "3", "5"] = "5") -> None:
        success: bool = True

        index: int = 0
        while success:
            receiver: str = receivers[index]
            success = self.send_email(subject, receiver, text, html, uploads, priority)
            index += 1

    def send_email(self, subject: str, receiver: str, text: str, html: str, attachments: dict[str, bytes], priority: Literal["1", "3", "5"] = "5") -> bool:

        try:
            with SMTP_SSL("smtp.gmail.com", 465, context=self.context) as server:
                server.login(self.address, self.password)

                email = MIMEMultipart("alternative")

                email["Subject"] = subject
                email["From"] = self.address

                email["To"] = receiver

                email.add_header("X-Priority", priority)  # 1 = Alta, 3 = Normal, 5 = Baja

                text_body: MIMEText = MIMEText(text, "plain")
                email.attach(text_body)

                html_body: MIMEText = MIMEText(html, "html")
                email.attach(html_body)

                for attachment_name, attachment_bytes in attachments.items():
                    application = MIMEBase("application", "octet-stream")
                    application.set_payload(attachment_bytes)
                    encoders.encode_base64(application)
                    application.add_header("Content-Disposition", f"attachment; filename= {attachment_name}")
                    email.attach(application)

                server.sendmail(self.address, receiver, email.as_string())

                print(f'Email "{subject}" sent to {receiver}')

                return True

        except Exception as e:
            print(f'Error sending email "{subject}" to {receiver}: {e}')
            return False

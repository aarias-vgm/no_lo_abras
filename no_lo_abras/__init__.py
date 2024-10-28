from no_lo_abras.email import Email
from no_lo_abras.utils import Reader


def run() -> None:

    receivers: list[str]

    # employees : list[str] = []
    # with open("source\\employees.txt", "r", encoding="utf-8") as file:
    #     while True:
    #         line = file.readline()
    # if line:
    #             employees.append(line.replace("\n",""))
    #         else:
    #             break
    # for employee in employees:
    #     print(employee)

    receivers = [
        "a.arias@vgmedical.com.co",
        # "desarrollador.junior@vgmedical.com.co",
        # "marketing@vgmedical.com.co"
    ]

    address: str = "alertas.bancl0mbia@gmail.com"
    password: str = "zoqx qdio ypte ltxd"

    text: str = Reader.read_plain_text_file("data", "email_body.txt")
    html: str = Reader.read_plain_text_file("data", "email_body.html")

    attachments: dict[str, bytes] = {"sucursal_virtual_personas.svg": Reader.read_binary_file("uploads", "sucursal_virtual_personas.svg")}

    email = Email(address, password)
    email.send_email("Alertas y notificaciones", "a.arias@vgmedical.com.co", text, html, attachments, "1")
    # email.send_massive_email("Alertas y notificaciones", receivers, text, html, attachments)

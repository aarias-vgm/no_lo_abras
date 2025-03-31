from no_lo_abras.user import User
from no_lo_abras.email import Email
from no_lo_abras.utils import Reader


def run() -> None:

    address: str = "alertas.bancl0mbia@gmail.com"
    password: str = "zoqx qdio ypte ltxd"

    text: str = Reader.read_plain_text_file("data", "email_body.txt")
    html: str = Reader.read_plain_text_file("data", "email_body.html")

    attachments: dict[str, bytes] = {"sucursal_virtual_personas.svg": Reader.read_binary_file("uploads", "sucursal_virtual_personas.svg")}

    users: list[User] = []

    user_lines = Reader.get_plain_text_file_lines("data", "users.psv")
    user_lines.pop(0)

    for user_line in user_lines:
        user_properties = user_line.split("|")

        user: User = User(name=user_properties[0], second_name=user_properties[1], last_name=user_properties[2], email=user_properties[3])

        users.append(user)

    email = Email(address, password)

    andrea = users[3]

    print(andrea)

    email.send_email("Alertas y notificaciones", andrea, text, html, attachments, "1")
    # email.send_massive_email("Alertas y notificaciones", receivers, text, html, attachments)

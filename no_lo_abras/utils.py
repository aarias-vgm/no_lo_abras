import os


class Utils:

    __package_parent_folder = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))

    print(__package_parent_folder)

    @staticmethod
    def create_abs_path(file_name: str) -> str:
        """
        Return the absolute path of the given file name related to package parent folder.

        Args:
            file_name (str): file name with extension
        Returns:
            str
        """
        return os.path.join(Utils.__package_parent_folder, file_name)


class Reader:

    @staticmethod
    def read_plain_text_file(path: str, name: str) -> str:
        text: str
        with open(f"{Utils.create_abs_path(path)}\\{name}", "r", encoding="utf-8") as file:
            text = file.read()
        return text

    @staticmethod
    def read_binary_file(path: str, name: str) -> bytes:
        binary: bytes
        with open(f"{Utils.create_abs_path(path)}\\{name}", "rb") as file:
            binary = file.read()
        return binary

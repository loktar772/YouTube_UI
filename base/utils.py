from typing import List


class Utils:

    @staticmethod #декоратор "статическая функция"
    def join_strings(str_list: List[str]) -> str: #функция принимает на себя список строк и возвращает строку
        return ",".join(str_list)
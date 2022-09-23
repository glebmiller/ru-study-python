from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        res = []
        modified_array = map(func, input_array)
        res = [element[1] for element in modified_array if element[0]]
        return sorted(res)
        """
        Реализовать функцию, которая ведет себя как filter и map. К каждому значению из
        списка применяется функция, которая в ответ возвращает кортеж
        (булево значение, результат работы функции,).
        Если первый элемент кортежа истина, то результат добавляется в список.
        Принимает в качестве аргументов функцию и итерируемый источник, а возвращает список.
        """

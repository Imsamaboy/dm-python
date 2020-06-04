import json
import inspect
import re
from DataStructures.Support import Support
from FuncModule.Func import Func
from OperModule.Oper import Oper


def to_str(obj, filename):
    """
    toStr(object) - Преобразует произвольный объект встроенного типа Python или
    экземпляр любого класса любого модуля пакета DMpy в строковый вид в формате JSON.
    В JSON формате должна сохраняться информация о типе данных объекта для
    возможности восстановления из строки
    """

    def dumper(obj):
        try:
            return obj.toJSON()
        except:
            return obj.__dict__

    with open(rf"{filename}.json", "w") as f:
        f.write(json.dumps(obj, default=dumper, indent=4))


def support_to_json(obj: Support, filename: str):
    """
    support_to_json(object: Support, filename: str)
    Преобразует объект типа Support в JSON файл.
    """
    return to_str(obj, filename)


# Реализаций объектов Set и Relation пока нет в проекте и они вызывают ошибку
'''
def set_to_json(object: Set, filename: str):
    """
    set_to_json(object: Set, filename: str)
    Преобразует объект типа Set в JSON файл.
    """
    return to_str(object, filename)



def relation_to_json(object: Relation, filename: str):
    """
    relation_to_json(object: Relation, filename: str)
    Преобразует объект типа Relation в JSON файл.
    """
    return to_str(object, filename)
'''


def function_to_json(obj: Func, filename: str):
    """
    function_to_json(object: Func, filename: str)
    Преобразует объект типа Func в JSON файл.
    """
    return to_str(obj, filename)


def operation_to_json(obj: Oper, filename: str):
    """
    operation_to_json(object: Func, filename: str)
    Преобразует объект типа Oper в JSON файл.
    """
    func = obj.operation
    func_string = str(inspect.getsourcelines(func)[0])
    func_string = func_string.strip("['\\n']").split(" = ")[1]
    oper_string = re.search(r"lambda (.*): (.*)\)", func_string)
    obj = {"operation": oper_string.group(2), "operands": [i.replace(' ', '') for i in oper_string.group(1).split(",")]}
    with open(rf"{filename}.json", "w") as f:
        f.write(json.dumps(obj, indent=4))


def from_str(filename: str):
    """
    fromSrt(json_object) - преобразует стандартный объект
    в JSON формате обратно в объект Python.
    """
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
        # try:
        return json.loads(json_object)
    # TODO как нибудь поймать исключение на объект не являющийся builtin
    # type(a).__module__ == "__builtin__"
    # except:
    #     raise TypeError("Файл не является сериализацией стандартного объекта Python")


def support_from_json(filename: str):
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
    obj = json.loads(json_object)
    if "_Support__data" in json_object:
        _Support__data = obj["_Support__data"]
        arguments = []
        for key, value in _Support__data.items():
            arguments.append(value)
        return Support(arguments)
    else:
        raise TypeError("Файл не является сериализацией класса Support")


# Set не реализован, на мой взгляд он ничем не отличается от Support
def set_from_json(filename: str):
    """
    def set_from_json(filename: str):
    :return: Set object
    """
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
    obj = json.loads(json_object)
    if "_Set__data" in json_object:
        _Set__data = obj["_Set__data"]
        arguments = []
        for key, value in _Set__data.items():
            arguments.append(value)
        return Set(arguments)
    else:
        raise TypeError("Файл не является сериализацией класса Set")


# Relation не реализован, по-моему продставлению он
# будет выглядеть так же, как и Function
def relation_from_json(filename: str):
    """
    def relation_from_json(filename: str):
    :return: Relation object
    """
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
    obj = json.loads(json_object)
    if "_Relation__map" in json_object:
        _Relation__map = obj["_Relation__map"]
        return Func(_Relation__map)
    else:
        raise TypeError("Файл не является сериализацией класса Relation")


def function_from_json(filename: str):
    """
    def function_from_json(filename: str):
    :return: Func object
    """
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
    obj = json.loads(json_object)
    if "_Func__map" in json_object:
        _Func__map = obj["_Func__map"]
        return Func(_Func__map)
    else:
        raise TypeError("Файл не является сериализацией класса Func")


def operation_from_json(filename: str):
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
    obj = json.loads(json_object)
    if "operation" in json_object:
        operstr = f" {obj['operation']} "
        operands = obj["operands"]
        # самый стремный момент
        if len(operands[0]) >= len(operands[1]):
            operstr = re.sub(rf"(\W){operands[0]}(\W)", r"\1x\2", operstr)
            operstr = re.sub(rf"(\W){operands[1]}(\W)", r"\1y\2", operstr)
        else:
            operstr = re.sub(rf"(\W){operands[1]}(\W)", r"\1y\2", operstr)
            operstr = re.sub(rf"(\W){operands[0]}(\W)", r"\1x\2", operstr)
        return Oper(lambda x, y: eval(operstr))
    else:
        raise TypeError("Файл не является сериализацией класса Oper")


if __name__ == "__main__":
    a = Support([1, "lol", 3, "hehehehheheheh", 6, True, 1])
    print(a)
    support_to_json(a, "file1")
    print(support_from_json("file1"))

    a = Func({1: 2, "23214": "lololol", "4": 1, True: 2, 1: False})
    print(a.__dict__)
    function_to_json(a, "file2")
    print(function_from_json("file2").__dict__)

    a = [1, 2, 3, 4, 5]
    print(a)
    to_str(a, "file3")
    print(from_str("file3"))

    a = Oper(lambda _x_x_, x_x: _x_x_ * x_x + x_x)
    print(a.operation(2, 3))
    operation_to_json(a, "file4")
    b = operation_from_json("file4")
    print(b.operation(2, 3))

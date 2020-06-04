import json
import inspect
import re
from DataStructures.Support import Support
from FuncModule.Func import Func
from OperModule.Oper import Oper


def dump_to_json(obj, filename):
    """
    dump_to_json(object) - Преобразует произвольный объект встроенного типа
    Python или экземпляр любого класса любого модуля пакета DMpy в строковый
    вид в формате JSON. В JSON формате должна сохраняться информация о типе
    данных объекта для возможности восстановления из строки
    """

    def dumper(dumped_obj):
        try:
            return dumped_obj.toJSON()
        except:
            return dumped_obj.__dict__

    with open(rf"{filename}.json", "w") as f:
        f.write(json.dumps(obj, default=dumper, indent=4))


def support_to_json(obj: Support, filename: str):
    """
    support_to_json(object: Support, filename: str)
    Преобразует объект типа Support в JSON файл.
    """
    return dump_to_json(obj, filename)


# Реализаций объектов Set и Relation пока нет в проекте и они вызывают ошибку
'''
def set_to_json(object: Set, filename: str):
    """
    set_to_json(object: Set, filename: str)
    Преобразует объект типа Set в JSON файл.
    """
    return dump_to_json(object, filename)



def relation_to_json(object: Relation, filename: str):
    """
    relation_to_json(object: Relation, filename: str)
    Преобразует объект типа Relation в JSON файл.
    """
    return dump_to_json(object, filename)
'''


def function_to_json(obj: Func, filename: str):
    """
    function_to_json(object: Func, filename: str)
    Преобразует объект типа Func в JSON файл.
    """

    def dumper(dumped_obj):
        try:
            return dumped_obj.toJSON()
        except:
            return dumped_obj.__dict__

    with open(rf"{filename}.json", "w") as f:
        f.write(json.dumps(obj, default=dumper, indent=4))


def operation_to_json(obj: Oper, filename: str):
    """
    operation_to_json(object: Func, filename: str)
    Преобразует объект типа Oper в JSON файл.
    """
    func = obj.operation
    func_string = str(inspect.getsourcelines(func)[0])
    func_string = func_string.strip("['\\n']").split(" = ")[1]
    oper_data = re.search(r"lambda (.*): (.*)\)", func_string)
    operands = []
    for operand_str in oper_data.group(1).split(","):
        operands.append(operand_str.replace(' ', ''))
    obj = {
        "operation": oper_data.group(2),
        "operands": operands
    }
    with open(rf"{filename}.json", "w") as f:
        f.write(json.dumps(obj, indent=4))


def load_from_json(filename: str):
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


def support_from_json(filename: str):
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
    obj = json.loads(json_object)
    if "_Support__data" in json_object:
        support_source_data = obj["_Support__data"]
        arguments = []
        for key, value in support_source_data.items():
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
        set_source_data = obj["_Set__data"]
        arguments = []
        for key, value in set_source_data.items():
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
        relation_source_data = obj["_Relation__map"]
        return Func(relation_source_data)
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
        func_source_data = obj["_Func__map"]
        for key, value in func_source_data.items():
            if key.isdigit():
                func_source_data.pop(key)
                func_source_data.update({int(key): value})
        return Func(func_source_data)
    else:
        raise TypeError("Файл не является сериализацией класса Func")


def operation_from_json(filename: str):
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
    obj = json.loads(json_object)
    if "operation" in json_object:
        oper_source_data = f" {obj['operation']} "
        operands = obj["operands"]
        # самый стремный момент
        if len(operands[0]) >= len(operands[1]):
            oper_source_data = re.sub(
                rf"(\W){operands[0]}(\W)", r"\1x\2", oper_source_data)
            oper_source_data = re.sub(
                rf"(\W){operands[1]}(\W)", r"\1y\2", oper_source_data)
        else:
            oper_source_data = re.sub(
                rf"(\W){operands[1]}(\W)", r"\1y\2", oper_source_data)
            oper_source_data = re.sub(
                rf"(\W){operands[0]}(\W)", r"\1x\2", oper_source_data)
        return Oper(lambda x, y: eval(oper_source_data))
    else:
        raise TypeError("Файл не является сериализацией класса Oper")


if __name__ == "__main__":
    a = Support([1, "lol", 3, "hehehehheheheh", 6, True, 1])
    print(a)
    support_to_json(a, "file1")
    print(support_from_json("file1"))

    a = Func({1: "2", 23214: "lololol", 4: 1, True: 2, 1: False})
    print(a.__dict__)
    function_to_json(a, "file2")
    print(function_from_json("file2").__dict__)

    a = [1, 2, 3, 4, 5]
    print(a)
    dump_to_json(a, "file3")
    print(load_from_json("file3"))

    a = Oper(lambda x_x, o_o: x_x * o_o + o_o)
    print(a.operation(2, 3))
    operation_to_json(a, "file4")
    b = operation_from_json("file4")
    print(b.operation(2, 3))

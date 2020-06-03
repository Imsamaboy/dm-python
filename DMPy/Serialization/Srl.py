<<<<<<< HEAD
import json
import inspect
import re
from DataStructures.Support import Support
from FuncModule.Func import Func
from OperModule.Oper import Oper


def toStr(object, filename):
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
        f.write(json.dumps(object, default=dumper, indent=4))


def SupportToJSON(object: Support, filename: str):
    """
    SupportToJSON(object: Support, filename: str)
    Преобразует объект типа Support в JSON файл.
    """
    return toStr(object, filename)


# Реализаций объектов Set и Relation пока нет в проекте и они вызывают ошибку
'''
def SetToJSON(object: Set, filename: str):
    """
    SetToJSON(object: Set, filename: str)
    Преобразует объект типа Set в JSON файл.
    """
    return toStr(object, filename)



def RelationToJSON(object: Relation, filename: str):
    """
    RelationToJSON(object: Relation, filename: str)
    Преобразует объект типа Relation в JSON файл.
    """
    return toStr(object, filename)
'''


def FunctionToJSON(object: Func, filename: str):
    """
    FunctionToJSON(object: Func, filename: str)
    Преобразует объект типа Func в JSON файл.
    """
    return toStr(object, filename)


def OperationToJSON(object: Oper, filename: str):
    func = object.operation
    funcString = str(inspect.getsourcelines(func)[0])
    funcString = funcString.strip("['\\n']").split(" = ")[1]
    operString = re.search(r"lambda (.*): (.*)\)", funcString)
    object = {"operation": operString.group(2), "operands": [i.replace(' ', '') for i in operString.group(1).split(",")]}
    with open(rf"{filename}.json", "w") as f:
        f.write(json.dumps(object, indent=4))


def fromStr(filename):
    """
    fromSrt(json_object) - преобразует стандартный объект
    в JSON формате обратно в объект Python.
    """
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
    # try:
        return json.loads(json_object)
    # TODO как нибудь поймать исключение
    # type(a).__module__ == "__builtin__"
    # except:
    #     raise TypeError("Файл не является сериализацией стандартного объекта Python")


def SupportFromJSON(filename):
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
def SetFromJSON(filename):
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


# Relation не реализован, сделал так, как по моему представлению
# он будет выглядеть, то есть как тот же Function.
def RelationFromJSON(filename):
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
    obj = json.loads(json_object)
    if "_Relation__map" in json_object:
        _Relation__map = obj["_Relation__map"]
        return Func(_Relation__map)
    else:
        raise TypeError("Файл не является сериализацией класса Relation")


def FunctionFromJSON(filename):
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
    obj = json.loads(json_object)
    if "_Func__map" in json_object:
        _Func__map = obj["_Func__map"]
        return Func(_Func__map)
    else:
        raise TypeError("Файл не является сериализацией класса Func")


def OperationFromJson(filename):
    with open(rf"{filename}.json", "r") as f:
        json_object = f.read()
    obj = json.loads(json_object)
    if "operation" in json_object:
        operstr = f" {obj['operation']} "
        operands = obj["operands"]
        # самый стремный момент
        operstr = re.sub(rf"(\W){operands[0]}(\W)", r"\1x\2", operstr)
        operstr = re.sub(rf"(\W){operands[1]}(\W)", r"\1y\2", operstr)
        return Oper(lambda x, y: eval(operstr))
    else:
        raise TypeError("Файл не является сериализацией класса Oper")



if __name__ == "__main__":
    a = Support([1, "lol", 3, "hehehehheheheh", 6, 1, 1])
    print(a)
    SupportToJSON(a, "file1")
    print(SupportFromJSON("file1"))

    a = Func({1: 2, "23214": "lololol", "4": 1, 1: 2, 1: 2})
    print(a.__dict__)
    SupportToJSON(a, "file2")
    print(FunctionFromJSON("file2").__dict__)

    a = [1, 2, 3, 4, 5]
    print(a)
    SupportToJSON(a, "file3")
    print(fromStr("file3"))

    a = Oper(lambda ffxx, x: ffxx*x*x*x*ffxx)
    print(a.operation(2, 3))
    OperationToJSON(a, "file4")
    b = OperationFromJson("file4")
    print(b.operation(2, 3))


#    func = lambda num1, num2: num1 + num2
#    funcString = str(inspect.getsourcelines(func)[0])
#    funcString = funcString.strip("['\\n']").split(" = ")[1]
#    print(re.search(r".*: (.*)", funcString).group(1))
=======
import pickle
from DataStructures.Carrier import Carrier


def toStr(something, filename):
    """
    Функция сериализации объектов в памяти,
    принимаемые аргументы - сам объект и Ваше название для файла.
    """
    with open(rf'{filename}.pickle', 'wb') as file:
        pickle.dump(something, file)


def fromStr(filename):
    """ Загрузка объекта из памяти, принимаемый аргумент - название файла."""
    with open(rf'{filename}.pickle', 'rb') as file:
        return pickle.load(file)

>>>>>>> master

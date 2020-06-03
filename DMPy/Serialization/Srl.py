import json
from DataStructures.Support import Support
from FuncModule.Func import Func


def toStr(object):
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
    return json.dumps(object, default=dumper, indent=4)


def fromStr(json_object):
    """ fromSrt(json_object) - преобразует объект в JSON формате обратно
    в объект Python
    """
    obj = json.loads(json_object)
    if "_Support__data" in json_object:
        _Support__data = obj["_Support__data"]
        arguments = []
        for key, value in _Support__data.items():
            arguments.append(value)
        return Support(arguments)
    elif "_Func__map" in json_object:
        _Func__map = obj["_Func__map"]
        return Func(_Func__map)
    else:
        return obj


if __name__ == "__main__":
    a = Support([1, 2, 3, 4, 5, 6])
    b = toStr(a)
    print(a)
    print(fromStr(b))

    a = Func({"1": 2})
    print(a.__dict__)
    b = toStr(a)
    print(fromStr(b).__dict__)

    a = [1, 2, 3, 4, 5]
    b = toStr(a)
    print(fromStr(b))

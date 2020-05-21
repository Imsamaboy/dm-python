## Техническое задание

## 1. Шифр = *DMPy*



## 2. Назначение и область применения

Расширяемый пакет целочисленных алгоритмов для проведения вычислительных экспериментов в элементарной части общей алгебры и теории множеств.



## 3. Краткая сводка возможностей

Пакет является расширяемым. В первой версии содержатся средства, которые позволяют манипулировать отношениями, одноместными и двухместными функциями (операциями), заданными на конечном носителе. В том числе, пакет позволяет определять, сохранять, визуализировать, вычислять и преобразовывать сами операции или функции, а также множества и семейства множеств, связанные с этими функциями.



## 4. Варианты использования

Подпараграфы этого параграфа представляют собой подробное ТЗ по каждому модулю проекта. Название каждого модуля включено в название подпараграфа.

Модуль содержит глобальную переменную `DMPy.universum` типа `Support.Support`, нужную для отображения данных, переданных в функции и методы пакета, в числа. Все функции и методы, в которые передаются элементы универсума, должны работать не с самими данными, а с их отображениями, получаемыми с помощью этого объекта. Но каждый метод, принимающий на вход элементы универсума, имеет также аргумент `images = False`, который, если равен `True`, означает, что переданные данные уже преобразованы в числа и второй раз преобразовывать их не нужно.

`DMpy` содержит метод `DMpy.setUniversum( iterable )`, устанавливающий универсум текущей задачи. Он должен проинициализировать  `DMpy.universum` значением  `DMpy.Support.Support( iterable )`. 



### 4.1 Носитель ( =*Support* )

Модуль содержит класс `Support`. Он нужен для того, чтобы преобразовывать фиксированный набор объектов в числа на отрезок 1 ..n и обратно.
 ( на начальном этапе требуется только поддержка базовых хэшируемых типов данных языка Python )

**Конструкторы:**

* `Support( iterable )`  :`iterable` - любой перечислимый объект - заданное рабочее множество.



**Методы:**

* `forth(elem)` возвращает численный образ переданного элемента универсума
* `back(number)` возвращает элемент универсума по его численному образу



Этот модуль предназначен исключительно для использования другими модулями.     



### 4.2 Подмножества и семейства ( =*Sets* )

#### Класс Set

Класс `Set` обеспечивает работу с множествами

**Конструкторы:**

* `Set(iterable, images = False)` конструирует множество, состоящее из произвольных элементов универсума, перечисленных в `iterable`. Если `images == True`, в `iterable` должны лежать не элементы универсума, а их числовые образы.

**Методы:**

* `__contains__(elem, images = False)` проверяет, содержится ли `elem` в множестве. `elem` - это элемент универсума, если `images == False`. иначе это его численный образ.
* `__iter__()` возвращает генератор всех элементов множества. 



#### Класс Graph

Класс граф обеспечивает работу с графами

**Конструкторы:**

* `Graph( V, E, names = None, images = False )` строит ориентированный граф (V, E), где V - список элементов универсума, а E - список пар элементов универсума. names - это список строк - подписей к вершинам графа, который, если задан, определяет подписи вершин при визуализации. Для вершины `V[i]` подписью будет `names[i]`. Если `images = True`, в `V` и `E` должны лежать не элементы универсума, а их числовые образы.

**Методы:**

* `getV( images = False )`
* `getE( images = False )`
* `getNames()`



### 4.3 Одноместные функции ( =*Functions* )

#### Класс Relation

Класс Relation обеспечивает работу с отношениями. 

**Конструкторы:**

* `Relation( graph = None, images = False )` строит отношение по переданному графику `graph` - списку пар элементов универсума
* `Relation( criterion = None, images = False )` строит такое отношение R, для которого aRb <=> существуют такие элементы универсума `a`, `b`, что criterion(a, b) == True`. Если `images = True`, критерий должен принимать на вход не элементы универсума, а их числовые образы.

**Методы:**

* `__contains__( pair, images = False )` , где `pair` - кортеж из двух элементов универсума. Позволяет применять операцию in на отношениях ( см. примеры использования )
* ``__iter__()`` - возвращает итератор по всем парам, составляющим график отношения.
* `__call__(arg, images = False, returnImages = False)` - возвращает результат применения функции к элементу универсума `arg`. `images` и `returnImages` обозначает, должна ли функция вместо этого принимать и возвращать численные образы объектов.
* `isFunctional()`
* `isTotal()`
* `isSurjective()`
* `isInjective()`
* `isSymmetrical()`
* `isTransitive()`
* `toGraph()` - возвращает ориентированный граф, эквивалентный отношению.  Он не должен содержать ни с чем не соединённых вершин.



#### Класс Function

Класс `Function` наследуется от `Relation`. 

Класс `Function` обеспечивает работу с одноместными функциями. Он представляет из себя отношение, для которого гарантирована функциональность - при попытке определить нефункциональную функцию будет брошено исключение.

**Конструкторы:**

* `Function( procedure=None, images = False )` строит функцию, эквивалентную функции `procedure`, принимающей и возвращающей элементы универсума. Если `images` установлено в `True`, `procedure` должна принимать и возвращать числовые образы элементов.

**Методы:**

* `periodicalClosure()` возвращает периодическое замыкание функции. 

**Пример:**

```python
import DMPy

DMPy.setUniversum({'a', 'b', 'c'})

graph = [('a', 'b'), ('b', 'c'), ('c', 'a')]

f = DMpy.Functions.Function(graph=graph)

print(f('a'))  # Должно быть 'b'

if ('a', 'c') in f:
    # Должно быть ложью
    pass
if ('b', 'c') in f:
    # Должно быть истиной
    pass

for pair in f:
    print(pair)  # Должно быть ('a', 'b'), ('b', 'c'), ('c', 'a')
```



#### **Функции:**

* `allRelations()` возвращает генератор, генерирующий все отношения на универсуме.



### 4.4 Двуместные операции ( =*Operations* )

#### Класс Operation

Класс `Operation` обеспечивает работу с операциями.

**Конструкторы:**

* `Operation(graph=None, images = False)`  строит операцию по переданному графику `graph` - списку пар из пары элементов универсума и образа этой пары. Например, [((1, 2), 3), ((4, 5), 6)]. 
* `Operation( procedure=None, images = False )` работает аналогично `Function.Function`, но `procedure` принимает два аргумента.

**Методы:**

* `__contains__( entry, images = False )` , где entry - кортеж из  пары двух элементов универсума и её образа. Позволяет применять операцию in на отношениях.
* ``__iter__()`` - возвращает итератор, стоящий график операции
* `__call__(arg1, arg2, images = False, returnImages = False)` - возвращает результат применения функции к элементам универсума `arg1` и `arg2` . `images` и `returnImages` обозначает, должна ли функция вместо этого принимать и возвращать численные образы объектов.
* `isTotal()`
* `isSymmetrical()`
* `isAssociative()`
* `isCommutative()`
* `hasNeutral()` - имеет ли операция нейтральный элемент
* `hasInverse()` - имеет ли операция обратный элемент



### 4.5 Тестирование ( =*Tests* )

Нуждается ли модуль тестирования в ТЗ?



### 4.5 Визуализация ( =*Visualization* )

#### **Функции:**

* `drawGraph( graph )` - рисует переданный ориентированный граф.
* `drawCycloTree( cycloTree )` - рисует переданный ориентированный граф, учитывая, что это циклодерево.
* `printCayleyTable(operation)` - печатает таблицу Кэли переданной операции



### 4.6 Сериализация ( =*Serialization* )

#### Функции:

* `toStr(obj)` - преобразует произвольный объект встроенного типа Python или экземпляр любого класса любого модуля пакета DMpy в строковый вид в формате JSON. В JSON формате должна сохраняться информация о типе данных объекта для возможности восстановления из строки
* `fromSrt( )` - преобразует объект в JSON формате обратно в объект Python



## 5. Программа и методика испытаний

В этом параграфе приведены тестовые примеры целочисленных экспериментов, позволяющие оценить степень завершённости проекта. Требуется, чтобы в завершённом состоянии весь код из этой главы был рабочим.



### Эксперимент 1: функция Капрекара

```python
import DMPy

DMPy.setUniversum(range(0, 10000))


def Kaprekar_python(n):
    digits = str(n)
    digits_to_biggest = ''.join(sorted(digits))
    digits_to_lowest = ''.join(sorted(digits, reverse=True))
    return int(digits_to_lowest) - int(digits_to_biggest)

Kaprekar = DMPy.Functions.Function(procedure=Kaprekar_python)

periodical_closure = Kaprekar.periodicalClosure()

periodical_closure_graph = periodical_closure.toGraph()

DMpy.Visualization.drawCycloTrees(periodical_closure_graph)
```



### Эксперимент 2: классификация отношений

```python
import DMPy

universum = [[(x, y) for y in range(1, 11)] for x in range(1, 11)]
# universum = (1...10)x(1...10)
DMPy.setUniversum(universum)

for relation in DMPy.Functions.allRelations():
    if relation.isFunctional():
        pass
    if relation.isTotal():
        pass
    if relation.isInjective():
        pass
    if relation.isSurjective():
        pass
```



### Эксперимент 3: построение примеров алгебр

```python
import DMPy

DMPy.setUniversum({0, 1})

for operation in DMPy.Operations.allOperations():
    if operation.isCommutative():
        pass
    if operation.isAssociative():
        pass
    if operation.isSymmetrical():
        pass
    if operation.hasNeutral():
        pass
    if operation.hasInverse():
        pass
    DMPy.Visualization.printCayleyTable(operation)

for op1 in DMPy.Operations.allOperations():
    for op2 in DMPy.Operations.allOperations():
        '''
        Тут определяется класс алгебры с op1 и op2, но,
        так как нет смысла добавлять в пакет поддержку работы с алгебрами,
        классификацию следует свести к получению свойств op1 и op2
        и их анализу.
        '''
```
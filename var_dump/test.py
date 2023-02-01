import var_dump


class A:
    ...


def foo(*args, **kwargs):
    ...


array = [1, 2, 3]
tpl = (1, 2, 3)
dtc = {"a": 1, "b": 2, "c": 3}
obj = object()

var_dump(array)
var_dump(tpl)
var_dump(dtc)
var_dump(obj)
var_dump(A)
var_dump(foo)


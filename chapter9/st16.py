# *args和**kwargs的强制参数签名
from inspect import Signature, Parameter


params = [
    Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
    Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
    Parameter('z', Parameter.KEYWORD_ONLY, default=None)
]
sig = Signature(params)
print(sig)


def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)


func(1, 2, z=3)
func(1)
func(1, z=3)
func(y=2, x=1)

func(1, 2, 3, 4)
func(y=2)
func(1, y=2, x=3)
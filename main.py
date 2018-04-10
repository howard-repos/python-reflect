import pkgutil
import importlib
from inspect import getmembers, isclass

import bar

result=[]
for importer, name, ispkg in pkgutil.walk_packages(bar.__path__, "%s." % bar.__name__):
    if not ispkg:
        module=importlib.import_module(name)
        object_list = [value() for (_, value) in getmembers(module) if isclass(value)]
        result.extend(object_list)

for o in result:
	print(o)

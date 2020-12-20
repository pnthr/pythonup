# Ensure you name your modules different from inbuilt python modules (e.g OS)
import utilFuncs
from utilFuncs import count
import ourPackage.where
# import ourPackage.where as wh
import ourPackage.sub.sub_where
# import ourPackage.sub.sub_where as sw

utilFuncs.count(56)
utilFuncs.greet("James, welcome to church!")

ourPackage.where.say_where()

ourPackage.sub.sub_where.say_where()

import module_ListFunction
listdemo = [(-x)**x for x in range(1,7)]
print("original list : ", listdemo)
print("maximum in the list is : ", module_ListFunction.maxList(listdemo))
print("minimum in the list is : ", module_ListFunction.minList(listdemo))
print("sum of the list is : ", module_ListFunction.sumList(listdemo))
print("average of the list is : ", module_ListFunction.averageList(listdemo))
print("median of the list is : ", module_ListFunction.medianList(listdemo))
# -*- coding:utf-8 -*-
def get_index(s1, s2):
    # Slave / Master
    if len(s1) >= len(s2):
        mas = s1
        sla = s2
    else:
        mas = s2
        sla = s1
    len_m = len(mas)
    len_s = len(sla)

    # Comparaison
    index_m, index_s = 0, 0
    offset = 0
    while index_s < len_s and index_m < len_m:
        if mas[index_m] == sla[index_s]:
            if index_s == len_s - 1:
                return index_m - len_s + 1
            index_s += 1
            index_m += 1

        else:
            offset += 1
            index_s = 0
            index_m = offset
    return None

s1 = "www.baidu.com"
s2 = "com"
print(get_index(s1, s2))


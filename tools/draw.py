def draw_bin_tree(nums):
    def __print_line(layer, length_layer, time_blank, line_l, line_r, cont):
        for j in range(length_layer):
            blank_left = ""
            blank_right = ""
            for k in range(time_blank):
                blank_left += (2 ** k) * line_l
            for k in range(time_blank):
                blank_right += (2 ** k) * line_r
            # if j != 0:
            #     blank_left = blank_left[1:]
            if cont == "layer":
                context = layer[j]
            else:
                context = cont
            print(blank_left + context + blank_right, end="")
        print("")

    length = len(nums)

    tree = []
    end = False
    i = 0
    index_layer_last_number = -1
    while not end:
        layer = []
        for j in range(index_layer_last_number + 1, length):
            if (2 ** i - 1) <= j < (2 ** (i + 1) - 1):
                layer.append(str(nums[j]).center(7))
                if j == (2 ** (i + 1) - 2):
                    index_layer_last_number = j
            else:
                break
            if j == length - 1:
                end = True
                if index_layer_last_number != j:
                    for k in range((2 ** (i)) + index_layer_last_number - j):
                        layer.append("       ")
        tree.append(layer)
        i += 1

    print(tree)
    number_layer = len(tree)
    print(number_layer)

    line_blank = "    "
    line = "___"
    shu = "___|___"
    shu_blank = "   |   "
    shu_solo = " "
    for i in range(number_layer):
        time_blank = number_layer - i
        layer = tree[i]
        length_layer = len(layer)

        __print_line(layer, length_layer, time_blank, (shu_solo + line), (line + shu_solo), shu_blank)
        __print_line(layer, length_layer, time_blank, line_blank, line_blank, "layer")
        __print_line(layer, length_layer, time_blank, (shu_solo + line), (line + shu_solo), shu)


nums = [1, 2, 3, 4, 5, 6, 7]

draw_bin_tree(nums)

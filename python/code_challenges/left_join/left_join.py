
# copy left table would be much easier, 
# but not sure how to make a copy of left

def left_join(left,right)
    # using hash implementation
    result = hash() 
    for index in left:
        # check if index is not empty
        if index.key: 
            search_key = index.key
                for index in right:
                    if index.key == search_key:
                        result.index.key = search_key

                        while left.index.value:
                            # loop through this specific index
                            result.index.value.append(left.index.value)
                        while right.index.value:
                            # on both left and right and add to result
                            result.index.value.append(right.index.value)

                    else:
                        # check for empty left table
                        result.index.value.append('None')
        else:
            return ('Left table is empty')


    return result
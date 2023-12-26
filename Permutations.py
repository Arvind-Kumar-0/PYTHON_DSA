def permutation(object: str,ans: str = '',length = None):
    if length is None:
        length = len(object)

    if len(ans) >= length:
        return [ans]


    first = object[0]
    object = object[1:]
    li = []

    for i in range(len(ans)+1):
        li += permutation(object,ans[:i]+first+ans[i:],length)
    return li

print(permutation('abc'))

#['cba', 'bca', 'bac', 'cab', 'acb', 'abc']

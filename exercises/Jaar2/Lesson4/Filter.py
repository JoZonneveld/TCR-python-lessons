array = ['this', 'is', 'no']


def check_on_i(x):
    return 'i' in x


res = list(filter(check_on_i, array))
res_lambda = list(filter(lambda x: 'i' in x, array))

print(res)
print(res_lambda)
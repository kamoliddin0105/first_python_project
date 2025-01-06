def sum(*nums):
    y = 0
    for n in nums:
        y += n
    return y


print(sum(1,2,3,4,5,6,7,8,9,10))
print(sum(1,2,4,7,0))

def car_info(company, model, **kwargs):
    kwargs['company'] = company
    kwargs['model'] = model
    return kwargs


car = car_info('chevrolet', 'lacetti', color="white", price=15000)
print(car)

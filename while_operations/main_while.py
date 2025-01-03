savol = 'Istalgan son kiriting!'
savol += "(agar dasturdan chiqmoqchi bo'lsangiz exit deb yozing)"
qiymat = ''
while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    try:
        print(float(qiymat)**2)
    except ValueError:
        print("Iltimos, son kiriting!")

print('Dastur tugadi')

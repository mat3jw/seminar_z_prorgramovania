try:
    citatel = int(input('zadajte citatela: '))
    menovatel = int(input('zadajte menovatela: '))
    delenie = citatel / menovatel

except ValueError:
    print('zadana hodnota nie je ciselna hodnota.')

except ZeroDivisionError:
    print('nemozno delit nulou')

else:
    print(delenie)

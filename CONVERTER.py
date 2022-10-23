# currency

def currency_convert(inp_curr, money, out_curr):
    if inp_curr.upper() == 'BGN':
        if out_curr.upper() == 'USD':
            money *= 0.504209
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'EUR':
            money *= 0.51129188
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CAD':
            money *= 0.68795087
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'GBP':
            money *= 0.44608688
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'JPY':
            money *= 74.450516
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CHF':
            money *= 0.50304592
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CNY':
            money *= 3.6440992
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'BGN':
            print(f'You have {money} {out_curr.upper()}')

    elif inp_curr.upper() == 'USD':
        if out_curr.upper() == 'BGN':
            money *= 1.9833055
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'EUR':
            money *= 1.014048
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CAD':
            money *= 1.3644168
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'GBP':
            money *= 0.88472657
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'JPY':
            money *= 147.65812
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CHF':
            money *= 0.99769376
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CNY':
            money *= 7.2273621
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'USD':
            print(f'You have {money} {out_curr.upper()}')

    elif inp_curr.upper() == 'EUR':
        if out_curr.upper() == 'BGN':
            money *= 1.95583
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'USD':
            money *= 0.9861466
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CAD':
            money *= 1.3455149
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'GBP':
            money *= 0.8724701
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'JPY':
            money *= 145.61255
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CHF':
            money *= 0.9838723
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CNY':
            money *= 7.1272386
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'EUR':
            print(f'You have {money} {out_curr.upper()}')

    elif inp_curr.upper() == 'GBP':
        if out_curr.upper() == 'BGN':
            money *= 2.2417158
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'USD':
            money *= 1.1302927
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CAD':
            money *= 1.5421903
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'EUR':
            money *= 1.1461711
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'JPY':
            money *= 166.8969
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CHF':
            money *= 1.127686
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CNY':
            money *= 8.1690348
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'GBP':
            print(f'You have {money} {out_curr.upper()}')

    elif inp_curr.upper() == 'JPY':
        if out_curr.upper() == 'BGN':
            money *= 0.01343174
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'USD':
            money *= 0.006772401
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'GBP':
            money *= 0.0059917231
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'EUR':
            money *= 0.0068675398
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CAD':
            money *= 0.0092403774
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CHF':
            money *= 0.0067567822
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CNY':
            money *= 0.048946594
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'JPY':
            print(f'You have {money} {out_curr.upper()}')

    elif inp_curr.upper() == 'CAD':
        if out_curr.upper() == 'BGN':
            money *= 1.4535922
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'USD':
            money *= 0.73291389
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'GBP':
            money *= 0.64842839
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'EUR':
            money *= 0.74320988
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'JPY':
            money *= 108.22069
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CHF':
            money *= 0.73122361
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CNY':
            money *= 5.2970341
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CAD':
            print(f'You have {money} {out_curr.upper()}')

    elif inp_curr.upper() == 'CHF':
        if out_curr.upper() == 'BGN':
            money *= 1.9878901
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'USD':
            money *= 1.0023116
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'GBP':
            money *= 0.88677168
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'EUR':
            money *= 1.0163921
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'JPY':
            money *= 147.99944
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CAD':
            money *= 1.3675707
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CNY':
            money *= 7.2440687
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CHF':
            print(f'You have {money} {out_curr.upper()}')

    elif inp_curr.upper() == 'CNY':
        if out_curr.upper() == 'BGN':
            money *= 0.27441624
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'USD':
            money *= 0.13836307
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'GBP':
            money *= 0.12241348
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'EUR':
            money *= 0.14030679
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'JPY':
            money *= 20.430431
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CAD':
            money *= 0.18878489
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CHF':
            money *= 0.13804397
            print(f'You have {money} {out_curr.upper()}')
        elif out_curr.upper() == 'CNY':
            print(f'You have {money} {out_curr.upper()}')
    else:
        print('Sorry wrong input')
# time


def time_convert(inp_time, value, out_time):
    if inp_time.upper() == 'SECONDS':
        if out_time.upper() == 'MINUTES':
            value /= 60
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'HOURS':
            value /= 3600
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'DAYS':
            value /= 86400
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'WEEKS':
            value /= 604800
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MONTHS':
            value /= 2629743.83
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'YEARS':
            value /= 31536000
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'SECONDS':
            print(f'{value} {out_time.upper()}')

    elif inp_time.upper() == 'MINUTES':
        if out_time.upper() == 'SECONDS':
            value *= 60
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'HOURS':
            value /= 60
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'DAYS':
            value /= 1440
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'WEEKS':
            value /= 10080
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MONTHS':
            value /= 43829.0639
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'YEARS':
            value /= 525948.766
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MINUTES':
            print(f'{value} {out_time.upper()}')

    elif inp_time.upper() == 'HOURS':
        if out_time.upper() == 'SECONDS':
            value *= 360
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MINUTES':
            value *= 60
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'DAYS':
            value /= 24
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'WEEKS':
            value /= 168
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MONTHS':
            value /= 730.5
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'YEARS':
            value /= 8765.81277
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'HOURS':
            print(f'{value} {out_time.upper()}')

    elif inp_time.upper() == 'DAYS':
        if out_time.upper() == 'SECONDS':
            value *= 86400
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MINUTES':
            value *= 1440
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'HOURS':
            value *= 24
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'WEEKS':
            value /= 7
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MONTHS':
            value /= 30
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'YEARS':
            value /= 365
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'DAYS':
            print(f'{value} {out_time.upper()}')

    elif inp_time.upper() == 'WEEKS':
        if out_time.upper() == 'SECONDS':
            value *= 604800
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MINUTES':
            value *= 10080
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'HOURS':
            value *= 168
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'DAYS':
            value *= 7
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MONTHS':
            value /= 4.33
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'YEARS':
            value /= 52
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'WEEKS':
            print(f'{value} {out_time.upper()}')

    elif inp_time.upper() == 'MONTHS':
        if out_time.upper() == 'SECONDS':
            value *= 2629743.83
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MINUTES':
            value *= 43829.0639
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'HOURS':
            value *= 730.5
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'DAYS':
            value *= 30
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'WEEKS':
            value *= 4.33
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'YEARS':
            value /= 12
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MONTHS':
            print(f'{value} {out_time.upper()}')

    elif inp_time.upper() == 'YEARS':
        if out_time.upper() == 'SECONDS':
            value *= 31536000
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MINUTES':
            value *= 525948.766
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'HOURS':
            value *= 8765.81277
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'DAYS':
            value *= 365
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'WEEKS':
            value *= 52
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'MONTHS':
            value *= 12
            print(f'{value} {out_time.upper()}')
        elif out_time.upper() == 'YEARS':
            print(f'{value} {out_time.upper()}')
    else:
        print('Sorry wrong input')
# temperature


def temp_convert(inp_temp, value, out_temp):
    if inp_temp.upper() == 'C':
        if out_temp.upper() == 'K':
            value += 273.15
            print(f'{value}{out_temp.upper()}')
        elif out_temp.upper() == 'F':
            value = (value*1.8)+32
            print(f'{value}{out_temp.upper()}')
    elif inp_temp.upper() == 'K':
        if out_temp.upper() == 'C':
            value -= 273.15
            print(f'{value}{out_temp.upper()}')
        elif out_temp.upper() == 'F':
            value = ((value-273)*1.8)+32
            print(f'{value}{out_temp.upper()}')
    elif inp_temp.upper() == 'F':
        if out_temp.upper() == 'C':
            value = (value+32)*0.5556
            print(f'{value}{out_temp.upper()}')
        elif out_temp.upper() == 'K':
            value = (value+459.67)*(5/9)
            print(f'{value}{out_temp.upper()}')
    else:
        print('Sorry wrong input')
# distance


def distance_convert(inp_dist, value, out_dist):
    if inp_dist.upper() == 'MM':
        if out_dist.upper() == 'CM':
            value /= 10
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'DM':
            value /= 100
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'M':
            value /= 1000
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'KM':
            value /= 1000000
            print(f'{value}{out_dist.lower()}')

    elif inp_dist.upper() == 'CM':
        if out_dist.upper() == 'MM':
            value *= 10
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'DM':
            value /= 10
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'M':
            value /= 100
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'KM':
            value /= 100000
            print(f'{value}{out_dist.lower()}')

    elif inp_dist.upper() == 'DM':
        if out_dist.upper() == 'MM':
            value *= 100
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'CM':
            value *= 10
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'M':
            value /= 10
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'KM':
            value /= 10000
            print(f'{value}{out_dist.lower()}')

    elif inp_dist.upper() == 'M':
        if out_dist.upper() == 'MM':
            value *= 1000
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'CM':
            value *= 100
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'DM':
            value *= 10
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'KM':
            value /= 1000
            print(f'{value}{out_dist.lower()}')

    elif inp_dist.upper() == 'KM':
        if out_dist.upper() == 'MM':
            value *= 1000000
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'CM':
            value *= 100000
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'DM':
            value *= 10000
            print(f'{value}{out_dist.lower()}')
        elif out_dist.upper() == 'M':
            value *= 1000
            print(f'{value}{out_dist.lower()}')
    else:
        print('Sorry wrong input')


while True:
    convert = input('What would you like to convert (currency, time, temperature, distance): ')
    if convert.upper() == 'CURRENCY':
        from_curr = input('What currency would you like to convert from (BGN, USD, EUR, GBP, CAD, JPY, CNY, CHF): ')
        currency = float(input('How much money would you like to convert: '))
        to_curr = input('What currency would you like to convert to (BGN, USD, EUR, GBP, CAD, JPY, CNY, CHF): ')
        currency_convert(from_curr, currency, to_curr)
    elif convert.upper() == 'TIME':
        from_time = input('What time would you like to convert from '
                          '(seconds, minutes, hours, days, weeks, months, years): ')
        time = float(input(f'How many {from_time.lower()} would you like to convert: '))
        to_time = input('What time would you like to convert to '
                        '(seconds, minutes, hours, days, weeks, months, years): ')
        time_convert(from_time, time, to_time)
    elif convert.upper() == 'TEMPERATURE':
        from_temp = input('What temperature would you like to convert from (C, F, K): ')
        temperature = float(input('How many degrees would you like to convert: '))
        to_temp = input('What temperature would you like to convert to (C, F, K): ')
        temp_convert(from_temp, temperature, to_temp)
    elif convert.upper() == 'DISTANCE':
        from_distance = input('What distance would you like to convert from (mm, cm, dm, m, km): ')
        distance = float(input(f'How many {from_distance.lower()} would you like to convert: '))
        to_distance = input('What distance would you like to convert to (mm, cm, dm, m, km): ')
        distance_convert(from_distance, distance, to_distance)
    else:
        print('Sorry wrong input')
    while True:
        try_again = input('Would you like to try again (Y,N): ')
        if try_again.upper() == 'Y':
            break
        elif try_again.upper() == 'N':
            quit()
        else:
            print('Sorry wrong input')
            pass

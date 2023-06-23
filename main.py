def main():

    celcius = float(input('Enter Temperature in Celcius '))
    fahrenheit = (9/5) * (celcius) + 32

    print('Temperature in Fahrenheit: {:.2f}'.format(fahrenheit))
    return celcius, fahrenheit


if __name__ == '__main__':
    main()

a_ticket = int(input('Сколько будет посетителей моложе 18 лет: '))
b_ticket = int(input('Сколько будет посетителей от 18 до 25 лет: '))
c_ticket = int(input('Сколько будет посетителей от 25 лет: '))
sum_ticket = a_ticket + b_ticket + c_ticket  # Количество всех билетов

price = sum([a_ticket * int(0), b_ticket * int(990), c_ticket * int(1390)])

if sum_ticket > 3:
    price = price * 0.9

print("Сумма к оплате ", price)

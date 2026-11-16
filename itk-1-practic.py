"""
Первая практическая по питону
Условие: У вас есть список словарей с информацией о пользователях. Некоторые ключи могут отсутствовать.
Задание: Напишите одно выражение (one-liner, используя list comprehension), 
которое вернет список имен (только имена) тех пользователей, которым 18 лет и больше, и у которых обязательно указан email. 
Если возраст не указан, считаем, что пользователь несовершеннолетний.
"""
users = [
{"name": "Alice", "age": 25, "email": "alice@example.com"},
{"name": "Bob", "age": 17},
{"name": "Charlie", "age": 30, "email": "charlie@example.com"},
{"name": "David", "email": "david@example.com"}
]
res = [user['name'] 
for user in users if 'email' in user and 'age' in user and user['age'] >= 18]
print(res)
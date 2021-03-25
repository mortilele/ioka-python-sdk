IOKA Asynchronous Python Client Library
======================================

Клиент для платежного сервиса [**IOKA**](https://ioka.kz). Позволяет обращаться к [**API IOKA**](https://ioka.kz/documentation) из кода на Python.

Установка
=========
```shell script
pip install ioka
```

Требования
==========

Python 3.7+

Использование
=============

```python
from ioka import IOKA
ioka_client = IOKA('IOKA_SECRET_KEY', 'IOKA_HOST')
```
* При создании клиента задаются параметры: **Secret Key** и **IOKA Host**:

    **SECRET_KEY**: для аутентификации.
    
    **IOKA_HOST**: для выбора среды (тестовый Host & боевой Host).

Обращение к API осуществляется через методы клиента.

**Регистрация платежа**([описание](https://ioka.kz/documentation/payment-register))
```python
from ioka.schemas import RegisterPaymentRequest

data = {
    "amount": 3000,
    "currency": 398,
    "order_id": 322,
    "client_id": 1247,
    "tr_type": 0,
    "email": "client.1247@gmail.com",
    "phone": "+7**********",
    "back_url": f"https://mywebsite.com/back/",
    "callback_url": "https://mywebsite.com/callback/",
}
payment = RegisterPaymentRequest(**data)
ioka_response = await ioka_client.register_payment(payment)
```
В случае успеха возвращает строку типа ``URL``.

from random import randint

from ioka import IOKA
from syncer import sync
from ioka.schemas import RegisterPaymentRequest
IOKA_HOST = 'https://stage.ioka.kz'
IOKA_SECRET_KEY = 'xVd_KZBHNgEWEJFmv0c1VZ8KsnQsXunUYlfypZzUVDESPQU6JNmdtPJET1ImKxUEOJRVaCFg-fCbGPAyjofJ0A'

client = IOKA(secret_key=IOKA_SECRET_KEY, host=IOKA_HOST)


async def test_register_payment():
    data = {
        "amount": 3000,
        "currency": 398,
        "order_id": randint(10000, 999999),
        "client_id": randint(10000, 999999),
        "tr_type": 0,
        "email": "user@example.com",
        "phone": "87*********",
        "back_url": "https://1fit.app",
        "callback_url": "https://dev.pay.1fit.app/api/v1/ioka/callback",
    }
    payment = RegisterPaymentRequest(**data)
    response = await client.register_payment(payment)
    return response


async def test_change_payment_amount():
    register_payment = await test_register_payment()
    reference = register_payment.reference
    return await client.change_payment_amount(reference, amount=1000)


async def test_withdraw_payment():
    register_payment = await test_register_payment()
    reference = register_payment.reference
    return await client.withdraw_payment(reference, amount=1000)


async def test_cancel_payment():
    register_payment = await test_register_payment()
    reference = register_payment.reference
    return await client.cancel_payment(reference)


async def test_refund_payment():
    register_payment = await test_register_payment()
    reference = register_payment.reference
    return await client.refund_payment(reference, amount=1000, reason='TEST')


async def test_get_payment_status():
    register_payment = await test_register_payment()
    reference = register_payment.reference
    return await client.get_payment_status(reference)


async def test_get_client_saved_cards():
    return await client.get_client_saved_cards(client_id=100)


async def test_get_client_saved_card_by_token():
    token = 'someToken'
    client_id = 100
    return await client.get_client_saved_card_by_token(token=token, client_id=client_id)


async def test_delete_saved_card_by_token():
    token = 'someToken'
    return await client.delete_saved_card_by_token(token)


# response = sync(test_register_payment)
# response = sync(test_change_payment_amount)
# response = sync(test_withdraw_payment)
# response = sync(test_cancel_payment)
# response = sync(test_refund_payment)
response = sync(test_get_payment_status)
# response = sync(test_get_client_saved_cards)
# response = sync(test_get_client_saved_card_by_token)
# response = sync(test_delete_saved_card_by_token)
print('RESPONSE:', response())

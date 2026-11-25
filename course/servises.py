import stripe
from config.settings import STRIPE_API_KEY
from stripe import StripeClient
stripe.api_key = STRIPE_API_KEY

client = StripeClient(stripe.api_key)

def create_stripe_product():
    """
    Создает продукт в Stripe.
    """
    product = client.v1.products.create({"name": "Gold Plan"})
    return product

def create_stripe_price(product, amount):
    """
    Создает цену в Stripe.
    """
    price = client.v1.prices.create(
        currency="rub",
        unit_amount = amount * 100,
        recurring={"interval": "month"},
        product=product.id,
    )
    return price


def create_checkout_session(price):
    """
    Создает сессию на оплату в Stripe.
    """
    session = client.v1.checkout.sessions.create(
        success_url="http://127.0.0/1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")


from starlette.config import Config

config = Config(".env")

RAZORPAY_KEY_ID = config.get("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = config.get('RAZORPAY_KEY_SECRET')
RAZORPAY_BASE_URL = "https://api.razorpay.com/v1"

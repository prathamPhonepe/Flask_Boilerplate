import os

TYPE = os.getenv('TYPE', 'development')  # 'development', 'production', 'test'

JWT_SECRET_KEY_DEV = 'devsecretkey'
JWT_SECRET_KEY_PROD = 'prodsecretkey'
JWT_SECRET_KEY_TEST = 'testsecretkey'

ALLOWED_ORIGINS = [
    'http://example.com',
    'http://anotherdomain.com',
    'http://localhost:3000',
    'http://localhost:5000',
    'http://localhost:3001',
    'http://localhost:4000'
]

if TYPE == 'development':
    JWT_SECRET_KEY = JWT_SECRET_KEY_DEV
elif TYPE == 'production':
    JWT_SECRET_KEY = JWT_SECRET_KEY_PROD
elif TYPE == 'test':
    JWT_SECRET_KEY = JWT_SECRET_KEY_TEST
else:
    raise ValueError("Invalid TYPE value. Must be 'development', 'production', or 'test'.")

constants = {
    'JWT_SECRET_KEY': JWT_SECRET_KEY,
    'ALLOWED_ORIGINS': ALLOWED_ORIGINS
}
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

password = "67945731797"


# Hashing the same password twice will generate different hashes
hash1 = pwd_context.hash(password)
hash2 = pwd_context.hash(password)

print(hash1)
print(hash2)

# Output will be two different hashes, like:
# $2b$12$RzjfJhYJtPuK2DJBoEvZlO5ZO3P63kNeW7w3YolWPKHidnJZn5IXS
# $2b$12$7Kt2r5mYXOhRmRoJ5bmrseA2Rt4Xf8FxNG5IX.bDJEnFmgc7TAcZC

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Verifying the password
is_valid = verify_password("67945731797", "$2b$12$hUZeclfE6WazQM97pDoypeTUZIou568mW3Kv2WjtT1F49jHvlceYa")  # This will return True
print(is_valid)

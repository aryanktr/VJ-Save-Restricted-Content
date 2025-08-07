import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7698825343:AAENJC1kdtEgfodd_otFJsBQY7MQi0gQP4w")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20831812"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9af7c0491f6f09017c3f491f571da3fe")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6288683814"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://aryanktr92:7698825343:AAENJC1kdtEgfodd_otFJsBQY7MQi0gQP4wpBw41GcqtlnpFjwq@cluster0.nqsufox.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))

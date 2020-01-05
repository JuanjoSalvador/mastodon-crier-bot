from mastodon import Mastodon

mastodon = Mastodon(
            access_token = 'YOUR TOKEN HERE',
            api_base_url = 'YOUR INSTANCE'S URL HERE'
        )

instance = mastodon.instance()

# Get last status
try:
    with open("current.csv") as file:
        current_data = file.read()
except FileNotFoundError:
    current_data = "0;0;0"

current = current_data.split(";")

# Saves current status into a file
with open("current.csv", 'w') as file:
    file.write("{};{};{}".format(
            instance.stats.user_count, 
            instance.stats.status_count,
            instance.stats.domain_count
        )
    )


user_change   = instance.stats.user_count   - int(current[0])
if user_change >= 0:
    user_change = "+{}".format(user_change)

status_change = instance.stats.status_count - int(current[1])
if status_change >= 0:
    status_change = "+{}".format(status_change)

connec_change = instance.stats.domain_count - int(current[2])
if connec_change >= 0:
    connec_change = "+{}".format(connec_change)

mastodon.status_post("""
Estado de Hispatodon.club

Usuarios: {} ({})
Estados: {} ({})
Conexiones: {} ({})
""".format(instance.stats.user_count, user_change, 
        instance.stats.status_count, status_change, 
        instance.stats.domain_count, connec_change)
)

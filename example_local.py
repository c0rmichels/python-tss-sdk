import json

from thycotic.secrets.server import (
    SecretServer,
    ServerSecret,
    SecretServerAccessError,
    SecretServerError,
)

if __name__ == "__main__":

    with open("test/test_local.json") as f:
        secret_server = SecretServer(**json.load(f))

    # try:
    #     secret = ServerSecret(**secret_server.get_secret(5424))
    #     print(f"""name: {secret.name}""")
    #     print(f"""template: {secret.secret_template_name}""")
    # except SecretServerAccessError as error:
    #     print(error.message)
    # except SecretServerError as error:
    #     print(error.message)

    try:
        secrets_dict = json.loads(secret_server.lookup_secrets_json(text='antwerpen', take=10))
        print(json.dumps(secrets_dict))
        print(secrets_dict['total'])
    except SecretServerAccessError as error:
        print(error.message)
    except SecretServerError as error:
        print(error.message)

    for secret in secrets_dict['records']:
        print(json.dumps(secret))

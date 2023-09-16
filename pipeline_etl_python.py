import pandas as pd
import requests
import json

df = pd.read_csv('SDW2023.csv')

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'


def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None


def transform_users_to_json(users):
    users_json = json.dumps(users, indent=2)
    with open('users.json', 'w') as file:
        file.write(users_json)
    print('Arquivo users.json criado com sucesso!')
    print(users_json)


if __name__ == '__main__':
    # lista de ids de usuarios
    user_ids = df['UserID'].tolist()
    print(user_ids)

    # cria arquivo json com os usuários capturados da API
    users = [user for id in user_ids if (user := get_user(id)) is not None]
    transform_users_to_json(users)

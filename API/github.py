import os
import argparse
import json
import requests

GITHUB_API_KEY ="8634aa9a7c11d3fa668c86781805e83452e5aac5"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', help='username')
    args = parser.parse_args()

    response = requests.get(
        'https://api.github.com/users/' + args.user,
        params={'name': args.user, 'APPID': GITHUB_API_KEY})

    body = response.json()
    if response.status_code != 200:
        print('Status code was {}. Reason: {}.'.format(body['cod'], body['message']))
        exit(1)

    print('{}は{}年{}月{}日にgithubのアカウントを作りました.'
        .format(body['name'], body['created_at'][0:4], body['created_at'][5:7], body['created_at'][8:10]))

if __name__ == "__main__":
    main()
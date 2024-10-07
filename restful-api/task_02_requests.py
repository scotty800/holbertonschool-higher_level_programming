#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        post = response.json()
        for index in post:
            print(index['title'])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        post = response.json()

    with open('post.csv', 'w', newline='') as fic:
        writer = csv.writer(fic)
        fields = ['id', 'title', 'body']
        writer.writerow(fields)
        for index in post:
            writer.writerow([index['id'], index['title'], index['body']])

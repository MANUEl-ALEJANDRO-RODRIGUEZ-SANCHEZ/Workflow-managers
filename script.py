import requests
import json
import sqlite3
from collections import namedtuple
from contextlib import closing
from prefect import task, Flow

## extract
@task
def get_post_data():
    r = requests.get("https://jsonplaceholder.cypress.io/posts")
    response_json = json.loads(r.text)
    return response_json[:10]  # Solo los primeros 10 registros

## transform
@task
def parse_post_data(raw):
    posts = []
    Post = namedtuple('Post', ['user_id', 'id', 'title', 'body'])
    for row in raw:
        this_post = Post(
            user_id=row.get('userId'),
            id=row.get('id'),
            title=row.get('title'),
            body=row.get('body')
        )
        posts.append(this_post)
    return posts

## load
@task
def store_posts(parsed):
    create_script = 'CREATE TABLE IF NOT EXISTS posts (user_id INTEGER, id INTEGER, title TEXT, body TEXT)'
    insert_cmd = "INSERT INTO posts VALUES (?, ?, ?, ?)"

    with closing(sqlite3.connect("posts.db")) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.executescript(create_script)
            cursor.executemany(insert_cmd, parsed)
            conn.commit()

with Flow("jsonplaceholder_etl") as f:
    raw = get_post_data()
    parsed = parse_post_data(raw)
    store_posts(parsed)

f.run()
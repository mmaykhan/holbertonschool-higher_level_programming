#!/usr/bin/python3
"""
Python script to fetch data from an API and process it.
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches all posts and saves them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    if r.status_code == 200:
        posts = r.json()
        fieldnames = ["id", "title", "body"]
        data_to_save = [
            {"id": p.get("id"), "title": p.get("title"), "body": p.get("body")}
            for p in posts
        ]
        with open("posts.csv", mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)

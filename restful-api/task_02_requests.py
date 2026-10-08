#!/usr/bin/python3
"""
Module to fetch posts from JSONPlaceholder API and interact with CSV.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints status code and titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        print("Status Code: {}".format(response.status_code))

        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post.get("title"))
    except Exception:
        return None


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves id, title, body to posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            data = [
                {
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body")
                }
                for post in posts
            ]

            with open("posts.csv", "w", encoding="utf-8", newline="") as f:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            return data
    except Exception:
        return None
    return None

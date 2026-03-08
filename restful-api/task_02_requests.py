#!/usr/bin/env python3
import requests
import csv

def fetch_and_print_posts():
    url="https://jsonplaceholder.typicode.com/posts"
    response=requests.get(url)
    print(f"Status Code:{response.status_code}")
    if response.status_code == 200:
        posts=response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
      url="https://jsonplaceholder.typicode.com/posts"
      response=requests.get(url)
      if response.status_code == 200:
          posts=response.json()
          structured_post=[{"id":post["id"], "title":post["title"],"body":post["body"]} for post in posts]
          with open ("posts.csv", "w", newline="", encoding="utf-8") as csvfiles:
              fieldnames=["id","title","body"]
              writer=csv.DictWriter(csvfiles,fieldnames=fieldnames)
              write.writeheader()
              writer.writerrows(structured_posts)
          print("post.csv file successfully created")
              

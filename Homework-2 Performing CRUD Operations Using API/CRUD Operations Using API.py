#CRUD Operations Using API

#Top business headlines in the US right now
from requests import get
from pprint import pprint
from uuid import uuid4

def fetch_news(api_key: str = "4b3e2c332fec45efa30bd394249c29e6") -> dict:
    """Fetch news from the API with error handling"""
    try:
        endpoint = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}'
        response = get(url=endpoint)
        return response.json()
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return {"articles": []}  # Return empty article list if API fails

try:
    data = fetch_news()
except Exception as e:
    print(f"Failed to initialize data: {e}")
    data = {"articles": []}

def create_data(source_name: str, author: str, title: str, description: str, publishedAt: str, content: str) -> dict:
    try:
        new_article = {
            "source": {"name": source_name, "id": str(uuid4())},
            "author": author,
            "title": title,
            "description": description,
            "publishedAt": publishedAt,
            "content": content
        }
        data["articles"].append(new_article)
        return data
    except Exception as e:
        print(f"Error creating article: {e}")
        return data

def update_data(author: str) -> dict:
    try:
        for article in data.get("articles", []):
            if article.get("author") == author:
                print("You will now update the article by the author of your choice !!!")
                try:
                    source_name = input("Please enter source name to update: ")
                    title = input("Please enter the title to update: ")
                    description = input("Please enter the Description to update: ")
                    publishedAt = input("Please enter the date to update: ")
                    content = input("Please enter content to update: ")

                    article["title"] = title
                    article["description"] = description
                    article["publishedAt"] = publishedAt
                    article["content"] = content
                    article["source"]["name"] = source_name
                except Exception as e:
                    print(f"Error during update input: {e}")
        return data
    except Exception as e:
        print(f"Error updating article: {e}")
        return data

def delete_data(author: str) -> dict:
    try:
        updated_articles = [article for article in data["articles"] if article.get("author") != author]
        data["articles"] = updated_articles
        return data
    except Exception as e:
        print(f"Error deleting article: {e}")
        return data

def read_data(author: str) -> str:
    try:
        output = ""
        if "articles" in data:
            for article in data["articles"]:
                if article.get("author") == author:
                    output += f"Source: {article.get('source', {}).get('name', 'Unknown')}\n"
                    output += f"Title: {article.get('title', 'N/A')}\n"
                    output += f"Description: {article.get('description', 'N/A')}\n"
                    output += f"Published At: {article.get('publishedAt', 'N/A')}\n"
                    output += f"Content: {article.get('content', 'N/A')}\n"
                    output += "-" * 40 + "\n"
            if output == "":
                output = f"No articles found for author: {author}"
        else:
            output = "No articles data available."
        return output
    except Exception as e:
        return f"Error reading article: {e}"

def read_all_data(data: dict) -> str:
    try:
        result = ""
        if "articles" in data and data["articles"]:
            for article in data["articles"]:
                result += (
                    f"Title: {article.get('title', 'N/A')}\n"
                    f"Author: {article.get('author', 'N/A')}\n"
                    f"Source: {article.get('source', {}).get('name', 'N/A')}\n"
                    f"Description: {article.get('description', 'N/A')}\n"
                    f"Published At: {article.get('publishedAt', 'N/A')}\n"
                    f"Content: {article.get('content', 'N/A')}\n"
                    f"{'-' * 50}\n"
                )
        else:
            result = "No articles available."
        return result
    except Exception as e:
        return f"Error reading all articles: {e}"

while True:
    print("Press 0 for exiting the while loop")
    process = input('Type a process name: ').strip().lower()

    match process:
        case 'create':
            create_data(
                source_name=input("Please enter source_name: "),
                author=input("Please enter Author name: "),
                title=input("Please enter the title: "),
                description=input("Please enter the Description: "),
                publishedAt=input("Please enter the date: "),
                content=input("Please enter content: ")
            )
            print("Please enter the 'list' keyword to see the content of the data that I extracted from API")

        case 'list':
            print(read_all_data(data))

        case 'update':
            author = input("Please enter the Author that you want to update: ")
            update_data(author=author)
            print("Please enter the 'list' keyword to see the content of the data that I extracted from API")

        case 'delete':
            author = input("Please enter the Author that you want to delete: ")
            delete_data(author=author)

        case 'read':
            author = input("Please write the name of the author whose article you would like to see: ")
            print(read_data(author=author))

        case '0':
            print('Have a nice day :)')
            break

        case _:
            print('Please type a valid process (create, list, update, delete, read, 0)')
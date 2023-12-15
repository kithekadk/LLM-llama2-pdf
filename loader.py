from bs4 import BeautifulSoup as soup
import requests
from llama_index import Document
from llama_index import SimpleDirectoryReader


urls = [
    "https://www.the-star.co.ke/health/2023-09-13-sickle-cell-stigma-moh-to-focus-on-community-awareness/"
]

def web_page_reader(urls=urls):
    docs=[]
    for url in urls:
        try:
            response = requests.get(url)
            page = soup(response.content, 'lxml')
            text = page.text
            docs.append(Document(
                text=text,
                extra_info = {
                    "source_url":url
                }
            ))
            print(f"Read {url}")
        except Exception as e:
            print(f"Error reading {url} due to {e}")
    return docs

# url = "https://llamahub.ai/l/web-simple_web?from=loaders"

# docs = web_page_reader([urls])

# docs[0]

def load_directory(folder_path = "storage/"):
    reader = SimpleDirectoryReader(folder_path, recursive=True)
    docs = reader.load_data()
    return docs

if __name__ == "__main__":
    docs = web_page_reader(urls)
    print(docs)
    docs = load_directory()
    print(docs)
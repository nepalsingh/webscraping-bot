import requests


def get_latest_news(country='in'):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=794fb70ac8ed45a7adec5297606cd106'
  headers = {"User-Agent":
             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
            }
  response = requests.get(url=url)
  data = response.json()
  print(data)
  return data


def main():
  data = get_latest_news()
  for article in data['articles']:
    print(article['title'])

if __name__ == '__main__':
  main()
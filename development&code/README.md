# Methodology
I will complete this project with 4 major steps.

1.	Crawl at least 10,000 articles different sources. 
2.	Extract keywords from the crawled articles.
3.	Create a relationship map between the extracted keywrods.
4.	Cluster the mapped keywrods.

## Step 1: Crawl
I used a python framework called [Scrapy](https://scrapy.org) to crawl articles. It’s intuitive and easy to use.

If you ever want to crawl web content, I strongly suggest this framework.

Check NewyorCrawler.py as an example to see how I crawl the articles from nytimes.com; and save them to the database.

The crawler visits every single URL on nytimes.com. It looks for an article content. If it finds an article content it saves it together with its attributes to our database. If not, it skips this url.

I predefined what “article content” means. For Newyork Times it means having the following html tag:
```html
<p class="story-body-text story-content">content content content</p>
```

If a nytimes.com url has this tag, it means it's an article url. 

And "article content" tags are different for different sources. So “article” needs to be defined again and again for each news source.

P.S. An axample for non-article url: [https://www.nytimes.com/section/arts]

By now I have 30 crawlers for 30 different news sources. Check “news_sources.csv” under “data_files” folder to see all the sources.

I will only disclose the crawler I wrote for Newyork Times, dues to NDA.

In this step I runned the crawlers for 5-6 hours and I collected 30,000+ articles. You can find thecrawled articles in [articles.csv](https://www.dropbox.com/s/jvo5dr04vamwb96/articles.csv?dl=0) file. 

## Step 2: Extract
I use [Open Calais](http://www.opencalais.com/) from Thomson Reuters to extract keyword.

## Step 3: Map
## Step 4: Cluster

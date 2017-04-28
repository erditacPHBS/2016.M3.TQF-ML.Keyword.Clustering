# Methodology
I will complete this project with 4 major steps.

1.	Crawl at least 10,000 articles different sources. 
2.	Extract keywords from the crawled articles.
3.	Create a relationship map between the extracted keywrods.
4.	Cluster the mapped keywrods.

## Step 1: Crawl
I used a python framework called [Scrapy](https://scrapy.org) to crawl articles. It’s intuitive and easy to use. If you ever want to crawl web content, I strongly suggest this framework.

Check [NewyorkCrawler.py](NewyorkCrawler.py) as an example to see how I crawl the articles from nytimes.com; and save them to the database.

The crawler visits every single URL on nytimes.com. It looks for an article content. If it finds an article content it saves it together with its attributes to our database. If not, it skips this url.

I predefined what “article content” means. For Newyork Times it means having the following html tag:
```html
<p class="story-body-text story-content">content content content</p>
```

If a nytimes.com url has this tag, it means it's an article url. 

"article content" tags are different for different sources. So “article” needs to be defined again and again for each news source.

P.S. An axample for non-article url: [https://www.nytimes.com/section/arts]

By now I have 30 crawlers for 30 different news sources. Check “news_sources.csv” under “data_files” folder to see all the sources. I will only disclose the crawler I wrote for Newyork Times, dues to NDA.

In this step I runned the crawlers for 5-6 hours and I collected 30,000+ articles. You can find the crawled articles in [articles.csv](https://www.dropbox.com/s/jvo5dr04vamwb96/articles.csv?dl=0) file. 

## Step 2: Extract
I use [Open Calais](http://www.opencalais.com/) from Thomson Reuters to extract keyword.

## Step 3: Map
I use [D3 Force](https://github.com/d3/d3-force) algorithm to map the keywords.

## Step 4: Cluster
I use [KMeans](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) algorithm from scikit-learn library to cluster the keywords.

# What does all these ipython notebooks and files mean?
I wanted to show you my journey to achieve clustering around 72000+ keywords.

I started with clustering around 100 keywords, I wanted to get familiar with all the methodology, functions and python libraries I need to use. [KeywordClusteringSmall.ipynb](KeywordClusteringSmall.ipynb) and [KeywordClusteringSmall2.ipynb](KeywordClusteringSmall2.ipynb) were written with that effort. You can still find useful information that explains why and how I followed a certain path to prepare the keywords for mapping.

After that I created a very clean purpose oriented ipython notebook: [KeywordClusteringCleaned.ipynb](KeywordClusteringCleaned.ipynb)

Larger sets of keywords (around 7000) are tested in this file: [KeywordClustering.ipynb](KeywordClustering.ipynb)

All the JSON and CSV files here are generated when I run the codes in the notebooks above.

After I made keywords ready for mapping I mapped them using D3-Force algorithm which you can see how I do it by simply running the [index.html](index.html) . But you need a server, if you open the file directly on your browser it won't work. So you need to call it with a server call.

Mapping is done and we generated this file: [data_files/afterMapping.csv](data_files/afterMapping.csv)
I run a few experiments on this file together with other "afterMappingxxx" files on the following notebooks:

1.	[AfterMapping.ipynb](AfterMapping.ipynb) 
2.	[AfterMappingLarge.ipynb](AfterMappingLarge.ipynb) 
3.	[AfterMappingClean.ipynb](AfterMappingClean.ipynb) 

And all the plots are under the "/plot/" directory.

### These were all before I collected around 70000 keywords.
After I collected enough keywords, just to present clean files I created this directory: "/final/"
You can find all you need to know in a clean way in that directory.

# Data Files (will be updated as new files are added)
## articles_sample.csv
This is a sample file. For full version go to: [articles.csv](https://www.google.com)
This file includes all attributes of the article except the article text (content). Article content can be found in “article_text.css” file. It has 12 columns:
|               | Name          | Explaination  |
|:-------------:|---------------|-------|
| 1 | id | A unique number given to each article. |
| 2 | title | The title of the article |
| 3 | slug      | The internal link of the article. This link will be used to access the article from Siphtor. |
"id"
A unique number given to each article.
"title"
The title of the article
"author_name"
The author name of the article.
"image"
The link of the featured image of the article
"link"
The link of the article
"summary"
The summary of the article.
"slug"
The internal link of the article. This link will be used to access the article from Siphtor.
For example: siphtor.com/[slug]
"date_crawled"
The date that we crawled this article.
"publish_date"
The date that this article is published on its own source.
"article_id"
A website specific id of the article. It’s unique for each article.
"news_source_id"
The id of the news source. Check the file: “news_sources.csv” for the name of the source.
"rss_source_id"
The id of the rss source of the article. Check the file: “rss_sources.csv” for the rss link.
 
## article_text_sample.csv
This is a sample file. For full version go to: [article_text.csv](https://www.google.com)
This file includes the text content of the article. In other words it includes the whole article as a text. It has 5 columns.
"id"
A unique number given to each article. This id matches with the one in “articles.csv”. Basically you can check check atricle attributes by looking for the same id in “articles.csv”
"description"
The content of the article.
"status"
A binary number to indicate whether keywords are extracted from this article of not.
0 means not extracted
1 means extracted
"date_crawled"
The date we crawl the article
"article_id"
A website specific id of the article. It’s unique for each article. We have the same id in “artciles.csv”

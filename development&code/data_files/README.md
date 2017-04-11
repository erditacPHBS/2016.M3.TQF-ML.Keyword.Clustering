# Data Files (will be updated as new files are added)
## articles_sample.csv
This is a sample file. For full version go to: [articles.csv](https://www.dropbox.com/s/jvo5dr04vamwb96/articles.csv?dl=0)

This file includes all attributes of the article except the article text (content).

Article content can be found in “article_text.css” file. It has 12 columns:

|               | Name          | Explaination  |
|:-------------:|---------------|-------|
| 1 | id | A unique number given to each article |
| 2 | title | The title of the article |
| 3 | author_name | The author name of the article|
| 4 | image | The link of the featured image of the article |
| 5 | link | The link of the article |
| 6 | summary | The summary of the article |
| 7 | slug | The internal link of the article. This link will be used to access the article from Siphtor. For example: siphtor.com/[slug] |
| 8 | date_crawled | The date that we crawled this article |
| 9 | publish_date | The date that this article is published on its own source |
| 10 | article_id | A website (Siphtor) specific id of the article. It’s unique for each article. |
| 11 | news_source_id | The id of the news source. Check the file: [news_sources.csv](news_sources.csv) for the name of the source. |
| 12 | rss_source_id | The id of the rss source of the article. Check the file: [rss_sources.csv](rss_sources.csv) for the rss link. |

## article_text_sample.csv
This is a sample file. For full version go to: [article_text.csv](https://www.dropbox.com/s/4v9xxuk3lb1geic/article_text.csv?dl=0)

This file includes the text content of the article.

In other words it includes the whole article as a text. It has 5 columns.

|               | Name          | Explaination  |
|:-------------:|---------------|-------|
| 1 | id | A unique number given to each article. This id matches with the one in [articles_sample.csv](articles_sample.csv) . Basically you can check check atricle attributes by looking for the same id in “articles.csv” |
| 2 | description | The full content of the article |
| 3 | status | A binary number to indicate whether keywords are extracted from this article of not. 0 means not extracted. 1 means extracted. |
| 4 | date_crawled | The date we crawl the article |
| 5 | article_id | A website (Siphtor) specific id of the article. It’s unique for each article. We have the same id in [articles_sample.csv](articles_sample.csv) |

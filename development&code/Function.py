from w3lib.html import remove_tags
# import scrapper.spiders


class Function(object):
    
    # count item in xml
    def rss_item_count(self,response,query):
        itemCount = response.xpath(query).extract()
        return itemCount
    
    # parse xml content for rss 
    def rss_parse(self,response,query,number):
        try: 
            rssContent = response.xpath(query)[number].extract()
        except IndexError:
            rssContent = "None"
        return rssContent
    
    # query function
    def rss_content(self,response,rssSourceId,itemNumber,newsSourceId,db):
        title =self.rss_parse(response,'//item/title/text()',itemNumber)
        link =self.rss_parse(response,'//item/link/text()',itemNumber)
        pubDate =self.rss_parse(response,'//item/pubDate/text()',itemNumber)
        description =self.rss_parse(response,'//item/description',itemNumber)
        author = self.rss_parse(response, "//item/author",itemNumber)
        slug = title.replace(" ","_")
        
        image =""
        summary = remove_tags(description)
        authorName = remove_tags(author)
        result = self.checkrss(rssSourceId, newsSourceId, slug, db)
        if result=="":
            self.insert_rssContent(title.strip(), authorName, image, link, summary, slug, newsSourceId, rssSourceId[0], db)
    
    # checked rss value already exits into database     
    def checkrss(self,rssSourceId,newsSourceId,slug,db):
        sql = "select id from api_article where news_source_id=%s and rss_source_id=%s and slug= %s COLLATE utf8_unicode_ci"
        data = (newsSourceId,rssSourceId[0],slug)
        result =""
        for result in db.save(sql,data):
            return result
        return result
        
    # get title from url    
    def extract_with_title(self,response,query):
        try :
            data_title = response.xpath(query).extract()[0]
        except IndexError:
            try:
                data_title = response.xpath("//meta[@name='twitter:title']/attribute::content").extract()[0]
            except IndexError:
                try:
                    data_title = response.xpath("//meta[@property='twitter:title']/attribute::content").extract()[0]
                except IndexError:
                    data_title = response.xpath("//title/text()").extract()[0]
        return remove_tags(data_title.encode('ascii','ignore'))
    
    # get summary from url
    def extract_with_summary(self,response,query):
        url = response.url
#         data_summary=""
        try:
            data_summary = response.xpath(query).extract()[0]
        except IndexError:
            try:
                data_summary = response.xpath("//meta[@name='Description']/attribute::content").extract()[0]
            except IndexError:
                try:
                    data_summary = response.xpath("//meta[@property='og:description']/attribute::content").extract()[0]
                except IndexError :
                    data_summary = 'None'
                    
        if data_summary=="" or data_summary=='None':
            
            if "https://www.nytimes.com/" in url:
                data = response.xpath("//div[@class='story-body-supplemental']/div/p").extract()
                data_summary = data[0]
            
            elif "http://www.wsj.com/" in url:
                data = response.xpath("//div[@class='wsj-snippet-body']/p").extract()
                data_summary = data[0]
                 
            elif "https://www.washingtonpost.com/" in url :
                data = response.xpath("//div[@class='article-body']/article[@itemprop='articleBody']/p").extract()
                data_summary = data[0]
                
            elif "http://www.gizmodo.in/" in url :
                data = response.xpath("//div[@class='articletxt']/div[@class='Normal']/div/p").extract()
                data_summary = data[0]
                
            elif "http://arstechnica.com/" in url :
                data = response.xpath("//div[@class='articleBody']/p").extract()
                data_summary = data[0]
                
            elif "http://www.latimes.com/" in url :
                data = response.xpath("//div[@itemprop='articleBody']/div[@class='trb_ar_page']/p").extract()
                data_summary = data[0]
                
            elif "https://www.theguardian.com/" in url :
                data = response.xpath("//div[@itemprop='articleBody']/p").extract()
                if data=="":
                    data = response.xpath("//div[@itemprop='reviewBody']/p").extract()
                data_summary = data[0]
                
            elif "http://www.foxnews.com/" in url :
                data = response.xpath("//div[@class='article-text']/p").extract()
                data_summary = data[0]
                
            elif "http://www.sportingnews.com/" in url :
                data = response.xpath("//div[@class='entry-content']/p").extract()
                data_summary = data[0]
                
            elif "http://www.si.com/" in url :
                data = response.xpath("//div[@itemprop='articleBody']/p").extract()
                data_summary = data[0]
                
            elif "http://www.politico.com/" in url :
                data = response.xpath("//div[@class='story-text ']/blockquote/p").extract()
                if data=="":
                    data = response.xpath("//div[@class='story-column']/div/p").extract()
                data_summary = data[0]
                
            elif "http://thehill.com/" in url :
                data = response.xpath("//div[@class='field-items']/div/p").extract()
                data_summary = data[0]
            
            elif "http://www.dailykos.com/" in url :
                data = response.xpath("//div[@class='story-intro']/p").extract()
                data_summary = data[0]
                
            elif "http://www.rollingstone.com/" in url :
                data = response.xpath("//div[@class='article-content']/p").extract()
                data_summary = data[0]
                
            elif "http://www.gqindia.com/" in url :
                data = response.xpath("//div[@class='container']/article/p").extract()
                data_summary = data[0]
                
            elif "http://europe.newsweek.com/" in url :
                data = response.xpath("//div[@itemprop='articleBody']/p").extract()
                data_summary = data[0]
                
            elif "http://foreignpolicy.com/" in url :
                data = response.xpath("//div[@class='shares-position ']/p").extract()
                data_summary = data[0]
                
            elif "http://dailycaller.com/" in url :
                data = response.xpath("//div[@class='dc-word-up']/p").extract()
                data_summary = data[0]
                
            elif "http://www.washingtonexaminer.com/" in url :
                data = response.xpath("//div[@class='body']/cnt/p").extract()
                data_summary = data[0]
                
            elif "https://www.bloomberg.com/" in url :
                data = response.xpath("//div[@class='body-copy']/p").extract()
                data_summary = data[0]
                
            elif "http://www.reuters.com/" in url :
                data = response.xpath("//div[@id='article-byline']/span/p").extract()
                data_summary = data[0]
                
            elif "https://www.afp.com/" in url :
                data = response.xpath("//div[@class='article_content']/div[@class='textcontent_img']/div/p").extract()
                data_summary = data[0]
             
            elif "https://www.theatlantic.com/" in url :
                data = response.xpath("//div[@class='article-body']/section/p").extract()
                data_summary = data[0]
                
            elif "http://www.thedailybeast.com/" in url :
                data = response.xpath("//div[@class='BodyNodes']/div/p").extract()
                data_summary = data[0]
                
            elif "http://www.huffingtonpost.in/" in url :
                data = response.xpath("//div[@data-part='contents']/p").extract()
                data_summary = data[0]
                
            elif "http://qz.com/" in url :
                data = response.xpath("//div[@itemprop='articleBody']/div/p").extract()
                data_summary = data[0]
                
            elif "http://www.washingtontimes.com/" in url :
                data = response.xpath("//div[@class='bigtext']/p").extract()
                data_summary = data[0]
                
        return remove_tags(data_summary.encode('ascii','ignore'))
    
    #get author
    def extract_with_author(self,response,query):
        author = response.xpath(query).extract()
        return remove_tags(author[0].encode('ascii','ignore'))
    
    #get author date
    def extract_with_author_date(self,response,query):
        date = response.xpath(query).extract()
        return remove_tags(date[0].encode('ascii','ignore'))
    
    #get full description
    def extract_with_allDescription(self,response,query):
        full_description = response.xpath(query).extract()
        data=""
        for desc in full_description:
            desc1 = remove_tags(desc)
            data += desc1
        return data
    
    # get link from url
    def extract_with_link(self,response,query):
        try:
            data_link = response.xpath(query).extract()[0]
            
        except IndexError:
                data_link = response.xpath("//link[@rel='canonical']/attribute::href").extract()[0]
        return remove_tags(data_link.encode('ascii','ignore'))
    
    # get keyword from url
    def extract_with_keywords(self,response,query):
        keyword=""
        try:
            keyword =response.xpath(query).extract_first()
        except IndexError:
            try:
                keyword = response.xpath("//meta[@name='keywords']/attribute::content")
            except IndexError :
                try:
                    keyword = response.xpath("//meta[@property='keywords']/attribute::content")
                except IndexError:
                    keyword = ""
        return str(keyword)
        
    # get image from url
    def extract_with_image(self,response,query):
        imgLink =response.xpath(query).extract_first()
        imageLink =str(imgLink)
        if imageLink=='None':
            imageLink = response.xpath("//meta[@name='og:image']/attribute::content").extract_first()
            if imageLink=="None":
                imageLink = response.xpath("//meta[@property='twitter:image']/attribute::content").extract_first()
            return str(imageLink)
        else:
            return remove_tags(imageLink)

    # insert data into articles tables 
    def insert_content(self,title,image,author,summary,newsSourceID,db,slug,link,publishDate,fullDescription,keyword,getArticleId):
        sourceID = str(newsSourceID)
        data = (title,image,author,summary,sourceID,slug,1,link,str(publishDate),getArticleId)
        sql = "insert into api_article(title,image,author_name,summary,news_source_id,slug,rss_source_id,date_crawled,link,publish_date,article_id) values(%s, %s, %s, %s, %s,%s,%s,NOW(),%s,%s,%s)"
        db.save(sql,data)
        
        articleId=""
        for aid in db.save("select id from api_article where publish_date=%s and news_source_id=%s and rss_source_id=%s",(str(publishDate),sourceID,1)):
            articleId = aid[0]
        if articleId!="":
            db.save("insert into api_articledescription(description,article_id,date_crawled,status) values(%s,%s,NOW(),%s)",(fullDescription,str(articleId),False))
        
        keywords = keyword.split(",")
        for k in keywords:
            key = k.strip()
            keywordID=""
            for kid in db.save("select id from api_keyword_from_source where name=%s",(key,)):
                keywordID = kid[0]
            
            if keywordID=="":    
                db.save("insert into api_keyword_from_source(name,date_added) values(%s,NOW())",(key,))
            
                for keyId in db.save("select id from api_keyword_from_source where name=%s",(key,)):
                    keywordID = keyId[0]
            
            db.save("insert into api_article_keyword(article_id,keyword_from_source_id) values(%s,%s)",(str(articleId),str(keywordID)))
      
    # checked condition if data already exits or not
    def slugCheck(self,slug,newsSourceId,db):
        item = (slug,newsSourceId)
        data = ""
        sql = "select id from api_article where slug = %s and news_source_id = %s"
        for data in db.save(sql,item):
            return data
        return data
    
    # update first crawler into table
    def updateNewSource(self,newsSourceId,db):
        data = db.query("update api_newssource set first_crawl=True, date_crawled=NOW() where id='"+str(newsSourceId)+"'")
        return data
    
    # get rss id from rsssource table
    def getRssSourceId(self,url,db,newsSourceID):
        sql = "select id from api_rsssource where rss_url = %s and news_source_id = %s"
        item = (url,newsSourceID)
        rssId = ""
        for rssId in db.save(sql,item):
            return rssId
        return rssId
    
    # insert rss data into article table
    def insert_rssContent(self,title,author,image,link,summary,slug,newsSourceId,rssSourceId,db):
        
        data = (title.strip(),author.strip(),image.strip(),link.strip(),summary.strip(),slug.strip(),str(newsSourceId),str(rssSourceId))
        sql = "insert into api_article(title,author_name,image,link,summary,slug,news_source_id,rss_source_id,date_crawled) values(%s,%s,%s,%s,%s,%s,%s,%s,NOW())"
        db.save(sql,data)              
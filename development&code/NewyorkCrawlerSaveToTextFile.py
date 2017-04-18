import scrapy
#from scrapper.spiders.DatabaseManager import DatabaseManager
from scrapper.spiders.Function import Function
from scrapper.spiders.FunctionCrawler import FunctionCrawler

class NewyorkCrawler(scrapy.Spider):
    # handle http status exception 
    handle_httpstatus_list = [403]
#     import pdb;pdb.set_trace();
    # spider calling name
    name = 'nytimes'
    
    # declare some variables
    newsSourceId=0
    siteUrl=[]
    firstCrawlStatus=""
    rssSourceStatus=""
    rssSourceId=[]
    
    # get object of connection from databaseManager Model
    #db = DatabaseManager()
    
    # fetch data from table according function name 
    '''for data in db.query("select id,url,first_crawl,has_rss from api_newssource where function_name='nytimes'"):
        newsSourceId = data[0]
        siteUrl.append(data[1].strip())
        firstCrawlStatus = data[2]
        rssSourceStatus = data[3]
    
    # checked condition for first crawler and rss exits
    if ((firstCrawlStatus==1) and (rssSourceStatus == 1)) :
        siteUrl.pop(0)
        for rssdata in db.query("select id,rss_url from api_rsssource where news_source_id='"+str(newsSourceId)+"'"):
            rssSourceId.append(rssdata[0])
            siteUrl.append(rssdata[1].strip())

    '''
    
    # start request called
    def start_requests(self):
        for site in self.siteUrl :
            yield self.make_requests_from_url(site)
      
    # called parse function after start_requests 
    def parse(self, response):
        
        # get url from response 
        url = response.url
        
        # get object of Function and FunctionCrawler 
        function = Function()
        fc = FunctionCrawler()
        
        # checked condition if url is a main url or rss url  
        if url=="https://www.nytimes.com/":
            # update first crawler in database
            data = function.updateNewSource(self.newsSourceId, self.db)
            if data!="":
                
                # fetch link from url
                for href in response.xpath("//a/@href").extract():
                    yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_Level1,meta={'newsSourceId':self.newsSourceId,'database':self.db})
                     
                for href in response.xpath("//*[@class='story-heading']/a/@href").extract():
                    yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_Level3,meta={'newsSourceId':self.newsSourceId,'database':self.db})
        else:
            # parse rss url
            fc.rss_function_crawl(response, self.db, self.newsSourceId)
            
    # parse url for level2
    def parse_Level1(self,response):
        newsSourceId = response.meta['newsSourceId']
        db = response.meta['database']
        for href in response.xpath('*//a/@href').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse_Level2,meta={'newsSourceId':newsSourceId,'database':db})
    
    def parse_Level2(self,response):
        newsSourceId = response.meta['newsSourceId']
        db = response.meta['database']
        for href in response.xpath('*//a/@href').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse_Level3,meta={'newsSourceId':newsSourceId,'database':db})

    def parse_Level3(self,response):
        f = FunctionCrawler()
        newsSourceId = response.meta['newsSourceId']
        db = response.meta['database']
        url = response.url
        if "https://www.nytimes.com/" in url:
            f.function_crawl(response, db, newsSourceId)    
            
#     def spider_closed(self):
#         raise CloseSpider('exception occuor')

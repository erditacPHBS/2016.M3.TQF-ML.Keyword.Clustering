from scrapper.spiders.Function import Function
import time
from calendar import timegm
import datetime
from datetime import timedelta


class FunctionCrawler(object) :
	
	# query function for url
	def function_crawl(self,response,db,newsSourceId):
# 		import pdb;pdb.set_trace();
# 		try:
		f = Function()
		url = response.url
		title = f.extract_with_title(response,"//meta[@property='og:title']/attribute::content"),
		image = f.extract_with_image(response,"//meta[@property='og:image']/attribute::content"),
		keywords = f.extract_with_keywords(response,"//meta[@name='news_keywords']/attribute::content"),
		summary = f.extract_with_summary(response,"//meta[@name='description']/attribute::content"),
		
		author_date=""
		epoch_time=""
		full_description=""
		if "https://www.nytimes.com/" in url:		#DEC. 13, 2016
			author = f.extract_with_author(response,"//meta[@name='author']/attribute::content")
			author = author.replace("\n","")
			author = author.replace("\t","")

			author_date = f.extract_with_author_date(response,"//time[@class='dateline']")
			if 'May' not in author_date:
				auth_date = author_date[:3]
			if 'SEP' or 'MAR' or 'APR' in author_date:
				dd = author_date.replace(author_date[:5],auth_date)
			else :
				dd = author_date.replace(author_date[:4],auth_date)
			try:
				utc_time = time.strptime(dd, "%b %d, %Y")
			except :
				utc_time = time.strptime(dd, "%b%d, %Y")

			epoch_time = timegm(utc_time)	# GMT+
		
			full_description = f.extract_with_allDescription(response,"//div[@class='story-body-supplemental']/div/p")
			full_description = full_description.replace("\n", "")
			full_description = full_description.replace("\t", "")
			full_description = full_description.replace("\t", "")	
				
		t = title[0].strip()
		i = image[0].strip()
		a = author
		s = summary[0].strip()
		k = keywords[0].strip()
		
		t = t.replace("\n"," ")
		s = s.replace("\n"," ")
		slug = t.replace(" ","_")
		

		# checked conditions into database if data already exits or not
		msg = ""
# 		2016-12-28 17:38:31
# 		print("***** %%%%%%%%% ",utc_time)
		local_time = time.strftime("%Y-%m-%d %H:%M:%S",utc_time)
# 		print("***** %%%%%%%%% ",local_time)
		
		getArticleId = str(epoch_time)
		getArticleId = getArticleId[:1].replace(getArticleId[:1], 'a')+getArticleId[1:]
		
		if msg=="":
			if len(url.strip())>0:
				if ('android-app' not in url):
					if full_description !="":
						f.insert_content(t,i,a,s,newsSourceId,db,slug,url,local_time,full_description,k,getArticleId)
# 		except:
# 			print
	# called rss function for parse data				
	def rss_function_crawl(self,response,db,newsSourceId):
		url = response.url
		f = Function()
		rssSourceId = f.getRssSourceId(url,db,newsSourceId)
		
		# count item into rss link
		itemCount = f.rss_item_count(response,'//item')
		for number in range (0,len(itemCount)):
			f.rss_content(response, rssSourceId, number, newsSourceId,db)
			
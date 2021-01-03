import scrapy
import json
import re
import time
from zhihu_comment.items import ZhihuCommentItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/topics/19564862/feeds/top_activity?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&after_id=00.00000']
    headers = {
        # "HOST": "www.zhihu.com",
        # "Referer": "https://www.zhizhu.com",
        # User-Agent必不可少
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    count = 0

    def parse(self, response):
        # count += 1
        # if count > 100:
        #     return
        # response.encoding = ('utf-8')
        first_layer = json.loads(response.text)
        # print(r.text)
        is_end = first_layer['paging']['is_end']
        next_url = first_layer['paging']['next']
        # print(first_layer['data'])
        for data in first_layer['data']:
            author_id = data['target']['id']
            type_comment = data['target']['type']
            # print(type_comment,'11111111111111')
            if data['target']['comment_count'] != 0:
                print(data['target']['comment_count'],'000000000000000000000')
                url = f"https://www.zhihu.com/api/v4/{type_comment}s/{author_id}/root_comments?order=normal&limit=20&offset=0&status=open"
                print(url,'111111111111111111')
                yield scrapy.Request(url, headers=self.headers,
                                     callback=self.parse_comment)

        # if not is_end:
        #     yield scrapy.Request(next_url, headers=self.headers,callback=self.parse)

    def parse_comment(self,response):
        # response.encoding = ('utf-8')
        second_layer = json.loads(response.text)
        gender_dic = {'1': '男', '-1': '匿名', '0': '女'}
        is_end = second_layer['paging']['is_end']
        next_url = second_layer['paging']['next']
        comment_item = ZhihuCommentItem()
        for data in second_layer['data']:
            if '<p>' in data['content']:
                data['content'] = re.findall('<p>(.+?)</p>', data['content'])[0]
            comment_item['author'] =  data['id'],
            comment_item['comment'] = data['content']
            comment_item['comment_time'] = time.strftime('%Y%m%d%H%S', time.gmtime(data['created_time']))
            comment_item['gender'] = gender_dic[str(data['author']['member']['gender'])]
            print(data['content'],'2222222222222')
        if not is_end:
            yield scrapy.Request(next_url, headers=self.headers,callback=self.rest_comment)



    def rest_comment(self,response):
        gender_dic = {'1':'男','-1':'匿名','0':'女'}
        # response.encoding = ('utf-8')
        second_layer = json.loads(response.text)
        is_end = second_layer['paging']['is_end']
        next_url = second_layer['paging']['next']
        comment_item = ZhihuCommentItem()
        for data in second_layer['data']:
            if '<p>' in data['content']:
                data['content'] = re.findall('<p>(.+?)</p>', data['content'])[0]
            comment_item['author'] = data['id'],
            comment_item['comment'] = data['content']
            comment_item['comment_time'] = time.strftime('%Y%m%d%H%S', time.gmtime(data['created_time']))
            comment_item['gender'] = gender_dic[str(data['author']['member']['gender'])]
            print(data['content'],'33333333333333')
        if not is_end:
            yield scrapy.Request(next_url, headers=self.headers, callback=self.rest_comment)


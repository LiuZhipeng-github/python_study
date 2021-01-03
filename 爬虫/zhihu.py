import requests, json, re
from lxml import etree
import time
import pandas as pd

def comments():
    url = 'https://www.zhihu.com/api/v4/answers/1651999668/root_comments?order=normal&limit=20&offset=0&status=open'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6) Gecko/20050225 Firefox/1.0.1',
        'Connection': 'close',
    }
    # res = requests.get(url,headers=headers)
    response = requests.get(url, headers=headers)
    text = response.text.encode('utf-8')

    comment = json.loads(text)
    print(comment)
    result = []
    for i in comment['data']:
        if '<p>' in i['content']:
            i['content'] = re.findall('<p>(.+?)</p>', i['content'])[0]
        result_tem = {'author': i['author']['member']['name'], 'comment': i['content'],
                      'child_comment_count': i['child_comment_count']}
        result.append(result_tem)
    for i in result:
        print(i)


def main():
    url = 'https://www.zhihu.com/topic/19564862/hot'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6) Gecko/20050225 Firefox/1.0.1',
        'Connection': 'close',
    }
    # res = requests.get(url,headers=headers)
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    html = etree.HTML(response.text)
    rear = html.xpath('//div[@class="List-item TopicFeedItem"]/div/@data-zop')
    for i in rear:
        i = json.loads(i)
        if i['authorName'] == '':
            i['authorName'] = '匿名用户'
        print(i['authorName'])


def first_parser(url, count):
    count += 1
    if count > 10:
        return
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6) Gecko/20050225 Firefox/1.0.1',
        'Connection': 'close',

    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    # r.encoding = r.apparent_encoding
    r.encoding = ('utf-8')
    first_layer = json.loads(r.text)
    # print(r.text)
    is_end = first_layer['paging']['is_end']
    next_url = first_layer['paging']['next']
    print(first_layer['data'])
    for data in first_layer['data']:
        # print(data)
        try:
            tem_dic = {'author_id': data['target']['id'], 'commit_time': data['target']['created'],
                       'comment_count': data['target']['comment_count'],
                       'type': data['target']['type']}
        except:
            tem_dic = {'author_id': data['target']['id'], 'commit_time': data['target']['created_time'],
                       'comment_count': data['target']['comment_count'],
                       'type': data['target']['type']}

        result.append(tem_dic)
    return first_parser(next_url, count)


def join_url():
    # print(result)
    url_list = []
    for i in result:
        if i['comment_count'] != 0:
            url = f'https://www.zhihu.com/api/v4/{i["type"]}s/{i["author_id"]}/root_comments?order=normal&limit=20&offset=0&status=open'
            url_list.append(url)
    return url_list


def second_parse(url_list):
    for url in url_list:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6) Gecko/20050225 Firefox/1.0.1',
            'Connection': 'close',
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = ('utf-8')
        second_layer = json.loads(r.text)
        gender_dic = {'1': '男', '-1': '匿名', '0': '女'}
        is_end = second_layer['paging']['is_end']
        next_url = second_layer['paging']['next']
        for data in second_layer['data']:
            if '<p>' in data['content']:
                data['content'] = re.findall('<p>(.+?)</p>', data['content'])[0]
            comment_tem = {'commenter_id': data['id'], 'content': data['content'],'created_time':time.strftime('%Y%m%d%H%S',time.gmtime(data['created_time'])),'gender':gender_dic[str(data['author']['member']['gender'])]}
            comments_result.append(comment_tem)
            print(comment_tem)
        if is_end:
            pass
        else:
            rest_comment(next_url)


def rest_comment(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6) Gecko/20050225 Firefox/1.0.1',
        'Connection': 'close',

    }
    gender_dic = {'1':'男','-1':'匿名','0':'女'}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = ('utf-8')
    second_layer = json.loads(r.text)
    is_end = second_layer['paging']['is_end']
    next_url = second_layer['paging']['next']
    for data in second_layer['data']:
        if '<p>' in data['content']:
            data['content'] = re.findall('<p>(.+?)</p>', data['content'])[0]
        comment_tem = {'commenter_id': data['id'], 'content': data['content'],'created_time':time.strftime('%Y%m%d%H%S',time.gmtime(data['created_time'])),'gender':gender_dic[str(data['author']['member']['gender'])]}
        comments_result.append(comment_tem)
        print(comment_tem)
    if is_end:
        pass
    else:
        return rest_comment(next_url)


def to_csv():
    df = pd.DataFrame(comments_result)
    df.to_csv('result.csv')




if __name__ == '__main__':
    comments_result = []
    result = []
    count = 0
    url = 'https://www.zhihu.com/api/v4/topics/19564862/feeds/top_activity?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&after_id=00.00000'
    # url = 'https://www.zhihu.com/api/v4/topics/19860414/feeds/top_activity?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&after_id=00.00000'
    first_parser(url, count)
    url_list = join_url()
    second_parse(url_list)
    to_csv()
    print(f'已完成任务，本次共爬取{len(comments_result)}条内容')


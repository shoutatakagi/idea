# encoding: utf-8

from requests_oauthlib import OAuth1Session
import json
import urllib
import urllib2
import BeautifulSoup
import time
import random
import requests
import sqlite3

伏せ                             # Consumer Key
伏せ       # Consumer Secret
伏せ　# Access Token
伏せ　#ai_idea
伏せ       # Accesss Token Secert
伏せ


def kaiwa(v,screen_name):
    print '接続を受信'
    appid = "なし"  # ID
    pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse"

    # 形態素解析
    def morph(sentence, appid=appid, results="ma", filter="1|2|3|4|5|6|7|8|9|10|11|12|13"):
        ret = []
        # 
        sentence = urllib.quote_plus(sentence.encode("utf-8"))
        query = "%s?appid=%s&results=%s&filter=%s&sentence=%s" % (pageurl, appid, results, filter, sentence)
        c = urllib2.urlopen(query)
        soup = BeautifulSoup.BeautifulSoup(c.read())
        return [(w.surface.string, w.reading.string, w.pos.string) for w in soup.ma_result.word_list]
    
    sentence = v
    result = morph(sentence, appid=appid)
    v = [x[0] for x in result] #わかち配列

    I=len(v)#入力した文の品詞数
    FList=[]
    s=0
    print v
    if I == 0:
        I=I+1
    
    con = sqlite3.connect("SLEAD.db")
    c = con.execute(u"select * from RES")
    for row in c:#SQLを一行づつrowに格納
        rowA=[x for x in row[0].split(" ")]#わかちを配列に
        IA=float(0)#IAをリセット
        for x in v:#入力された文を品詞ごとに比較
            if x in rowA:#もし同じ単語が中にあるならIAに加算
                IA=IA+1
        A=len(rowA)#AはrowAの単語数
        try:
            FList.append(IA/I*IA/A)
        except:
            FList.append(0)
            print '0'
            print 'ここ'
    space=""
    #if max(FList)>=0.6:
    print unicode(FList.index(max(FList)))
    sql=[u"select * from RES limit 1,",unicode(FList.index(max(FList))),u";"]
    sql=space.join(sql)
    c = con.execute(sql)
    for x in range(FList.index(max(FList))-1):
        row = c.fetchone()
    row = c.fetchone()

    print row[1]
    print unicode(max(FList))
    
    # URL
    url = "https://api.twitter.com/1.1/statuses/update.json"

    #本文
    honbun=[u'.',u'@',screen_name,u' ',row[1],u'（類似率＝',unicode(max(FList)),u')']
    space=''
    honbun=space.join(honbun)
    print 'honbunをプリント'
    print honbun
    
    params = {"status":honbun}

    # 投稿
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.post(url, params = params)
    
    # 確認
    if req.status_code == 200:
        print "OK"
    else:
        print "Error: %d" % req.status_code
        print "1"
    con.close()
    






Id="100"
while(True):

    url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"
    
   
    params = {"since_id":Id}

   
    try:
        twitter = OAuth1Session(CK, CS, AT, AS)
        req = twitter.get(url, params = params)

        if req.status_code == 200:
            # レスポンスはJSON形式なので parse
            timeline = json.loads(req.text)
            # 各ツイートの本文を表示
            tweet=timeline[0]
            user=tweet["user"]
            Id = tweet["id"]
            if user["screen_name"]=="ai_idea" or user["screen_name"]== u"ai_idea":
                print 'それ自分'
                print errorororor
            print tweet["text"]
            u=tweet["text"]
            lister=[x for x in u]
            text=[x for x in lister[len(user["screen_name"])+2:]]
            space=''
            text=space.join(text)
            print 'kaiwaに接続'
            kaiwa(text,user["screen_name"])
        else:
            # エラーの場合
            print "Error: %d" % req.status_code
            print "2"

    except:
        print '失敗'
        pass
    
    time.sleep(61)

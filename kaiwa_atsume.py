import urllib
import urllib2
import BeautifulSoup
import time
import random
import requests
import wikipedia
import sqlite3

#RES収集

con1 = sqlite3.connect("URLs.db")
c = con1.execute(u"select * from URL")
for x in range(2285):
    a = c.fetchone()

for row in c:
    print row[0]
    space=''
    url=['ここにURL',row[0]]
    url=space.join(url)
    print url

    con = sqlite3.connect("SLEAD.db")

    try:
        sql = u"""
        create table RES (
        resa varchar(500),
        resp varchar(500)
        );
        """
        con.execute(sql)#Tableを作る。
    except:
        pass
    
    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(url))
    for x in range(0,1000):
        resa=1
        resp=1
        x=unicode(int(x)+2)
        try:#レス番がなければ飛ばす
            pointer=soup.find('div',id=x)
            text=pointer.find('div',{"class":"comment"})
        except:#レス番がないのでブレイク
            print 'No more res'
            print 'currentURL = ',url
            break
        try: #intで変換できた場合（アンカの場合）
            an=text.find('a')['href']
            an=int(an)
            if an < x and an!=1:#未来安価or>>1ではないか判定
                texts=text.findAll(text=True)
                a=[x for x in texts]
                resp=a[3]
                pointer=soup.find('div',id=an)#アクティブのレスを取得
                text=pointer.find('div',{"class":"comment"})
        except:#int変換できなかった場合（アンカでない場合）
            print 'not P'
        try:#アクティブにアンカがあるかどうか
            an=text.find('a')['href']
            texts=text.findAll(text=True)
            a=[x for x in texts]
            resa=a[3]
        except:#アクティブにアンカがなければ
            texts=text.findAll(text=True)
            a=[x for x in texts]
            resa=a[0]
        try:#respが無ければ（2番目のtryでexceptされてればor ifがFalseだったら）エラーとなる
            con = sqlite3.connect("SLEAD.db")
            print '0'
            
            #伏せ

            pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse"

            # 形態素解析
            def morph(sentence, appid=appid, results="ma", filter="1|2|3|4|5|6|7|8|9|10|11|12|13"):
                ret = []
                
                sentence = urllib.quote_plus(sentence.encode("utf-8"))
                query = "%s?appid=%s&results=%s&filter=%s&sentence=%s" % (pageurl, appid, results, filter, sentence)
                c = urllib2.urlopen(query)
                soup = BeautifulSoup.BeautifulSoup(c.read())
                return [(w.surface.string, w.reading.string, w.pos.string) for w in soup.ma_result.word_list]

            print '1'            
            resa = [x for x in resa]
            space=""
            resa = space.join(resa[1:])
            sentence = resa
            result = morph(sentence, appid=appid)
            resa = [x[0] for x in result]
            space=" "
            resa = space.join(resa)

            print '2'
            
            resp = [x for x in resp]
            space=""
            resp = space.join(resp[1:])
            
            sql=[u"insert into RES values ('",resa,u"','",resp,u"')"]
            print resp
            print resa
            sql=space.join(sql)
            print '4'
            con.execute(sql)
            print '5'
            con.commit()
            print 'AP'
        except:
            print 'pass'
            pass
    time.sleep(150)
print '取得完了しました'
c = con.execute(u"select * from RES")
#for row in c:
#    print 'A',row[0],'P',row[1]
#    print '--------'
con.close()
con1.close()

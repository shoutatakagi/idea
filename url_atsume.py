import BeautifulSoup
import urllib
import urllib2
import time
import sqlite3

#URL収集

def loger():#データを取得
    i=200
    f=0
    for x in range(150):
        i=int(i)
        i=unicode(i+1)
        print '■',i,'■'
        space=''
        url=['ここにURL集積場所URL']
        url=space.join(url)
        rss = BeautifulSoup.BeautifulSoup(urllib.urlopen(url))#から一覧を取得
        sleads=rss.find('div',id="contents")
        sleads=sleads.find('div',{"class":"bbs-thread-list"})
        sleads=sleads.find('table')
        sleads=sleads.find('tbody')
        sleads=sleads.findAll('tr')
        for x in sleads:
            sleads=x.find('a')['href']#リンクの部分だけ抽出
            con = sqlite3.connect("URLs.db")
            sql=[u"insert into URL values ('",sleads,u"')"]
            sql=space.join(sql)
            con.execute(sql)
            url=['ここにURL',sleads]
            url=space.join(url)
            con.commit()
            print url
            print '----'
        time.sleep(10)
        if 0==1:
            if 0==1:
                soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(msg.Body))
                for x in range(0,1000):
                    x=unicode(int(x)+1)
                    pointer=soup.find('div',id=x)
                    text=pointer.find('div',{"class":"comment"})
                    a=[x for x in text]
                    msg.Chat.SendMessage(a[0])

def main():
    i=1
    print 'go'
    con = sqlite3.connect("URLs.db")
    sql = u"""
    create table URL (
      urldata varchar(25)
    );
    """
    #con.execute(sql)
    #loger()
    #↓SQLのデータを羅列
    c = con.execute(u"select * from URL")
    for row in c:
        print row[0]
    con.commit()
    con.close()
if __name__ == "__main__":
    main()

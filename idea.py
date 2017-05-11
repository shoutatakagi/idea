# encoding: utf-8

import Skype4Py
import urllib
import urllib2
import BeautifulSoup
import time
import random
import requests
import wikipedia
import sqlite3

#　i　d　e　a　本　体

def handler(msg, event):
    if event == u"RECEIVED":
        name=msg.FromDisplayName
        lister=[x for x in msg.Body]
        if msg.Body == u'shogoとは' or msg.Body == u'shogoって何？':
            msg.Chat.SendMessage('''shogoは私の開発者です！
Twitter @dr_shogo
http://dr-shogo.net''')
        elif lister[-4:] == [u'\u3063',u'\u3066', u'\u4f55', u'\uff1f']:#もし　って何？　で終わったら
            word=[x for x in lister[:-4]]
            space=''
            word=space.join(word)
            #wikiurl=['http://ja.wikipedia.org/wiki/',urllib2.quote(word.encode("utf-8"))]
            #wikiurl=space.join(wikiurl)#wikipediaURLと連結
            #msg.Chat.SendMessage(wikiurl)
            wikipedia.set_lang("ja")#wikipediaの言語を指定
            try:
                wiki=wikipedia.summary(word, sentences=1)#wikipediaで定義を取得
                msg.Chat.SendMessage(wiki)
            except:
                msg.Chat.SendMessage(u'※該当無し又は複数該当')
        elif lister[-2:] ==[u'\u3068',u'\u306f']:#もし　とは　で終わったら
            word=[x for x in lister[:-2]]
            space=''
            word=space.join(word)
            #wikiurl=['http://ja.wikipedia.org/wiki/',urllib2.quote(word.encode("utf-8"))]
            #wikiurl=space.join(wikiurl)#wikipediaURLと連結
            #msg.Chat.SendMessage(wikiurl)
            wikipedia.set_lang("ja")#wikipediaの言語を指定
            try:
                wiki=wikipedia.summary(word, sentences=1)#wikipediaで定義を取得
                msg.Chat.SendMessage(wiki)
            except:
                msg.Chat.SendMessage(u'※該当無し又は複数該当')
        elif lister[-3:] == [u'\u3067',u'\u691c',u'\u7d22']:#もし　で検索　で終わったらhttps://www.google.co.jp/search?q=%E3%83%A8%E3%82%B9%E3%82%AC&safe=off&source=lnms&tbm=isch
            word=[x for x in lister[:-3]]
            space=''
            word=space.join(word)
            sarchurl=['https://www.google.co.jp/#q=',urllib2.quote(word.encode("utf-8")),'&safe=off']
            sarchurl=space.join(sarchurl)
            msg.Chat.SendMessage(sarchurl)
        elif lister[-5:] == [u'\u3067',u'\u753b',u'\u50cf',u'\u691c',u'\u7d22']:#もし　で画像検索　で終わったら
            word=[x for x in lister[:-5]]
            space=''
            word=space.join(word)
            sarchurl=['https://www.google.co.jp/search?q=',urllib2.quote(word.encode("utf-8")),'&safe=off&source=lnms&tbm=isch']
            sarchurl=space.join(sarchurl)
            msg.Chat.SendMessage(sarchurl)
        elif lister[-4:] == [u'\u3067',u'\u691c',u'\u7d22',u'\uff01']:#もし　で検索！　で終わったら
            word=[x for x in lister[:-4]]
            space=''
            word=space.join(word)
            sarchurl=['http://www.google.com/search?btnI=I%27m+Feeling+Lucky&lr=lang_ja&ie=UTF-8&oe=UTF-8&q=',urllib2.quote(word.encode("utf-8"))]
            sarchurl=space.join(sarchurl)
            msg.Chat.SendMessage(sarchurl)
        elif lister[0:22] == [XXXXXXXXXXXXXXXXXX]:#もし　とは　で終わったら
            #lデータを取得
            soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(msg.Body))
            for x in range(0,1000):
                x=unicode(int(x)+1)
                pointer=soup.find('div',id=x)
                text=pointer.find('div',{"class":"comment"})
                a=[x for x in text]
                msg.Chat.SendMessage(a[0])
        elif lister[0:4] == [u'h', u't', u't', u'p']:#もし　http　で始まっていたら
            soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(msg.Body))
            response = urllib2.urlopen(msg.Body)
            html = response.read()
            a=[x for x in soup.title]
            b=[u'↑■　']
            b.extend(a)
            space=''
            a=space.join(b)
            msg.Chat.SendMessage(a)
            if 'Goose house' in html:
                msg.Chat.SendMessage(u'※注意※Goosehouse関連である可能性があります。')
        elif msg.Body == u"tester":#もし　tester　だったら
            msg.Chat.SendMessage(u"：：：正常に動作")
        elif msg.Body == u'idea情報':
            msg.Chat.SendMessage(u'name: idea')
            msg.Chat.SendMessage(u'最終更新 2014/08/23')
            msg.Chat.SendMessage(u'言語：Python2')
            msg.Chat.SendMessage(u'作者：shogo')
        elif msg.Body == u'idea機能':
            msg.Chat.SendMessage(u'■ideaは会話支援プログラムです。■')
            msg.Chat.SendMessage(u'・URLからタイトルを取得して返す')
            msg.Chat.SendMessage(u'・末尾「って何？」or「とは」で概要を提示')
            msg.Chat.SendMessage(u'・末尾「で検索」でgoogleリンク生成')
            msg.Chat.SendMessage(u'・末尾「で検索！」でim feeling lucky')
            msg.Chat.SendMessage(u'・末尾「で画像検索」で画像検索URL')
            msg.Chat.SendMessage(u'・「検索検索ぅ！」でガールフレンド(仮)')
            msg.Chat.SendMessage(u'・末尾「で形態素解析」で形態素解析')
            msg.Chat.SendMessage(u'・「まーじゃん」で個室リンク')
            msg.Chat.SendMessage(u'・「ごっどふぃーるど」でgodfieldリンク')
            msg.Chat.SendMessage(u'・idea情報,idea機能,ideaモジュール,ideaソース,などで開示')
            msg.Chat.SendMessage(u'・末尾「..」or 先頭スペース で会話')
            msg.Chat.SendMessage(u'・ちょっとしたおしゃべり')
        elif msg.Body == u'ideaモジュール':
            msg.Chat.SendMessage('''import Skype4Py
import urllib
import urllib2
import BeautifulSoup
import time
import random
import requests
import wikipedia''')
        elif msg.Body == u'いであ' or msg.Body == u'idea' or msg.Body == u'いであ～' or msg.Body == u'イデア' or msg.Body == u'イデア～' or msg.Body == u'いであー':
            rander=random.randint(1,5)
            if rander == 1:
                msg.Chat.SendMessage(u'はーい！')
            if rander == 2:
                msg.Chat.SendMessage(u'呼んだ？')
            if rander == 3:
                msg.Chat.SendMessage(u'いであです！')
            if rander == 4:
                msg.Chat.SendMessage(u'どうしたの？')
            if rander == 5:
                msg.Chat.SendMessage(u'ん？')
        elif msg.Body == u'ただいま' or msg.Body == u'tadaima':
            rander=random.randint(1,5)
            if rander == 1:
                a=[u'おかえり～']
            if rander == 2:
                a=[u'おかえりなさい！']
            if rander == 3:
                a=[u'おかりなさーい！']
            if rander == 4:
                a=[u'おかえりんこ！']
            if rander == 5:
                a=[u'おかえり！']
            b=[name]
            b.extend(a)
            space=''
            a=space.join(b)
            msg.Chat.SendMessage(a)
        elif msg.Body == u'殺すぞ' or msg.Body == u'殺す' or msg.Body == u'ぶっ殺す' or msg.Body == u'ころすぞ' or msg.Body == u'ころす':
            msg.Chat.SendMessage(u'通報しています...')
        elif msg.Body == u'まーじゃん':
            msg.Chat.SendMessage(u'http://tenhou.net/0/?6287')
        elif msg.Body == u'ごっどふぃーるど':
            msg.Chat.SendMessage(u'http://www.godfield.net/')
        elif msg.Body == u'検索検索ぅ！':
            msg.Chat.SendMessage(u'http://vcard.ameba.jp/pc/index.html')
        elif msg.Body == u'ありがとうidea' or msg.Body == u'ありがとういであ':
            rander=random.randint(1,5)
            if rander == 1:
                msg.Chat.SendMessage(u'どういたしましてっ')
            if rander == 2:
                msg.Chat.SendMessage(u'どいたま～')
            if rander == 3:
                msg.Chat.SendMessage(u'どういたしまして。')
            if rander == 4:
                msg.Chat.SendMessage(u'いえいえ～')
            if rander == 5:
                msg.Chat.SendMessage(u'またいつでも！')
        elif msg.Body == u'ぬるぽ':
            msg.Chat.SendMessage(u'ｶﾞｯ')
        elif msg.Body == u'おやすみ' or msg.Body == u'おやす' or msg.Body == u'oyasumi':
            rander=random.randint(1,5)
            if rander == 1:
                msg.Chat.SendMessage(u'おやすみ～')
            if rander == 2:
                msg.Chat.SendMessage(u'もう寝るの？')
            if rander == 3:
                msg.Chat.SendMessage(u'また明日ね！')
            if rander == 4:
                msg.Chat.SendMessage(u'oyasumi')
            if rander == 5:
                msg.Chat.SendMessage(u'ん？')
        elif msg.Body == u'おはよう' or msg.Body == u'おは' or msg.Body == u'おはよー' or msg.Body == u'ohayo' or msg.Body == u'oha':
            rander=random.randint(1,5)
            if rander == 1:
                msg.Chat.SendMessage(u'おはよー')
            if rander == 2:
                msg.Chat.SendMessage(u'おはよっ！')
            if rander == 3:
                msg.Chat.SendMessage(u'おはようございまーす')
            if rander == 4:
                msg.Chat.SendMessage(u'おはようございます！')
            if rander == 5:
                msg.Chat.SendMessage(u'おはようございますぅ！')
        elif lister[-6:] == [u'\u3067',u'\u5f62',u'\u614b',u'\u7d20',u'\u89e3',u'\u6790'] and 1==0:#もし　で形態素解析　で終わったら
            word=[x for x in lister[:-6]]
            space=''
            word=space.join(word)
            appid = "なし"  #S
            pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse"

            # 形態素解析
            def morph(sentence, appid=appid, results="ma", filter="1|2|3|4|5|6|7|8|9|10|11|12|13"):
                ret = []
                # 文章
                sentence = urllib.quote_plus(sentence.encode("utf-8"))
                query = "%s?appid=%s&results=%s&filter=%s&sentence=%s" % (pageurl, appid, results, filter, sentence)
                c = urllib2.urlopen(query)
                soup = BeautifulSoup.BeautifulSoup(c.read())
                return [(w.surface.string, w.reading.string, w.pos.string) for w in soup.ma_result.word_list]

            sentence = word
            result = morph(sentence, appid=appid)
            msg.Chat.SendMessage('■形態素■読み■品詞')
            for word in result:
                word=[x for x in word]
                space=" "
                word=space.join(word)
                msg.Chat.SendMessage(word)


        elif lister[-2:] == [u'.',u'.'] and lister[1] == u'tanakatanaka':#もし　..で終わったら
            word=[x for x in lister[:-2]]
            space=''
            word=space.join(word)

            #会話システム

            v=word#入力

            appid = "なし"  #ID
            pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse"

            
            def morph(sentence, appid=appid, results="ma", filter="1|2|3|4|5|6|7|8|9|10|11|12|13"):
                ret = []
                
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

            con = sqlite3.connect("SLEAD.db")
            c = con.execute(u"select * from RES")
            for row in c:#一行づつrowに格納
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
            space=""
            #if max(FList)>=0.6:
            print unicode(FList.index(max(FList)))
            sql=[u"select * from RES limit 1,",unicode(FList.index(max(FList))),u";"]
            sql=space.join(sql)
            c = con.execute(sql)
            for x in range(FList.index(max(FList))-1):
                row = c.fetchone()
            row = c.fetchone()
            msg.Chat.SendMessage(row[1])
            msg.Chat.SendMessage(unicode(max(FList)))

            con.close()



                        
        
def main():
    i=0
    skype = Skype4Py.Skype()
    skype.OnMessageStatus = handler
    skype.Attach()
    while True:
        time.sleep(1) 

if __name__ == "__main__":
    main()

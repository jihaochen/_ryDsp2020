'''
ryLyric.py
'''

LyricToki= [
    'テレサテンさん。 時の流れに身をまかせ ',
    '----                                  ',
    'もしも あなたと　   逢えずに いたら   ',
    'わたしは 何を　     してた でしょうか ',
    '平凡 だけど　       誰かを 愛し       ',
    '普通の 暮らし　     してた でしょうか ',
    '----                                  ',
    '時の 流れに　       身を まかせ       ',
    'あなたの 色に　     染められ          ',
    '一度の 人生   それさえ                ',
    '捨てる ことも かまわない              ',
    'だから お願い　     そばに 置いてね   ',
    'いまは あなたしか　 愛せない          ',
    '----                                  ',
    'もしも あなたに　   嫌われたなら      ',
    '明日という日　      失くして しまうわ ',
    '約束なんか　        いらない けれど   ',
    '想い出 だけじゃ　   生きて ゆけない   ',
    '----                                  ',
    '時の 流れに　       身を まかせ       ',
    'あなたの 胸に　     より添い          ',
    '綺麗に なれた それ だけで　           ',
    'いのち さえも いらないわ              ',
    'だから お願い　     そばに 置いてね   ',
    'いまは あなた しか　見え ないの       ',
    '====                                  ']
   
LyricTokiAppendix=[
    '時の 流れに　       身を まかせ       ',
    'あなたの 色に　     染められ          ',
    '一度の 人生   それさえ                ',
    '捨てる ことも かまわない              ',
    'だから お願い　     そばに 置いてね   ',
    'いまは あなたしか　 愛せない          ',
    '====                                  ',
    '詩：荒木とよひさ                      ',
    '作曲：三木たかし                      ',
    '編曲：川口真                          ',
    '------------                          '
    ]


LrcToki= {
     10: '作詞：荒木とよひさ',
    100: '作曲：三木たかし',
    200: '編曲：川口真',
    283: 'テレサテンさん。 時の流れに身をまかせ ',
    387: '----                                  ',
    408: 'もしも あなたと\u3000   逢えずに いたら   ',
    513: 'わたしは 何を\u3000     してた でしょうか ',
    617: '平凡 だけど\u3000       誰かを 愛し       ',
    724: '普通の 暮らし\u3000     してた でしょうか ',
    829: '----                                  ',
    836: '時の 流れに\u3000       身を まかせ       ',
    953: 'あなたの 色に\u3000     染められ          ',
    1057: '一度の 人生   それさえ                ',
    1162: '捨てる ことも かまわない              ',
    1260: 'だから お願い\u3000     そばに 置いてね   ',
    1385: 'いまは あなたしか\u3000 愛せない          ',
    1500: '----                                  ',
    1510: 'もしも あなたに\u3000   嫌われたなら      ',
    1616: '明日という日\u3000      失くして しまうわ ',
    1723: '約束なんか\u3000        いらない けれど   ',
    1831: '想い出 だけじゃ\u3000   生きて ゆけない   ',
    1937: '----                                  ',
    1944: '時の 流れに\u3000       身を まかせ       ',
    2061: 'あなたの 胸に\u3000     より添い          ',
    2164: '綺麗に なれた それ だけで\u3000           ',
    2267: 'いのち さえも いらないわ              ',
    2364: 'だから お願い\u3000     そばに 置いてね   ',
    2486: 'いまは あなた しか\u3000見え ないの       ',
    2676: '====                                  '}
    
TimeTextGeau= '''
[00:01.85]家後
[00:05.60]作詞：鄭進一/陳維祥 作曲：鄭進一
[00:21.58]有一日咱若老　找無人甲咱友孝
[00:31.21]我會陪你　坐惦椅寮
[00:36.33]聽你講少年的時陣　你有外摮
[00:41.50]吃好吃醜無計較　怨天怨地嘛袂曉
[00:51.48]你的手　我會甲你牽條條
[00:56.03]因為我是你的家後
[01:04.34]阮將青春嫁置恁兜　阮對少年跟你跟甲老
[01:13.84]人情世事已經看透透　有啥人比你卡重要
[01:24.65]阮的一生獻乎恁兜　才知幸福是吵吵鬧鬧
[01:34.19]等待返去的時陣若到　我會讓你先走
[01:44.74]因為我會嘸甘　放你為我目屎流
[02:00.25]
[02:16.08]有一日咱若老　有媳婦子兒友孝
[02:26.05]你若無聊　拿咱的相片
[02:30.99]看卡早結婚的時陣　你外緣投
[02:36.20]穿好穿醜無計較　怪東怪西嘛袂曉
[02:46.38]你的心我會永遠記條條　因為我是你的家後
[02:59.11]阮將青春嫁置恁兜　阮對少年就跟你跟甲老
[03:08.66]人情世事嘛已經看透透　有啥人比你卡重要
[03:19.49]阮的一生獻乎恁兜　才知幸福是吵吵鬧鬧
[03:29.47]等待返去的時陣若到　我著讓你先走
[03:39.24]因為我會嘸甘　放你為我目屎流
[03:50.47]
'''

LrcGeau= {
      28: '作詞：鄭進一/陳維祥 作曲：鄭進一',
     100: '江蕙，家後。',
     337: '有一日咱若老\u3000找無人甲咱友孝',
     487: '我會陪你\u3000坐惦椅寮',
     567: '聽你講少年的時陣\u3000你有外摮',
     648: '吃好吃醜無計較\u3000怨天怨地嘛袂曉',
     804: '你的手\u3000我會甲你牽條條',
     875: '因為我是你的家後',
    1005: '阮將青春嫁置恁兜\u3000阮對少年跟你跟甲老',
    1153: '人情世事已經看透透\u3000有啥人比你卡重要',
    1322: '阮的一生獻乎恁兜\u3000才知幸福是吵吵鬧鬧',
    1471: '等待返去的時陣若到\u3000我會讓你先走',
    1636: '因為我會嘸甘\u3000放你為我目屎流',
    1878: '',
    2126: '有一日咱若老\u3000有媳婦子兒友孝',
    2282: '你若無聊\u3000拿咱的相片',
    2359: '看卡早結婚的時陣\u3000你外緣投',
    2440: '穿好穿醜無計較\u3000怪東怪西嘛袂曉',
    2599: '你的心我會永遠記條條\u3000因為我是你的家後',
    2798: '阮將青春嫁置恁兜\u3000阮對少年就跟你跟甲老',
    2947: '人情世事嘛已經看透透\u3000有啥人比你卡重要',
    3117: '阮的一生獻乎恁兜\u3000才知幸福是吵吵鬧鬧',
    3272: '等待返去的時陣若到\u3000我著讓你先走',
    3425: '因為我會嘸甘\u3000放你為我目屎流',
    3601: ''}
    
'''    
>>> 麥.音檔名
'rySongs/ry_GangHui16K03C_JC18_2001_江蕙_家後_官方MV.wav'
'''

LrcDic= {
    'rySongs/ry_GangHui16K03C_JC18_2001_江蕙_家後_官方MV.wav':LrcGeau,
    'rySongs/ryTokiDo16K03C.wav':LrcToki
    }


TranslateGeau= '''
有一日咱若老　找無人甲咱友孝。      
我會陪你　坐惦椅寮。                  
聽你講少年的時陣　你有外摮。        
吃好吃醜無計較　怨天怨地嘛袂曉。      
你的手　我會甲你牽條條。              
因為我是你的家後。                    

有一天，如果我們變老了，找不到人來孝順我們。
我會陪你，坐在長椅子上。
聽你講說年輕的時候，你有多麼厲害。
我不計較生活過得如何，也不會埋怨天地。
你的手，我會緊緊握著。
因為我是你的妻子。

One day, if we get older, we can not find people to filial piety.
I will accompany you, sitting on the bench.
Hear you speak when you're young, how powerful you are.
I do not care about whether to live well, do not blame the world.
Your hands, I will hold tightly.
Because I am your wife.

ある日、私たちは年を取る場合、私たちは親孝行に人を見つけることができません。
私はベンチに座って、あなたを同行します。
あなたはどのように強力な、あなたは若いしているとき、あなたが話す聞きます。
私は世界を責めないで、よく生きるべきかどうかを気にしないでください。
あなたの手は、私はしっかりと保持します。
私はあなたの妻だから。
'''




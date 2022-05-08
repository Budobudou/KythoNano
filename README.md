# KythoNano
KythonaClient 2.1をベースとしたKythonaのPythonモジュール  
## KythonaClientはこちら
https://github.com/Budobudou/Kythonaclient
## 必要パッケージ
requests
## 使用例
```py
import kythonano
kid = "KanaAPIのID"
kpass = "パスワード"
kdict = "none"
a = kythonano.send("こんにちは",kid,kpass,kdict)
print(a["reaction"])
```  
> こんにちは。 どうぞよろしくお願いします  
## kythonano.send関数の使い方
```py
kythonano.send(送るメッセージ,KanaAPIのID,パスワード,辞書のURL(noneでもOK))
```
## 帰ってくる辞書型変数について
kythonano.send関数でKanaAPIに指定された情報が送信され、このような辞書で帰ってきます。  
> こんにちは  
{'reaction': 'こんにちは。 どうぞよろしくお願いします', 'times': 'none', 'timee': 'none', 'time': 'none'}  
> 10秒タイマーをセットして  
{'reaction': '申し訳ありません\nこの端末はタイマーに対応していません', 'times': '10秒のタイマーを開始しました', 'timee': '10秒のタイマーが終わりました', 'time': 10}  
  
reaction: KanaAPIからの応答メッセージです。  
times: タイマーの開始メッセージです。  
timee: タイマーの終了メッセージです。  
time: タイマーの秒数です。  

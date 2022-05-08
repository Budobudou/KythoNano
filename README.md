# KythoNano
KythonaClient 2.1をベースとしたKythonaのPythonモジュール  
## KythonaClientはこちら
https://github.com/Budobudou/Kythonaclient    
## 使用例
```py
import kythonano
kid = "KanaAPIのID"
kpass = "パスワード"
kdict = "none"
a = kythonano.send("こんにちは",kid,kpass,kdict)
print(a)
```  
kythonano.send関数でKanaAPIに指定された情報が送信され、このような辞書で帰ってきます。  

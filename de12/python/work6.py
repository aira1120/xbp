<!DOCTYPE html>
<html lang="jp">
<head>
    <title>XBPのページ</title>
    <link rel="stylesheet" href="./css/style.css">
</head>
<body>
    <h1>ゲーム作成</h1>
<div>
    <h2>詳細</h2>
    グループでは、確率の原理を使ったゲームを作ることにしました。<br>
    実行ボタンを押すと、「あたり」「はずれ」のどちらかの結果が表示される仕組みです。<br>
    また、よりゲーム性を持たせるため、当選内容や当選確率の変更が容易にできると良いのではないかと考えました。
</div>
<div>
    <h2>ソースコード</h2>
    <pre><code>
    import random
    number = random.randint(1,99) #1~99のランダムな整数。
if number == 1:         
    print("121　はずれ")
elif number == 3:     
    print("212　はずれ")
elif number == 5:      
    print("343　はずれ") 
elif number == 8:     
    print("454　はずれ") 
elif number == 12:       
    print("565　はずれ") 
elif number == 22:       
    print("656　はずれ") 
elif number == 77:       
    print("777　当たり") 
elif number == 55:       
    print("898　はずれ") 
elif number == 15:       
    print("989　はずれ") 
elif number == 99:       
    print("565　はずれ") 
elif number == 76:       
    print("787　はずれ") 
elif number == 88:       
    print("676　はずれ")...
# 導入方法

(Yeah, there's no English version of this file. If you can read this sentence, you don't need to read this file.  
Because this is a install instruction for Japanese players!)

ここでは、Bingle Bingleにこの日本語化パッチを当てる方法を解説します。  
後ほどわかりやすい…かどうか微妙な解説動画も作成します。お楽しみに。

## 1. 7-Zipのダウンロード
[公式サイト](https://7-zip.opensource.jp/)にアクセスし、7-Zipをダウンロード・インストールします。

## 2. パッチのダウンロード
[最新リリース](https://github.com/ShieruCHR/bingle-bingle-jp-patch/releases/latest)の「Assets」内にある  
「release.zip」をダウンロードします。

ダウンロードしたら展開してください。

## 3. パッチを適用
SteamからBingle Bingleのローカルファイルを開き、`/app/desktop-1.0.jar`を7-Zipで開きます。  
`source`フォルダ内にある`GameText_ENG.json`を手順2でダウンロードした`GameText_ENG.json`で**上書き**します。  

一段階階層を戻り、`graphic/font`を開きます。  
パッチ内にある**全ての`.fnt`ファイルと`.png`ファイル**をD&Dし、**上書き**します。

## 4. 確認
Bingle Bingleを起動し、以下のようにタイトル画面が日本語化されていたら完了です。  
![image](https://github.com/ShieruCHR/bingle-bingle-jp-patch/assets/81741561/30ce2021-92ba-4e83-b5ac-b8f362dcbc27)

もし何も文字が表示されていなければ、フォントの差し替えがうまくいっていない可能性があります。  
手順3をよく見て、もう一度やり直してください。

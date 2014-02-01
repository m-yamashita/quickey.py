quickey.py
==========

# Mouse click? Alt + Tab? No, Quickey!!
Linux上で予め設定しておいたウィンドウを、キーボードショートカット一発でアクティブ化する為のPythonスクリプトです。
アクティブ化する対象となるウィンドウが起動していない場合は、指定したコマンドを実行(例えばそのウィンドウを新たに起動したりも)できます。
任意のショートカットキーによる高速なタスク切り替え機能にランチャーがくっついたようなもんだと思ってください。

キーのバインド、及び対象ウィンドウ、コマンドの設定は、
Autokey( https://code.google.com/p/autokey/ )を利用して行います。
WinでいうところのAutoHotKeyのようなものです。

キーバインドはGUIベースで簡単に行えます。
対象ウィンドウの指定及びコマンドの設定は、
インストール時にAutokeyに登録されるサンプルスクリプトをコピーして設定値を2行書き換えるだけの簡単仕様です。
同じようにコピーしてわずかな修正を加えるだけで、あらゆるウィンドウに対応できると思います。
また、ウィンドウの指定部分では正規表現が利用できます。

# Install(Autokeyを利用する場合)

## 事前準備

本スクリプトの動作には、Python, Autokey, wmctrlが必要です。
それぞれ以下のようにインストールしてください(Ubuntu、その他Debian系Distributionについて書いています)。

- Autokey

        $ sudo apt-get install autokey-gtk

- wmctrl

        $ sudo apt-get install autokey-gtk

AutokeyはPythonで動作している為、基本的には自動で入ると思います。

## 本体のインストール

基本的にはinstall.shを叩くだけです。
install.shを実行する事により ~/.config/autokey 配下にquickey.pyがコピーされます。
また、サンプルスクリプトも ~/.config/autokey/data 配下にコピーされるので、
Autokeyの次回起動時に自動で読み込まれるようになっています。

このサンプルスクリプトは、quickey.pyが上記箇所にインストールされていることを前提として動作する為、
個別にカスタマイズしている方等は、quickey.pyをAutokeyの設定通りの場所にコピーし、
各サンプル及び作成済みのスクリプトの最終行で実行している quickey.py のパスを変更してください。

## 実はコマンドラインでも動きます(Autokeyを利用しない場合。インストール不要)

実は本スクリプトの内部ではAutokeyの組み込み関数を一切使用せずに作成している為、
Pythonから直接叩く事で、Autokeyを利用せずとも動作させることが可能です。
お使いのDesktop環境に応じて、キーボードショートカットとしてコマンドを登録させればすぐに使うことができます。
コマンドラインにてご利用の際には、以下のようなコマンドで実行してください。

    $ python path/to/dir/quickey.py/quickey.py "Your regexp of window title" "Your command"

以下はGoogle Chromeのウィンドウをアクティブ化、存在しなければGoogle Chromeを起動するコマンドの例です。

    $ python path/to/dir/quickey.py/quickey.py " - Google Chrome$" "google-chrome"

# 最後に

バグ、要望、その他ご意見等御座いましたら下記よりお問い合わせください。

- Blog: http://m-yamashita.github.io/
- Mail: mxyamashita at gmail.com

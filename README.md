# 4grade-zennki
## 概要
サーバに対する監視を行うソフトウェアである．独自のフォーマットである.mtrファイルを使用して監視の設定を行う．
## 環境
環境は以下を想定している．
- Ubuntu 20.04.5 LTS
- Python 3.8.10

### 設定ファイル
.mtrファイルを用いて監視を行う．今回の場合ではtest.mtrファイルを使用

監視対象，監視条件，配置方法を記載する．


### 実行ファイル
config_and_run.pyを起動して監視を実行していく．

このプログラムファイル実行するとtest.mtrファイルで設定した項目をもとに監視を行う．

### 使い方例

必要なpackageのインストール
```
$ sudo apt install python3-pip
$ pip3 install --upgrade kubernetes
```

test.mtrの設定


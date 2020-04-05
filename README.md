# moja-radio

定義したルールに応じて radiko の番組を録音して GooglePlayMusic にアップロードするやつ

## 準備

### rules.json の定義

`$ cp rules.sample.json rules.json` して `rules.json` を編集

### oauth_credentials の生成

gmusicapi に必要

`$ docker-compose run -v $(pwd):/usr/src/app app python`

```
>>> from gmusicapi import Musicmanager
>>> mm = Musicmanager()
>>> mm.perform_oauth('./oauth_credentials')
# oauth authentication
>>> exit()
```

## usage

`$ docker-compose up` で `rules.json` に定義されたうち前日に放送されたラジオをタイムフリーから録音し、ID3 タグを付けた上で GooglePlayMusic へアップロードする。

- 00:00 に実行してしまうと 24:00 終了のラジオがうまく録音できないので、crontab などへ記述する際は少し遅らせる

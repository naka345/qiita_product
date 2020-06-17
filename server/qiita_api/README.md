# qiitaの記事をgitで管理する

macにuwsgiをhttps通信可能状態でインストールしたい場合
```
CFLAGS="-I/usr/local/opt/openssl/include" LDFLAGS="-L/usr/local/opt/openssl/lib" UWSGI_PROFILE_OVERRIDE=ssl=true pip install uwsgi -Iv
```
pipy経由だと`--https`コマンドが使えないため、`-I`オプションをつける

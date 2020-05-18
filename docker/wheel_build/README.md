# [multi stage build でpythonモジュールインストールする]()
上記記事を書いた時に作成したdockerimage

./require/c_require.txtのモジュールを内包したpythonイメージを作成するためのdockerfileが含まれています

## 使い方
筆者の公開リポジトリを使うなら、このREADME.mdがあるディレクトリに移動して
```
docker build -f ./dockerfiles/wheel_install -t wheel_install:latest ./
```

一からビルドしたい場合は

```
docker build -f ./dockerfiles/wheel_build -t wheel_build:latest ./
# ./dockerfiles/wheel_installの一行目のイメージ指定を`wheel_build:latest`に変更
docker build -f ./dockerfiles/wheel_install -t wheel_install:latest ./
```

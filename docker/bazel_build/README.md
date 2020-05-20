# [alpineでbazelをビルドする]()
上記記事での生成物です

## 使い方
このREADMEがある場所に移動してから、コマンドを実行。

```
docker build -f ./dockerfiles/bazel_build -t bazel_build:latest ./
```

バージョン指定をしたい場合は`--build-arg`オプションを追加してください。

```
docker build -f ./dockerfiles/bazel_build -t bazel_build:latest ./ --build-arg bazel_ver=3.0.0
```

## 注意点
軽量化のためこのdockerイメージ単体ではbazelを利用できません。

もし利用できるようにしたい場合は、`openjdk`を追加する必要があります。

```
apk add --virtual .bazel_build --no-cache
```

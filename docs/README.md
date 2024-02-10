# django-restapi-liked-button
django restapiでいいねボタンを実装


# DjangoとAjaxを使った「いいね」ボタンの実装

このレポジトリは、DjangoのAPIとAjax通信を使用して「いいね」ボタンを作成するためのサンプルコードを含んでいます。これにより、ユーザーはページをリロードすることなく、投稿やコメントに「いいね」をつけることができます。

## 必要なもの

- Python
- Django
- JavaScript, jQuery (Ajax)

## 使い方

まずはリポジトリをクローンして下さい。

```bash
git clone https://github.com/yoshiyuki-140/liked-button.git
cd liked-button
```

次に、Python環境をセットアップします。仮想環境の使用を推奨します。

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

マイグレーションを行い、Djangoサーバーを起動します。

```bash
python manage.py migrate
python manage.py runserver
```

サーバが正常に起動したら、ブラウザで`http://localhost:8000`を開き、アプリケーションをテストします。

## プロジェクトの構造

後で書く

## ライセンス

このプロジェクトはMITライセンスのもとで公開されています。

## 参考

- [DjangoのAPIとAjax通信する「いいねボタン」を作成する](https://django.kurodigi.com/ajax-django-api/)
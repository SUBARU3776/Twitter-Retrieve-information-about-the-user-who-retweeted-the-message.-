# Twitter-Retrieve-information-about-the-user-who-retweeted-the-message.

### このスクリプトは、指定したツイートをリツイートしたユーザーの情報を取得し、その情報をCSVファイルに書き出すPythonスクリプトです。
##### 具体的には、以下のような処理を行っています。

- ツイートIDを指定して、リツイートしたユーザーの情報を取得するためのAPIエンドポイントを生成します。
- リツイートしたユーザーの情報を取得するためにエンドポイントURLを使用します。
- 一度に最大200件の情報を取得します。
- レスポンスヘッダーから次のページのトークンを取得し、次のページが存在する場合は再度APIエンドポイントにアクセスします。
- 取得可能な情報が無くなるまで繰り返します。
- 取得した情報をcsvファイルに保存します。<br>
*********************************************************************************************************************************
### This script is a Python script that retrieves information about users who retweeted a given tweet and writes that information to a CSV file.
##### Specifically, the process is as follows
- Generates an API endpoint to retrieve information about a retweeted user by specifying the tweet ID.
- Use endpoint URLs to retrieve information about retweeted users.
- Retrieve up to 200 items of information at a time.
- The next page token is obtained from the response header, and the API endpoint is accessed again if the next page exists.
- Repeat until there is no more information available.
- Saves the acquired information in a csv file.

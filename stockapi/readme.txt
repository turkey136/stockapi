本APIの使い方<BR>
<BR>
GET /api/stocks<BR>
返却例<BR>
  ```<BR>
  [<BR>
    {"code": "A", "name": "Agilent Technologies, Inc.", "industry": "Biotechnology: Laboratory Analytical Instruments", "url": "http://www.nasdaq.com/symbol/a"},<BR>
    ・・・・<BR>
  ]<BR>
  ```<BR>
<BR>
GET /api/stoks/&lt;Symbol&gt;<BR>
リクエスト例（ティッカーシンボル=Aで絞り込み）<BR>
  ```<BR>
  GET /api/stoks/A<BR>
  ```<BR>
返却例<BR>
  ```<BR>
  {"code": "A", "name": "Agilent Technologies, Inc.", "industry": "Biotechnology: Laboratory Analytical Instruments", "url": "http://www.nasdaq.com/symbol/a"}<BR>
  ```<BR>
エラー返却<BR>
  ```<BR>
  {"status": "false", "message": "not found Symbol 1111111111111111"}<BR>
  ```<BR>
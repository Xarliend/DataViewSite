# 說明
- 使用Django以及Django REST framework所撰寫的網頁後端。
- 包含以下幾個部分：
    * DataView: 網頁主體。
    * api：api服務。
    * NewsPage: 瀏覽所抓取的新聞資料。
    * Crawler: 使用Scrapy撰寫之爬蟲程式。

# 使用方式
- Crawler分別有兩隻Spider:
    * TechNews: 用來從(https://technews.tw/category/fintech/)抓取標題中含有「區塊練」關鍵字的新聞。
    * userstates: 用來從[Steam平台的PTT群組](https://steamcommunity.com/groups/pttcc/members/)抓取所有成員的使用者名稱、目前狀態、使用者頁面連結。
- DataView提供REST api服務，以及瀏覽抓取新聞資料的頁面。

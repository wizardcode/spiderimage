# spiderimg
* 一个下载斗鱼主播图片并重命名的Python scrapy小例子。
* 使用ImagesPipeline，重写get_media_requests和item_completed
* 通过拼接url，每次请求20条数据，从API中读取数据。
* 我第一个下载网络图片的爬虫，感谢我上个周末的奋斗。
### 代码运行
```
scrapy crawl imagespider
```
### 爬虫运行完毕后，在spiderimg/spiderimg/spiders/images下看到下载完毕的图片。

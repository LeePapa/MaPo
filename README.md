
#MaPo


接码服务器，采集各个手机验证码短信接码平台的免费号码，自定义插拔 路由和处理器，低耦合的接码服务器~

## 使用

* 依赖: `pip install -r requirements.txt`
* 运行: `python index.py`
* 插拔: 
    > * `custom.py`是自定义采集器文件，根据`crawlers.py`中的`F4Crawler`类格式编写自己的新增采集器
    > * 每个采集器类的属性`urls`即是服务器的路由和处理器映射
 
 
 ## 示例
 
 ### 1.使用内置的接码器获取可用手机号码
 通过`python index.py`运行服务器,而后：
 ```python
import requests
api = 'http://127.0.0.1:8899/F4/phone'
data = requests.get(api)
```
返回数据：
```json
{
  "success": 0,
  "data": [
    {
      "code": "44",
      "url": "https://f4.work/list_free.php?list=PHONELIST_1_1_44",
      "area": "(+44) 英国 United Kingdom ",
      "phones": [
        "07366507512",
        "07853962493",
        "07367417565",
        "07723662724",
        "07838031796"
      ]
    },
    {
      "code": "852",
      "url": "https://f4.work/list_free.php?list=PHONELIST_1_1_852",
      "area": "(+852) 香港 Hong Kong ",
      "phones": [
        "65894142",
        "64860069",
        "69951654",
        "65799786",
        "51359484"
      ]
    },
    {
      "code": "63",
      "url": "https://f4.work/list_free.php?list=PHONELIST_1_1_63",
      "area": "(+63) 菲律宾 Philippines ",
      "phones": [
        "9664706948",
        "9664706966",
        "9664706978",
        "9664706988",
        "9664706994"
      ]
    },
    {
      "code": "853",
      "url": "https://f4.work/list_free.php?list=PHONELIST_1_1_853",
      "area": "(+853) 澳门 Macao ",
      "phones": [
        "63215758",
        "63846752",
        "63215896",
        "63847041",
        "68436533"
      ]
    }
  ]
}
```      

### 2.使用内置服务器查询手机号码 +853 68436533中 “美团网” 相关的长度为4的验证码信息

 通过`python index.py`运行服务器,而后：
 ```python
import requests
api = 'http://127.0.0.1:8899/F4/fetch?pattern=美团网&code=853&phone=68436533&length=4'
data = requests.get(api)
```

返回数据：
```json
{
  "success": 0,
  "data": [
    {
      "text": "【美团网】3831（登录验证码，请完成验证），如非本人操作，请忽略本短信。",
      "time": "2020-06-24 21:44:56",
      "code": [
        "3831"
      ]
    }
  ]
}
```

## 自定义

。。。后续增加或自己插进去

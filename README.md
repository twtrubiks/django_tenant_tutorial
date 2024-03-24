# django tenant use PostgreSQL schemas 教學

本篇教學的目的, 主要是學習 多租戶 tenant 的概念,

這邊使用 [django-tenants](https://github.com/django-tenants/django-tenants) 這個套件來說明.

拿作者的範例來介紹架構 (強烈建議要觀看原作者的說明).

## 多租戶說明

首先, 多租戶技術 (Multi-Tenancy Technology), 他是一種軟體架構,

主要的目的就是實現多個客戶之間的隔離性, 安全性, 獨立性，以及同時降低管理和維護成本.

實作多租戶的方式有很多,

這套件主要是透過 PostgreSQL 中的 schemas 來實現多租戶,

只有一個 db(共享資料庫), 然後一個 schema(獨立 schema) 代表一個租戶 tenant.

## 教學

安裝套件

```cmd
pip install django-tenants
pip install psycopg2-binary # 使用 PostgreSQL
```

接著把 db 執行起來, `docker compose up -d`

然後可以執行 django,

```cmd
python manage.py migrate
```

依照範例總共會有3個網址, 分別為

`trendy-sass.com` 共用

`tenant1.trendy-sass.com` 租戶1

`tenant2.trendy-sass` 租戶2

因為要在本機測試, 所以要設定 host

```cmd
sudo vim /etc/hosts
```

```text
127.0.0.1	trendy-sass.com
127.0.0.1	tenant1.trendy-sass.com
127.0.0.1	tenant2.trendy-sass.com
```

先建立一個主要的 tenant

```cmd
❯ python manage.py create_tenant
schema name: public
name: Trendy SaSS
description: Public Tenant
domain: trendy-sass.com
is primary (leave blank to use 'True'): True
```

建立 tenant 1

```cmd
❯ python manage.py create_tenant
schema name: tenant1
name: Tenant1
description: A one tenant
domain: tenant1.trendy-sass.com
is primary (leave blank to use 'True'): False
```

建立 tenant 2

```cmd
❯ python manage.py create_tenant
schema name: tenant2
name: Tenant2 - Even Awesome-r
description: A second tenant, even more awesome!
domain: tenant2.trendy-sass.com
is primary (leave blank to use 'True'): False
```

執行 server

```cmd
python3 manage.py runserver 8088
```

`trendy-sass.com` 畫面

![](https://i.imgur.com/nEYIaio.png)

`tenant1.trendy-sass.com` 租戶1 畫面

![](https://i.imgur.com/b8ZRbTC.png)

`tenant2.trendy-sass` 租戶2 畫面

![](https://i.imgur.com/FlA9oH5.png)

資料庫也切成了3個 schema 彼此不互相影響, 除了共用的 public,

然後 tenant1 和 tenant2 裡面的 table 都是一樣的.

![](https://i.imgur.com/FJ2c1MA.png)

連 user 權限彼此都是完全切開的,

可以嘗試進去 `sample-random/` 這個 url, 因為他會幫你建立一些 user.

然後你可以嘗試再進去 `admin/` 登入看看.

如果你想要在 public 中建立 super user, 可執行

`python manage.py createsuperuser`

建立 tenant 中的 super user

`python manage.py create_tenant_superuser --username=admin --schema=tenant1`

## 其他 tenant command

官方文件可參考 [tenant_command](https://django-tenants.readthedocs.io/en/latest/use.html#tenant-command)

指定進入特定的 tenant

`python3 manage.py tenant_command shell --schema=tenant1`

進入全部的 tenant (當你退出後會自動進入下一個 shell)

`python3 manage.py all_tenants_command shell`

範例如下, tenant1, tenant2, public

```cmd
❯ python3 manage.py all_tenants_command shell
['manage.py', 'shell']
Applying command to: tenant1
Python 3.9.16 (main, Dec  7 2022, 01:11:58)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
now exiting InteractiveConsole...
Applying command to: tenant2
Python 3.9.16 (main, Dec  7 2022, 01:11:58)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
now exiting InteractiveConsole...
Applying command to: public
Python 3.9.16 (main, Dec  7 2022, 01:11:58)
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
now exiting InteractiveConsole...

```

## 其他範例

作者總共提供三種範例

[django-tenants examples](https://github.com/django-tenants/django-tenants/tree/master/examples)

這篇介紹的是 tenant_tutorial,

還有 tenant_subfolder_tutorial 是類似下的概念

`http://trendy-sass.com:8088/`

`http://trendy-sass.com:8088/clients/tenant2.trendy-sass.com/`

至於最後的 tenant_multi_types 我沒有測試出來.

## Reference

* [Multi-tenancy strategies with Django+PostgreSQL](https://www.youtube.com/watch?v=j-bbaf6hCMo)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

綠界科技ECPAY ( 不需註冊會員 )

![alt tag](https://payment.ecpay.com.tw/Upload/QRCode/201906/QRCode_672351b8-5ab3-42dd-9c7c-c24c3e6a10a0.png)

[贊助者付款](http://bit.ly/2F7Jrha)

歐付寶 ( 需註冊會員 )

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## 贊助名單

[贊助名單](https://github.com/twtrubiks/Thank-you-for-donate)

## License

MIT license
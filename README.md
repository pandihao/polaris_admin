# 基于Django开发的运维后台管理项目

### 项目简介

> 基于Django REST framework 开发的运维管理后台

### 项目源码
|     |   后端源码  |   前端源码  |
|---  |--- | --- |
|  github   |  https://github.com/pandihao/polaris_admin.git   |  https://github.com/pandihao/polaris_admin_vue.git   |


### 安装

**环境安装**

>* python3.8.1 ，建议python3.6.2以上
>* redis 3.2及以上

**项目部署**

> * 下载项目代码

```
git clone  https://github.com/pandihao/polaris_admin.git

```
> * 安装第三方包

```
pip install -r requirements.txt

```


### 模块文档

占位

### 代码结构

```
polaris_admin
├── doc          #文档说明
│   └── start.md
├── __init__.py
├── manage.py    
├── polaris_admin # 后端项目入口
│   ├── apps      # app入口
│   │   ├── information  # 个人信息profile 模块
│   │   ├── __init__.py
│   │   ├── oauth        # 用户认证
│   │   └── system       # 系统管理
│   ├── asgi.py
│   ├── common           # app通用组件
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   └── __pycache__
│   ├── __init__.py
│   ├── media           # 文件上传路径
│   │   └── avatar
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings        #配置文件目录
│   │   ├── dev.py       # dev配置运行入口
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── urls.py
│   ├── utils            # 项目共用模块
│   │   ├── exceptions.py
│   │   ├── __init__.py
│   │   ├── middleware.py
│   │   ├── models.py
│   │   ├── pagination.py
│   │   ├── permissions.py
│   │   ├── __pycache__
│   │   └── views.py
│   └── wsgi.py
├── README.md
└── requirements.txt       # 依赖包

```

### 系统预览

 占位
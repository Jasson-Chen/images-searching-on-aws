# Images 多模态搜索

#### 业务背景

电商场景中，用户希望通过输入图片，用以图搜图/文搜图/图+文搜图的方式可快速在图片库中检索到与输入图片相似的图片集合。可广泛应用于拍照购物、商品推荐、电商选品、产品设计管理等场景。

图片搜素的三个需求：

1. 根据整张图片搜索近似图片列表，并根据相似度排序；
2. 根据局部图片从图片库中搜索包含局部图片的列表，并根据匹配度排序；
3. 根据整张图的局部特征描述搜索近似图片列表，并根据匹配度排序。

传统方案的挑战：

1. 通过图片的关键词做纯文本检索，无法完全捕捉图片细节，通常取决于文本内容。然后大部分图片的描述信息又会有很多重复；
2. 通过小模型的图片特征匹配，维度较少，匹配精度不高；
3. 通过纯图片的向量化召回，无法根据特定的细节进行匹配，如描述一个图片里局部的匹配；

## 架构说明

![1729170034791](image/1729170034791.png)

![1729170049892](image/1729170049892.png)

**组件说明**

Amazon Bedrock: 是Amazon 完全托管的AI服务，通过API的方式提供访问多种FMs 比如Anthropic/AI21 Labs/Cohere/Meta等模型

Amazon Opensearch: 是AWS完全托管的Text Search/Vector 数据库

Amazon S3:  Amazon S3是高可用的，几乎无限扩张的对象存储服务, 这边我们使用它来存储图片

Amazon Lambda: 是Amazon Serverless的计算服务，在这边封装了image search的API如upload image/search image等

## 部署说明

利用 ARM 架构 EC2 （如T4g），Amazon linux 2023 系统部署参考

1. 开启SSH访问安全组
2. 采用Session Manager方式连接到EC2
3. 配置对应Session Manager的IAM Role（在实例描述中可以找到）权限如下图所示
   ![1729170034791](image/iam_config.png)
4. 运行以下命令

    ```
    yum install npm
    npm install -g aws-cdk
    npm install docker 
    service docker start
    ```

    ```
    # 登陆aws public ECR 获取基础镜像（多阶段构建，这边是通过Lambda Web Adapter的镜像层构建Lambda容器）
    aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
    ```

    ```
    # CDK依赖
    npm install

    # CDK在AWS上做环境准备的。引导Stacksets在AWS环境配置S3存储桶和ECR镜像仓库的配置
    cdk bootstrap

    # CDK进行部署
    cdk deploy
    ```

## 测试说明

1. 利用ssh远程连接ec2，并map到本地8888端口，启动Jupyter notebook服务器

2. 上传 .ipynb 文件，根据注释修改对应内容并进行测试即可

### 工程结构说明

```
├── API_Docs.md  //API文档
├── README.md
├── asserts
├── bin
├── cdk.context.json
├── cdk.json
├── image
├── jest.config.js
├── lambda     //业务逻辑
├── lib
├── package.json
└── tsconfig.json
```


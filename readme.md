## 使用方法
### 环境
- 安装 *Python 3+*
- 执行 ``pip install typer``
- 执行 ``pip install rich``

### 自动deploy
 - 执行 ``python auto.py deployall D:\Projects develop``
    - 其中 **D:\Projects** 替换为自己项目所在父目录
    - 其中 **develop** 为自动 *deploy* 的代码分支

### TODO

- 构建一个专属maven镜像，指定公司的settings.xml配置文件
- 接入github actions，监听分支上代码提交，比如``irt-cfg-api``有代码变动提交到develop分支就自动*deploy*该分支对应的cfg-api package
- 多个*deploy*可以同时执行

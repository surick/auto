## 使用方法
### 环境
- 安装 *Python 3+*
- 执行 ``pip install typer``
- 执行 ``pip install rich``

### 自动deploy
 - 执行 ``python auto.py deployall D:\Projects develop``
    - 其中 **D:\Projects** 替换为自己项目所在父目录
    - 其中 **develop** 为自动 *deploy* 的代码分支

### 自动创建QC文件夹
使用 `autoQC.py` 脚本可以自动创建质量放行文件夹并复制必要的文档文件。

#### 功能特点
- 自动创建新的质量放行文件夹
- 从指定的源文件夹复制并更新文档文件名
- 支持自定义源文件夹和目标文件夹日期
- 自动处理文件名中的日期更新

#### 使用方法
1. 自动模式（使用上周五和下周五日期）：
   ```bash
   python autoQC.py
   ```

2. 手动指定日期模式：
   ```bash
   python autoQC.py <源文件夹日期> <目标文件夹日期>
   ```
   例如：从0124文件夹复制文件到0207文件夹
   ```bash
   python autoQC.py 0124 0207
   ```

#### 注意事项
- 日期格式必须为MMDD（例如：0207）
- 源文件夹必须存在且包含所需的文档文件
- 如果目标文件夹已存在，脚本会提示但不会覆盖现有文件
- 确保复制文件时没有其他程序正在使用这些文件

#### 复制的文件
脚本会自动复制并更新以下文件的文件名：
1. TAPD需求追溯矩阵 TAPD Requirements Traceability Matrix.docx
2. 迭代发布质量放行报告 Iteration Release Quality Release Report.docx
3. 需求发布生产上线前检查清单 Requirement Release Production Pre-launch Checklist.xlsx

### TODO

- 构建一个专属maven镜像，指定公司的settings.xml配置文件
- 接入github actions，监听分支上代码提交，比如``irt-cfg-api``有代码变动提交到develop分支就自动*deploy*该分支对应的cfg-api package
- 多个*deploy*可以同时执行

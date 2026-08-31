# funplay

一次性的比赛代码存档，**不是通用工具/库，目前已废弃、未维护**。

仓库里保存的是作者参加阿里云天池比赛（比赛编号 `531803`）时提交的方案雏形：`funplay/tianchi/531803/core.py` 定义了一个下载训练/测试数据集的 `Task`，实际下载调用被注释掉，`step2` 是空方法，没有完成的比赛逻辑。

> 命名说明：PyPI 上查不到 `funplay` 已发布的版本（返回 `Not Found`），尽管 `script/build.sh` 里写了 `twine upload` 发布步骤。**不建议 `pip install`**：`pyproject.toml` 依赖的 `notedrive` 传递依赖了 `demjson==2.2.4`，这个版本的 `demjson` 在现代 Python/setuptools 环境下构建会直接失败（`use_2to3` 参数已被移除），导致 `pip install` 无法完成。

## 使用

没有命令行入口，也没有可直接调用的公共函数。如果要看当年的方案雏形，直接阅读 `funplay/tianchi/531803/core.py` 即可。

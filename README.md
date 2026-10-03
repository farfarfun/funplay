# funplay

一次性的比赛代码存档，**不是通用工具/库，目前已废弃、未维护**。

仓库里保存的是作者参加阿里云天池比赛（比赛编号 `531803`）时提交的方案雏形：`src/funplay/tianchi/531803/core.py` 定义了一个下载训练/测试数据集的 `Task`，实际下载调用被注释掉，`step2` 是空方法，没有完成的比赛逻辑。项目采用标准 `src/` 布局。

> 命名说明：PyPI 上查不到 `funplay` 已发布的版本（返回 `Not Found`），本仓库不再发布新版本，也不依赖已失效的下载库。

## 使用

可以读取当年的数据集地址，但不会自动下载：

```python
from importlib import import_module

Task = import_module("funplay.tianchi.531803.core").Task
train_url, test_url = Task().step1()
print(train_url, test_url)
```

使用 [uv](https://docs.astral.sh/uv/) 安装依赖并运行：

```bash
uv sync
uv run python -c "
from importlib import import_module
Task = import_module('funplay.tianchi.531803.core').Task
print(Task().step1())
"
```

也可以直接把源码包安装到当前环境：

```bash
uv pip install .
```

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 组织主页：<https://github.com/farfarfun>
- PyPI：<https://pypi.org/user/niuliangtao/>
- 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。

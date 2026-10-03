# 说明：fundrive 没有 PyCurlDownLoad 的等价实现（fundrive.core.base 只有
# DriveFile/BaseDrive 这类网盘驱动抽象，不是通用 URL 下载器）。下方的下载调用
# 在迁移前就已被注释掉，因此这里直接去掉通用下载器导入，而不是伪造一个假迁移。
# 背景见 farfarfun/todo-list#369。


class Task:
    """天池 531803 比赛数据集任务的存档接口。"""

    def __init__(self, path_root: str = "") -> None:
        """创建任务。

        :param path_root: 数据文件保存目录，仅保留供历史方案使用。
        """
        self.path_root = path_root

    def step1(self) -> tuple[str, str]:
        """返回训练集和测试集下载地址，不执行网络下载。"""
        return (
            "http://tianchi-competition.oss-cn-hangzhou.aliyuncs.com/531803/trainset.zip",
            "https://tianchi-competition.oss-cn-hangzhou.aliyuncs.com/531803/test_input.zip",
        )

    def step2(self) -> None:
        """保留历史流程中的第二步，目前没有实现。"""

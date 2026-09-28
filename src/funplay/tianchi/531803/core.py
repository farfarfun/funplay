# NOTE: fundrive has no PyCurlDownLoad equivalent (fundrive.core.base only has
# DriveFile/BaseDrive). The download calls below were already commented out
# pre-migration, so the generic downloader import is dropped rather than faked.
# See farfarfun/todo-list#369.


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

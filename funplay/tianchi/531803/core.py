# NOTE: fundrive has no PyCurlDownLoad equivalent (fundrive.core.base only has
# DriveFile/BaseDrive). The download calls below were already commented out
# pre-migration, so the generic downloader import is dropped rather than faked.
# See farfarfun/todo-list#369.


class Task:
    def __init__(self):
        self.path_root = ""

    def step1(self):
        # trainset.zip,7.34GB,
        url1 = 'http://tianchi-competition.oss-cn-hangzhou.aliyuncs.com/531803/trainset.zip'

        # test_input.zip,510.58MB,
        url2 = 'https://tianchi-competition.oss-cn-hangzhou.aliyuncs.com/531803/test_input.zip'
        # dowmer.download(url1, self.path_root + 'trainset.zip')
        # dowmer.download(url1, self.path_root + 'test_input.zip')

    def step2(self):
        pass

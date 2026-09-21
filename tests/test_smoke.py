from importlib import import_module

import funplay
import funplay.tianchi

Task = import_module("funplay.tianchi.531803.core").Task


def test_import_funplay():
    assert funplay is not None


def test_import_funplay_tianchi():
    assert funplay.tianchi is not None


def test_task_step1_returns_dataset_urls():
    """Task 应返回两个数据集地址而不依赖外部下载库。"""
    task = Task("/tmp/data/")
    assert task.path_root == "/tmp/data/"
    train_url, test_url = task.step1()
    assert train_url.endswith("trainset.zip")
    assert test_url.endswith("test_input.zip")


def test_task_step2_is_explicit_noop():
    """未实现的历史步骤应明确返回 None。"""
    assert Task().step2() is None

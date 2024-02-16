import shutil

import pytest


@pytest.fixture(scope="session")
def dataset_dir(tmp_path_factory):
    test_dir = tmp_path_factory.mktemp("dataset")
    apple = test_dir / "apple"
    apple.mkdir()
    banana = test_dir / "banana"
    banana.mkdir()
    (apple / "1.jpg").touch()
    (apple / "2.jpg").touch()
    yield test_dir
    shutil.rmtree(test_dir)

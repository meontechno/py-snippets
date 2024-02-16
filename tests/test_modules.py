import shutil
import time

import pytest
import structlog

from src.files import list_all_files

logger = structlog.get_logger()


# @pytest.fixture(scope="session")
# def dataset_dir(tmp_path_factory):
#     test_dir = tmp_path_factory.mktemp("dataset")
#     apple = test_dir / "apple"
#     apple.mkdir()
#     banana = test_dir / "banana"
#     banana.mkdir()
#     (apple / "1.jpg").touch()
#     (apple / "2.jpg").touch()
#     yield test_dir
#     shutil.rmtree(test_dir)


def test_if_dir_exists(dataset_dir):
    assert dataset_dir.exists()


def test_list_all_images_empty(dataset_dir):
    image_files = list_all_files(dataset_dir, [])
    assert len(image_files) == 0


def test_list_all_images(dataset_dir):
    image_files = list_all_files(dataset_dir, ['*.jpg', '*.jpeg', '*.png', '*.gif'])
    assert len(image_files) == 2


def test_jpeg_images(dataset_dir):
    image_files = list_all_files(dataset_dir, ['*.jpg', '*.jpeg'])
    assert len(image_files) == 2


def test_all_images_invalid_path_type():
    directory = "../../digit7/dataset/classification_test"
    with pytest.raises(TypeError):
        image_files = list_all_files(directory, ['*.jpg', '*.jpeg'])
        assert len(image_files) == 7


# Setup and teardown alternative
# TEST_DIR = Path("images")
# TEST_DIR.mkdir(exist_ok=True)
# (TEST_DIR / "class1").mkdir(exist_ok=True)
# (TEST_DIR / "class2").mkdir(exist_ok=True)
# (TEST_DIR / "class1" / "class11.jpg").touch()
# (TEST_DIR / "class1" / "class12.png").touch()
# (TEST_DIR / "class1" / "class13.jpg").touch()
# (TEST_DIR / "class2" / "class21.jpeg").touch()
# (TEST_DIR / "class2" / "class22.gif").touch()


# def teardown():
#     for f in TEST_DIR.rglob("*.*"):
#         f.unlink()
#
#     for d in TEST_DIR.iterdir():
#         d.rmdir()
#
#     TEST_DIR.rmdir()

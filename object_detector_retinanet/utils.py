import logging
import os
import sys

__author__ = 'roeiherz'

FILE_EXISTS_ERROR = (17, 'File exists')

IMG_FOLDER = 'annotations'
ANNOTATION_FOLDER = 'annotations'
DEBUG_MODE = False #'ubuntu' not in os.environ['HOME']
if DEBUG_MODE:
    IMG_FOLDER += '_debug'
    ANNOTATION_FOLDER += '_debug'


def create_folder(path):
    """
    Checks if the path exists, if not creates it.
    :param path: A valid path that might not exist
    :return: An indication if the folder was created
    """
    folder_missing = not os.path.exists(path)

    if folder_missing:
        # Using makedirs since the path hierarchy might not fully exist.
        try:
            os.makedirs(path)
        except OSError as e:
            if (e.errno, e.strerror) == FILE_EXISTS_ERROR:
                print(e)
            else:
                raise

        print('Created folder {0}'.format(path))

    return folder_missing


def root_dir():
    return os.path.join('/content/drive/My Drive/SKU110K_code', 'Documents', 'SKU110K')


def image_path():
    return os.path.join(root_dir(), IMG_FOLDER)


def annotation_path():
    return os.path.join(root_dir(), ANNOTATION_FOLDER)

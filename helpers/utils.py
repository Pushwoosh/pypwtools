import sys

import requests

PROGRESS_BAR_WIDTH = 50  # in characters


def download_file(src: str, dst: str):
    """ Saves url to a file. Also draws cute progress bar.
    :param src: source url, for example: http://google.com/file.zip
    :param dst: destination file example: file.zip
    """
    resp = requests.get(src, stream=True)
    total_length = resp.headers.get('content-length')

    with open(dst, "wb") as output:
        if total_length is None:
            output.write(resp.content)
        else:
            downloaded_bytes = 0
            total_length = int(total_length)
            for data in resp.iter_content(chunk_size=4096):
                downloaded_bytes += len(data)
                output.write(data)
                draw_progress(total_length, downloaded_bytes)
        print("")


def draw_progress(total: int, completed: int):
    ratio = completed / total
    done = int(PROGRESS_BAR_WIDTH * ratio)
    remained = int(PROGRESS_BAR_WIDTH - done)
    sys.stdout.write("\r[%s%s] %.2f%%  " % ('=' * done, ' ' * remained, ratio * 100))
    sys.stdout.flush()

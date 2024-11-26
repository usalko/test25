# basic1/test064.py


from datetime import datetime
from pathlib import Path
from typing import Tuple


def test064(filename: str) -> Tuple[datetime, datetime]:
    '''
    Retrieves the date and time of file creation and modification
    returns Tuple[datetime, datetime] (creation and modification datetime)
    '''
    file_statistics = Path(filename).lstat()
    return datetime.fromtimestamp(file_statistics.st_ctime), datetime.fromtimestamp(file_statistics.st_mtime)
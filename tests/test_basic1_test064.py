from datetime import date, datetime, timedelta
from math import floor
from os import remove
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Tuple
from unittest import TestCase

from basic1 import test064


class TestsBasic1Test064(TestCase):
    '''
    Write a Python program that retrieves the date and time of file creation and modification.
    '''

    @staticmethod
    def time_diff(dt: datetime) -> timedelta:
        dt_time = dt.time()
        return timedelta(
            hours=dt_time.hour,
            minutes=dt_time.minute,
            seconds=dt_time.second,
            microseconds=dt_time.microsecond
        )

    @classmethod
    def create_tmp_file(cls, name: str, ext: str) -> Tuple[str, date, timedelta]:
        file_name = ''
        with NamedTemporaryFile(prefix=name, suffix=ext, delete_on_close=False) as writer:
            writer.write(b' ')
            file_name = writer.name
        creation_datetime = datetime.now()
        return str(Path(file_name).absolute().resolve()), creation_datetime.date(), cls.time_diff(creation_datetime)

    @classmethod
    def modify_file(cls, filename: str, text: str) -> Tuple[str, date, timedelta]:
        with open(filename, 'wb') as writer:
            writer.write(bytes(text, 'utf-8'))
        modification_datetime = datetime.now()
        return modification_datetime.date(), cls.time_diff(modification_datetime)
    
    @staticmethod
    def seconds(creation_ord_modification_timedelta: timedelta)-> float:
        floor(creation_ord_modification_timedelta.total_seconds())

    def test_case1(self):
        filename, test_creation_date, test_creation_time = self.create_tmp_file('test', 'txt')
        try:
            test_modification_date, test_modification_time = self.modify_file(filename, 'A')
            
            creation_datetime, modification_datetime = test064(filename)
            self.assertEqual(
                creation_datetime.date(),
                test_creation_date,
            )
            self.assertEqual(
                self.seconds(self.time_diff(creation_datetime)),
                self.seconds(test_creation_time),
            )
            self.assertEqual(
                modification_datetime.date(),
                test_modification_date,
            )
            self.assertEqual(
                self.seconds(self.time_diff(modification_datetime)),
                self.seconds(test_modification_time),
            )
        finally:
            remove(filename)

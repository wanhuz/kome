

import unittest
from module.ffs_api import FFS_API
import os

class FFS_APITest(unittest.TestCase):

    def test_generate_output_filename(self):
        input_sub = '[FFF] Love Live! - 11 [BD][720p-AAC][A5C92D49].srt'
        valid_ffs_sub = '[FFF] Love Live! - 11 [BD][720p-AAC][A5C92D49].ffs.srt'

        self.assertEqual(FFS_API.generate_output_filename(input_sub), valid_ffs_sub)
# ===============================================================================
# Copyright 2017 dgketchum
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

import unittest
from datetime import datetime

from metio.misc import BBox
from metio.thredds import GridMet


class TestGridMet(unittest.TestCase):
    def setUp(self):
        self.bbox = BBox(west_lon=-116.4, east_lon=-103.0,
                         south_lat=44.3, north_lat=49.1)

        self.vars = ['pr', 'pet', 'not_a_var']

        self.start = datetime(2011, 5, 1)
        self.end = datetime(2011, 7, 31)

    def test_instantiate(self):
        gridmet = GridMet(self.vars, start=self.start, end=self.end,
                          bbox=self.bbox)
        self.assertIsInstance(gridmet, GridMet)


if __name__ == '__main__':
    unittest.main()

# ===============================================================================

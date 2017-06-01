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

import os
import unittest
import rasterio

from pprint import pprint

from sat_image.image import Landsat5, Landsat8
from sat_image.fmask import Fmask
from ssebop.utils.ras_point_index import raster_point_row_col


#
# class FmaskTestCaseL5(unittest.TestCase):
#     def setUp(self):
#         self.dirname_cloud = 'tests/data/lt5_cloud'
#         self.image = Landsat5(self.dirname_cloud)
#         point_extract = 'tests/data/point_data/butte_lt5_extract.shp'
#         self.point_data = raster_point_row_col(self.image, point_extract)
#         # pprint(self.point_data)
#
#     def tearDown(self):
#         pass
#
#     def test_instantiate_fmask(self):
#         self.assertIsInstance(self.image, Landsat5)
#
#     def test_get_potential_cloud_layer(self):
#         f = Fmask(self.image)
#         self.assertIsInstance(f, Fmask)
#         cloud, shadow = f.cloud_mask()
#         home = os.path.expanduser('~')
#         outdir = os.path.join(home, 'images', 'sandbox')
#         f.save_array(cloud, os.path.join(outdir, 'cloud_mask.tif'))
#         f.save_array(shadow, os.path.join(outdir, 'shadow_mask.tif'))


class FmaskTestCaseL8(unittest.TestCase):
    def setUp(self):
        self.dirname_cloud = 'tests/data/lc8_cloud'
        self.image = Landsat8(self.dirname_cloud)
        # point_extract = 'tests/data/point_data/butte_lt5_extract.shp'
        # self.point_data = raster_point_row_col(self.image, point_extract)
        # # pprint(self.point_data)

    def tearDown(self):
        pass

    def test_instantiate_fmask(self):
        self.assertIsInstance(self.image, Landsat8)

    def test_get_potential_cloud_layer(self):
        f = Fmask(self.image)
        self.assertIsInstance(f, Fmask)
        cloud, shadow = f.cloud_mask()


if __name__ == '__main__':
    unittest.main()

# ===============================================================================

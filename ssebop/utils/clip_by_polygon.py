# =============================================================================================
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
# =============================================================================================

import os
import rasterio
import fiona
import rasterio.tools.mask


def clip_w_poly(rasters, polygon, out):
    files = os.listdir(rasters)
    tifs = [x for x in files if x.endswith('.TIF') or x.endswith('.tif')]
    with fiona.open(polygon, 'r') as shapefile:
        features = [feature['geometry'] for feature in shapefile]

    for tif in tifs:
        with rasterio.open(os.path.join(rasters, tif)) as src:
            out_image, out_transform = rasterio.tools.mask.mask(src, features, crop=True)
            out_meta = src.meta.copy()

            out_meta.update({'driver': 'GTiff', 'height': out_image.shape[1],
                             'width': out_image.shape[2], 'transform': out_transform})

            new_tif_name = os.path.join(out, tif)
            # print(new_tif_name)
            with rasterio.open(new_tif_name, 'w', **out_meta) as dst:
                dst.write(out_image)


if __name__ == '__main__':
    home = os.path.expanduser('~')
    raster_dir = os.path.join(home, 'images', 'LT5', 'cloudtest', 'fmask_prods')
    test_data = os.path.join(home, 'images', 'test_data', 'cloudtest')
    out_dir = os.path.join(test_data, 'LT5_cloud_test')
    shape = os.path.join(test_data, 'clip_shapes', 'test_cloud_butte.shp')
    clip_w_poly(raster_dir, shape, out_dir)

# LT05_L1TP_040028_20060706_20160909_01_T1_B7.TIF
# LE07_L1TP_039028_20100702_20160915_01_T1_B8

# ========================= EOF ====================================================================

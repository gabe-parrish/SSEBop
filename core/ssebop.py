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

from __future__ import print_function

import numpy as np

from app.paths import paths, PathsNotSetExecption
from sat_image.image import Landsat5, Landsat7, Landsat8


class SSEBopModel(object):
    _date_range = None
    _k_factor = None
    _satellite = None

    _is_configured = False

    def __init__(self, cfg):

        if not paths.is_set():
            raise PathsNotSetExecption

        self._cfg = cfg

        paths.set_polygons_path(cfg.polygons)
        paths.set_mask_path(cfg.mask)
        paths.set_image_path(cfg.image_directory)

        if cfg.verify_paths:
            paths.verify()

        self._info('Constructing/Initializing SSEBop...')
        # self._constants = set_constants()

    def configure_run(self, runspec):

        self._info('Configuring SSEBop run')

        self._date_range = runspec.date_range
        self._k_factor = runspec.k_factor
        self._satellite = runspec.satellite

        print('Instantiating image...')
        if self._satellite == 'LT5':
            self.img = Landsat5(paths.image)
        elif self._satellite == 'LE7':
            self.img = Landsat7(paths.image)
        elif self._satellite == 'LC8':
            self.img = Landsat8(paths.image)
        else:
            raise ValueError('Must choose a valid satellite in config.')

        print('----------- CONFIGURATION --------------')
        for attr in ('date_range', 'satellite', 'k_factor'):
            print('{:<20s}{}'.format(attr, getattr(self, '_{}'.format(attr))))
        print('----------- ------------- --------------')
        self._is_configured = True

    def run(self):
        """ Run the SSEBop algorithm.
        :return: 
        """

        albedo = self.img.albedo()
        emissivity = self._emissivity_ndvi()

    def _emissivity_ndvi(self):

        ndvi = self.img.ndvi()
        bound_ndvi = np.where((ndvi >= 0.2) & (ndvi <= 0.5), ndvi, np.nan)


    @staticmethod
    def _info(msg):
        print('---------------------------------------')
        print(msg)
        print('---------------------------------------')

    @staticmethod
    def _debug(msg):
        print('%%%%%%%%%%%%%%%% {}'.format(msg))

# ========================= EOF ====================================================================

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

from app.config import Config


def run_ssebop(cfg_path):
    cfg = Config(cfg_path)
    for runspec in cfg.runspecs:
        paths.build(runspec.input_root, runspec.output_root)

        welcome()

        sseb = SSEBopModel(runspec)
        sseb.configure_run(runspec)
        sseb.run()


if __name__ == '__main__':
    home = os.path.expanduser('~')
    config_path = None
    run_ssebop(config_path)

# ========================= EOF ====================================================================

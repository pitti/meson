# Copyright 2016 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

logfile = 'meson-logs/install-log.txt'

def do_uninstall(log):
    failures = 0
    successes = 0
    for line in open(log):
        if line.startswith('#'):
            continue
        fname = line.strip()
        try:
            os.unlink(fname)
            print('Deleted:', fname)
            successes += 1
        except Exception as e:
            print('Could not delete %s: %s.' % (fname, e))
            failures += 1
    print('\nUninstall finished.\n')
    print('Deleted:', successes)
    print('Failed:', failures)
    print('\nRemember that files created by custom scripts have not been removed.')

def run(args):
    if len(args) != 0:
        print('Weird error.')
        return 1
    if not os.path.exists(logfile):
        print('Log file does not exist, no installation has been done.')
        return 0
    do_uninstall(logfile)
    return 0

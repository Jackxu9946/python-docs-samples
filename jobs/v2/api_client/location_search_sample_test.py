# Copyright 2018 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def test_location_search_sample(capsys):
    import location_search_sample
    import re

    location_search_sample.run_sample()
    out, _ = capsys.readouterr()
    expected = ('.*appliedJobLocationFilters.*\n'
                '.*appliedJobLocationFilters.*\n'
                '.*appliedJobLocationFilters.*\n'
                '.*appliedJobLocationFilters.*\n'
                '.*appliedJobLocationFilters.*\n')
    assert re.search(expected, out, re.DOTALL)
    expected = ('.*matchingJobs.*\n'
                '.*matchingJobs.*\n'
                '.*matchingJobs.*\n'
                '.*matchingJobs.*\n'
                '.*matchingJobs.*\n')
    assert re.search(expected, out, re.DOTALL)

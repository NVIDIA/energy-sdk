
# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
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

import sys
import dask.array as da
import dask.dataframe as ddf
from typing import  Dict, List, Tuple, Callable
from d2geo.attributes.CompleTrace import ComplexAttributes
from d2geo.attributes.SignalProcess import SignalProcess

sys.path.append('./d2geo/attributes')

def get_sub_cube(cube, examples_percent):
    assert examples_percent > 0 and examples_percent <= 1.0, "Percent must be in (0,1] range."

    i_num, x_num, t_num = cube.shape

    i_start_idx = int((i_num - (i_num * examples_percent))/2)
    i_end_idx   = int(i_start_idx + (examples_percent * i_num))

    x_start_idx = int((x_num - (x_num * examples_percent))/2)
    x_end_idx   = int(x_start_idx + (examples_percent * x_num))

    t_start_idx = int((t_num - (t_num * examples_percent))/2)
    t_end_idx   = int(t_start_idx + (examples_percent * t_num))

    return cube[i_start_idx:i_end_idx,
                x_start_idx:x_end_idx,
                t_start_idx:t_end_idx]

def get_default_funcs():
    complex_att = ComplexAttributes()
    signal_process = SignalProcess()

    def amplitude_arr(input_cube):
        return da.from_array(input_cube)

    # List of tuples with attribute name, the function 
    # to run (with cube as input) and additional kwargs dict.
    funcs = [
        ('Amplitude', amplitude_arr, {}),
        ('Envelope', complex_att.envelope, {}),
        ('Instantaneous Phase', complex_att.instantaneous_phase, {}),
        ('Instantaneous Frequency', complex_att.instantaneous_frequency, {}),
        ('Instantaneous Bandwidth', complex_att.instantaneous_bandwidth, {}),
        ('Dominant Frequency', complex_att.dominant_frequency, {}),
        ('Cosine Instantaneous Phase', complex_att.cosine_instantaneous_phase, {}),
        ('Second Derivative', signal_process.second_derivative, {}),
        ('Reflection Intensity', signal_process.reflection_intensity, {})
    ]
    
    return funcs
    
def run_attributes(input_cube, attributes: List[Tuple[str, Callable, Dict[str, str]]]=None):    
    if attributes == None:
        attributes = get_default_funcs()

    datas = [attr_func(input_cube, **attr_kwargs).flatten() for _, attr_func, attr_kwargs in attributes]            
    datas = da.stack(datas, axis=1)
    return ddf.from_dask_array(datas, columns=[attr_name for attr_name, _, _ in attributes])

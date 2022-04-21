## https://github.com/devitocodespro/Rice-Workshop-2022

## Deep dive into performance benchmarking and optimization

### Outline

The operator used in this training session is based on simplifications of the
systems presented in:

_Self-adjoint, energy-conserving second-order pseudoacoustic systems for VTI
and TTI media for reverse migration and full-waveform inversion (2016). Kenneth
Bube, John Washbourne, Raymond Ergas, and Tamas Nemeth SEG_. [Technical Program
Expanded Abstracts](https://library.seg.org/doi/10.1190/segam2016-13878451.1)

In particular, we will use a simplified version of the TTI self-adjoint
variable-density forward-propagating operator:

* This is a notable proxy of code used in production.
* We focus on the *stencil part of the propagator*, that is, the loops and
  expressions that Devito generates given the finite-difference approximation
  of the TTI partial differential equations expressed in the DSL. 
* Several simplifications made to remove what would be noise in this tutorial:
  * "Dummy" datasets (e.g., all material parameters initialized to constant
    values), but such that the simulation output remains finite;
  * No boundary conditions;
  * No host-device data streaming (by default);
  * No higher-order optimizations (by default) such as adapting boxes;
  * ...


### Login

You will log in to a VM in the Azure Cloud that has been pre-configured with all
the necessary packages to run the TTI demo on an A100 GPU.

To log in, first go to this page and locate yourself (only the last three letters of
your surname will be shown):

```
https://docs.google.com/spreadsheets/d/1oPmvZ9Z_kEcK4iSIOrLExDggZ1_kJRDU3Oz8NObWvjY/edit#gid=0
```

Then, ssh into the VM you've been assigned.

```
ssh -p 2222 <USER>@<VM>
```

The password is `DevitoWorkshop2022`.

To spawn the docker container from which you'll run the demo execute

```
docker run --gpus <GPU> --rm -it devitopro:nvidia.run.<BACKEND>
```

where `<BACKEND>` should be replaced with either `acc` or `cuda`. This will create and take you
to a fresh Docker container where Devito:

* `<BACKEND>=acc`: generates OpenACC,
* `<BACKEND>=cuda`: generates CUDA

Note that the CUDA backend is still in its infancy. It generates functioning
code for this workshops example, but still suffers from several performance
bugs, some of which will be analyzed and fixed in this training session.


### Run the TTI demo

To run the demo simply execute the following commands

```
cd demos/dummy_benchmark
python run.py -d 412 423 476 -nt 200 --broken-mpirun True
```

This will run the TTI demo on a `412x423x476` grid for `200` timesteps.

Some performance metrics, including GFlops/s and GPoints/s, will be emitted to
standard output when the simulation terminates. More info about the Devito
Operator performance available
[here](https://github.com/devitocodes/devito/wiki/FAQ#is-there-a-way-to-get-the-performance-of-an-operator).

If targeting CUDA, please run with

```
CUDA_LAUNCH_BLOCKING=1 python run.py ...
```

for meaningful performance data, otherwise the CUDA kernels in the timed
regions will run asynchronously, making it look like their cost is almost zero.


### Hack the TTI demo

The TTI demo tells you where the generated code is stashed. Run it, and you'll
see a message along the lines of:

```
Operator `TTISelfAdjointForward` jit-compiled
`/tmp/devito-jitcache-uid1002/a60cccac86fdd90c77b2d67c11268042ec93e014.cpp` in
2.95 s with `NvidiaCompiler`
```

You can edit the generated file and test your changes through the "JIT
backdoor" -- a mechanism in Devito that allows users and developers to test
their hacks directly without having to interfere with the Devito compiler.
Make your edits, save the file, and re-run via:

```
DEVITO_JIT_BACKDOOR=1 python run.py -d 412 423 476 -tn 200
```

You may start, for example, by adding a `printf` before the time loop, just
to get familiar with this feature.

More on the JIT backdoor available
[here](https://github.com/devitocodes/devito/wiki/FAQ#can-i-manually-modify-the-c-code-generated-by-devito-and-test-these-modifications).


### NVidia session

<see devito-CUDA-workshop.pdf>

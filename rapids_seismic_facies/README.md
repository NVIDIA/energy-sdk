# Seismic Facies Analysis using Machine Learning

In this notebook, you will find step-by-step guidance on how to use the accelerated machine learning (ML) framework RAPIDS to perform unsupervised facies classification on 3D post-stack seismic datasets.

For detailed documentation, check the arXiv white paper: https://arxiv.org/abs/2007.15152

<img src="https://github.com/NVIDIA/energy-sdk/blob/master/rapids_seismic_facies/figs/intro.png?raw=true" width=700 align=center>

## Getting Started
You can build the whole environment using the provided Dockerfiles at `dockerfile` folder. Also, check the Dockerfiles for extra dependencies.<br>
The scripts `build_docker.sh` and `run_docker.sh` show some basic Docker commands to both build and run the environment. Notice that the *runtime* RAPIDS container already runs Jupyter Lab by default. You may choose a different [NGC RAPIDS](https://ngc.nvidia.com/catalog/containers/nvidia:rapidsai:rapidsai/tags) image if you prefer. Search for *base* containers for a plain environment.

## Notes & Limitations
1. The notebook runs both on CUDA 11.0 and 10.2, with RAPIDS 0.15 and 0.14, respectively.
2. The *first half* of the notebook was executed using a single **A100 GPU**. It is necessary at least 20 GB of GPU memory, but the input dataset can be sub-sampled by changing the `examples_percent` to decrease memory requirement.  You will find this variable along with the code.
3. For the *second half* it is necessary a multi-GPU system. We validate the results on a **DGX-A100** server using **4x GPUs**.

## End User License Agreement (EULA)
This sample code is released under the Apache 2.0 license.

## Third Party Dependencies
docker (https://www.docker.com/)<br>
segyio (https://github.com/equinor/segyio)<br>
numpy (https://numpy.org/)<br>
dask (https://dask.org/)<br>
sklearn (https://scikit-learn.org/)<br>
cupy (https://cupy.dev/)<br>
d2geo (https://github.com/dfitzgerald3/d2geo)<br>
matplotlib, mpl_toolkits (https://matplotlib.org/)<br>
python3 native libraries. (https://www.python.org/) <br>

## References

The code provided was developed by NVIDIA in partnership with the University of Campinas ([UNICAMP](https://ic.unicamp.br/en/)).

Authors:
**João Paulo Navarro** [jpnavarro@nvidia.com](mailto:jpnavarro@nvidia.com)
**Otávio O. Napoli** [onapoli@lmcad.ic.unicamp.br](mailto:onapoli@lmcad.ic.unicamp.br)
**Edson Borin** [edson@ic.unicamp.br](mailto:edson@ic.unicamp.br)
**Pedro Mário Cruz e Silva** [pcruzesilva@nvidia.com](mailto:pcruzesilva@nvidia.com)
**Vanderson Martins do Rosário** [vrosario@lmcad.ic.unicamp.br](mailto:vrosario@lmcad.ic.unicamp.br)

**Joao Paulo de Oliveira** jpnavarro@nvidia.com

FROM nvcr.io/nvidia/rapidsai/rapidsai:0.14-cuda10.2-runtime-ubuntu18.04

RUN apt-get update && apt-get install -y --no-install-recommends \
	apt-utils 

ENV PATH /opt/conda/envs/rapids/bin:$PATH
RUN /bin/bash -c "source activate rapids && pip install segyio=='1.9.1' h5py=='2.10.0'"

EXPOSE 8888
EXPOSE 8787

WORKDIR /workspace

CMD ["/bin/bash"]


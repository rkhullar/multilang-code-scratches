ARG PYTHON_VERSION=3.12
FROM public.ecr.aws/sam/build-python${PYTHON_VERSION}
RUN pip install -U pip setuptools
RUN pip install cffi wheel
COPY example example/
COPY setup.py manifest.in ./
RUN python setup.py bdist_wheel
ENTRYPOINT ["/bin/sh"]

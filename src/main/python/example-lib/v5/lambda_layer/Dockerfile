ARG PYTHON_VERSION=3.12
FROM public.ecr.aws/sam/build-python${PYTHON_VERSION}
COPY build.sh ./
COPY dist/*.whl dist/
#RUN ./build.sh
ENTRYPOINT ["/bin/sh"]
FROM public.ecr.aws/lambda/python:latest
COPY . ${LAMBDA_TASK_ROOT}
RUN pip3 install -r requirements.txt
CMD ["lambda_function.lambda_handler"]
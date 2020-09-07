#!/bin/bash
set -x
awslocal s3 mb s3://airflow/logs
set +x
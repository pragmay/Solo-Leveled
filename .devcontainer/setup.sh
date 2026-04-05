#!/bin/bash
set -e
source /opt/conda/etc/profile.d/conda.sh
conda create -n soloenv python=3.11 -y
conda activate soloenv
conda install -c conda-forge mysql-connector-python python-dotenv -y
echo "==> Done! Run: conda activate soloenv"

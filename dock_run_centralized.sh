#!/bin/bash
# Prepare directory to backup results
saving_path=$(pwd)/results/nuimages10/yolov7/centralized
mkdir -p $saving_path
# Transfer the training and validation sets from the network storage to the local storage of the compute node
#use /fedpylot/datasets/nuimages10/client3  for trainning
#use /fedpylot/datasets/nuimages10/server   for vallidating
echo "Current directory: $(pwd)"
# Download pre-trained weights already downloaded
bash weights/get_weights.sh yolov7


# Run centralized experiment (see yolov7/train.py for more details on the settings)
python yolov7/train.py \
    --client-rank 0 \
    --epochs 3 \
    --weights weights/yolov7/yolov7_training.pt \
    --data data/nuimages10.yaml \
    --batch 32 \
    --img 640 640 \
    --cfg yolov7/cfg/training/yolov7.yaml \
    --hyp data/hyps/hyp.scratch.clientopt.nuimages.yaml \
    --workers 8 \
    --project experiments \
    --name ''

# Backup experiment results to network storage
cp -r ./experiments $saving_path


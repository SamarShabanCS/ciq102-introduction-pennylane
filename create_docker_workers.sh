#!/bin/bash

# Check if the number of containers is passed as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <number_of_containers>"
    exit 1
fi

# Get the number of containers to create
NUM_CONTAINERS=$1

# Define the Docker image to use
DOCKER_IMAGE="fl_mpi_cluster_base:latest" # Replace with your desired image

# Loop to create the specified number of containers
for ((i = 1; i <= NUM_CONTAINERS; i++)); do
    CONTAINER_NAME="fl_mpi_cluster_client__$i" # Generate a unique name for each container
    echo "Creating container: $CONTAINER_NAME"

    # Create and start the container
    docker run --name "$CONTAINER_NAME" --mount type=bind,source=/shared_mnt/AnacondaInstallation/envs/my_pytorch_env,target=/fedpylot/ -dit "$DOCKER_IMAGE"
    
    # Check if the container was created successfully
    if [ $? -eq 0 ]; then
        echo "Container $CONTAINER_NAME created successfully."
    else
        echo "Failed to create container $CONTAINER_NAME."
    fi
done

# List all running containers
echo "Listing all running containers:"
docker ps

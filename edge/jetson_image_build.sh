#!/bin/bash
# Jetson Nano SD card image build script
# Reference: https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit

set -e

IMAGE_URL="https://developer.download.nvidia.com/embedded/L4T/r32.7.1/jetson-nano-sd-card-image.zip"
IMAGE_ZIP="jetson-nano-sd-card-image.zip"
IMAGE_DIR="jetson-nano-image"

mkdir -p "$IMAGE_DIR"
cd "$IMAGE_DIR"

if [ ! -f "$IMAGE_ZIP" ]; then
    echo "Downloading image from $IMAGE_URL"
    curl -L -o "$IMAGE_ZIP" "$IMAGE_URL"
fi

unzip -o "$IMAGE_ZIP"

IMG_FILE=$(ls *.img | head -n 1)

echo "Writing $IMG_FILE to /dev/sdX..." 
# Example dd command, replace /dev/sdX with your SD card device
# sudo dd if="$IMG_FILE" of=/dev/sdX bs=1M status=progress

echo "Image ready."

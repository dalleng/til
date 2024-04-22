# Check volume size in docker

`docker system df` can be used to check the size of images, containers and volumes. By default,
it just shows the aggregated data.

To get the size of a specific image, container or volume the `-v` must be used, so `docker system df -v`.
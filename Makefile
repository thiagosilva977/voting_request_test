# Docker info
DOCKER_IMAGE_NAME=thiago977/election_pandas_future
DOCKER_IMAGE_TAG=1.0.0

# Install project dependencies
setup:
	pip3 install -e . --upgrade --no-cache-dir
	mkdir -p pipeline
	touch make_setup

# Uninstall project dependencies
unsetup:
	rm -f make_setup


# Build docker package
docker/package:
	python3 setup.py bdist_wheel --dist-dir=docker/package
	rm -rf build

# Build docker image
docker/image: docker/package
	docker build docker -f docker/Dockerfile -t $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)
	touch docker/image

# Push docker image
docker/push: docker/image
	docker push $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)
	touch docker/push

# Push docker image with latest tag
docker/push-latest: docker/image
	docker tag $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) $(DOCKER_IMAGE_NAME):latest
	docker push $(DOCKER_IMAGE_NAME):latest
	touch docker/push-latest

# Clean all
clean:
	rm -rf docker/package
	rm -rf docker/image
	rm -rf docker/push
	rm -rf docker/push-latest

# Uninstall/install dependencies, create docker image and push.
do_all:
	make clean
	make unsetup
	python setup.py sdist
	make setup
	make docker/image
	make docker/push-latest
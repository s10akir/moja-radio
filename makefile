SHELL=/bin/bash

build:
	docker build . -t s10akir/moja-radio:latest
	docker push s10akir/moja-radio:latest

# Age and Gender prediction using CNN with XRay Chest Scans (+WebApp)

# THE DATASET
    https://www.kaggle.com/datasets/felipekitamura/spr-x-ray-age-and-gender-dataset

## Environments setup

Install "docker" and "docker-compose"

```sh
$ docker version
Client:
 Cloud integration: v1.0.35
 Version:           24.0.2
 API version:       1.43
 Go version:        go1.20.4
 Git commit:        cb74dfc
 Built:             Thu May 25 21:53:15 2023
 OS/Arch:           windows/amd64
 Context:           default

Server: Docker Desktop 4.21.1 (114176)
 Engine:
  Version:          24.0.2
  API version:      1.43 (minimum version 1.12)
  Go version:       go1.20.4
  Git commit:       659604f
  Built:            Thu May 25 21:52:17 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.21
  GitCommit:        3dce8eb055cbb6872793272b4f20ed16117344f8
 runc:
  Version:          1.1.7
  GitCommit:        v1.1.7-0-g860f061
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

## Quick start

### build and up

```sh
$ git clone https://github.com/mjmichael73/age-gender-prediction-using-chest-x-ray-scans.git
$ cd age-gender-prediction-using-chest-x-ray-scans
$ docker-compose build
$ docker-compose up -d
Starting dockercomposeflask_redis_1 ... done
Starting dockercomposeflask_web_1 ... done
Starting dockercomposeflask_nginx_1 ... done
```

Check the service running information

```sh
$ docker-compose ps
           Name                         Command               State           Ports
--------------------------------------------------------------------------------------------
dockercomposeflask_nginx_1   /usr/sbin/nginx                  Up      0.0.0.0:80->80/tcp
dockercomposeflask_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp
dockercomposeflask_web_1     /runserver.sh                    Up      0.0.0.0:8000->8000/tcp
```

Check the web service

```sh
$ curl 127.0.0.1
Hello Container World! I have been seen 1 times and my hostname is 09ad15ad1b51.
$ curl 127.0.0.1
Hello Container World! I have been seen 2 times and my hostname is 09ad15ad1b51.
$ curl 127.0.0.1
Hello Container World! I have been seen 3 times and my hostname is 09ad15ad1b51.
```

### stop the service

```sh
$ docker-compose stop
Stopping dockercomposeflask_nginx_1 ... done
Stopping dockercomposeflask_web_1   ... done
Stopping dockercomposeflask_redis_1 ... done
```

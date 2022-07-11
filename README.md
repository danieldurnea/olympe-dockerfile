# Olympe Dockerfile 🐋

This repository contains a [Parrot Olympe](https://developer.parrot.com/docs/olympe/overview.html) dockerfile. For testing purposes the dockerimage will start an Olympe Python script and connect to a simulated ANAFI Ai drone using the [Sphinx simulator](https://developer.parrot.com/docs/sphinx/index.html).

## Prerequisites ✔

* [Docker](https://www.docker.com/)
* [Sphinx](https://developer.parrot.com/docs/sphinx/index.html) - For testing only, not required

## Folder content 🗃️
```
/olympe-dockerfile
    ├── README.md           Repository README
    ├── Dockerfile          Dockerfile for Olympe
    └── main.py             Python script to test dockerfile           
```

## Setup ⚙️

In your terminal run 

```
git clone https://github.com/mgr098/olympe-dockerfile.git
cd olympe-dockerfile
```

Once you have cloned and navigated to the folder build the image

```
docker build -t olympe:latest .
```
<details>
<summary> Verify build success </summary>
<br>

To verify that the build succeded run 
```
docker images
```
The expected result is
```
REPOSITORY              TAG       IMAGE ID       CREATED          SIZE
olympe                  latest    078c596242ad   0 days ago       690MB
```
</details>

## Usage 🖥

Run the olympe dockerfile 

```
docker run --network host olympe:latest
```



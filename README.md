<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Belvo Test: Future of Pandas </h3>

  <p align="center">
    Belvo Web-scraping trial.
    <br />
    <a href="https://github.com/thiagosilva977/belvo_test_docker/issues">Report Bug</a>
    ·
    <a href="https://github.com/thiagosilva977/belvo_test_docker/pulls">Request Feature</a>
  </p>
</div>




### Topics 

[Description](#project-description)

[Docker](#docker-image)

[How I solved this challenge](#how-i-solved-this-challenge)


## Project Description

You are in a fictitious alternate universe where the Great Bear Council (GBC) is about to decidethe fate of the panda bears.
The GBC has a total of five votes, based on the outcome of the 5 votes, the pandas will eitherlive in a reservation or they 
will perish in abearbaricdeath.

Your mission is to write a program that will perform the 5 required votes to either beary thepandas forever in a bearicade 
of death or to save them, allowing them to stay in a bambooreservation.Along with the contract, you are given the secret 
voting tokens that are unique to each memberof the GBC (they were secretly stolen).

## Docker Image

### Pull Image
```docker pull thiago977/election_pandas_future:latest```

### Run

#### Run image
```docker run thiago977/election_pandas_future start-elections```
#### Arguments
You can use ``` --pandas-should-live = Bool``` to decide if pandas should live or not.

```docker run thiago977/election_pandas_future start-elections --pandas-should-live=False```

## How I solved this challenge



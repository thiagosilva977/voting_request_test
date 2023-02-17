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
The voting system is divided in four steps. 

The most important variables: 
- **panda_key**: Basically the token for this trial ( ```https://panda.belvo.io/?trial_key=<ID>``` ).
- **panda_type**: It's the panda token like ```bearfoot_bearitone```.
- **op_sys**: Each panda_type (or panda token) has your unique operating system.
- **current_useragent**: Randomic User-Agent for requests.
- **first_step_cookies**: First collected cookie from request.
- **first_step_html**: First HTML collected in the first request.
- **secondary_panda_type**: Secondary variable that I named secondary_panda_type. Is basically ```['bearwitness', 'beararms', 'beargarden',
                                 'bearfruit', 'osopanda', 'papabear', 'pandosobearinmind', 'bearmarket',
                                 'mamabear', 'tedybear']```
- **secondary_panda_token**: 
- **encoded_user_agent**: 
- **rats_token**: 
- **raccoon_token**: 

### Step 1 - Initial request
The first step is making a request to ```https://panda.belvo.io/?trial_key=A3F3D333452DF83D32A387F3FC3-THSI```. 

All we need in this request is getting **aaa**



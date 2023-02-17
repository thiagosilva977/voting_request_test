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
- **secondary_panda_token**: Token collected in hidden form named ```carnivoreatingbambu```. 
- **encoded_user_agent**: Encoded user agent with the following format: **base64(user-agent + secondary_panda_type + op_sys)**
- **rats_token**: Base64 string following format: **base64(  secondary_panda_type letters replaced by corresponding dictionary values: "{'_': 341, 'a': 332, 'b': 335, ...}" and "|" between letter numbers ) "** like: ```16540|16536|16537|16549|16551|16539|16535|16546|16540|16536|16537|16549|16545|16534``` 
- **raccoon_token**: Necessary UUI token to post a valid vote. Like: ```feb5487a-0357-43e6-bbbe-1c08b7cc5957```.

### Step 1 - Initial request
The first step is making a request to ```https://panda.belvo.io/?trial_key=A3F3D333452DF83D32A387F3FC3-THSI```, using **current_useragent** and **panda_key** to succeed the request.

All we need in this request is getting **first_step_cookies** to use in future requests and **first_step_html** wich have important values to use in future steps. 

We can also collect **secondary_panda_type** and **secondary_panda_token** to generate the **encoded_user_agent** variable.



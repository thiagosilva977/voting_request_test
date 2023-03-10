<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Voting System Test</h3>

  <p align="center">
    Program that tries to vote in a test website.
    <br />
    <a href="https://github.com/thiagosilva977/voting_request_test/issues">Report Bug</a>
    ·
    <a href="https://github.com/thiagosilva977/voting_request_test/pulls">Request Feature</a>
  </p>
</div>




### Topics 

[Description](#project-description)

[Docker](#docker-image)

[How I solved this challenge](#how-i-solved-this-challenge)

[Feedback and annotations](#feedback-and-annotations)

## Project Description

You are in a fictitious alternate universe where the Great Bear Council (GBC) is about to decidethe fate of the panda bears.
The GBC has a total of five votes, based on the outcome of the 5 votes, the pandas will eitherlive in a reservation or they 
will perish in abearbaricdeath.

Your mission is to write a program that will perform the 5 required votes to either beary thepandas forever in a bearicade 
of death or to save them, allowing them to stay in a bambooreservation.Along with the contract, you are given the secret 
voting tokens that are unique to each memberof the GBC (they were secretly stolen).

## Docker Image

### Creating docker image and pushing to registry
I use a makefile to make this process more quickly. 

- Use the command ```make_setup``` to setup the project and install all requirements.
- Use the command ```make_unsetup``` to unsetup the project and uninstall all requirements.
- Use the command ```make_do_all``` to create and push the docker image to docker registry.

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
- **panda_key**: Basically the token for this trial ( ```https://panda.-----.io/?trial_key=<ID>``` ).
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
- **step_3_cookies**: Cookies generated in ```daxiongmao.js``` request.
- **raccoon_token**: Necessary UUID token to post a valid vote. Like: ```feb5487a-0357-43e6-bbbe-1c08b7cc5957```.

### Step 1 - Initial request
The first step is making a request to ```https://panda.-----.io/?trial_key=A3F3D333452DF83D32A387F3FC3-THSI```, using **current_useragent** and **panda_key** to succeed the request.

All we need in this request is getting **first_step_cookies** to use in future requests and **first_step_html** wich have important values to use in future steps. 

We can also collect **secondary_panda_type** and **secondary_panda_token** to generate the **encoded_user_agent** variable.


### Step 2 - Request to hastorni.js

The second step is making a request to ```	https://panda.-----.io/hastorni.js```, using **session_cookie**, **useragent**, **panda_type** and **panda_key** to succeed the request.

All we need in this request is getting **rats_token** to use in step 3 and 4.

### Step 3 - Request to daxiongmao.js

The third step is making a request to ```https://panda-----o.io/daxiongmao.js```, using  **session_cookie**, **useragent**, **secondary_panda_token**, **encoded_useragent** and **panda_key** to succeed the request.

All we need in this request is getting **raccoon_token** and **step_3_cookies** to use in the voting request.

We can also collect **secondary_panda_type** and **secondary_panda_token** to generate the **encoded_user_agent** variable.

### Step 4 - Finally the voting request

This is the most important part. We will decide the future of pandas. We already know that they are causing some troubles(like sleeping too much), and it's time to decide if they will live forever or sleep eternally.

The fourth step is making a request to ```https://panda------.io/ursidaecarinove_eating_bambu_must_die```, using  **step_3_cookies**, **useragent**, **secondary_panda_name**, **raccoons_token** , **rats_token** and **panda_token** to succeed the request.

All we need in this request is getting **succeed_request** and **response_from_request** to just get the validation that the vote was registred.

## Feedback and Annotations

### Feedback
This was one of the most interesting test-project that I've done.
This test can be simple and complex at the same time, and I love it! 

Resillience is the right answer to solve this test. It took me about five to six hours to discover how the website works and all variables needed to succeed with each request. During the process I tried a lot of techiniques to do requests, decode and encode variables and more. This was the main reason that caused some disorganization with code and that I've spent soo much time refactoring and cleaning the code.

I would like to congratulate all the people who developed this test.

```#PandasShouldLive```

### Time tracker
![image](https://user-images.githubusercontent.com/11250089/219534814-a4c72c20-0e88-4575-b57b-41d6793d4df3.png)


### Future improvements
- Better detailed code and repository documentation
- Better logs
- More precision of data collected
- Reduce the number of necessary requests to getting a single vote
- Find the pattern between **panda_type** and **secondary_panda_type**


### Result files
- [Logs for voting to pandas live](https://github.com/thiagosilva977/voting_request_test/blob/master/voting_request_test/assets/example_successful_run.log)
- [Logs for voting to pandas die](https://github.com/thiagosilva977/voting_request_test/blob/master/voting_request_test/assets/pandas_should_die.log)
- [Some informations for success voting](https://github.com/thiagosilva977/voting_request_test/blob/master/voting_request_test/assets/success_data.xlsx)
- [Time tracker for this project](https://github.com/thiagosilva977/voting_request_test/blob/master/voting_request_test/assets/clockfy_time_tracker_for_belvo.pdf)

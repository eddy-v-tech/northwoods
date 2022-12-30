# Northwoods Babysitter Kota

This implementation of of the babysitter kota aims to deliver on the objective of calculating a nightly charge based on on the constraints given in the file provided by Northwoods. It also aims to show a degree of automated testing and TDD. Levaraging pytest and github actions to perform automated testing on every push I believe that has been achieved. 

Below you will find the requirements to run the python program as well as the tests associated with it. 

## Requirements to run on local machine

This program was written using python 3.9 so any other version is not guarenteed to work. (Probably would though)

Required installs:
1. Run to be able to run tests
    ```
    pip install pytest
    ```

## Local Usage

To run the program navigate to the /app directory and use the following command as an example -s is for start and -f is for finish
1. Run
    ```
    python babysitting_calc_app.py -s 5:00PM -f 12:00AM
    ```

This will give you a calculation of a nightly charge between 5PM and 12AM (the default bedtime is set to 10PM, but you can change this with the optional -b agrument)

To get help with any issues on running the command use the command below for guidance
1. Run
    ```
    python babysitting_calc_app.py -h
    ```

## Requirements to run with docker

Optionally if you do not want to worry about having to install python. I have provided a compose file to use that will take care of all the set up for you. With instructions below. Here is a link to get the latest version of docker. 

https://docs.docker.com/get-docker/

## Docker Usage

1. Navigate to the /docker directory
    ```
    cd docker
    ```

2. Run the following command to build the image we will be running against
    ```
    docker-compose up
    ```

3. After that is complete run the following as an example (you can use -h for help instead of using -s or -f)
    ```
    docker run docker-babysitter-service -s 12AM -f 1AM
    ```

## Docker Clean Up

The actions above can lead to a bunch of containers being made if ran many times (there are ways to not have this happen but for simplicity I will just have the clean up steps available.)

1. Run the following command
    ```
    docker-compose down
    ```
2. Run the following command to remove the stopped containers
    ```
    docker ps -a | awk '{ print $1,$2 }' | grep docker-babysitter-service | awk '{print $1 }' | xargs -I {} docker rm {}
    ```
3. Run the following command to delete the image that was created
    ```
    docker rmi docker-babysitter-service
    ```

## Testing

Testing is set up to happen automatically when pushing to github on any branch in the repo. You can see the test results per push by going to "Actions" next to "Pull Requests" at the top of this repo.

To test locally you just have to navigate to the /app directory and run (the v is to make it more verbose)
    ```
    pytest -v
    ```

I did not have time to configure the docker portion to run the tests, but with a little more time that could get added as well.

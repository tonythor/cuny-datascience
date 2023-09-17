# AWS Rekognition Demo
*by: Tony Fraser, 16 Sept 2023*

*for: fellow classmates of CUNY 607* 

## About this demo
This chunk of python code makes API calls to the Amazon Rekognition API. Basically, it sends up pictures to AWS for AWS to scan. AWS then returns metadata about the pictures. Within that return data, among other things, one can find out if a picture contains skateboarders, happy little kids, streets named Broadway, or even Will Smith drinking a glass of wine. 

The AWS Rekognition API does a _lot_ more than tiny program demonstrates, but hopefully it sets the seed that sometimes using an existing compute API's might be the right way go to. 

* Rekognition overview: [https://aws.amazon.com/rekognition/](https://aws.amazon.com/rekognition/)
* API documentation: [https://docs.aws.amazon.com/cli/latest/reference/rekognition/](https://docs.aws.amazon.com/cli/latest/reference/rekognition/)
* Pricing: [https://aws.amazon.com/rekognition/pricing/](https://aws.amazon.com/rekognition/pricing/)


## Look closely at:
* [./wrapper_by_tf.py](wrapper_by_tf.py)
* [./output.log](./output.log)

## Why did I choose this as my demo?
Multiple times in my career I've had build systems to extract metadata from images, pdfs, word docs, quicktimes, etc. On multiple occasions, these rocket-science-complex projects were person-years worth of effort. With the introduction of open source in the 2010's it got a little easier, but everything changed when cloud took over. Now days, AWS, GCP and Azure have hundreds of API's data scientists can use

This particular demo took me about eight hours to set up and get working. 20 years ago, my team did something similar and it was one of those person-year long projects. 

The point is, sometimes you have to roll your own system, sometimes you don't. Think about it before you do either. This is demo is charged by API call. If we were doing a billion of API calls for non profit, it might not make sense. If you're working on a startup and tying to push something out the door by enxt month, pay per use api's might be perfect.


## Demo assumes:
1. You already have python3 installed somewhere so you can use it to setup your virtualenv. Verify python3 with this command: 
    ```sh
    hurricane:cuny-datascience afraser$ python3 --version
    Python 3.11.5
    ```
1. You already have the awscli set up and working on your mac, which includes the correct setup of `~/.aws/credentials`. *If you have it running locally, your boto library will work with your virtualenv!* Test with this command:  
    ```sh
    hurricane:cuny-datascience afraser$ aws sts get-caller-identity
    {
        "UserId": "ABCDEFDGHIJKLOMNOPRS",
        "Account": "11111111111111111",
        "Arn": "arn:aws:iam::11111111111111111:user/tony.fraser"
    }
    ```
1. You  have a virtualenv created from a `requirements.txt` like the one in the root of this project. Building your virtualenv would look roughly like this:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    .venv/bin/python -m pip install --upgrade pip 
    ##if necessary)## .venv/bin/pip freeze | xargs pip uninstall -y 
    .venv/bin/python -m pip install -r ./requirements.txt
    ```



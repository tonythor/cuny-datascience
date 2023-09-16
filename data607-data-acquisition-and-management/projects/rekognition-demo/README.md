# AWS Rekognition Demo
*by: Tony Fraser, 16 Sept 2023*

*for: fellow classmates of CUNY 607* 

Written in python, this demo shows one how to use the rekognition api to extract metadata from photo and video content.

* Rekognition overview: [https://aws.amazon.com/rekognition/](https://aws.amazon.com/rekognition/)
* API documentation: [https://docs.aws.amazon.com/cli/latest/reference/rekognition/](https://docs.aws.amazon.com/cli/latest/reference/rekognition/)


## Assumes:
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
1. You  have a virtualenv created from a requirements.txt like the one in the root of this project. Building your virtualenv would look roughly like this:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    .venv/bin/python -m pip install --upgrade pip 
    .venv/bin/pip freeze | xargs pip uninstall -y 
    .venv/bin/python -m pip install -r ./requirements.txt
    ```

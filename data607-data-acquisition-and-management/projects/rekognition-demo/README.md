# AWS Rekognition Demo
* Written in python, this demo shows one how to use the rekognition api to extract metadata from photo and video content.
* Intended Audience: fellow classmates of 607 data acquisition and management



## Assumes:
1. You already have the awscli set up and working, and that you already have correctly set up `~/.aws/credentials`. Test with this command:  
    ```sh
    (.venv) hurricane:cuny-datascience afraser$ aws sts get-caller-identity
    {
        "UserId": "ABCDEFDGHIJKLOMNOPRS",
        "Account": "11111111111111111",
        "Arn": "arn:aws:iam::11111111111111111:user/tony.fraser"
    }
    ```
1. You already have your virtual env set up. Replicate this virtualenv with requirements.txt in the root of this project. Building your virtualenv would look roughly like this:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    .venv/bin/python -m pip install --upgrade pip 
    .venv/bin/pip freeze | xargs pip uninstall -y 
    .venv/bin/python -m pip install -r ./requirements.txt
    ```

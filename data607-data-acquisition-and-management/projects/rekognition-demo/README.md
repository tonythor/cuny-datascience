# AWS Rekognition Demo
* Written in python, this demo shows one how to use the rekognition api to extract metadata from photo and video content.
* Intended Audience: fellow classmates of 607 data acquisition and management



## Assumes:
1. You already have the awscli set up and working, and that you already have correctly set up `~/.aws/credentials``, Test with this command.  


```sh
(.venv) hurricane:cuny-datascience afraser$ aws sts get-caller-identity
{
    "UserId": "ABCDEFDGHIJKLOMNOPRS",
    "Account": "11111111111111111",
    "Arn": "arn:aws:iam::11111111111111111:user/tony.fraser"
}
```


<!-- # 1. get all teh AWS client stuff on your mac.
# 1.a. brew install awscli, etc. 
# 1.b. make sure ~/.aws/credentials is working

# 2. Set up requriments 
## use requirements.txt in the root of this project to set up your virtualenv.
# python3 -m venv .venv
# source .venv/bin/activate
# .venv/bin/python -m pip install --upgrade pip 
##(if necessary ->)## pip freeze | xargs pip uninstall -y  
# .venv/bin/python -m pip install -r ./requirements.txt
 -->

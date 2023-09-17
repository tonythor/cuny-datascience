# AWS Rekognition Demo
*by: Tony Fraser, 16 Sept 2023*

*for: fellow classmates of CUNY 607* 

## About this demo
This chunk of python code makes API calls to the Amazon Rekognition API. Basically, this code sends up pictures to AWS, then AWS scans them and then returns metadata about what is in the pictures. Within that returned data, among other things, one can find out if a picture contains skateboarders, happy little kids, streets named Broadway, or even Will Smith. 

The AWS Rekognition API does a _lot_ more than tiny program demonstrates, but hopefully it sets the seed that sometimes using an existing compute API's might be the right way go to. 

* Rekognition overview: [https://aws.amazon.com/rekognition/](https://aws.amazon.com/rekognition/)
* API documentation: [https://docs.aws.amazon.com/cli/latest/reference/rekognition/](https://docs.aws.amazon.com/cli/latest/reference/rekognition/)
* Pricing: [https://aws.amazon.com/rekognition/pricing/](https://aws.amazon.com/rekognition/pricing/)


## The Demo mostly in these two files
* [./wrapper_by_tf.py](wrapper_by_tf.py)
* [./output.log](./output.log)

## Why did I choose this as my demo?
Many times in my career I've built systems to extract metadata from images, pdfs, word docs, videos, etc. These rocket-science-complex projects were often person-years worth of effort. In the early 2000's, extraction got a little easer due to the momentum of open source. Later though, when compute microservices like Rekognition started to be offered via API, everything totally changed. Now days, AWS, GCP and Azure have hundreds of API's data scientists can use. Picking underlying technology, like metadata extraction, is now more like picking what store to buy a commodity from.

The point of this demo is, sometimes you have to roll your own systems and build the rocket-science-complex tools, and sometimes you don't. From somebody that has done both, I only suggest think first before you pick. This is demo cost per API call. A billion of API calls for nonprofit might not make sense, but if you're working with a startup trying to build a new product by October, pay per use API's might be perfect. 

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
    ##if necessary## .venv/bin/pip freeze | xargs pip uninstall -y 
    .venv/bin/python -m pip install -r ./requirements.txt
    ```



import boto3
import json
from rekognition_image import RekognitionImage
from rekognition_objects import RekognitionFace, RekognitionCelebrity, RekognitionText
import logging
from typing import List


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

client = boto3.client('rekognition')
bucket = 'tonyfraser-public'

def p_url(_p: str, bucket: str = "tonyfraser_public") -> str:
    return f"http://{bucket}.s3-website-us-east-1.amazonaws.com/{_p}"

def log_f(_string, _filepath="./output.log"):
    with open(_filepath, 'a') as f:
        f.write(f"{_string}\n")



log_f("---------------------------------------------")
tonyHawkPath='images/tonyhawkandson.jpg'
log_f(p_url(tonyHawkPath))
tonyHawkImg = {'S3Object': {'Bucket': bucket, 'Name': tonyHawkPath}}
tonyHawk = RekognitionImage( 
    image=tonyHawkImg,
    image_name=tonyHawkPath,
    rekognition_client=client)
faces: List[RekognitionFace] = tonyHawk.detect_faces() 
for face in faces:
    log_f(f"{face.gender} in {face.bounding_box}. Is smiling? {face.smile}" )

celebs = tonyHawk.recognize_celebrities()[0]
for celeb in celebs:
    log_f(f"{celeb.name} is in the picture!")


log_f("---------------------------------------------")
sixtiesSuitPath='images/60s_poolside_swimsuit.jpg'
log_f(p_url(sixtiesSuitPath))
sixtiesSuitImg = {'S3Object': {'Bucket': bucket, 'Name': sixtiesSuitPath}}
sixtiesBathingSuit = RekognitionImage(
    image=sixtiesSuitImg,
    image_name=sixtiesSuitPath,
    rekognition_client=client)
labels = sixtiesBathingSuit.detect_moderation_labels()
for label in labels :
    log_f(f"{label.name}: {round(label.confidence, 3)} confidence")


log_f("---------------------------------------------")
avengersPath='images/the-avengers.jpg'
log_f(p_url(avengersPath))
avengersImg = {'S3Object': {'Bucket': bucket, 'Name': avengersPath}}
avengers = RekognitionImage(
    image=avengersImg,
    image_name=avengersPath,
    rekognition_client=client)
celebs = avengers.recognize_celebrities()[0]
for celeb in celebs:
    log_f(f"{celeb.name} is in the picture!")


log_f("---------------------------------------------")
plazaPath='images/crownplaza.jpg'
log_f(p_url(plazaPath))
plazaImg = {'S3Object': {'Bucket': bucket, 'Name': plazaPath}}
plaza = RekognitionImage(
    image=plazaImg,
    image_name=plazaPath,
    rekognition_client=client)

# faces: List[RekognitionFace] = tonyHawk.detect_faces() 
texts: List[RekognitionText] = plaza.detect_text()
for txt in texts:
    log_f(f"txt: {txt.text}")




 

# django-rest-captcha
This Service provides a tool for generating captchas and verifying them which is useful for security of websites in order to be safe from bots' attacks.
Implemantation of this service is with django and it works as a Restful API. It can be used by any end user (specially client side) in order to enhance saftey of your website.General procedure of this serveice which includes mehtods of sending request and verfying captcha will be described briefly.



## **How to receive captcha**
For receiving picture of the captcha user should send a Post request to the following endpoint:
```http:localhost:8000/api/captcha/```


then you will receive a Json as a response which has a structure like bellow:
``` json
{
    "captcha_key": "key of captcha",
    "captcha_image": "encoded image of captcha",
    "image_type": "image/png",
    "image_decode": "base64"
}
```
then by decodeing key of **captcha_image** in the response user can receive and show the image of captcha on it's interface.

As a sample for approach of decodoing image, I put a file with the name of imageBase64Decoder.py that can be used for decoding and showing the image. it receives encoded_image as input and shows the picture as output.


## **How to validate Captcha**
After showing picture, now it's time to see if the answer of user it true or not. To do this a Post request with 2 parameters in the body should be sent to the following address:

```http:localhost:8000/captcha/verify/```

The parameters which you need to send are:

**captcha_key** which was sent as a response of first request and **captcha_value** that indicates the answer of user to the captcha. For instance body of your request should be sth like this:
``` json
{
    "captcha_key":"the key which was received by the last request",
    "captcha_value":"answer of user to captcha"
}
```
 If everithing goes fine you will receive **verified** however **notverified** will be shown if there is a problem.


Requirments of this service with its exact version are in requirements.txt :))
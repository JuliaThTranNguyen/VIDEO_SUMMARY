"""upload tests"""

import base64
import os
import unittest
import requests
from flask import Flask, Request, request,url_for, current_app
from io import StringIO
import unittest
import werkzeug

import app

# https://raw.githubusercontent.com/mathiasbynens/small/master/jpeg.jpg
SMALLEST_JPEG_B64 = """/vid_sum/flask/backend/app/static/video/Samsung_Galaxy_Z_Flip_3_Impressions__Design_Refresh.mp4
"""

class BaseTestCase(unittest.TestCase):
    URL = "HTTP://127.0.0.1:5000/uploads"

    def test_save(self):
        with app.create_app().test_client() as client:
            file = werkzeug.datastructures.FileStorage(
                stream=io.BytesIO(base64.b64decode(SMALLEST_JPEG_B64)),
                filename="example Samsung_Galaxy_Z_Flip_3_Impressions__Design_Refresh.mp4",
                content_type="video/mp4",
            )
            response = client.post(
                '/',
                data=dict(
                    file=file,
                ),
                follow_redirects=True,
                content_type='multipart/form-data',
            )
    print("Client_test_case: Test completed! DONE. OKAY!!!   run from: test_app.py")


class TestAPI (unittest.TestCase):
    URL = "HTTP://127.0.0.1:5000/uploads"

    def test1_case(self):
        resp=requests.get(self.URL)
        self.assertEqual(resp.status_code,200)
        self.assertEqual(len(resp.json))
    print ("API Test for URL /uploads  is completed.   DONE!!! from: test_app.py - class TestAPI")


if __name__ == "__main__":
    tester = BaseTestCase()
    tester = TestAPI()
    

  

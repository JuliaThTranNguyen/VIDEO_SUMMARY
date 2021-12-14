# VIDEO-SUMMARASION
# Upload and Play Video using Flask application for deploying AC-SUM-GAN: Connecting Actor-Critic and Generative Adversarial Networks for Unsupervised Video Summarization

## Environment setup?

### Code editer framework which I used in this project "Visual Studio Code"

 Visit at "https://code.visualstudio.com/"
 

### Install Python version for VScode
 Visit at "https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment"

 Or Visit this link "https://phoenixnap.com/kb/install-flask"
 
 These link above have the available version for Python on OS X, WINDOWS, LINUX OS based system.
 

## Create Flask application

## This should be done in this directory /vid_sum/flask/backend/

### Make a virtual environemnt to deploy Flask application

Run

<pre>
$ python -m venv _name_of_environment_
</pre>

### Make a virtual environemnt to deploy Flask application

Run on OS X and LINUX:

<pre>
$ source _name_of_environment_/bin/activate
</pre>

Run on WINDOWS:

<pre>
$ _name_of_environment_\Scripts\activate.ps1
</pre>

### Install requirements.txt

Run on OS X, LINUX:
<pre>
$ pip3 install -r requirements.txt --no-warn-script-location
</pre>

Run on WINDOWS:
<pre>
$ pip install -r requirements.txt --no-warn-script-location
</pre>

### Run the Flask application

Run:

<pre>
$ flask run
</pre>

Or run this: run.py located in /vid_sum/flask/vid_sum/backend/
Run on OS X, LINUX:

<pre>
$ python3 run.py
</pre>

Run on WINDOWS:

<pre>
$ python run.py
</pre>

### You can visit the dotenv file ".env" in /vid_sum/flask/vid_sum/backend/

### To change config as your wish


## How to run test cases?

## Noticed : These test cases are located in /vid_sum/flask/vid_sum/backend/app/tests/

Run on OS X, LINUX:

<pre>
$ python3 test_app.py
</pre>

Run on WINDOWS:

<pre>
$ python test_app.py
</pre>


## This action should be activate within /vid_sum/flask/backend/vid_sum

## PyTorch Implementation of AC-SUM-GAN

- From **"AC-SUM-GAN: Connecting Actor-Critic and Generative Adversarial Networks for Unsupervised Video Summarization"** (IEEE Transactions on Circuits and Systems for Video Technology (IEEE TCSVT 2020), Early Access)
- Reimplemented by Minh Hoang

## Dependency

Run

<pre>
pip install -r requirements.txt
</pre>

## Generating video

To summarize videos stored in a directory, run:

<pre>
python evaluate.py [path_to_video_dataset_folder] [duration_of_result]
</pre>

## Data

Dataset generated by `generate_dataset.py` have the following structure:

<pre>
/key
    /features                 2D-array with shape (n_steps, feature-dimension)
    /picks                    positions of subsampled frames in original video
    /n_frames                 number of frames in original video
    /fps                      fps of original video
    /change_points            2D-array with shape (num_segments, 2), each row stores indices of a segment
    /n_frame_per_seg          1D-array with shape (num_segments), indicates number of frames in each segment
    /video_name               original video name
</pre>
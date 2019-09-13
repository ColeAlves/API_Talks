This was coded and ran in Jupyter notebook, but there is a python file for those that don't have Jupyter notebook.
The code will error out without the following things downloaded. 
It will also error out since I removed the secrets and my account information.
Need to create an account for Reddit and Imgur and install the following to work correctly.

Installs
pip install praw
pip install opencv-python
pip install imgur-uploader


The Praw api demostration is a python reddit bot that grabs an image from a post and does the following to the image.

-> downloads the image from the post
-> applies the grayscale filter to the post 
-> post the image to imgur using the imgur api
-> grabbing the link of the image that was posted to imgur

The demostration also shows how to reply to a post.  If there is any questions feel free to ask me in the umsl computing club slack channel and I will answer 
as quickly as possible.  

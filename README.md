# Forgegy Image Detection Using Error level Analysis and Deep Learning

Many images are spread in the virtual world of social media. With the many editing software that
allows so there is no doubt that many forgery images. By forensic the image using Error Level Analysis to
find out the compression ratio between the original image and the fake image, because the original image
compression and fake images are different. In addition to knowing whether the image is genuine or fake
can analyze the metadata of the image, but the possibility of metadata can be changed.

`image forensic is a field of the study identifying the origin and verifying the
authenticity of the image.`

Many methods are used to determine the level of authenticity of the picture, one with
determining the quality of the image compression level results. He, the methods used to measure the level of compression is using `Error Level Analysis (ELA)`. 

`Error level analysis` is one technique for knowing images that have been manipulated by
storing images at a certain quality level and then calculating the difference from the
compression level.

In this we have applied Deep Learning to recognize images of manipulations through the dataset of a fake image
and original images via Error Level Analysis on each image and supporting parameters for error rate
analysis. 

The result of my experiment is given below:

|Architecture|Accuracy|
|--------|------------|
|CNN|88.8|
|Pretrained Resnet|94.4|


Paper: https://www.sciencedirect.com/topics/computer-science/image-manipulation



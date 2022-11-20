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
|Pretrained Resnet|96.2|

`Classification Report`

<img width="140" alt="image" src="https://user-images.githubusercontent.com/43055935/202889601-109aa2fb-7cb5-46b7-8945-c7f2a1bfedf3.png">

`ELA Images batch`

<img width="451" alt="image" src="https://user-images.githubusercontent.com/43055935/202889344-ab00fe0b-1927-48e9-9d9b-b9eab7f3f9c4.png">

`Decrease in Loss on a subset of dataset`

<img width="575" alt="image" src="https://user-images.githubusercontent.com/43055935/202889273-8a90fa7f-4ae8-4fff-b58a-5f000812de36.png">

`Increase in F1 Score over on a subset of dataset`

<img width="576" alt="image" src="https://user-images.githubusercontent.com/43055935/202889310-2c5fe55b-3a5a-41e0-9a49-fa9bb5d7c044.png">

`Training `

<img width="641" alt="image" src="https://user-images.githubusercontent.com/43055935/202889418-5f407379-0fdb-4014-a1a4-d81610eb4f33.png">

Paper: https://www.researchgate.net/publication/332561655_Image_forgery_detection_using_error_level_analysis_and_deep_learning



# Colab_fastai
Colab Compatible FastAI notebooks for mainly NLP, Computer Vision, and Recommender Systems.
Fastai describes the work in **4 forms:** 

**1. Tabular**- We are provided with a Tabular Data and we need to do Regression/ Classification. Jeremy believes in using Deep Learning wherever we can and for the situation where we are not sure about Deep Learning implement Random Forests as taught in ML series.

    Find more related works at https://github.com/navneetkrc/Colab_fastai/tree/master/Tabular

**2. NLP**- Here we have NLP related tasks and we are using ULMFiT models as our Embeddings and find great results. This is based on **Language Models**, they are fine-tuned to our Dataset to include dataset specific words and sentence structure. The Language Model training is converted into semisupervised task by trying to predict the next word, using Transfer Learning starting from WikiText model and finetuning for our dataset, and we implement our text classifier from scratch based on the newly finetuned word embeddings.

    Find more related work at https://github.com/navneetkrc/Colab_fastai/tree/master/NLP

**3. CV- Image Datasets**- Here we have a lot of Images as our data and we want to implement image classifiers usually. Here we use transfer learning and we use one of the Imagenet pretrained model and finetune it as well for our dataset and the classifier part gives probability distribution for the classes that we want for prediction.

    Find such datasets and work at https://github.com/navneetkrc/Colab_fastai/tree/master/Image%20Datasets

**4. Recommender Systems**- Here we implement Recommender Systems based on **User and Item Embeddings** and it turns out that by using these simple approach we are able to get good results for recommender systems.

    Find more related work at https://github.com/navneetkrc/Colab_fastai/tree/master/Recommender%20Systems



# Major Highlights of the projects/work done
**Computer Vision Projects**

https://github.com/navneetkrc/Colab_fastai/blob/master/Image%20Datasets/Intel_Image_Classification3.ipynb
This is a Google Colab Notebook on the Intel Image Classification hosted on the Analytics Vidhya
In this There are 17034 images in train and 7301 images in test data.
The categories of natural scenes and their corresponding labels in the dataset are as follows -
'buildings' -> 0,
'forest' -> 1,
'glacier' -> 2,
'mountain' -> 3,
'sea' -> 4,
'street' -> 5
Reached 95% accuracy on the validation data, in order to classifiy with more accuracy need to handle the mislabelled data that we provide as part of training data, for now it is not done as it is more time taking.

https://github.com/navneetkrc/Colab_fastai/blob/master/Image%20Datasets/food_image.ipynb
This is Google Colab Notebook for the Food Data Hackathon hosted by Rakuten in which I got good accuracy almost Top 10 but was not able to submit the test results, after the added documentation in the FASTAI library testing for the test data and adding for that has become more convenient and same has been applied in the Intel Image Classification Challenge as well.

https://github.com/navneetkrc/Colab_fastai/blob/master/Image%20Datasets/KYC_multimodels.ipynb
This Google Colab notebook is for KYC verification of ID documents and classify them correctly as **Aadhar, Pancard, DL, Passport, VoterID**, data is scraped from Google and by only using 30 images for each classes I was getting good results. This can be extended to any number of documents just need to add the corresponding data.

**NLP Based Projects**

NewsGroup DataSet
https://github.com/navneetkrc/Colab_fastai/blob/master/NLP/NewsGroup_ULMFiT_fastai_Text_Classification.ipynb
is the first project in NLP, in this we used a lot of sklearn data handling as well and suggest this to be your first dataset as well to check your understanding. This is the example I used in my Meetup presentation.

Medicinal Review Rating prediction-
https://github.com/navneetkrc/Colab_fastai/blob/master/NLP/Medicine_review_ULMFiT_fastai_Short.ipynb
This is a Google Colab Notebook on the medicinal dataset provided on Kaggle
!kaggle datasets download -d jessicali9530/kuc-hackathon-winter-2018

In this I created a subtask of getting the reviews and the Rating. I have created a Classifier model in which I predict the Rating that a user would give based only on text.
Next iterations I will add more columns and see how adding those columns will affect the results.

AV_Funny_Jokes
https://github.com/navneetkrc/Colab_fastai/blob/master/NLP/AV_Funny_jokes.ipynb
is a dataset provided by Analytics Vidhya where they provide text dataset of jokes and then based on different users and joke we predict what rating would a new user give to the joke.

FASTAI Movie Review 
https://github.com/navneetkrc/Colab_fastai/blob/master/NLP/fast_ai_movie_review.ipynb
This is just the Colab Implementation of the Lecture in FASTAIV3 for the NLP example.

Yelp Movie Review using FASTAI V1
https://github.com/navneetkrc/Colab_fastai/blob/master/NLP/YELP_review_ULMFiT_fastai_Short.ipynb
Similar to the FASTAI dataset of movie review this one is also there, very big dataset and that is the only thing that restricts us for now in training in the Google Colab envirionment, rest is ready and well documented.

**Recommender Systems** 

MovieLens Recommender Systems based on User and Movie Embeddings using only PyTorch
https://github.com/navneetkrc/Colab_fastai/blob/master/Recommender%20Systems/Emb_based_RecSys_PyTorch/movielens_emb_pytorch.ipynb

I will keep adding more projects and try out some of the projects based on the FASTAI V3 Part 2.


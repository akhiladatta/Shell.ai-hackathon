# Shell.ai-hackathon
Solar Power Prediction Hackathon


Goal: To predict the Solar Power after 2 hours, Given past data of sky images and weather parameters.

Data Engineering:
 Used Web Scraping to Collect Sky Images and Raw Data.
 Performed extensive Data Cleaning, Imputation, Feature Engineering and
Visualization.

Model Development - Developed a completely new architecture:
 Trained a CNN with dilation filters to encode a sky image to obtain a full-
sky representation of the sky.
 The representation of images and weather data are separately passed
through LSTMs with certain window size, which are then merged and
passed through another LSTM to get the final predictions of Solar Power
resulting in a MAE Loss of 103.
 As the images lacked sharp features, using dilation filters was helpful
and thus turned out to perform better than VGG16 Pre-trained model for
this task.

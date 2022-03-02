# Shell.ai-hackathon.<br />
Solar Power Prediction Challenge.<br />
Its basically a Time Series Forecasting Challenge.<br />
I  Secured a Global rank of 8, which corresponds to Top 0.5% in the Shell.ai Hackathon for Sustainable and Affordable
Energy 2021.<br />

Goal: To predict the Solar Power after 2 hours, Given past data of sky images and weather parameters.<br />

Data Engineering:<br />
 Used Web Scraping to Collect Sky Images and Raw Data.<br />
 Performed extensive Data Cleaning, Imputation, Feature Engineering and Visualization.<br />

Model Development - Developed a completely new architecture:<br />
 Trained a CNN with dilation filters to encode a sky image to obtain a full-
sky representation of the sky.<br />
 The representation of images and weather data are separately passed
through LSTMs with certain window size, which are then merged and
passed through another LSTM to get the final predictions of Solar Power
resulting in a MAE Loss of 103.<br />
 As the images lacked sharp features, using dilation filters was helpful
and thus turned out to perform better than VGG16 Pre-trained model for
this task.<br />

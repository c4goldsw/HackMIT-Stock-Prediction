# HackMIT-Stock-Prediction

##Inspiration
We have an interest in neural networks and have heard of recurrent neural networks being used for stock price prediction. We then thought that we could try to augment past market data used to train stock prediction RNNs with sentiment data on those stocks.

##What it does
It forecasts stock prices using a time series of stock data that is labelled with sentiments on those stocks at a given time point.

##How we built it
We built our neural network using Keras, and visualized data outputed from our model on a node.js webapp. We first tried a variety of different architectures for the neural networks but we decided to do a simple LSTM - Dense setup for simplicity. Deeper networks prover longer to train and harder to find suitable hyperparamaters (i.e. layer dimensions). It was run both locally on CPU and on AWS on GPU, but due to the small size of the data and network

##Challenges we ran into
Quite a few - ranging from setting up our node.js server, obtaining sentiment data, training our neural net - quite a range of things, mainly pertaining to using data.

##Used Data:
For our stock prices, we used Hourly Nasdaq market data for Facebook and Apple. For our sentiment data, we used sentiment data on theses stocks gathered and kindly provided by (late on a Saturday night) Pierce Crosby of StockTwits

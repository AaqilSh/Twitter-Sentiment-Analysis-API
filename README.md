# Twitter Sentiment Analysis Application

 This is a simple sentiment analysis application

 The API supports only Http POST request.
Example 

>`curl -X POST -F 'sentence=Hello world' 127.0.0.1/api/`

If the request is valid, the server will return either negative or positive based on the input.

If the request is not valid, the server will return HTTP_400_BAD_REQUEST response.

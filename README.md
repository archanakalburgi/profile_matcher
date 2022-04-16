## How to run 

Provide path to the desired resume, assign the path to the 'resume_path' variable. 

Initialize an object of ProfileMatcher and run the last cell of the script named 'ProfileMatcher.ipynb'

This will generate 5 excel sheets with job descriptions ranked based on the uploaded resume. These are job rankings, where the text is tranformed into the numeric form using the following 5 technique  

1. Countvectorizer 
2. Term Frequency 
3. Term frequency inverse document frequency 
4. Pretrained embeddings 
5. Custom trained trained embeddings 

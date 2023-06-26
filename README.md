# Simple Movie and series recommendation model
This simple model mimics a movie recommendation model similiar to Netflix. I created a list of 6-7 movies and shows along with their short descriptions. A model sentence is then created with a novie and its description. it is assumped that this model sentence represents the content recently watched by the user. i used spaCy and its english language model to analyse the similiar words between the model sentence and the sentences in the list. Thus, recommending the movies most similiar to the one recently watched by the user.

# Packages and Installation
I used spaCy in VS code for this project. spaCy can be installed from the link https://spacy.io/usage. The version suiltable for each OS can be installed from here.
For my project I used the following commands to install spaCy and its english language model, 'en_core_web_sm'.

pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm

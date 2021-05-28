# Big-Scale-Analytics-2021-Tesla <img src="https://user-images.githubusercontent.com/61697398/114187790-b0553000-9948-11eb-8cda-df0721cac5bc.png" width="35" height="30">
# Text Analytics : Prediction Of French Sentences' CEFR Level


Tesla Group's repository for the course project "Big Scale Analytics 2021" (University of Lausanne)




This projects aims to predict the CEFR level of a sentence in a foreign language (here French) based on machine learning techniques.
## Group member 🧍🧍🧍
- Adrian Sestan
- Igor Ranisavljevic
- Hugo Macedo Candido

## The Idea (project description) 📜
To improve one’s skills in a new foreign language, it is important to read texts in that language. These text have to be at the reader’s language level. However, it is difficult to find texts that are close to someone’s knowledge level (A1 to C2). The idea is to build a model for English speakers that predicts the difficulty of a French written text. This can be then used, e.g., in a recommendation system, to recommend texts (for example, recent news articles) that are appropriate for someone’s language level. If someone is at A1 French level, it is inappropriate to present a text at B2 level, as she won’t be able to understand it. Ideally, a text should have many known words and may have a few words that are unknown so that the person can improve.

In order to learn more about the subject, we consulted various research sources including the same objectives such as :
- Word lists in Reference Level Descriptions of CEFR (Common European Framework of Reference for Languages): https://euralex.org/wp-content/themes/euralex/proceedings/Euralex%202012/pp328-335%20Marello.pdf
- Duolingo's blog on the use of AI for adapting learning content based on CEFR level: https://blog.duolingo.com/the-duolingo-cefr-checker-an-ai-tool-for-adapting-learning-content/
- Duolingo's CEFR checker (what we're aiming to, but in french): https://cefr.duolingo.com/
- English vocabulary profile (the english equivalent of what we need to build our model): https://www.englishprofile.org/wordlists/evp
- Machine Learning for learner English, April 2020, International Journal of Learner Corpus Research: https://www.researchgate.net/publication/339736712_Machine_learning_for_learner_English_A_plea_for_creating_learner_data_challenges
- Rule-based and machine learning approaches for second language sentence-level readability, June 2014,  9th Workshop on Innovative Use of NLP for Building Educational Applications: https://www.researchgate.net/publication/263057662_Rule-based_and_machine_learning_approaches_for_second_language_sentence-level_readability

## Milestones & Goals 🎯
The project is separated in three main milestones :
1. Thinking how to model the problem and gathering data (French texts, sentences, news articles etc.) and labelling them with the relevant level
2. Building a model that predicts the difficulty/level of a new text
3. Evaluating how good the model is

The final goal is to provide an API with an UI wich returns the level of a given french sentence.

## Methodology :mag:

- Gather existing informations and scientific articles on the subject :white_check_mark:
- Build and labelize a dataset containing french sentences :white_check_mark:
  - Upload our data on AutoML (Google Cloud) :white_check_mark:
  - Train first model (classification model) :white_check_mark:
  - Evaluate first model :white_check_mark:
  - Test first model :white_check_mark:
  - Deal with cognates ⏳
- Create a web service (with interface) with flask and AppEngine :white_check_mark:
- Connect the web service to our API :white_check_mark:
- Improve our model
- Improve the UI

## Data 📊
The data used for this project comes from two different sources. The first data set was created by our team based on relevant literary sources. The second, larger than the first, was imposed on us by our teachers. Each dataset contains two columns, the first one contains the sentences to be analysed and the second one represents the label of each sentence (A1, A2, B1, B2, C1, C2).

Exemple :

| Sentences | Label |
| :---         |          ---: |
| Bonjour, je m'appelle Lucia. | A1 |

### First data set

In order to create our dataset, we had to find specific ressources that are a reference in the labeling of french language. We have used several sources such as grammar exercises, french language learning websites and sources provided by teachers. After collecting **1224 sentences**, we objectively assessed their levels under different selection criteria like words, verbs, cognats, grammar and expressions difficulties.

### Number of sentences per level :
- A1 : 221
- A2 : 209
- B1 : 192
- B2 : 203
- C1 : 197
- C2 : 202

Website sources:
- French Reading Practice Bilingual reader articles: https://french.kwiziq.com/learn/reading 
- Lingua: https://lingua.com/french/reading/
- Podcast français facile (niveau B2):  https://www.podcastfrancaisfacile.com/niveau-delf-b2
- LaPhilo (EXEMPLE DE DISSERTATION EN PHILOSOPHIE): https://la-philosophie.com/exemple-dissertation-philosophique 

Book: 
- ABC-TCF Test de Connaissance du Français pour le Québec, Bruno Mègre & Sébastien Portelli, september 2014.

### Second data set

## Tools 🛠
Different tools are used for this project :
- Google Colab Python Notebooks
- Google Cloud Services

## Models

## Preprocessing

## Project results and iteration

### Iteration
#### Google Cloud AutoML
#### First Iteration

As a first try using the google cloud autoML, we labbeled the sentences according to their respective level in french. The tool proposed by google calculated automatically using a classification method. 

With a threshold set at 0.5, we have the following results:

- The precision is of 61.68%
- The recall is of 54.55%

##### Per class score

| Label | Precision | Recall |
| :---         |     :---:      |          ---: |
| A1   | 68%     | 72.27%    |
| A2     | 55.56%       | 50%      |
| B1   | 66.67%     | 42.11%    |
| B2     | 58.82%       | 50%      |
| C1  | 62.50%     | 50%    |
| C2    | 57.89%       | 50%      |

##### Confusion matrix
<img src="https://user-images.githubusercontent.com/71492453/116902770-d4501c80-ac3b-11eb-980a-576ee38282f0.PNG" width="330" height="300">


#### Second iteration

As the first results were not satisfying, we decided to include the cognats in our second iteration.
We've worked on Google Colab to pre-process our data, tokenize the sentences, and put the number and whihch cognates each sentence has as a feature.

By using the Google autoML, we reached the following results :

- The precision is of 61.54%
- The recall is of 46.28%

As a conclusion to this iteration, the way we uploaded the cognates into the dataset resulted in Google autoML not capable of recognizing the weight of the cognates.

#### Third iteration

## CamemBERT - Jupyter Model

## Repository organisation 🗂
Here's how the repo is organized :
- Data : you'll find [here](https://docs.google.com/spreadsheets/d/1oQGKQZLj6JRbgY-ZQLfClUsq-AHA8LIegtSZvxw6s6A/edit#gid=1203710396) all of the 1224 sentences that composes our  data for the project
- Code : the python notebooks containing our code
- ABC-TCF book : our [litterature](https://github.com/TetraFaal/Big-Scale-Analytics-2021-Tesla/tree/main/ABC-TCF%20book) used for the french knowledge test for Quebec.

## Web service

You can try the model that was built with Google AutoML by following [this link](https://massive-incline-305713.appspot.com/) to our web app.

The project is iterative, this repository is meant to evolve regulary





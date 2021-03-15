# Big-Scale-Analytics-2021-Tesla
# Text Analytics : Prediction Of French Sentences' CEFR Level
Tesla Group's repository for the course project "Big Scale Analytics 2021" (University of Lausanne)

This projects aims to predict the CEFR level of a sentence in a foreign language (here French) based on machine learning techniques.

## The Idea (project description) 📜
To improve one’s skills in a new foreign language, it is important to read texts in that language. These text have to be at the reader’s language level. However, it is difficult to find texts that are close to someone’s knowledge level (A1 to C2). The idea is to build a model for English speakers that predicts the difficulty of a French written text. This can be then used, e.g., in a recommendation system, to recommend texts (for example, recent news articles) that are appropriate for someone’s language level. If someone is at A1 French level, it is inappropriate to present a text at B2 level, as she won’t be able to understand it. Ideally, a text should have many known words and may have a few words that are unknown so that the person can improve.

## Milestones & Goals 🎯
The project is separated in three main milestones :
1. Thinking how to model the problem and gathering data (French texts, sentences, news articles etc.) and labelling them with the relevant level
2. Building a model that predicts the difficulty/level of a new text
3. Evaluating how good the model is

The final goal is to provide an API with an UI wich returns the level of a given french sentence.

## Tools 🛠
Different tools are used for this project :
- Google Colab Python Notebooks
- Google Cloud Services

## Repository organisation 🗂
Here's how the repo is organized :
- Data : you'll find [here](https://docs.google.com/spreadsheets/d/1oQGKQZLj6JRbgY-ZQLfClUsq-AHA8LIegtSZvxw6s6A/edit#gid=1203710396) all of the 1181 sentences that composes our  data for the project
- Code : the python notebooks containing our code
- Ressources : our [litterature](https://github.com/TetraFaal/Big-Scale-Analytics-2021-Tesla/tree/main/Ressources) review on the subject and usefull ressources

The project is iterative, this repository is meant to evolve regulary 

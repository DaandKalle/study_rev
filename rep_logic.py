"""
This module contains the logic for spaced repetition.
Author: Hud
"""

import numpy as np
import datetime as dt

def rep_date(score : int)-> str:
    """
    THis function takes an input of type int(score) from gpt module and then uses it to provide a date when the student has to revise his stuff.This returns date  as a str.  
    n_days is the number of days that the code decides are to be added to need to revise
    a weight check is in the same function that checks the weight before assigning the date
    """
    max_weight =  5
    if (score < 50):
        n_days = 1
    elif (50 < score < 80):
        n_days = 3
    elif(score > 80):
        n_days = 5


    revision_date = (dt.date.today() + dt.timedelta(days=n_days)).isoformat()

    
    #revision_date = dt.date.today() + dt.timedelta(days  = n_days)
    #keeping this here to decide where to store this revision date outside the code.
    #add another function to find the numver of words in the text originally ot make sure that student is not overwhelmeed
    #
"""
{
  "score": 72,
  "review_gap_days": 3,
  "total_attempts_for_topic": 2,
  "avg_past_score_topic": 65.5,
  "quiz_type": "MCQ",
  "word_count": 1200,
  "answer_length": 35,
  "time_taken_sec": 90,
  "was_due_today": true,
  "day_of_week": "Tuesday",
  "label": 1  // `
}

will use this tabular data to trian xgboost and random forrest along with multivariate linear regeression
agar fursat mili to pygames se gamify karenge

""" 
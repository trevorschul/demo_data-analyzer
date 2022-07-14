import pandas
import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()
    # print(race_count)

    # What is the average age of men?
    men_only = df.loc[df["sex"] == "Male"]
    average_age_men = men_only["age"].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df.education.value_counts().Bachelors / (df.shape[0]) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")]
    lower_education = df[(df["education"] != "Bachelors") | (df["education"] != "Masters") | (df["education"] != "Doctorate")]

    # percentage with salary >50K
    higher_education_rich = higher_education.salary.value_counts()[">50K"] / (df.shape[0]) * 100
    lower_education_rich = lower_education.salary.value_counts()[">50K"] / (df.shape[0]) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df1 = df.loc[df["hours-per-week"] == min_work_hours]
    num_min_workers = df1.salary.value_counts()[">50K"]

    rich_percentage = num_min_workers / (df1.shape[0]) * 100

    # What country has the highest percentage of people that earn >50K?
    countries = df.loc[df["salary"] == "<50K"]
    final = countries.loc[countries["native_country"].]
    # print(thing)
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# SkyScraper
An ETL pipeline for scraping Google Play reviews for [Sky: Children of the Light](https://play.google.com/store/apps/details?id=com.tgc.sky.android&hl=en_CA&gl=US). I used Airflow for task scheduling, extracted the data using the [google-play-scraper](https://pypi.org/project/google-play-scraper/) library, transformed it with pandas and loaded it into a local MySQL database. 
<br><br>

**Review Table**
|     Column      |                 Description                  |
|       :-:       |                     :-:                      |
|    review_id    | Google Play review ID                        |
|    user_name    | Google username                              |
|     content     | Google Play review                           |
|     rating      | rating (1 - 5)                               |
| thumbs_up_count | Number of users who found the review helpful |
|     version     | Game version                                 |
|  last_modified  | Date on which the review was last modified   |

**Folder Structure**
```
  |--- skyscraper
  |    |-- modules
  |    |   |-- ... 
  |    |-- skyscraper.py (Airflow DAG definition file)
  |
  |--- sql
       |-- create_sky_database.sql 
```


References\
*Sky* [Game]. (2020). Santa Monica (California): thatgamecompany.

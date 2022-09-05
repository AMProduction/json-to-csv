# Data Engineer coding challenge

## Some data

The Aspire Global platform generates events that are sent to our API for us to
understand how our users behave. In this exercise we are interested in a
particular type of event, the `bets`.

Here is an example of such an event, in JSON:

```json
{
  "bet_id": 28092914447,
  "bet_dt": "2021-10-04 12:02:26",
  "player_code": "C3EC54F273CE90DF",
  "game_id": 1681,
  "real_debit_amount": "0.00",
  "real_credit_amount": "0.20",
  "bonus_debit_amount": "0.00",
  "bonus_credit_amount": "0.00",
  "bet_channel_code": "C",
  "bet_status_code": "A",
  "player_jackpot_contribution_amount": "0.00000",
  "player_jackpot_win_amount": "0.00",
  "bet_action_id": null,
  "bet_transaction_type_id": 2,
  "last_event_dt": null,
  "game_odds": null,
  "fee_amount": "0.00",
  "operating_company_id": 1,
  "partner_company_id": 133,
  "brand_id": null
}
```
Along with these events we also receive the players and games events which are relevant to this task. You can see samples below:

Players
```json
{
  "partner_company_id": 133,
  "player_code": "73CD0938C6E2DB51",
  "language_code": "ENG",
  "suffix": "",
  "gender": "M",
  "birth_city_name": "",
  "birth_country_code": "  ",
  "city_name": "",
  "nationality_country_code": null,
  "citizenship_country_code": null,
  "state": "  ",
  "post_code": "",
  "country_code": "FI",
  "player_ccy_code": "EUR",
  "registration_dt": null,
  "kyc_id_verification_dt": null
}
```

Games
```json
{
  "game_id": 1,
  "game_name": "Fast Hands",
  "game_category_code": "C",
  "game_type_code": "FastHands"
}
```


## The challenge

Your task is to process the input raw data and generate an output that can be
used to analyze some bets metrics. In particular, with the output you will 
generate we want to be able to measure:
 * the number of bets placed per player
 * the amounts spent per player bonus and real
 * the most played games
 * the number of distinct games played per player
 

On top of that:

 * we want to be able to analyze data at daily, weekly, monthly and yearly
   granularity.
 * we want to be able to slice the data by several dimensions:
   - Player country
   - Game type code
   - Currency
   - activity type and collection
 * we are not interested in being able to analyze every single bets.


You will find in this repository 3 files in
[JSON Lines format](https://jsonlines.org/) that are samples of the 3 datasets
described above.

## Expectations

We expect you to write code that: loads the datasets; transforms them as
necessary; produces one or several datasets that can be used to perform further
analysis.

The code should be written in Python but you are free to use the libraries/frameworks that you
prefer.

You can generate your output in the format you find most appropriate and can
assume that we have access to modern querying/processing tools for consuming
them (data warehouse, query engine, database , ...).

We expect you to:

 * deliver the test within time allotted. 
 * write a solution that we can easily execute for evaluation
 * include a Readme that describes your approach, and the assumptions you made
   (if any)
 * write code with the same care you would use in your job
 * include some level of automated testing
 * explain in the Readme how you would scale your solution to handle millions
   of daily bets, players and games

We will evaluate all aspects of your submission, in particular code quality, so avoid spending all your time on just the perfect data processing approach. If your submission meets our expectations you will have time to discuss improvements with us in the following interviews.

If you have any doubt regarding any part of this challenge, do no hesitate to
email us with your questions.

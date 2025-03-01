-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find crime scene descriptions
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';

--See the interviews
SELECT * FROM interviews WHERE transcript LIKE '%bakery%';

-- Know the name of the suspected people;
SELECT * FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25;

--Second withness ATM
SELECT * FROM atm_transactions
WHERE atm_location = 'Leggett Street'
AND transaction_type = 'withdraw' AND year = 2023 AND month = 07 AND day = 28;

--Know the name of the ATM suspictious

sqlite> SELECT * FROM atm_transactions
   ...> JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number
   ...> JOIN people ON people.id = bank_accounts.person_id
   ...> WHERE atm_location = 'Leggett Street'
   ...> AND transaction_type = 'withdraw' AND year = 2023 AND month = 07 AND day = 28;

--Know the caller 2nd witness who made the call

SELECT * FROM phone_calls
JOIN people ON phone_calls.caller = people.phone_number
WHERE year = 2023 AND month = 7 AND DAY = 28 AND duration < 60;

--Know Fiftyville Airport
SELECT * FROM airports WHERE city = 'Fiftyville';

-- Know the first fligh from Fiftyville

SELECT * FROM flights WHERE
origin_airport_id = 8 AND year = 2023 AND month = 7 AND DAY = 29
ORDER BY hour, minute;

--Know the destination aiport ant its name
SELECT * FROM airports WHERE id = 4;

--Looking for the people's name which complies with the witnesses 1, 2 and 3

sqlite> SELECT people.name
FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE bakery_security_logs.year = 2023
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute BETWEEN 15 AND 25
AND atm_transactions.atm_location = 'Leggett Street'
AND atm_transactions.transaction_type = 'withdraw'
AND atm_transactions.year = 2023
AND atm_transactions.month = 07
AND atm_transactions.day = 28
AND phone_calls.year = 2023
AND phone_calls.month = 7
AND phone_calls.day = 28
AND phone_calls.duration < 60;

--Who was on flight Bruce or Diana?

SELECT * FROM people
JOIN passengers ON passengers.passport_number = passengers.passport_number
WHERE flight_id = 36
AND people.name IN ('Bruce','Diana');

--Who called Bruce?

SELECT * FROM phone_calls
JOIN people ON people.phone_number = phone_calls.receiver
WHERE year = 2023
AND month = 7
AND day = 28
AND duration < 60
AND caller = (SELECT phone_number FROM people WHERE name = 'Bruce');

# Crypto Core Take Home Assignment

## Getting started

#### Build Image

```
docker build . -t gemini
```

#### Run Container

```
docker run gemini
```

## My Approach

To tackle this challenge, I approached by dismantling the problem into smaller, manageable pieces. I focused on one aspect at a time, starting with exploring the Public API.

#### API Navigation

Then, I navigated through the API to identify the essential endpoints for fetching the required data. This involved discovering the endpoints for retrieving traded symbols and their corresponding prices.

#### Data Population

Once I had access to the necessary endpoints, I utilized a dictionary to populate candle data. This data structure allowed for efficient one-to-one matching, making it ideal for storing and manipulating the data.

#### Data Cleaning and Processing

After populating the data, I ensured it was cleaned and processed accurately. This step was crucial in preparing the data for analysis. I used the closing price for every symbol.

#### Deviation Calculation and Alert Generation

Finally, I calculated the deviation and created alerts based on the assessment criteria. This involved comparing the calculated deviation against a threshold value and generating alerts accordingly.

By breaking down the problem into smaller tasks and addressing each one systematically, I was able to effectively solve the challenge.

## Issues faced with implementation

One of the main obstacles I faced was obtaining the candle data in accordance with the assessment criteria. Specifically, I needed to retrieve hourly data for the past 24 hours. However, when I used the 1-hour time interval, I unexpectedly received 2 months' worth of data. To resolve this issue, I opted for a more granular approach by switching to a 1-minute time interval. This allowed me to precisely control the data range and fetch only the required 24 hours' worth of data.

## Improvement

The code can be made more efficient. For instance, in the main function, prices are fetched for each symbol, resulting in a higher time complexity.

## Interesting checks

To take monitoring to the next level, I'd suggest adding team-specific tags for seamless integration with popular paging apps like PagerDuty and xMatters, as well as Slack channels. This enhancement enables alerts to trigger notifications on Slack, pages, and even automatically create incidents as needed, ensuring teams stay informed and responsive in real-time.

## Time

- Took an 1.5 - 2 hours to implement the code
- Took another 20 - 30 min to refine the code

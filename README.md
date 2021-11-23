# Election Audit Analysis

![election](https://user-images.githubusercontent.com/36451701/143140009-934f0aa7-5d74-4020-a19d-8f47b15af81e.png)

## Project Overview:
*A Colorado Board of Elections would like to have the following tasks completed as part of an election audit for their congressional election.*

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes for each candidate. 
4. Calculate the percentage of votes for each candidate.
5. Determine the winner of the election based on the popular vote.

In addition to the election audit, they want to know if there is a way to automate the process so that it can be used for other districts and local elections. 

### Project Resources:
- Data Source: election_results.csv
- Software: Python 3.9.4, Visual Studio Code, 1.56.0

## Project Results:
The analysis of the election shows that:
- There were 369,711 votes cast in the congressional election.

- The candidates were:
    - Charles Casper Stockham 
    - Diana DeGette
    - Raymon Anthony Doane

- The candidate results were:
    - Charles Caseper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane recieved 3.1% and 11,606 number of votes. 

- The winner of the election was:
    - Diana DeGette who received 73.8% of the vote and 272,892 number of votes. 

![election_results](https://user-images.githubusercontent.com/36451701/117600797-a4f94e00-b11a-11eb-9f16-4c604b4f9254.png)

## Project Summary:
- The voter turnout and count for each county was:
    - Jefferson County with 10.5% of the vote and 38,855 total votes.
    - Denver County with 82.8% of the vote and 306,055 total votes.
    - Arapahoe County with 6.7% of the vote and 24,801 total votes. 

*The Colorado Board of Elections also requested some additional data about voting county details for the election audit.*

1. Provide a breakdown of voter turnout for each county. 
2. Calculate the percentage of votes from each county out of the total count.
3. Determine the county with the highest turnout.

## Election-Audit Summary
The election-audit script created worked extremely well for me.  The script is automated and will allow any congressional district, senatorial district, or any local election authority to get a quick election audit once the data for the elections is made available. 

# Investigating Traffic Violation Patterns in Montgomery County, MD
Flatiron Mod 3 Project by Manisha, Tim, and Jon

## Project Overview:

The purpose of this project was to investigate patterns in traffic violations issued in Montgomery County, MD from January 1, 2012 through June 4, 2019. In recent years, a growing number of police departments across the country have been making an effort to make their data on police-citizen interactions publicly available in an effort to help build trust, transparency and communication between police and community members. 

The full database, which is made available to the public through the [Montgomery County Government website](https://data.montgomerycountymd.gov/Public-Safety/Traffic-Violations/4mse-ku6q/data), had over 1.5 million records of traffic violations at the time we conducted our analysis. Each record in the database contains the following information: basic demographic information on the driver, information about the driver's vehicle, a description of the reported offense, outcome of the interaction (e.g., whether a citation was issued), and the date, time, and location the violation occurred.  

## Central Questions That Guided the Current Investigation:

* Are Black and Hispanic drivers being issued citations at equal rates for failing to display a registration card?

* Are White and Black drivers being issued citations at equal rates?

* When comparing different racial groups (Black vs. White), is there a difference in the rate at which male vs. female drivers in each of these groups are being issued citations? 

* Is car color related to car accidents?


## Hypothesis-Testing:

We tested four sets of hypotheses in order to investigate the above questions.  Each of the following statistical tests was conducted 1000 times on samples randomly drawn from the full database in order to minimize the potential for sampling bias, and increase the likelihood our findings are representative of the general traffic violation patterns found in Montgomery County.

#### H0) For drivers pulled over where the description of offense is "failure to display registration card upon demand," there is no difference in the proportion of hispanic and black drivers who are given only a warning.

Out of 1000 repeated tests, the null hypothesis was rejected 1000 times (100.0%) at an alpha level of 0.05.

#### H0) For drivers pulled over, there is no difference in the proportion of White vs. Black drivers who are given a citation.

Out of 1000 repeated tests, the null hypothesis was rejected 70 times (7.0%) at an alpha level of 0.05.

#### H0) For drivers pulled over, there is no difference by race and gender in the proportional rate at which they are given a citation.

* comparing Black male vs. White male drivers: out of 1000 repeated tests, the null hypothesis was rejected 557 times (55.7%) at an alpha level of 0.05.

* comparing White female vs. Black female drivers: Out of 1000 repeated tests, the null hypothesis was rejected 232 times (23.2%) at an alpha level of 0.05.

* comparing Black male vs. Black female drivers:  Out of 1000 repeated tests, the null hypothesis was rejected 52 times (5.2%) at an alpha level of 0.05.

* comparing White male vs. White female drivers: Out of 1000 repeated tests, the null hypothesis was rejected 948 times (94.8%) at an alpha level of 0.05.
 
#### H0) The color of a car is not related to that car being in an accident.

The result of a chi-square test indicated that car color and accident rate are not independent of one another.

## Summary of Findings:

While our analyses suggest that there may be some some racial/ethnic and gender differences in the rate in which drivers have been issued citations for traffic violations in Montgomery County in recent years, this is a correlational dataset and we need to be cautious about making claims of causation with the current findings. 

## Further Resources:

[Police Data Initiative](https://www.policedatainitiative.org):(includes a database of police departments that provide public access datasets)

[National Initiative for Building Community Trust and Justice](https://www.policedatainitiative.org/datasets/): a project to improve relationships and increase trust between communities and the criminal justice system 



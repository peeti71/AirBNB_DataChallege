# AirBNB_DataChallege

<img src="image/statueofl.jpg" width=900 height=300/>

<h1 style="color:black;">Airbnb Data Challenge</h1>

  * By: Peeti Sriwongsanguan
 
 <hr style="height:2pt">
 
 
 
<h2 style="color:black;">Problem Statement</h2>

 
The task is to provide an analysis on which zip codes are the most profitable to invest in within New York 
City for two bedroom types. Two datasets, Airbnb and Zillow, are provided for this challenge. 

 * <b>Airbnb</b>: Data contains rental history from 1996-04 to 2019-09 which contains 106 features and 48,895 records providing rental information.
 * <b>Zillow</b>: Data contains monthly information of the property cost within New York City for the past 20 years which contains zip code. The data contains 8946 records and 262 columns. 


<h2 style="color:black;">Data Challenges & Findings</h2>
<p>
For Airbnb, There are too many unrelated and unnecessary features and I found many missing values, incorrect zip code format, 
properties not listed in New York.


Zillow data, monthly property costs are in columns which are not a friendly structure for an analysis. 
</p>
<h2 style="color:black;">Data Cleaning and Preparing Approaches</h2>
<p>
    
<b>Airbnb</b>
<ul>
<li><b>Missing Value</b>: I removed columns that have data less than 80% and filled zero in null values.</li>
<li><b>Remove unrelevant records</b>:</li>
<ul>
<li>I removed records where state is in CA and NJ.</li>
<li>Since our analysis is for 2 bedroom property, so I removed those records that were not 2 bedroom property.</li>
</ul>
<li><b>Fomat correction</b>:</li>
<ul>
<li>State: some records used state abbreviaton, some were written in full.</li>
<li>Zip Code: There are 5 records formatted ZIP+4 and 515 records missing zip code</li>
<li>Price: I remove `$` and , characters.</li>
</ul>
</ul>    

<b>Zillow</b>
<ul>
<li><b>Transpose transformation</b>: I reversed a YYYYMM property cost from column entity to row.</li> 
<li><b>Rename column header</b>: To make it more meaningful, I renamed RegionName to zip code.</li>
<li><b>Change Date to Date format</b></li>
</ul>

<h2 style="color:black;">Packages Required</h2>

* <b>pandas</b>: It provides a fast and friendly way to work with dataframe.
* <b>matplotlib</b>: It provides an easy way to create a visualization.
* <b>bokeh</b>: It is for animated and interactive visualzations.
* <b>re</b>: Regular expression enables me have a faster way to clean data and correct data format.
* <b>numpy</b>: It is the core library for scientific computing.
</p>

<h1 style="color:black;">Airbnb May Be More Lucrative Than Traditional Renting</h1>

<p>

<b>New York City</b> has been one of the hottest markets for Airbnb, with over 50,000 listings as of July 2019.

A solidly-booked Airbnb rental may be more profitable than renting the same property to a long-term single tenant. 
That’s because you’re usually able to charge more on a nightly basis.In New York City, for example, the average apartment
rents for about <b>`$4000`</b> per month. That is <b>`$48,000`</b> gross income if the tenant signed a 12-month lease. 


What if you went with the Airbnb theory and invest some properties? According to the given AirBnB dataset, 
the average daily rate for an Airbnb rental in is about `$290` and units are occupied an average of 273 days
out of the year (about 75%). If you rented out your Airbnb for <span>`$290`</span> per night for a total 273 nights per year, 
it’s possible to rake in about <b>`$79,000`</b> in gross revenue from the rental. <b>That’s `$31,000` or 65% more than you would make through traditional renting.</b> 

</p>

<p>
One of the most beautiful things about Airbnb is the conceptualization and execution of a free market. 
Airbnb reservation prices are often much lower than the local rates that a traditional hotel or motel 
demands to keep its books balanced. Often tourists or short-term visitors want to escape from the high 
rates charged by the hotels in the city.


<b>That's why Airbnb is so popular in demand and attracts tourists from all over the world</b>


<i>And the big question is where to invest? How much money you want to put it in? What is the ROI?</i>
</p>


<h1 style="color:red;">Insight</h1>
<p>

From my findings, I found Top 3 of the zip codes in New York City that are most profitable for rental. All three of them have an average of `$300` and higher a night. 
* <b>10036</b>: <b>Average of `$367` a night</b>
* <b>10003</b>: <b>Average of `$361` a night</b>
* <b>10011</b>: <b>Average of `$353` a night</b>

</p>




![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Guided Project: Working with Web Data

## Overview

The goal of this project is for you to practice what you have learned in the APIs and Web Scraping chapter of this program. For this project, you will choose both an API to obtain data from and a web page to scrape. For the API portion of the project will need to make calls to your chosen API, successfully obtain a response, request data, convert it into a Pandas data frame, and export it as a CSV file. For the web scraping portion of the project, you will need to scrape the HTML from your chosen page, parse the HTML to extract the necessary information, and either save the results to a text (txt) file if it is text or into a CSV file if it is tabular data.

**You will be working individually for this project**, but we'll be guiding you along the process and helping you as you go. Show us what you've got!

---

## Technical Requirements

The technical requirements for this project are as follows:

* You must obtain data from an API using Python.
* You must scrape and clean HTML from a web page using Python.
* The results should be two files - one containing the tabular results of your API request and the other containing the results of your web page scrape.
* Your code should be saved in a Jupyter Notebook and your results should be saved in a folder named output.
* You should include a README.md file that describes the steps you took and your thought process for obtaining data from the API and web page.

## Necessary Deliverables

The following deliverables should be pushed to your Github repo for this chapter.

* **A Jupyter Notebook (.ipynb) file** that contains the code used to work with your API and scrape your web page.
* **An output folder** containing the outputs of your API and scraping efforts.
* **A ``README.md`` file** containing a detailed explanation of your approach and code for retrieving data from the API and scraping the web page as well as your results, obstacles encountered, and lessons learned.

## Suggested Ways to Get Started

* **Find an API to work with** - a great place to start looking would be [API List](https://apilist.fun/) and [Public APIs](https://github.com/toddmotto/public-apis). If you need authorization for your chosen API, make sure to give yourself enough time for the service to review and accept your application. Have a couple back-up APIs chosen just in case!
* **Find a web page to scrape** and determine the content you would like to scrape from it - blogs and news sites are typically good candidates for scraping text content, and [Wikipedia](https://www.wikipedia.org/) is usually a good source for HTML tables (search for "list of...").
* **Break the project down into different steps** - note the steps covered in the API and web scraping lessons, try to follow them, and make adjustments as you encounter the obstacles that are inevitable due to all APIs and web pages being different.
* **Use the tools in your tool kit** - your knowledge of intermediate Python as well as some of the things you've learned in previous chapters. This is a great way to start tying everything you've learned together!
* **Work through the lessons in class** & ask questions when you need to! Think about adding relevant code to your project each night, instead of, you know... _procrastinating_.
* **Commit early, commit often**, don’t be afraid of doing something incorrectly because you can always roll back to a previous version.
* **Consult documentation and resources provided** to better understand the tools you are using and how to accomplish what you want.

## Useful Resources

* [Requests Library Documentation: Quickstart](http://docs.python-requests.org/en/master/user/quickstart/)
* [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Stack Overflow Python Requests Questions](https://stackoverflow.com/questions/tagged/python-requests)
* [StackOverflow BeautifulSoup Questions](https://stackoverflow.com/questions/tagged/beautifulsoup)

## Project Feedback + Evaluation

* __Technical Requirements__: Did you deliver a project that met all the technical requirements? Given what the class has covered so far, did you build something that was reasonably complex?

* __Creativity__: Did you add a personal spin or creative element into your project submission? Did you incorporate domain knowledge or unique perspective into your analysis.

* __Code Quality__: Did you follow code style guidance and best practices covered in class?

* __Total__: Your instructors will give you a total score on your project between:

    **Score**|**Expectations**
    -----|-----
    0|Does not meet expectations
    1|Meets expectactions, good job!
    2|Exceeds expectations, you wonderful creature, you!

This will be useful as an overall gauge of whether you met the project goals, but __the more important scores are described in the specs above__, which can help you identify where to focus your efforts for the next project!

## Presentation Guideline and Criteria

### Format

* Presentation Time: 6 minutes
* Q & A: 3 minutes
* **Total Time:** 9 minutes

### Attire

* DRESS TO IMPRESS: [Smart casual](https://en.wikipedia.org/wiki/Smart_casual) would be great

### Outputs

* A presentation in [slides.com](https://slides.com/)
* A demo deployed on GitHub Pages
* The presentation and demo will be executed on a class computer (instead of your own)
* Get ready to explain some of your code in GitHub

### Things you might want to talk about

* Short presentation of yourself:
	* Who are you?
	* A hobby you have.
  * __Note: we are getting you ready for final presentation!__
* Elevator pitch:
  * The API and web page your chose.
  * Why did you chose that API and web page?
  * The most important thing you learned.
* One technical challenge you faced:
  * Explain the challenge.
  * Explain how and what you did to overcome it.
  * Show and explain code snippets in your presentation slides.
* Git:
  * Display an screenshot of your GitHub graphs to show your commit frequency and how much work you did.
* API Walkthrough:
  * Walk the audience through the API you chose, the type of data you decided to obtain from it, and how you went about calling the API, obtaining that data, and structuring it.
* Web Scraping Walkthrough:
  * Walk the audience through the web page you chose, the type of data you decided to obtain from it, and how you went about scraping the page, parsing the HTML, and cleaning the data.
* One important mistake you made:
  * Did you call the API incorrectly? Did you make some errors while scraping the web page?
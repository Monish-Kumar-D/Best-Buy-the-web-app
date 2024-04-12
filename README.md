# Best Buy, The Online Store
#### Video Demo:  [video link](https://youtu.be/79Ldvw7ME5g)
#### Description: Best buy is a web based application which is a Shopping site which is used to buy the products that the seller offers to the sell. This web application is developed using python,javascript,sql,html,css and flask with jinja.

## Introduction:

This is a web based application which uses python and javascript for programming with sql database (sqlite3),Markup Languages(HTML,CSS) and Flask with jinja.

This website helps the user to login, select and buy their items among the vast amount of products that the seller offers. Since it is a web application, multiple images from online been used to improve the user experience.Some of the css been taken from popular library like Bootstrap.

## Attributes used to construct this web application includes:
### Files used:
* A primary python file (app.py) which runs the backend of the web application.
* Another python file (helpers.py) which helps the primary python file for some of the functions.
* A database file (shop.db) which has the required data for the web application
* Two text files coupon.txt, feedback.txt which were used for storing information regarding coupons and feedback respectively.
* A template which has 12 html files including layout.html which has the layout of the web application and so on...
* A static directory which has all the images that has been used to develop the images.
* A css file (style.css) which has most of the basic css for the web application.

### Languages and things used to build
* 1.Python handles the backend of the web application
* 2.Javascript handles some of the responsive performance
* 3.Hypertext Markup Language (HTML) which used for Structuring the web pages.
* 4.Cascading Style Sheets (CSS) to add style to a web page by dictating how a site is displayed on a browse
* 5.Structured Query Language(SQL) as the database used to Store, Extract, Process and Manipulate data.
* 6.Flask as Framework to develop this web application
* 7.Jinja as the template engine for web application.

## Structure of the program
* 1 . This website first ask for the user to login to their account to create the session id for the rest of the operations. If the user don't have the account, they'll be redirected to register and open their account.
* 2 . As soon as the user registered for the first time, hash for their password been generated and their account been added into the database and the index of the we app been displayed with the new session id.
* 3 .In index, The vast number of categories which been taken from the category table from the shop.db  been displayed as cards so that user experience will be good, then it gives the user the choice to pick their category.
* 4 . As soon as the users chooses their category. Then it will redirect the user with the products available in that particular category with their respective prices which was already been saved in the database. Then user been given chance to choose their choice of product that they want or else go to the index site if they clicked the wrong category.
* 5 . Once the user chooses their product, system will redirect them to a site which shows the information about that particular product. And then system asks the user for an input of how many does the users wants to buy.
* 6 . Once the user enters the input, Its been stored in the database to keep track of products that the user have bought. Then the user been redirected to page where the user been notified about what they added to the cart.
* 7 . Then user been asked to choose either they want to lookup for other categories and other products or to check their cart.
* 8 . If the user opts to seek for the other products, Then system will redirect the user to the index page of the application and the cycle repeats.
* 9 . If the user chooses the same product again, then the product will be updated with the total number of products that they want.
* 10 . If the user opts to check their cart, then the user will be redirected to the cart page which displays the products that the user bought and also the total amount that the user have to pay in order to buy products.The user will be asked for an input whether the user has any coupon code to get discount.
* 11 . If the user input for the coupon code is correct, then the user will be redirected and been notified that the code been redeemed, the final amount been displayed, as soon as the code matches, that particular code will be removed in order to stop the repeated usage of the same code.Else If coupon is incorrect, then the amount is unchanged and been notified that incorrect code.Else if the user never entered an input, Then the user been notified that coupon not entered and the amount unchanged.
* 12 . Then the user been asked to enter the input which equals to the amount that the user need to pay.If the user enters lesser than required, then the user will be again asked for the input by subtracting the values that they entered in the form from the total.Else if the user been correctly entered the total, then they will be redirected to the bill page which tabulates the products that the user bought which been stored in the database and been thanked and asked to logou and feedbackt.Else if the user entered the input more than the required amount. Then the user been redirected to the Bill page and also returns the user the excess and then asked to logout and feedback.
* 13 . If the user chooses to give a feedback, then the user been redirected to the feedback page and asked for the input. As soon as the user gives the feedback, it will be then added to text file which will be useful for the web host and the seller.
* 14 . As soon as the user pays for the products and logsout, The current data been reset for future shopping. And then the session been terminated and exits the user.
# >>>End of the program<<< #
## Highlights
* Basic value assigns, type convertions.
* The code uses basic interactive input functions.
* Usage of conditional statements.
* Loops(for/while).
* Calling functions and passing parameters to the function.
* Handling several Data Structes such as Lists, Dictionaries etc...
* Basic I/O handling.
* Installation and usage of several libraries.
* Handling multiple routes.
* Selecting,inserting,altering and dropping tables in sql database.
* Well developed Hypertext Transfer Protocol methods and its handling.
* Image handling.
* Session Creation.
* Fully structured Flask framework.
* Rendering multiple web pages.
* Usage of Jinja syntax."# Best-Buy-the-web-app" 

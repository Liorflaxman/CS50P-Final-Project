## Gringo Movie Night Assistant

# Personal information
Name: Lior Flaxman Spiro
GitHub username: Liorflaxman
EdX username: LF_2505_MFS1
City and country: London, UK
Date you have recorded the walkthough video: 16 February 2026

# Link to the walk through is here: https://youtu.be/hatPV1TN38g?si=gDM-IkkKLFFC84Ow

# Description
I chose to create a movie platform finder for my final project as i am currently on a gap year travelling South and Central America with 4 friends who, unlike me, have  watched all the industry classics . I wanted to make this project as practical as i could so that we can find ways to have movie nights without having the difficulties of searching 5 platforms in order to find which one streams the movie we want to watch, while also presenting the live URLs for easy access to the platforms and portraying the price for renting or buying the movie so we can have travel-budget friendly movie nights

This tool leverages the free version of the Watchmode API to provide instant access to streaming platforms, type of way to stream the film, price, and the URL to watch. The project can provide this details for any movie/series, based on a specific country.

This project is built around a Object oriiented programming (OOP) structure to ensure data is handled and validated in the Movie class before any external network requests are made. This ensures the project is efficient and only intereacts with the API using Validated data.

## Project Features:
* **Real time verification** - The project uses Class properties and setters to validate movie titles and 2 letter country codes as the user inputs the data
* **2 step API search** - User country and movie input triggers an initial API call to retrieve the Unique Watchmode film ID, which then queries streaming sources using the ID and country tags
* **Duplicate output filter** - Uses sets to filter out duplicate streaming services to ensure more readable and accessible output
* **Table format** - program uses tabulate grid features to present the data in row format so that data for each streaming service is isolated and presentable

## Design Choices
* **Movie Class** - I decided on a Class function instead of a series of single functions and dictionaries. This was so i could encapsulate the movie and country input validation in a hidden format using @property and @setters. The Class skeleton ensures that any incorrect formats are rejected before being passed onto the API. These formats include rejecting country codes without the APIs desired 2 character format, and also rejecting empty movie inputs.

* **Data transformation** - The JSON response returned by the API contains many fields for 10s of streaming services per movie. My logic specifically extracts 4 key values which i believe the user will care most about. These include the Streaming services name, The type of way to watch, The price and the URL. These were transformed into a list to become compatable with the tabulate library

* **API and error handling** - I used error handling in my Movie class to ensure invalid data is not passed onto the API. Additionally, i used the requests library alongside try, except data handling to catch error 400s and prevent API usage crashes.

## Challenges Overcome
* When testing various tabulate formats, i found that the program outputted the same streaming services 4/5 times, each output differentiated by small data peices such as the quality of the movie (HD/SD) or price etc. Seeing this made the output unreadable and unnavigatable which influenced me to use a set() and some duplicate erasing logic to ensure Amazon or Netflix only appear twice at most, differentiated by the type of way to stream it (rent, buy, etc.)

* When testing in early stages before API implementation, my error handling wasnt live since the user had to input both country and movie before receiving a system exit with a message. Because of this i for optional arguments in my initialisation to allow empty values (self, movie=None, etc...). This meant that i could create an empty object initially while adding the user input into the object in real time to go through error checking. I also changed my error output method from sys to Raising ValueErrors to allow for live output when a movie field is empty, or if the country tag overflows the character requirement. This improves the UX instead of crashing the program at the end.

## Future Implementations to Improve the Application
* **Live Currency conversion** - As my friends and I are travelling through Peru, Guatemala and Brazil, i want to look into an API which can handle live exchange rate currency conversion. This will ideally take the price to rent or buy the movie in $ and convert them into real, soles or any currency of the users input

* **Watchlist feature** - i want to explore features that can allow a user to input multiple movies at once, or import a watchlist they have of desired movies. I want this feature to also allow the user to save the urls onto their desire file for easy access later on in the day where wifi may be limited.

## How to use
1. **Clone the repository** and navigate to the project file
2. **Install the requirements.txt** - run pip install -r requirements.txt
3. **Setup a Watchmode API** - create a .env file and add WATCH_MODE_API=your_key_here
4. execute python project.py
5. **Follow the programs prompts** - enter a movie and a 2 character country code

# City Journeys

## Project Structure

```
.
├── config                  -> Config classes for Database, Static File CDN etc.
├── migrations              -> Database migrations
│   └── versions
├── public                  -> HTML files used for serving the webpage
├── src                     -> Source files
│   ├── controller          -> Classes which link Views and Models
│   ├── routes              -> URL routes
│   ├── views               -> Interfaces which present information to the user
│   ├── db.py               -> Classes to interact with Databases
│   ├── models.py           -> Database models (e.g. Cities, Countries)
│   └── router.py           -> Collecting all routes from `routes` folder
└── static                  -> Static ressources used for serving the webpage
    ├── icons
    │   └── filter_icons
    ├── images
    │   ├── cities
    │   ├── country_flags
    │   │   └── svg
    │   ├── images
    │   └── sights
    └── styles              -> CSS style sheets
```

## Features
- LP: City Gallery
    - Interactive Filter for City Gallery 
- City Page
    - Facts
    - Accomidations
    - Flights 
    - Sights
    - Rating
- Login and User Authenitification

## To-Do
- LP: City Gallery
    - [x] Create a Database model(s)
    - [x] Load data into Database table(s)
    - [x] Create a View to display images and city information
- Interactive Filter for City Gallery
    - [ ] Create REST API using FastAPI
    - [ ] Use REST API to construct CDN URL
- Optimize City Gallery
    - [ ] Load smaller images from CDN
    - [ ] Implement "infinite scroll"
- Create City Page
    - [ ] Create basic layout

- Webserver Security
    - [ ] HTTPs certificate
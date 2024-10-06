# City Journeys

## Project Structure

```
.
├── config                  -> 
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
- LP: Cities Gallery
- Login and User Authenitification


## To-Do
- LP: Cities Gallery
    - [ ] Create a Database model(s)
    - [ ] Load data into Database table(s)
    - [ ] Create a View to display images and city information


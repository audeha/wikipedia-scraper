# Wikipedia Scraper

Welcome to the Wikipedia Scraper, the NICE_TO_HAVE version!
 <pre>
        __________      ________________ _______ ______ ________________
|\     /\__   __| \    /\__   __(  ____ (  ____ (  __  \\__   __(  ___  )
| )   ( |  ) (  |  \  / /  ) (  | (    )| (    \| (  \  )  ) (  | (   ) |
| | _ | |  | |  |  (_/ /   | |  | (____)| (__   | |   ) |  | |  | (___) |
| |( )| |  | |  |   _ (    | |  |  _____|  __)  | |   | |  | |  |  ___  |
| || || |  | |  |  ( \ \   | |  | (     | (     | |   ) |  | |  | (   ) |
| () () ___) (__|  /  \ ___) (__| )     | (____/| (__/  ___) (__| )   ( |
(_____________________ _______________ _________________________|/     \|
      (  ____ (  ____ (  ____ (  ___  (  ____ (  ____ (  ____ )
      | (    \| (    \| (    )| (   ) | (    )| (    \| (    )|
      | (_____| |     | (____)| (___) | (____)| (__   | (____)|
      (_____  | |     |     __|  ___  |  _____|  __)  |     __)
            ) | |     | (\ (  | (   ) | (     | (     | (\ (
      /\____) | (____/| ) \ \_| )   ( | )     | (____/| ) \ \__
      \_______(_______|/   \__|/     \|/      (_______|/   \__/

 </pre>
  ascii from http://www.patorjk.com/software/taag/

## Description
This programs calls an API that gives a list of countries and a list of leaders for each country. </p>
Each leader is represented by an ID linked to a Wikipedia url.</p>
The programs reads the first paragraph of each leader and writes the output in a json file.

This version differs from the normal because it use a requests session to manage the cookie, instead or using functions to call and refresh the cookie.

## Installation
`git clone git@github.com:audeha/wikipedia-scraper.git`  </p>
`cd wikipedia-scraper`

## Usage
`pip install -r requirements.txt` </p>
`python3 main.py` </p>
The results are in "leaders_data.json" --> open with your browser</p>

## Visuals
![Alt Text](./Screenshot1.png)

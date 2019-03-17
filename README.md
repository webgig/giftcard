
# Gift Card Application

The application is a SPA. Frontend is done using React

In the project directory, you can run:

## `Running the app locally`

#### `python(3) manage.py runserver`

This should run the whole application including the frontend which is embeded in the django template. You can run the frontend separately. Instuctions below

Open [http://localhost:8000](http://localhost:8000) to view it in the browser.


## `Load Initial Data`

Users -> wallet/fixtures/users.json
Wallets -> wallet/fixtures/wallets.json
Cards ->  cards/fixtures/cards.json

A user can have a wallet 
A wallet can have many cards

#### `python(3) manage.py loaddata users`
#### `python(3) manage.py loaddata wallets`
#### `python(3) manage.py loaddata cards`

## `Testing`

#### `python(3) manage.py test`


## Running frontend separately in a development mode

In the project directory, you can run:

#### `npm start`
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

## Build the frontend
This outputs the html and compiled frontend in the build directory
### `npm run build` 

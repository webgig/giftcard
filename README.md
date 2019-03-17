
# Gift Card Application

This is a React based SPA.

In the project directory, you can run:

## Database Configuration & Migration

Create a mysql database named 'wallet' and update the config in ./prezzee/settings.py if required.

Run the following migration to create the schema
```
python manage.py migrate
```

## Load Initial Data

Users -> wallet/fixtures/users.json
Wallets -> wallet/fixtures/wallets.json
Cards ->  cards/fixtures/cards.json

A user can have a wallet 
A wallet can have many cards

```
python manage.py loaddata users
python manage.py loaddata wallets
python manage.py loaddata cards
```

## Running the app locally

```
python manage.py runserver
```

This should run the whole application including the frontend which is embeded in the django template. You can run the frontend separately. Instuctions below

Open [http://localhost:8000](http://localhost:8000) to view it in the browser.


## Testing

```
python manage.py test
```


## Running frontend separately in a development mode

In the project directory, you can run:

```
npm start
```
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

## Build the frontend
This outputs the html and compiled frontend in the build directory
```
npm run build
```

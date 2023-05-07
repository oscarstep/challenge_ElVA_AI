# Challenge - Oscar Rodríguez

For this challenge I followed the next steps:

## Create virtual environment

The first step was to create the virtual environment to install the necessary dependencies. Since I use Windows, I used the next to command to accomplish this:

```bash
python -m venv env
```
I added this virtual environment in the gitignore file.

## Install dependencies

I used the next dependencies:
- googlemaps - The most important one, to get the coordinates from an address
- python-dotenv - I used this one to get an environment variable from my .env file, which contains the google maps api key
- requests - This one is to consume the portlandmaps REST endpoint to get the neighborhood name from coordinates

After this, I created a requirements file to facilitate the installation for you to test the program.

## Development

In this step I started developing the solution to the challenge, for which I did next:

- Created a function to get the coordinates from a given address.
- Created a function to get a neighborhood from given coordinates.
- Created a recursive function to get the next different neighborhood found from an original address.

You can check the code in the challenge.py file.

## Test

You can test the python program with the next command:

```bash
python challenge.py
```
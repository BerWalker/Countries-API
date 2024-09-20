# Countries-API

This repository contains a simple terminal-based program that interacts with the **Rest Countries API** to provide information about countries. This project is part of a **bonus project** from the **Pentest: From Zero to Professional** course by **Solyd**. The project showcases how to consume a REST API using Python and interact with it via a command-line interface (CLI).

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
    - 2.1. [Main Files](#main-files)
    - 2.2. [Functions](#functions)
3. [Core Features](#core-features)
    - 3.1. [Country Count](#country-count)
    - 3.2. [Listing Countries](#listing-countries)
    - 3.3. [Country Population](#country-population)
    - 3.4. [Currency Information](#currency-information)
4. [How to Use](#how-to-use)
    - 4.1. [Installation](#installation)
    - 4.2. [Command-Line Arguments](#command-line-arguments)
5. [Final Considerations](#final-considerations)

---

## 1. Introduction
This project is part of the **Pentest: From Zero to Professional** course by **Solyd**, and it demonstrates how to consume and interact with the **Rest Countries API** using Python. The program allows users to fetch country-specific data like population and currency, count the total number of countries, and list all countries in the world.

## 2. Project Structure

### 2.1. Main Files
- **`countries.py`**: The main file that handles the command-line interface (CLI) logic and interacts with the Rest Countries API. It includes functions for fetching data such as population and currency information.

### 2.2. Functions
- **`request(url)`**: A helper function that handles the HTTP requests to the API and returns the JSON data.
- **`country_count()`**: Fetches all countries from the API and returns the total number of countries.
- **`list_countries()`**: Fetches and lists all countries' names.
- **`show_population(country_name)`**: Fetches and displays the population of a specified country.
- **`show_currencies(country_name)`**: Fetches and displays the currency or currencies of a specified country.
- **`read_country_name()`**: Reads the country name from the command-line arguments.

---

## 3. Core Features

### 3.1. Country Count
This feature fetches the total number of countries available from the Rest Countries API. The function `country_count()` makes an API call to `/all` and counts the number of country entries.

### 3.2. Listing Countries
The `list_countries()` function fetches and lists the names of all countries returned by the API. This provides a quick overview of all the available countries.

### 3.3. Country Population
The `show_population(country_name)` function takes the name of a country as input, retrieves the population data from the API, and displays it. This allows the user to check how many people live in a specific country.

### 3.4. Currency Information
The `show_currencies(country_name)` function retrieves information about the currency or currencies used by a given country. The data includes both the name and the code of each currency.

---

## 4. How to Use

### 4.1. Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/countries-api.git
cd countries-api
```

2. **Install dependencies: The program uses the requests library to interact with the API. If you don't have it installed, run:**

```bash
pip install requests
```

### 4.2. Command-Line Arguments

This program is operated through the command-line interface (CLI). Below are the available commands:

**Example Usage**

```bash
python paises.py <action> <country-name>
```

**Available Actions:**

count: Displays the total number of countries in the world.

**Example:**

```bash
python paises.py count
```

currency <country-name>: Displays the currency or currencies used by the specified country.

**Example:**

```bash
python paises.py currency Brazil
```

population <country-name>: Displays the population of the specified country.

**Example:**

```bash
python paises.py population Brazil
```


**If an invalid action or no action is provided, the program will display a help message with instructions on how to use the tool.**

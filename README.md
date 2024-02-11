# Nano Representative Manager

This application provides a web interface for managing nano account representatives based on a given seed. 
It performs RPC calls to generate account keys and retrieves account information to manage delegator assignments.

## Features

- Generate up to 1000 account keys based on a provided seed.
- Retrieve account information, including current representatives.
- Reassign delegators to new representatives. (Create and publish the change blocks to the network)
- Render a dynamic interface for managing accounts.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installing

A step-by-step series of examples that tell you how to get a development env running:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/account-management-system.git
cd account-management-system
touch .env
```

You need to adjust the `.env` file with the following variables:

```
RPC_URL=${RPC_URL}
AUTH_USERNAME=${AUTH_USERNAME}
AUTH_PASSWORD=${AUTH_PASSWORD}
```


3. Run the Flask application:

```bash
docker-compose build && docker-compose up -d
```

4. Access the web interface at `http://localhost:5222/`.

## Usage

To manage accounts, navigate to `/manage/<seed>`.




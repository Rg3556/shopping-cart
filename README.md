# Shopping-cart Projct

## Prerequisites ##
- Anaconda 3.7    
- Python 3.7
- Pip


## Setup ##

### Repo Setup/Installation

Visit the source code repository for the Rg3556's shopping-cart project [github source] (https://github.com/Rg3556/shopping-cart) and click "Fork" to copy the repo under your own control.

Then download (or "clone") your copy of the repo onto your local computer using GitHub Desktop or the command-line. Choose a familiar download location like the Desktop.

Then use your command line application (Mac Terminal or Windows Git Bash) to navigate to the location where you downloaded this repo.

Open the repo with your text editor (VS Code), and inspect the contents of the repo's "README.md" file.



After cloning the repo, navigate there from the command-line:
    
    ```sh
    cd ~/Desktop/shopping-cart
    ```

Use your text editor or the command-line to create a file in that repo called "shopping_cart.py", and then place the following contents inside:



### Environment Setup

Create and activate a new Anaconda virtual environment:

    ```sh
    conda create -n shopping-env python=3.7 # (first time only)
    conda activate shopping-env
    ```

From within the virtual environment, install the pytest package:

NOTE: we won't need pytest until/unless addressing the optional "Automated Testing" challenge,so you can feel free to skip this now and return later...

    ```sh
    pip install pytest
    ```

### Sendgrid Setup

To get receipt via emial, sign up for a Sendgrid free account:https://signup.sendgrid.com/, then click the link in a confirmation email to verify your account. Then create an API Key with "full access" permissions: https://app.sendgrid.com/settings/api_keys.

Store and replace the API Key value in an environment variable called SENDGRID_API_KEY. Also set and replace with an environment variable called MY_EMAIL_ADDRESS to be the email address you just associated with your SendGrid account (e.g. "abc123@gmail.com").


From within the virtual environment, install the pytest package:
    
    ```sh
    pip install sendgrid == 6.0.5
    ```


## Usage ##

Run the shopping cart scripts, respectively:

    ```sh
    python shopping_cart.py
    ```


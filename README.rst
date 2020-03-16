Broad DSP Engineering Challenge
===============================

What is the challenge?
---------------------

Boston's transportation system, the MBTA (https://mbta.com/), has a
website with APIs https://api-v3.mbta.com/docs/swagger/index.html.
You will not need an API key, but you might get rate-limited without one.

The MBTA's documentation https://api-v3.mbta.com/docs/swagger/index.html is
written using OpenAPI/Swagger.

Question 1

Write a program that retrieves data representing all, what we'll call "subway"
routes: "Light Rail" (type 0) and “Heavy Rail” (type 1). The program should list
their “long names” on the console.
Partial example of long name output: Red Line, Blue Line, Orange Line...
There are two ways to filter results for subway-only routes. Think about the two options below
and choose:
1. https://api-v3.mbta.com/routes
2. https://api-v3.mbta.com/routes?filter[type]=0,1
Please document your decision and your reasons for it.

Question 2
Extend your program so it displays the following additional information.
1. The name of the subway route with the most stops as well as a count of its stops.
2. The name of the subway route with the fewest stops as well as a count of its stops.
3. A list of the stops that connect two or more subway routes along with the relevant route
names for each of those stops.

Question 3
Extend your program again such that the user can provide any two stops on the
subway routes you listed for question 1.
List a rail route you could travel to get from one stop to the other. We will
not evaluate your solution based upon the efficiency or cleverness of your
route-finding solution. Pick a simple solution that answers the question. We
will want you to understand and be able to explain how your algorithm performs.
Examples:
1. Davis to Kendall -> Redline
2. Ashmont to Arlington -> Redline, Greenline
How you handle input, represent train routes, and present output is your choice.

Requirements
------------

You need Python 3.5 or later to run challenge.

Getting the Sources
-------------------

broad-challenge can be downloaded using via git clone:

    $ git clone https://gitub.com/ehigham/broad-challenge

For development, it's a good idea to set up a virtual environment (if you just
want to run the code, you can skip this step)

    $ cd broad-challenge
    $ python -m venv ./.venv

All dependencies required to build, test and run the code can be installed
using the requirements file:

    $ pip install -r ./requirements.txt


Building the Sources
--------------------

The Makefile documents a number of targets. Most useful of them all is test,
lint and coverage.

    $ make test


Running the Code
----------------

To see all options, enter

    $ python challenge.py --help

Options and Switches:

--list-routes
Lists all "Light" and "Heavy" rail routes

--print-route {longest, shortest}
Prints the selected route with its number of stops

--list-connections
Lists all stops that connect two or more routes, along with the associated routes

--plan-route START FINISH
List the subway routes needed to travel from the stop START to the stop FINISH
(case insensitive). Names with spaces should be enclosed in quotes.

Example:

    $ python challenge.py --plan-route Prudential "Back Bay"

Example Output:

    Prudential (Green Line E)
    Park Street (Red Line)
    Downtown Crossing (Orange Line)
    Back Bay ()

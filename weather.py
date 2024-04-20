"""Compute weather statistics from csv of data from Charlotte-Douglass Airport weather station."""

from typing import Dict, List
from csv import DictReader
import sys


"""Named Constants."""
LENGTH_OF_ARGS: int = 4
REPORT_TYPE: str = "SOD  "


def main() -> None:
    """Entrypoint of my progam."""
    arguments: Dict = read_args()
    if arguments["operation"] == str("list"):
        listfn(arguments)
        exit()
    if arguments["operation"] == str("min"):
        minfn(arguments)
        exit()
    if arguments["operation"] == str("max"):
        maxfn(arguments)
        exit()
    if arguments["operation"] == str("avg"):
        averagefn(arguments)
        exit()
    if arguments["operation"] == str("chart"):
        chart_data(arguments)
        exit()
    else:
        print("Invalid operation: " + arguments["operation"])
    exit()


def read_args() -> Dict[str, str]:
    """Reads arguments from command line."""
    if len(sys.argv) != LENGTH_OF_ARGS:
        print("Usage: python -m projects.pj01.weather [FILE] [COLUMN] [OPERATION]")
        exit()
    return {
        "file": sys.argv[1],
        "column": sys.argv[2],
        "operation": sys.argv[3],
    }


def listfn(arguments: Dict) -> None:
    """Prints a list of floats from a given column in SOD reports."""
    listtoprint: List[float] = list(arguments)
    print(listtoprint)


def maxfn(arguments: Dict) -> float:
    """Finds max value of list of floats of a given category."""
    listformax: List[float] = list(arguments)
    print(max(listformax))
    return max(listformax)


def minfn(arguments: Dict) -> float:
    """Finds min value of list of floats of a given category."""
    listformin: List[float] = list(arguments)
    print(min(listformin))
    return max(listformin)


def averagefn(arguments: Dict) -> float:
    """Finds average value of list of floats of a given category."""
    listforaverage: List[float] = list(arguments)
    length: int = len(listforaverage)
    total: float = sum(listforaverage)
    average: float = total / length
    print(average)
    return average


def chart_data(parameters: Dict) -> None:
    """Charts data for a given column from SOD reports."""
    import matplotlib.pyplot as plt
    data: List[float] = list(parameters)
    dates: List[str] = dates_list(parameters)
    # plot the values of our data over time
    #plt.plot(dates, data)
    # label the x-axis Date
    plt.xlabel("Date")
    # label the y-axis whatever column we are analyzing
    plt.ylabel(parameters["column"])
    # plot!
    plt.show()


""" Beginning of helper functions."""


def list(arguments: Dict) -> List[float]:
    """Takes arguments from command line and generates a list of values."""
    columnlist: List[float] = []
    data: List[Dict[str, float]] = strstr_to_strfloat(sodonly(arguments))
    for dictionary in data:
        for key in dictionary:
            if key == arguments["column"]:
                columnlist.append(dictionary[key])
    if len(columnlist) == 0:
        print("Invalid column: " + arguments["column"])
        exit()
    else:
        return (columnlist)


def sodonly(arguments: Dict) -> List[Dict[str, str]]:
    """Takes a weather report csv file, generates a List of Dictionaries [{str, str}] for report of certain type."""
    file = arguments["file"]
    file_handle = open(file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    listofsod: List[Dict[str, str]] = []
    for row in csv_reader:
        if row["REPORT_TYPE"] == REPORT_TYPE:
            listofsod.append(row)
    file_handle.close()
    return(listofsod)


def strstr_to_strfloat(input: List[Dict[str, str]]) -> List[Dict[str, float]]:
    """Turns a dictionary of type str, str and makes a dictionary of str, float."""
    sodlist: List[Dict[str, float]] = []
    for dictionary in input: 
        float_row: Dict[str, float] = {}
        for key in dictionary:
            try:
                float_row[key] = float(dictionary[key])
            except ValueError:
                None
        sodlist.append(float_row)
    return sodlist


def dates_list(parameters: Dict) -> List[str]:
    """Takes the parameters, and produces a list of dates for sod types."""
    LENGTH_OF_DATE: int = 10
    dates_list: List[str] = []
    listfordates: List[Dict[str, str]] = sodonly(parameters)
    listforshortdates: List[str] = []
    i: int = 0
    for dictionary in listfordates:
        for key in dictionary:
            if key == "DATE":
                dates_list.append(dictionary[key])
    for dates in dates_list:
        currentdate: str = ""
        i = 0
        while i < LENGTH_OF_DATE:
            currentdate = currentdate + dates[i]
            i += 1
        listforshortdates.append(currentdate)
    return listforshortdates
    

if __name__ == "__main__":
    main()
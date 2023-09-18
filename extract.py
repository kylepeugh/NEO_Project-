"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neos_csv):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neoinfo = []

    with open(neos_csv, 'r') as infile1:
        reader1 = csv.DictReader(infile1)
        for row in reader1:
            neo = NearEarthObject(name=row['name'],
                                  designation=row['pdes'],
                                  diameter=(row['diameter']),
                                  hazardous=row['pha'])
            neoinfo.append(neo)

    return neoinfo

    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """


def load_approaches(cad_json):
    """Read close approach data from JSON file.
    
    :param neo_csv_path: A path to a JOSN file containing data about close approaches.
    :return a collection of 'Close Approach'es.
    """
    approachinfo = []
    with open(cad_json, 'r') as infile2:
        reader2 = json.load(infile2)
    for item in reader2['data']:
        item = dict(zip(reader2['fields'], item))
        ca = CloseApproach(
            _designation=item['des'],
            time=item['cd'],
            distance=float(item['dist']),
            velocity=item['v_rel']
        )
        approachinfo.append(ca)
    return approachinfo

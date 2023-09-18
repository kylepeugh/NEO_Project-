"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, name,
                 diameter=float('nan'), hazardous='N'):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self.designation = designation
        self.name = name
        if self.name == '':
            self.name = None
        else:
            self.name = name
        self.diameter = diameter
        if not self.diameter:
            self.diameter = float('nan')
        else:
            self.diameter = float(diameter)
        self.hazardous = hazardous
        if hazardous == 'Y':
            self.hazardous = True
        else:
            self.hazardous = False

        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name:
            return f"{self.designation} ({self.name})"
        return f"{self.designation}"

    def __str__(self):
        """Return `str(self)`."""
        return f"NEO {self.fullname} has a diameter of " \
               f"{self.diameter:.3f} km " \
               f"and {'is' if self.hazardous else 'is not'} " \
               f"potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject (designation={self.designation!r}, " \
               f"name={self.name!r}, diameter={self.diameter:.3f}, " \
               f"hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, _designation, time,
                 distance=float('nan'), velocity=float('nan')):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self._designation = _designation
        self.time = cd_to_datetime(time)
        self.distance = distance
        if not distance:
            self.distance = float('nan')
        else:
            self.distance = distance
        self.velocity = velocity
        if not velocity:
            self.velocity = float('nan')
        else:
            self.velocity = float(velocity)
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return (f"On {self.time_str!r}, NEO '{self.neo.fullname}'"
                f" approaches Earth at a distance of"
                f" of {self.distance:.2f} au with a velocity of"
                f" {self.velocity:.2f} km/s.")

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r},"
                f" distance={self.distance:.2f},"
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

# ----------------------------------------
# CSC 315 / DSC 615
# Project 4 Miami-Dade Schools
# Name: Alex Ramos
# ----------------------------------------
import sys
import random
from typing import cast
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, MultiPolygon, Point, GeometryCollection
from shapely.geometry.base import BaseGeometry
from shapely.plotting import plot_polygon


class Region:
    def __init__(self, name: str, geometry: BaseGeometry):
        self.name = name
        self.geometry = geometry

    def intersects(self, other):
        return self.geometry.intersects(other.geometry)

    def intersection(self, other):
        outname = self.name
        outgeom = self.geometry.intersection(other.geometry)
        return Region(outname, outgeom)


class School(Region):
    def __init__(self, name: str, geometry: BaseGeometry):
        super().__init__(name, geometry)

    def plot(self):
        if isinstance(self.geometry, Point):
            plt.plot(self.geometry.x, self.geometry.y, "k.", markersize=7)


#
# Add Functions
#
class Place(Region):
    def __init__(self, name: str, geometry: BaseGeometry):
        super().__init__(name, geometry)
        self.schools = []

    def add_school(self, school: School):
        if school.geometry.within(self.geometry):
            self.schools.append(school)

    def plot(self):
        if not isinstance(self.geometry, (Polygon, MultiPolygon)):
            return

        poly_geom = cast(Polygon | MultiPolygon, self.geometry)
        plot_polygon(poly_geom, facecolor="tab:blue", edgecolor="black", alpha=0.45)

        c = self.geometry.centroid
        plt.text(c.x, c.y, self.name, fontsize=6, ha="center", va="center")

        for school in self.schools:
            school.plot()


#
# Add Functions
#
class District(Region):
    def __init__(self, name: str, geometry: BaseGeometry):
        super().__init__(name, geometry)
        self.places = []

    def add_place(self, place: Place):
        if not self.geometry.intersects(place.geometry):
            return

        cut_geom = self.geometry.intersection(place.geometry)
        if isinstance(cut_geom, GeometryCollection):
            cut_geom = cut_geom.buffer(0)

        if cut_geom.is_empty:
            return

        if not isinstance(cut_geom, (Polygon, MultiPolygon)):
            return

        cut_place = Place(place.name, cut_geom)
        for school in place.schools:
            cut_place.add_school(school)

        self.places.append(cut_place)

    def plot(self):
        if isinstance(self.geometry, (Polygon, MultiPolygon)):
            poly_geom = cast(Polygon | MultiPolygon, self.geometry)
            plot_polygon(poly_geom, facecolor="none", edgecolor="black", linewidth=1.5)

        for place in self.places:
            place.plot()

        plt.title(self.name)
        plt.gca().set_aspect("equal", adjustable="box")


#
# Add Functions
#
# ------------------------------------------
# ------------------------------------------
# Driver code, do not modify
# ------------------------------------------
# ------------------------------------------
import geopandas as gpd
import pandas as pd


def main():
    # Make the Schools
    schools = []
    df = pd.read_csv("public_schools.csv")
    for row in range(df.shape[0]):
        name = df["NAME"][row]  # Parse School
        lat = df["LAT"][row]
        lon = df["LON"][row]
        school = School(name, Point(lon, lat))  # Construct School
        schools.append(school)  # Append School

    # Make the Places
    places = []
    df = gpd.read_file("place_pop_2010.geojson")
    for row in range(df.shape[0]):
        name = df["NAME10"][row]  # Parse Place
        geom = df["geometry"][row]
        place = Place(name, geom)  # Construct Place
        for s in schools:
            place.add_school(s)  # Add all of the Schools
        places.append(place)  # Append Place

    # Make the Districts
    districts = []
    df = gpd.read_file("commission_district.geojson")
    df = df.sort_values(by="ID", ascending=True, ignore_index=True)
    for row in range(df.shape[0]):
        name = "District %d (%s)" % (df["ID"][row], df["COMMNAME"][row])
        # Parse District
        geom = df["geometry"][row]
        district = District(name, geom)  # Construct District
        for p in places:
            district.add_place(p)  # Add all of the Places
        plt.figure(figsize=(8, 8))
        district.plot()
        plt.show()
        districts.append(district)  # Append District


main()
print("Done!")

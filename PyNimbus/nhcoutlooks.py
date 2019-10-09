#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:12:46 2019

@author: Brandon
"""

import hurricane_names as hn
import os, requests, shutil, zipfile, io
import datetime

class nhcOutlooks():
    
    def __init__(self, name, year, advisory_num): 
        self.info = self._hurricane_info(name, int(year))
        self.name = name
        self.year = int(year)
        self.advisory_num = int(advisory_num)
    
    def _hurricane_info(self, name, year):
        
        def check_if_exists_in_dict():
            
            # put 2008 on top for forward compatability reasons - append to list below
            # for future years (2020, etc) using elif.
            if   year == 2008 : h_dict = hn.h_2008
            elif year == 2009 : h_dict = hn.h_2009
            elif year == 2010 : h_dict = hn.h_2010
            elif year == 2011 : h_dict = hn.h_2011
            elif year == 2012 : h_dict = hn.h_2012
            elif year == 2013 : h_dict = hn.h_2013
            elif year == 2014 : h_dict = hn.h_2014
            elif year == 2015 : h_dict = hn.h_2015
            elif year == 2016 : h_dict = hn.h_2016
            elif year == 2017 : h_dict = hn.h_2017
            elif year == 2018 : h_dict = hn.h_2018
            elif year == 2019 : h_dict = hn.h_2019
            
            # if the name is in the dictionary, return. If not, raise error.
            if name in h_dict:
                return h_dict[name]
            raise ValueError("{0} not in {1} - double check spelling and/or year.".format(name, year))
        
        # check to see if it's a valid year.
        now = datetime.datetime.now()
        if not 2008 <= year <= now.year:
            raise ValueError("Year must be between 2008 and current year")
        
        return check_if_exists_in_dict()
    
    def get_cyclone_outlook(self, verbose = False, extract_dir = None):
        
        # As of right now, the files should be downloaded into a new directory
        #   and extracted, saved, then the whole directory should be deleted
        #   once the information is extracted.
        
        # Future work: is there a way to extract the information from the
        #   zipped shapefile without having to download it?
        
        zip_file_url = "https://www.nhc.noaa.gov/gis/forecast/archive/\
{0}{1}_5day_{2:03d}.zip".format(self.info[0], self.year, self.advisory_num)

        if verbose: print("Downloading: " + zip_file_url)
        
        # This chunk of code:
        #   1. Checks to see if os.getcwd()/nhc_downloads exists (deletes if does)
        #   2. Remakes the directory
        #   3. Downloads from zip file url above
        #   4. Extracts information (now in memory!)
        #   5. Removes folder

        if extract_dir is None:    
            path = os.path.join(os.getcwd(), "nhc_downloads")
        else:
            path = os.path.join(extract_dir, "nhc_downloads")
        
        # checks if path exists
        if os.path.isdir(path):
            shutil.rmtree(path)
            if verbose: print("Found {}, removed".format(path))

        os.mkdir(path)
        r = requests.get(zip_file_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(path)
        if verbose: print("Extracted into directory: {}".format(path))
    

a = nhcOutlooks("Barbara", 2019, 1)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
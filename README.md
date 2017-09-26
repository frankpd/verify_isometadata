# verify_isometadata
**Parse geospatial ISO 19139 XML metadata records to check them for completeness**

Frank Donnelly, Geospatial Data Librarian, Baruch College CUNY
Released under Creative Commons Attribution-Non Commercial-ShareAlike License 4.0 International
http://creativecommons.org/licenses/by-nc-sa/4.0/

Disclaimer:

The creator, Baruch College, and CUNY disclaim any liability for errors, inaccuracies, or omissions that may be contained within this script and for any damages that may arise from the foregoing. Users should independently verify the accuracy of the code and it's output for their own purposes.

Purpose:

This script uses Python and the ElementTree module to parse ISO 19139 XML metadata records to check them for completeness. In this context, completeness means that all of the elements enumerated in the script are present in the metadata (an element isn't missing) and that these elements have values (a value isn't blank - it contains an actual value or the attribute nil or null). Two reports are generated: one lists errors (an element is missing or a value is blank) while the other is a list of all the values that are checked. The goal was to capture most of the elements and attributes that are required by the North American Profile of ISO 19115 2003, and that are required by the standards we use in-house.

A sample metadata record (that is intentionally missing information) with output is included.

Assumptions:

1. The script was written in Python 3.4, and should be run using a 3.x version of Python.

2. The script should be stored and run from a directory that is immediately above the directory that contains the metadata files to be checked. By default, it looks for a directory called 'processed'. If this isn't desired, change the value for rootdir at the beginning of the script.

3. The script will parse all metadata files in the directory that end with the string '_export.xml'. This is the default suffix that ArcCatalog adds to all metadata records that are exported in batch mode. If this isn't desired, change the string and corresponding index number to something else (for example, file[-4]=='.xml' would parse all XML files).

4. The only elements and attributes that are checked are specified in a series of dictionaries. If you want to check additional elements or attributes, you can add them to the appropriate dictionary. Conversely you can comment out or remove elements or attributes that you don't want to check.

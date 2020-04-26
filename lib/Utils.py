"""
    Utility class. Containing the most used common functions

"""
import os
from fuzzywuzzy import fuzz


class Utils:

    @classmethod
    def string_trim(cls, string: str):
        """ Removes escape characters and strips the string

        :param string: string to clean
        :return: cleaned string
        :rtype str:
        """
        return string.replace("\n", "").strip()

    @classmethod
    def name_check(cls, real_name, check_name):
        """ Match first names with eachother for similarity > 95. Then match everything af with 75 > Simliary

        :param real_name: Name of person
        :type real_name: str
        :param check_name: Name to check against
        :type check_name: str
        :return: If name is similar or not
        :rtype: bool
        """
        real_name_split = real_name.split(" ", 1)
        check_name_split = check_name.split(" ", 1)

        return fuzz.ratio(real_name_split[0], check_name_split[0]) >= 90 and fuzz.token_sort_ratio(real_name_split[1],
                                                                                                   check_name_split[
                                                                                                       1]) > 80

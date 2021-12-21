""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'informat.suporte'  # <- enter username here
insta_password = 'informat2021'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["leandrodamasio.adm", "jardimplataforma", "ljwebsites"])
    session.set_dont_like(["wines", "#store"])

    # activity
    session.like_by_tags(["computadores"], amount=10)

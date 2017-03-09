import requests, tweepy, boto3
import logging, logging.handlers, os, json
from functions import getSecret

# ------------------------------------------------------------------------------------
# LOGGING INITIALIZATION
# ------------------------------------------------------------------------------------

logger = logging.getLogger('logger')
# set level
logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.ERROR)

# set vars
log_file_dir = "./logs/"
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fileLogger = logging.handlers.RotatingFileHandler(filename=("{0}debug.log".format(log_file_dir)), maxBytes=256*1024, backupCount=5) # 256 x 1024 = 256K
fileLogger.setFormatter(formatter)
logger.addHandler(fileLogger)

# Uncomment below to print to console
#handler = logging.StreamHandler()
#handler.setFormatter(formatter)
#logger.addHandler(handler)

# ------------------------------------------------------------------------------------
# MAIN SCRIPT
# ------------------------------------------------------------------------------------

# Last hour
r = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson')
# Last day (for testing)
#r = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson')
# Last month (for testing)
#r = requests.get('http://127.0.0.1/github/robertdenton/cascadiaquakes/testdata.json')

logger.debug("got usgs data")
usgs = r.json()

quakes = usgs['features']
logger.debug("{} earthquakes in the past hour".format(len(quakes)))

# read hash dictionary file
if len(quakes):
    # Test to see if id.json exists (good for first run)
    if  os.path.exists('id.json')==False: 
        old = {}
        logger.debug("no id json file")
    else:
        # Open up id file # See: https://docs.python.org/3/library/functions.html#open
        id_json = open('id.json', 'r')
        old = json.load(id_json)
        logger.debug("got id json file")
    #for key, value in old.items():
    #    print(key)
    # Make new dictionary for new data structure
    new = {}
    # Loop over quakes in usgs data
    for quake in quakes:
        # Get quake ID
        quakeid = quake['id']
        exact   = quake['geometry']['coordinates']
        mag     = quake['properties']['mag']
        loc     = quake['properties']['place']
        url     = quake['properties']['url']
        tsu     = quake['properties']['tsunami']
        #logger.debug("quakeid: {}".format(quakeid))
        new[quakeid] = exact
        # Check to see if the id is already in the file
        if (quakeid not in old):
            # These could be interpreted as ints or floats, should standardize as float
            newlon   = float(exact[0])
            newlat   = float(exact[1])
            newdepth = float(exact[2])
            #print("{0}, {1}".format(newlon, newlat))
            #print("{0}".format(newlon))
            # See: https://github.com/robertdenton/cascadiaquakes/issues/
            # and (40.6 < newlat < 49.6)
            if (-128.8 < newlon < -121.3) and (40.6 < newlat < 49.6):
                logger.debug("{0}, {1}: CASCADIA!!!".format(newlon, newlat))
                # Get access token from secrets.json
                secrets = getSecret('twitter-rob')
                consumer_key = secrets['consumer_key']
                consumer_secret = secrets['consumer_secret']
                access_token = secrets['access_token']
                access_token_secret = secrets['access_token_secret']
                # Set up SNS
                aws = getSecret('aws-arn')
                client = boto3.client('sns')
                # Tweepy auth
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)
                # Construct tweet text
                content = "{0} - {1}: {2}".format(mag,loc,url)
                try:
                    # Send tweet (Uncomment to go live)
                    api.update_status(status=content)
                    # Send text (Uncomment to go live)
                    response = client.publish(TopicArn=aws,Message=content)
                    logger.debug('Success! Data sent: ' + content)
                except tweepy.TweepError as err:
                    logger.error(err)
                    success = False
                # make new dictionary 
                #new[quakeid] = {}
                #new[quakeid]['mag'] = mag
                #new[quakeid]['loc'] = loc
                #new[quakeid]['url'] = url
                #new[quakeid]['tsu'] = tsu
                # Tweet it
    logger.debug("new length: {}".format(len(new)))
    # Open up id file to override
    new_id_json = open('id.json', 'w')
    json.dump(new, new_id_json, indent=4)

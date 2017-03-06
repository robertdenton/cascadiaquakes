Under development...

[Cascadia subduction zone](https://www.pnsn.org/outreach/earthquakesources/csz)

Steps:

1. Get [geoJSON](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson) from USGS. [More info](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).
2. Test to see if there are any new events.
3. Test to see if events are near CSZ. +/- 100 miles from coast from BC to CA? Might need to ask an expert about this.
4. Send tweet/text alert? [TEXT ALERTS WOULD BE COOL](https://aws.amazon.com/sns/) 

Notes:

* At time of research, [this page](https://earthquake.usgs.gov/fdsnws/event/1/), labeled "API Documentation - Earthquake Catalog" says that the real-time GeoJSON feeds are the best for any automated applications. "...they will have the best performance and availability for that type of information."
  * [Last hour earthquakes](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson)
* [Deploying to ElasticBeanstalk](https://realpython.com/blog/python/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/) (EC2 + RDS)


Set up:

```
brew install python3
mkvirtualenv cascadiaquakes --python=python3
(cascadiaquakes) pip install -r requirements.txt
(cascadiaquakes) pip install -e .
```

Create secrets.json file with your twitter credentials. To make a new Twitter app, go to [dev.twitter.com](https://dev.twitter.com).

```json
{
    "twitter-example": {
        "consumer_key": "asdf",
        "consumer_secret": "asdf",
        "access_token":"asdf",
        "access_token_secret":"asdf"
    }
}
```


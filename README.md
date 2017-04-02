I live in Cascadia, a section of the Pacific northwest stretching from Washington down to California along the [Cascadia subduction zone](https://www.pnsn.org/outreach/earthquakesources/csz). 

That's the area where experts expect to see [the big one](http://www.newyorker.com/magazine/2015/07/20/the-really-big-one) in the next century. 

A few weeks ago I went looking for a text or Twitter notification service from USGS for earthquakes in this area. What I found was that they didn't have any for *only* this particular region. They have plenty of earthquake alerts for [larger areas](https://earthquake.usgs.gov/earthquakes/ted/) though.

So I started poking around and found a number of [real-time APIs](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) for earthquakes. I thought it might be cool to build an alert for just Cascadia earthquakes.

To do this I looked at several maps of the Cascadia region online and made a **rough** [geofence](https://drive.google.com/open?id=1z2HFdpvb-ObqZMChB9jgLhKfknY&usp=sharing) around the area to focus on. In other words, any earthquake with a lat/long within those coordinates will be sent as a notification.

## Goals

* [x] Create working Twitter bot for Cascadia earthquakes (Bonus: SMS alerts)
* [x] Sign up for AWS, spin up my first EC2 (Bouns: Try out SNS for the first time)
* [x] Learn something new and make something useful


## Local set up

```
brew install python3 # If not installed
mkvirtualenv cascadiaquakes --python=python3
(cascadiaquakes) pip install -e .
```

Create secrets.json file with your twitter credentials. To make a new Twitter app, go to [dev.twitter.com](https://dev.twitter.com). You'll also need to set up an [AWS SNS topic](http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) and get an arn. 

```json
{
    "twitter-example": {
        "consumer_key": "asdf",
        "consumer_secret": "asdf",
        "access_token":"asdf",
        "access_token_secret":"asdf"
    },
    "aws-arn": "arn:aws:sns:us-east-1:123456789012:asdf"
}
```

## Notes

* I'm not going to walk through all the steps to deploy to AWS, but I will say that I had to increase my default spend limit to more than $1 during testing because I was sending multiple texts a day. [This article](https://aws.amazon.com/premiumsupport/knowledge-center/python-boto3-virtualenv/) also came in handy.
* At time of research, [this page](https://earthquake.usgs.gov/fdsnws/event/1/), labeled "API Documentation - Earthquake Catalog" says that the real-time GeoJSON feeds are the best for any automated applications. "...they will have the best performance and availability for that type of information."
  * [Last hour earthquakes](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson)
* Would be cool to write earthquakes into RDS but not going to do that right now...

## Prelim plan

1. Get [geoJSON](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson) from USGS. [More info](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).
2. Test to see if there are any new events.
3. Test to see if events are near CSZ. +/- 100 miles from coast from BC to CA? Might need to ask an expert about this.
4. Send tweet/text alert? [TEXT ALERTS WOULD BE COOL](https://aws.amazon.com/sns/) 







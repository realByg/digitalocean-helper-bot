import digitalocean

do = digitalocean.FloatingIP(region_slug='nyc3',
                             token='e208263bfd6f12649c7c9a42e504b89d4f7e4b993c3f83ee9b1314249220e66e').reserve()

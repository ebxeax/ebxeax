I always faced issues when running jekyll locally, my blog uses jekyll to generate static pages, but every time my os is upgraded or I change my laptop, I always get into trouble of installing/managing ruby version, bundles etc. To my rescue comes the docker, I have created a simple a docker file and script to serve my jekyll pages locally, and it now works like a charm.

I always have been admirer of docker, I tend to use docker more often if have to install any dev app, databases etc or package but still want to keep my machine clean. In this case as well I wanted a consistent mechanism to run my blogs locally.

# Dockerfile
The first thing I do is create a simple dockerfile in my Jekyll app. I copy my Gemfile and Gemfile.lock to install the bundles.
```dockerfile
FROM jekyll/jekyll:3.8

COPY Gemfile* ./

RUN gem install bundler:2.2.24 && bundle install

ENTRYPOINT [ "jekyll" ]

CMD [ "build" ]
```

The reason I copied Gemfile is because sometimes the bundle version is different, so now I install the required bundler (in my case its 2.2.24), and install all the dependencies.

# Execution Script
Next I created a simple script to build and serve my code, so that i don’t keep on typing the commands every time.local_serve.sh
```bash
#!/usr/bin/env bash

set -e

case $1 in
    'prod-build')
        echo "Building docker image of Jekyll"
        docker build -t jekyll .

        echo "Building Jekyll site"    
        docker run \
            --volume="$PWD:/srv/jekyll:Z" \
            -e JEKYLL_ENV=prod \
            -t jekyll \
            build
    ;;
    'build')
        echo "Building docker image of Jekyll"
        docker build -t jekyll .

        echo "Building Jekyll site"    
        docker run \
            --volume="$PWD:/srv/jekyll:Z" \
            -t jekyll
    ;;
    'serve')
    docker run \
            --volume="$PWD:/srv/jekyll:Z" \
            -p 4000:4000 \
            -it jekyll serve
    ;;
esac
```

In the build command, I am creating the jekyll image. I can mapping the current directory to /srv/jekyll and running my jekyll container to build the site.

In the serve command, I using the same directory to serve my pages at port 4000 and using interactive mode to explicitly invoke serve command.

# Run the Jekyll container
Before we proceed do not forget to give executable permission to local_service.sh
``` bash
$ chmod a+x local_serve.sh
So, first thing to do is to build our Jekyll app so that all the dependencies are downloaded. We will just run

$ ./local_serve.sh build
Once the dependencies are downloaded, now lets start our Jekyll server

$ ./local_serve.sh serve
```
And we can see the server started
```bash
ruby 2.6.3p62 (2019-04-16 revision 67580) [x86_64-linux-musl]
Configuration file: /srv/jekyll/_config.yml
            Source: /srv/jekyll
       Destination: /srv/jekyll/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
       Jekyll Feed: Generating feed for posts
   GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
                    done in 17.778 seconds.
 Auto-regeneration: enabled for '/srv/jekyll'
    Server address: http://0.0.0.0:4000/
  Server running... press ctrl-c to stop.
```
Enjoy running Jekyll locally without installing ruby or jekyll directly on your system.
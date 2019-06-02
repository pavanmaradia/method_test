# Method Test


#### What’s your proudest achievement? It can be a personal project or something you’ve worked on professionally. Just a short paragraph is fine, but I’d love to know why you’re proud of it.
> Through out my carrier, I witness great amount of Proud moments, however there are few which could be worth mention here. 
While I was leaning to become a FullStack developer, I started side project (to learn HTML5, SASS, JQuery) "Online review system" , where reviewer can review shots online from anywhere and create note (either text or drawing) on any frame and those review screens has been store inside respective shot for artist. Feel proud of that because though its a side project on which I was working in my leisure time but it was most loved one in Trace VFX Studio.
The other Proud moment is while one non performer resource aline to me and he becomes the performer of team.

#### Tell me about a technical book or article you read recently, why you liked it, and why I should read it.
> Recently I came across few interesting articles like, 
> 1. [10x Faster Parallel Python Without Python Multiprocessing](https://towardsdatascience.com/10x-faster-parallel-python-without-python-multiprocessing-e5017c93cce1). I liked the processing options we could get with some framework which is quite faster than traditional one.
> 2. [CNNs, Part 1: An Introduction to Convolutional Neural Networks](https://victorzhou.com/blog/intro-to-cnns-part-1/). I am quite fond of image processing from the beginning while I started exploring ML, so obvious reason could be my curiosity.
> 3. [Kubernetes Operator Pythonic Framework (Kopf)](https://github.com/zalando-incubator/kopf). Its quite handful tool for DevOps to manage Kubernetes clusters 


#### Tell me about something on visual effects that you really like, and why.
> Lion King (2019)'s Animation and VFX. The trailer itself drives you how technology helped to recreate memorable movie to real life experience, just no words.


#### Write some code, that will flatten an array of arbitrarily nested arrays of integers into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4].
> This code is stored in flatten_list module. Example execution is stored in test.py

#### Write a class TempTracker with these methods:
- insert()—records a new temperature.
- get_max()—returns the highest temp we've seen so far.
- get_min()—returns the lowest temp we've seen so far.
- get_mean()—returns the mean of all temps we've seen so far.
- get_mean() should return a float, but the rest of the getter functions can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..110.
> There were three types of endpoints for this class. 
> 1. Execute it from test.py or import temp_tracker module inside your repository and call api
> 2. Run App.py, which will serve as localhost rest api for insert, max, min and mean
> 3. Run docker-compose file and containers will be deployed and you can access endpoint for insert, max, min and mean
> ##### Pre-requisite to run above code,
> - postgresql server with database
> - docker and docker-compose installed if you want to run docker-compose
> ##### Note: Refer test.py for endpoint payload 
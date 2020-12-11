# Cache Stuff

If a call relies on I/O, it can stay in the scope of a computer for a long while.
Especially, when it goes to a remote network like calling an external API, I/O is slow.
Many calls are re-done over time. Some similar calls even happen several times per second in a production setup.

In order to improve the performance, store the result of such a call locally and just use the stored value the next time.
This is done by the caching framework in the Python SDK.

## Compute the key

The caching framework is used in combination with a decorater. 

If you call a function or a method that is decorated with the caching decorator, a key is computed from the call in a way that it is unique for a call to the same function with the same arguments.

For computing the key, the following items are taken into account:

- the full qualified name of the callable (aka. the function or method)
- the type of the callable
- the pickled value of the arguments
- the type of the arguments

The result is then hashed with SHA512 to make sure the key is not giving a hint to the value or the initial arguments.

The resulting key will be used to store and receive entries in the caches. 

## The chain of caches

The decorator receives the chain of caches as an argument.

The chain represents federated relations of caches. It is a list of cache instances.
The first instance given is asked first.
If it does not have the requests key stored, the next cache in the chain is asked.

In case a cache later in the chain has the requested entry, this key also updates the caches before.

This system of chained caches allows to store some data locally and some data on a centralized caching system.

## Our first cached call

Imagine that you have a call that fetches the weather for a given city by its name:

```python
def get_weather_by_city(city_name):
    # your code
    return {"temperature": …}
```
    
This calls an external API that takes a rather long time. The API does not update the data more than one time every 5 minutes.

To simply decorate the funtion, proceed as shown below:

```python
from skill_sdk.caching.decorators import CallCache
from skill_sdk.caching.local import LocalTimeoutCache

@CallCache([LocalTimeoutCache(300)])
def get_weather_by_city(city_name):
    # your code
    return {"temperature": …}
```

>Now, you cache calls.

The first call for a `city_name` is made to the API and the result stored.
All calls with the same `city_name` within 300 seconds are **not** made to the API but answered from the cache instead.

For this case, the `LocalTimeoutCache` has been choosen. Other types are described below.

## The different types of caches

The caching system offers a few different caching types with different behaviours.
To find these types, execute `from skill_sdk.caching.local`.

>Choose the right caching type for your use-case wisely.

### LocalFIFOCache

The **LocalFIFOCache** is a cache with a maximum number of entries. If it is full, it removes the oldest item.

- **call**: `LocalFIFOCache(max_size=100)`
- **limitation**: number of entries (*max_size*)
- **removal strategy**: oldest item

### LocalLRUCache

The **LocalLRUCache** is nearly similar to the LocalFIFOCache. But instead of the oldest item, it removes the least recently used item when the cache is full.

- **call**: `LocalLRUCache(max_size=100)`
- **limitation**: number of entries (*max_size*)
- **removal strategy**: for the longest time not used item

### LocalTimeoutCache

The **LocalTimeoutCache** has no limitation in size. Items in this cache expire after a given time.

- **call**: `LocalTimeoutCache(timeout=60)`
- **limitation**: life-time of an entry (*timeout*)
- **removal strategy**: expired items

>A validation of the constraints for the cache and all stored items is done every 1000 writes to the cache.
Items that do not fit the constraints anymore (expired, too many) are removed.

## Decorating methods

When you decorate, `self` methods are injected as the first implicit argument and taken into account for the key generation.
This might result in a different key for passing the same argument to the same method.

To solve this, you can pass the argument `ignore_first_argument` to the decorator:

```python
from skill_sdk.caching.decorators import CallCache
from skill_sdk.caching.local import LocalTimeoutCache

class WeatherAPI:

    # ...

	@CallCache([LocalTimeoutCache(300)], ignore_first_argument=True)
    def get_weather_by_city(self, city_name):
        # your code
        return {"temperature": …}
```

## Useful hints

>Make sure that your arguments are easy to serialize! *The less complex their types are, the better.*

>Think about memory consumption! *Especially the LocalTimeoutCache can use large amounts of memory.*

>The first argument to the `CallCache` (the cache chain) decorator is always a list. 

## Current status and future

At this point in time, only local cache is implemented. This makes the federated caching system rather pointless.

In the future, there will be Level 2 caches as well and the caching chain will start to make sense. 
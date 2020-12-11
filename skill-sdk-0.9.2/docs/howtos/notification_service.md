# How to use Notification Service

[Notification Service](https://gard.telekom.de/gardwiki/display/SH/Notification+Management+API) is an internal service 
that can send push notifications to the device. It wakes up the client and displays notification animation.

There are currently two types of animation ("push_soft" and "push_hard").
They both display similar animation (moving orange LED) with "push_hard" type also notifying user by voice:


|        |    push_soft      |  push_hard
| ------ | :-----------------| :-------------------
|LED     |   color=orange    |   color=orange
|        |   style=moving    |   style=moving
|Speaker |   quiet           |   message


## API

Python Skill SDK provides the following API to send push notifications:  

 **services.notification.NotificationService.add**

`add(notification: Notification) -> Dict[str, Notification]` adds a notification.

Returns a dictionary object with notification UUID as key and the notification itself as value. 

For details about how to create notifications, please refer to 
[Notification Center Tutorial](https://gard.telekom.de/gardwiki/display/SHD/Notification+Center+tutorial). 

**services.notification.NotificationService.mark_as_read**

`mark_as_read(id_: str = None, read: bool = True) -> requests.Response` marks a single notification 
(if parameter **id_** provided) or all notifications as read (or unread if **read** parameter is set to `False`).

The returned value is a raw response from the service.

**services.notification.NotificationService.delete**

`delete(id_: str = None) -> requests.Response` deletes either a single notification (if parameter **id_** provided 
or all notifications)

The returned value is a raw response from the service.

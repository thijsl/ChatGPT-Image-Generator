# Concept

The following two statements are true:

1. ChatGPT can render markdown (images)
2. Markdown images can be represented by base64 encoded data

The following statement seems true:

1. When your single ChatGPT Plugin API endpoint returns a hardcoded markdown image of a yellow circle represented by base64 encoded data, ChatGPT knows how to alter this response to respect your request.

# Limitations

* It can only generate simple shapes. ChatGPT refuses to collaborate on more complex requests.

# Learning process

# 1

Initially I thought I'd need to be responsible for feeding in the base64. 

Not needed.

Instead, just returning one example was sufficient, e.g.

```
![Yellow Circle](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCI+PHRpdGxlPlllbGxvdyBDaXJjbGU8L3RpdGxlPjxjaXJjbGUgY3g9IjUwIiBjeT0iNTAiIHI9IjUwIiBmaWxsPSJ5ZWxsb3ciIC8+PC9zdmc+)
```

which renders the following image:

![Yellow Circle](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCI+PHRpdGxlPlllbGxvdyBDaXJjbGU8L3RpdGxlPjxjaXJjbGUgY3g9IjUwIiBjeT0iNTAiIHI9IjUwIiBmaWxsPSJ5ZWxsb3ciIC8+PC9zdmc+)

# 2

Then I wanted to know whether I even needed to return an example.

Maybe the system is smart enough?

Remember, I started from this code:

```
  img = "![Yellow Circle](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCI+PHRpdGxlPlllbGxvdyBDaXJjbGU8L3RpdGxlPjxjaXJjbGUgY3g9IjUwIiBjeT0iNTAiIHI9IjUwIiBmaWxsPSJ5ZWxsb3ciIC8+PC9zdmc+)"
  return JSONResponse(content=img, status_code=200)
  ```
  
Next, I tried:
```
  img = "![<description>](data:image/svg+xml;base64,<data>)"
  return JSONResponse(content=img, status_code=200)
 ```
 
It was still working when I rebooted my server. 

I could see in the call history that ChatGPT was fetching this new type of response, so I knew it acknowledged my chamge.

Next, I tried:


```
  return JSONResponse(content="", status_code=200)
```
 
Still worked. 🥴

I started cleaning up code, made a nice Github repo, uninstalled the plugin, and reinstalled the updated one.

No longer works. Huh?

It started returning the following:

```
I apologize for the inconvenience. It seems there was an issue with generating the image. Here is an ASCII art representation of a yellow star:

     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
```

This caused a small panic, because I did various small changes, and never pushed out a stable version.

Finally figured out that my original was the best one, but that a clean re-install was needed.

```
  img = "![Yellow Circle](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCI+PHRpdGxlPlllbGxvdyBDaXJjbGU8L3RpdGxlPjxjaXJjbGUgY3g9IjUwIiBjeT0iNTAiIHI9IjUwIiBmaWxsPSJ5ZWxsb3ciIC8+PC9zdmc+)"
  return JSONResponse(content=img, status_code=200)
  ```
  
Conclusion (?): never trust relaunching your server. If you want to know whether the behavior stays the same, reinstall your plugin. It seems that the plugin remembered my initial response.


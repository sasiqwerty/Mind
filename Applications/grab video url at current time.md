---
aliases: 
tags: 
date created: Sunday, August 6th 2023, 4:34:48 pm
date modified: Sunday, August 6th 2023, 4:48:22 pm
---
#learn https://developers.google.com/youtube/v3/docs/

## 1. Get the Video URL of the Current Video You Are Watching

``` js
const url = window.location.href;
console.log(url); // https://www.example.com/
```

## 2. Calculate the Current time in the Video that is Played

```js
const player = new YT.Player('player', {
  videoId: 'Fk2bUvrv-Uc',
});
const currentTime = player.getCurrentTime();
console.log(currentTime); // 100
```

> **Using the YouTube API.** The YouTube API allows you to get information about YouTube videos, including the current time. You can use the API to get the current time of a video by calling the `getCurrentTime()` method on a `YouTubePlayer` object.  


> **Using JavaScript.** You can use JavaScript to get the current time of a YouTube video by calling the `currentTime()` method on a `YouTubeIFramePlayer` object.

## Append it to the URL of the Video

## Copy the Generated URL to the Clipboard

**Using the `Clipboard API`.** The `Clipboard API` is a newer API that was introduced in HTML5. The `Clipboard API` provides a more consistent and secure way to copy data to the clipboard. To copy text to the clipboard using the `Clipboard API`, you would use the `writeText()` method. For example, the following code would copy the text "Hello, world!" to the clipboard:

```js
const text = "Hello, world!";
navigator.clipboard.writeText(text);
```

## Send a Small Notification that the Clipboard Has Your URL Ready for Sharing
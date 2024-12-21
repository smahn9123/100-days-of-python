# Day 43

Lessons: <br>

Everything in web page is just a whole bunch of boxes. <br>
The properties of these boxes can be affected by changing the CSS code. <br>
The <body> has some default values that prevents our changing the height.<br>
<br>
There is hierarchy among three different ways of implementing CSS:<br>
Inline CSS -> Internal CSS -> External CSS (Higher to lower order)<br>
You can apply a global CSS rule to all of your web pages,<br>
but on the individual web pages, you can apply more specific rules through using internal or inline CSS<br>
as more or less one off changes for that specific page or that specific element on that page.<br>
Now in terms of best practice as a web designer it's usually suggested that you implement all of your styles inside your external CSS.<br>
So by using the class as the selector you can better differentiate and and make more specific styling choices for your web site elements.<br>
So use classes when you want to apply the same style to a group of related items and use the id to apply a specific style to a single element on your web page.<br>
Some of tags have predefined CSS styles that are applied by the browsers. For example the h1, if we have a look inside our Chrome Developer Tools and I select the h1 then you can see that these user agent stylesheets, this comes from the browser and this is applied no matter what CSS style you put down. But if you do specify something using a tag selector inside your css file, for example here for the h1 I said that the font size should be 200 pixels and that overrides the default size for the browser and it can be further overridden using ids or classes. <br>

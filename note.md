Background
==========

This library creates substitutes, i.e., objects that can stand in for other
objects. Such objects are often called "mocks" or "stubs", but I find these
terms destructive, in that I have worked with people who had problems
understanding test driven development because these terms got in the way.

Back then, I was working with Dermot Kilroy, who just for fun, wrote a mocking
framework to solve this problem - he called it [NPretend](https://bitbucket.org/dkil1972/npretend)
(we were working with  C# back then).

Inspired by the simplicity of the NPretend API, I had developed a library named
"Substitute" but it grew too complicated (I got carried away).
So I rewrote the whole thing in a much simpler way. To prevent the naming
conflict, I renamed the new library to "kazookid".

I imagine that given you know the Kazookid video, where the kid says
"I like to sing, dance, pretend..." then you could imagine that the kazookid
framework creates objects that pretend to other objects
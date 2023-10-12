---
aliases: 
tags: 
date created: Wednesday, August 16th 2023, 2:19:25 pm
date modified: Monday, August 21st 2023, 12:27:01 pm
---

#ai #prompt

## Proooompt First

This is the an example for a mindmap, this is the structure you have to follow but ignore the words in it. The words will be given in later prompt.  
The first line starts with the word mindmap  
The second line should always contain the word root and the heading following the word as illustrated in the example  
the indentation of the line tells us about level of the heading and its content.  
Icons can be used where needed

mindmap  
  root((mindmap))  
    Origins  
      Long history  
      ::icon(fa fa-book)  
      Popularisation  
        British popular psychology author Tony Buzan  
    Research  
      On effectiveness and features  
      On Automatic creation  
        Uses  
            Creative techniques  
            Strategic planning  
            Argument mapping  
    Tools  
      Pen and paper  
      Mermaid

extra Syntax

[text inside] - using a square brackets around the text creates a rectangle around the text in the mind map, so only use square brackets when needed to create rectangles

(text inside) - using parenthesis around the text creates a rounded rectangle around the text in the mind map, so only use parenthesis when needed to create rounded rectangles.

((text inside)) - using double parenthesis around the text creates circle around the text in the mind map, so only use double parenthesis when needed to create circles.

Using this syntax in the text will only show the text in the above mentioned symbols, when using this syntax all the text should be wrapped with the above symbols properly

IT IS IMPORTANT TO NOTE THAT ONE SHAPE CANNOT BE NESTED IN ANOTHER


After processing ask the user for the content, once the user gives the content generate the text in the above-mentioned fashion.  
This is how we create a mind Map in mermaid.

---
aliases: 
tags: 
date created: Saturday, August 19th 2023, 2:11:00 pm
date modified: Saturday, August 19th 2023, 2:15:25 pm
---
<iframe src="https://dev.to/iggredible/the-only-vim-insert-mode-cheatsheet-you-ever-needed-nk9" allow="fullscreen" allowfullscreen="" style="height:100%;width:100%; aspect-ratio: 16 / 9; "></iframe>

Vim has several modes, and one of the most commonly used is the Insert mode. Here are some ways to enter and exit this mode, as well as some useful commands:

## Entering Insert Mode

- `i`: Insert text before the cursor.
- `I`: Insert text before the first non-blank character of the line.
- `a`: Append text after the cursor.
- `A`: Append text at the end of the line.
- `o`: Starts a new line below the cursor and insert text.
- `O`: Starts a new line above the cursor and insert text.
- `gi`: Insert text in the same position where last insert mode was stopped in the current buffer.
- `gI`: Insert text at the start of line (column 1).

## Exiting Insert Mode

- `<esc>`: Exits insert mode and go to normal mode.
- `Ctrl-[`: Exits insert mode and go to normal mode.
- `Ctrl-c`: Like Ctrl-[ and <esc>, but doesn’t check for abbreviation.

## Repeating Insert Mode

You can give a count before you enter insert mode. For example: `10i` Then if you type “hello world!” and exit insert mode, it will repeat the text “hello world!” 10 times. This works with any methods you use to enter insert mode (`10I`, `11a`, `12o`).

## Deleting Chunks in Insert Mode

There are different ways to delete while in insert mode besides `<backspace>`:

- `Ctrl-h`: Delete one character.
- `Ctrl-w`: Delete one word.
- `Ctrl-u`: Delete entire line.

## Inserting from Register

Vim can insert contents from any register with Ctrl-r plus register symbol. You can use any alphabetical character a-z for named register. To use it, if you want to yank a word to register a, you can do: `"ayiw` To insert content from register a: `Ctrl-r a` Vim also has 10 numbered registers (0-9) to save the most recent 10 yanks/deletes. To insert content from numbered register 1: `Ctrl-r 1` In addition to named and numbered registers, here are another useful register tricks:

- `Ctrl-r "`: Insert the last yank/delete.
- `Ctrl-r %`: Insert file name.
- `Ctrl-r /`: Insert last search term.
- `Ctrl-r :`: Insert last command line.

Vim has an expression register, =, to evaluate expressions. You can evaluate mathematical expressions 1 + 1 with: Ctrl-r =1+1 You can use expression register to get the value of your vim settings. You can do this with setting name prepended with &.
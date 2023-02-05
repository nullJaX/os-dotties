# os-dotties

*Text art collection of OS/Distributions' logos in Braille charset format (Unicode)*

## :information_source: About this repository

This repository contains a collection of OS/Distribution's logos saved as Braille texts (similar to ASCII/ANSI art). You can see [the preview of all logos here](https://nulljax.github.io/os-dotties/index.html) (up-to-date with `master` branch, some lines may not display properly - I could not find the correct font).

These files may serve as a nice addition to your favourite terminal information fetcher. Each directory stores files for specific OS/distribution, files with:

- `*.mono` suffix store raw text (no color)
- `*.color` suffix store the same text with an addition of ANSI escape color codes, to provide colorful logo.

**ANSI escape color codes for reference:**
|Color|Black|Red|Green|Yellow|Blue|Magenta|Cyan|White|Reset|
|-|-|-|-|-|-|-|-|-|-|
|Code|`^[[30m`|`^[[31m `|`^[[32m`|`^[[33m`|`^[[34m`|`^[[35m`|`^[[36m`|`^[[37m`|`^[[0m`|

## :computer: How to use it

A. If your terminal information fetcher supports customization over the displayed logo, just download or copy and paste the contents of the file/logo you like and adjust your fetcher's specific configuration.

B. If you wish to just display the file in the terminal, you can download the specific file and run following command: 

`cat <path_to_the_downloaded_file>`

C. Alternatively, you can:
1. Clone this repository: `git clone https://github.com/nullJaX/os-dotties.git`
2. Display contents of the specific file: `cat os-dotties/<chosen_distribution>/<chosen_logo_file>`

## :memo: Licensed under [ISC license](LICENSE)
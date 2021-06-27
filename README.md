# Gesko

Simple and minimal Jekyll blog. 
Forked from [Asko](https://github.com/manuelmazzuola/asko).
Inspired from [Klisé](https://github.com/piharpi/jekyll-klise)
## Screenshot

## Installation

Run local server:

```bash
$ git clone https://github.com/P0WEX/Gesko.git
$ cd Gesko
$ bundle install
$ bundle exec jekyll build
$ bundle exec jekyll serve
```

To create new tag, create a folder in `tag/` with the name of the new one. In this folder add an `index.html` file and just add this header:
```
---
layout: tag
tag: yourNewTag
---
```
Then build again and you're ready!!

## Contributing

Yeaaa feel free to open a pull request.


If you see any typos or formatting errors in a post, or want to helping reduce backlogs or any other issue that needs to be addressed, please do not hesitate to open a pull request and fix it!, please read [contributing](./CONTRIBUTING.md) before PR.

## License

This project is open source and available under the [MIT License](LICENSE.md).

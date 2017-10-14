# TensorGlow

[![Build Status](https://travis-ci.org/boennemann/badges.svg?branch=master)](https://github.com/maxwhoppa/tensorglow)


[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)


> "I don't even understand it. I must be dumb." - Johann Miller

**TensorGlow** is an open source software library for numerical noncomputation using data flow graphs. The graph nodes are nonexistent, while the graph edges represent the multidimensional glowing data arrays (tensors) that flow between them. This flexible architecture lets you deploy noncomputation to your terminal without writing code, in a glowing fashion. TensorGlow also includes this README.


## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
	- [Generator](#generator)
- [Badge](#badge)
- [Example Readmes](#example-readmes)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)
- [Contribute](#contribute)
- [License](#license)

## Background

TensorGlow started with an issue originally posed by [@JohannMiller](https://github.com/johannkm), about how TensorFlow's static graph nature prevented me from being able to debug projects properly. Additionally, while working on my personal machine-learning projects, I realized I needed a way to standardize the viewing of Tensors in a way that would (1) fit 3D tensors on my small 2D screen, and (2) look flashy enough to keep me awake and to secure funding from VCs. And thus, TensorGlow was born.

> I don't wear base, as I don't like to cover up my freckles, but I couldn't live without YSL Touche Eclat for hiding my under-eye circles. I love the smoky-eye look, so I use Dior's 5-Colour Eyeshadow in Night Dust and lashings of mascara.

> I finish with a dash of bronzer for a healthy **glow**.

~ [Eva Green](https://www.brainyquote.com/quotes/quotes/e/evagreen596775.html?src=t_glow)

Understanding deep-learning is too hard, and so we need a way to gain some geometric intuition about the data that is flowing through our machines in order to even begin to try to approach the problem of starting to initially comprehend or even touch the surface of how neural networks work.

We hope that TensorGlow will meet the needs of machine-learning researchers and labs throughout the world, and will become a household name for machine-learning visualization.

## Install

This project doesn't use [node](http://nodejs.org) or [npm](https://npmjs.com). Go check them out if you don't have them locally installed. You can type in the following but it won't do anything. Just pretend I guess?

```sh
$ npm install --global tensorglow
```

## Usage

This is only a documentation package. You can print out [spec.md](spec.md) to your console:

```sh
$ python3 app.py
Enter dimensions for m x n x p tensor: 3 4 2
7 0 1 5
5 9 4 9
4 9 4 7

matrix: 2

# Prints out the glowing matrix (note it's B&W in this)
```


## Related Efforts

- [Goex Search](https://github.com/johannkm/goex-search) - 💌 A machine-learning rude restaurant search.
- [iMessage Clone](https://github.com/johannkm/imessage-clone) - An iMessage lookalike for Apple fanboys

## Maintainers

[@MaxNewman](https://github.com/maxwhoppa).
[@KevinChen](https://github.com/kevchn).

## Contribute

Feel free to dive in! [Open an issue](https://github.com/Maxwhoppa/tensorglow-readme/issues/new) or submit PRs.

Standard Readme follows the [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) Code of Conduct.

## License

[MIT](LICENSE) © Max Newman and Kevin Chen

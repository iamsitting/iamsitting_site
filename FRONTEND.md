# Frontend
These are instructions for setting up webpack on django on production mode. There is a way for setting up webpack on development mode using hot-reload. It's setup in the GitHub project, although not documented.


## NPM Setup

Install NPM, Node dependencies. NPM is super usefule to manage js and css libraries.
``` 
sudo apt-get install build-essential curl git m4 ruby texinfo libbz2-dev libcurl4-openssl-dev libexpat-dev libncurses-dev zlib1g-dev
```

Intialize NPM and install Webpack
```
cd ~/path/to/workspace #this is one level above project root
npm init #this creates the node_modules dir and the package.json file
npm install webpack webpack-bundle-tracker css-loader mini-css-extract-plugin file-loader node-sass sass-loader style-loader webpack-merge jquery # install modules
```
Use npm install [package] to install other tempalate dependencies, font-awesome, bootstrap, etc. (see package.json)

## Webpack 4 Setup

Create webpack config files and index.js
```
mkdir webpack
touch webpack/webpack.base.config.js
touch webpack/webpack.production.config.js
mkdir project_root/templates/js
touch project_root/templates/js/index.js
```

Setup base webpack config files (this is only an overivew). This basically maps where all the critical files are located.
```
//webpack.base.config.js
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker') //this is the output that django uses

module.exports = {
  context: __dirname,

  entry: {
    main: [ //name of bundled js file
      'path/to/index', // entry point of our app.
    ], //you can add multiple entries
  },

  output: {
    path: path.resolve('path/to/static/bundles/'),
    filename: "[name].js", // will take the name of entry if left as [name]
  },

  module: {
    rules: [...]  // setup rules for transpiling differnt file types.
  }

  plugins: [
    new BundleTracker({filename: './webpack/webpack-stats.json'}), //output of blude tracker
  ],

  resolve: {
    modules: [ //import statements will look at these two directories
      'node_modules',
      path.resolve(__dirname, '../frontend'),
    ],
  }
}
```


Setup production webpack config files (this is only an overivew). This basically tells webpack how to process all the static files.

```
//webpack.production.config.js
var MiniCssExtractPlugin = require("mini-css-extract-plugin") // generates css files
var merge = require("webpack-merge") //merges config files

var baseConfig = require("./webpack.base.config")

var prodConfig = {
  mode: 'production',
  module: {
    rules: [ //use these rules to process scss files
      {
        test: /\.(sa|sc|c)ss$/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          "sass-loader"
        ]
      },
    ]  // -rules
  },  // -module

  plugins: [
    new webpack.LoaderOptionsPlugin({
      minimize: true,
      debug: false
    }),
    new MiniCssExtractPlugin({
      filename: '[name].css'
    })
  ]  // -plugins
}

module.exports = merge.smart(prodConfig, baseConfig)
```

##Django Webpack Loader

Install django-webpack-loader
```
pip install django-webpack-loader # remember to use virtualenv
```

Update the settings file
```
# settings.py

APPS = [
    'webpack_loader'
]

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": 'bundles/',
        "STATS_FILE": os.path.join(BASE_DIR, '../webpack/webpack-stats.json'), # tied to BundleTracker in webpack config file
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static") # project_root/static/bundles/main.js... this is the goal... to have access to main.js, etc.
```


## Where do I code?

Create a frontend workspace
```
mkdir frontend
mkdir frontend/base_theme
mkdir frontend/base_theme/sass
mkdir frontend/base_theme/js
touch frontend/base_theme/sass/main.scss
touch frontend/base_theme/js/dothis.js
```

### First, SCSS
Your scss code can be written as described in http://thesassway.com/beginner/how-to-structure-a-sass-project. Your main.scss will be imported in the entry js file.
```
// sass/main.scss
@import 'components/_file'; // import custom scss files
@import "~font-awesome/css/font-awesome.min.css"; //import node module css files

// scss code
```

### Second, Javascript
Like SCSS, you can write your JS in the frontend workspace or in the django modules depending on the scope of your function.

```
// js/dothis.js

//import from node_modules
import 'jquery.scrolly/jquery.scrolly'
import 'jquery.scrollex/jquery.scrollex'
import skel from 'skel-framework-npm/src/skel'

//js code
```


### Third, JS Entry Point
Webpack will not look at any of the code you wrote until it's imported into one of the entry js files you defined in the config file.

```
//templates/js/index.js

import 'base_theme/sass/main.scss' //scss
import 'base_theme/js/dothis' //js

//very little js code, this should mostly be just imports

```


## Project Structure
Here what it should look like (sort of).
```
+-- project_root
|   +-- another_app
|   +-- manage.py
|   +-- project_app
|       +-- settings.py
|   +-- static
|      +-- bundles
|         +-- main.js, main.css, etc. # we want this.
|   +-- templates
|         +-- index.js (imports frontend/base_theme/js/script.js, etc.)
+-- frontend
|   +-- base_theme
|       +-- sass
|          +-- main.scss, components, etc.
|       +-- js
|          +-- dothis.js, dothat.js, etc.
|       +-- images
+-- package.json
+-- webpack
|   +-- webpack-stats.json
|   +-- webpack.base.config.js
|   +-- webpack.production.config.js
+-- node_modules
|   +-- modules
```

## Bundles
Now how do we generate and access bundles? First let's go to package.json. Let's create the 'npm run build' command.

```
//package.json
"scripts": {
    "build": "webpack --config webpack/webpack.production.config.js --progress --colors",
    "test-build": "webpack --config webpack/webpack.base.config.js --progress --colors",
},

```

By running npm run build this will generate js (and css thanks to ExtractTextPlugin) under the static/bundles directory.

Now let's go to the Django template files.

```
{# templates/base.html #}

{% load render_bundle from webpack_loader %}
{% load static %}
<!DOCTYPE HTML>
<html>
    <head>
        {% render_bundle 'main' 'css' %}
        {% render_bundle 'main' 'js' %}
    </head>
</html>
```

That's it.
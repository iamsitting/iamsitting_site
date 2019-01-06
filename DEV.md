# Development
These are instructions for setting up a development environemnt for webpack and django.

## Webpack Setup

Create webpack config files and index.js

```
cd webpack
touch webpack/webpack.development.config.js
```

Setup base webpack config files (this is only an overivew). This basically maps where all the critical files are located.
```
//webpack.development.config.js
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker') //this is the output that django uses
var MiniCssExtractPlugin = require("mini-css-extract-plugin");
var baseConfig = require('./webpack.base.config')

module.exports = {
  mode: 'development',
  context: __dirname,

  entry: {
    main: [
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
    ], //you can add multiple entries
  },

  output: {
    publicPath: 'http://localhost:3000/iamsitting_site/static/bundles/'
  },

  module: {
    rules: [
      {
        test:  /\.(sa|sc|c)ss$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader'
        ]
      },
    ]  //-rules
  }, //-module

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
    new webpack.NamedModulesPlugin(),
    new MiniCssExtractPlugin({
      filename: '[name].css'
    })
],
}
```


## Node

Edit the package.json file
```
//package.json
"scripts": {
   ...,
   "dev": "node webpack/server.js"
}
```

Install NVM and node
```
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
```

Restart the terminal and verify that nvm was installed
```
nvm --version
nvm use --lts
cd webpack
touch server.js
```

```
// server.js
var webpack = require('webpack')
var WebpackDevServer = require('webpack-dev-server')
var devConfig = require('./webpack.development.config')

new WebpackDevServer(webpack(devConfig), {
  publicPath: devConfig.output.pubblicPath,
  hot: true,
  inline: true,
  historyApiFallback: true,
  headers: {
    'Access-Control-Allow-Origin': '*'
  }
}).listen(3000, '0.0.0.0', function (err, result){
  if (err) {
    console.log(err)
  }

  console.log('Listening at 0.0.0.0:3000')
})
```

Update the settings file. It's better to create a seperate file
```
# settings.development.py
DEBUG = True

APPS = [
    'webpack_loader'
]

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": 'bundles/',
        "STATS_FILE": os.path.join(BASE_DIR, '../../webpack/webpack-stats.json'), # tied to BundleTracker in webpack config file
    }
}

STATIC_ROOT = ''

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```

It should be good to go. If you create a seperate file make sure to:
```
export DJANGO_SETTINGS_MODULE=iamsitting_site.settings.development
```

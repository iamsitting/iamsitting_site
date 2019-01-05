var path = require("path")
var webpack = require('webpack')
var BundleTracker  = require('webpack-bundle-tracker')
var merge = require('webpack-merge')

var baseConfig = require('./webpack.base.config')

var devConfig = {
  mode: 'development',
  entry: {
    main: [
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
    ],
    blog_post: [
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
    ]
  },  //-entry

  output: {
    publicPath: 'http://localhost:3000/iamsitting_site/static/bundles/',
  },  //-output

  devtool: 'cheap-module-eval-source-map',

  module: {
    rules: [
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader?sourceMap'
      },
      {
        test: /\.scss$/,
        use: [
          {
            loader: 'style-loader',
          }, {
            loader: 'css-loader',
            options: {
              sourceMap: true
            }
          }, {
            loader: 'sass-loader',
            options: {
              sourceMap: true
            }
          }
        ]  //-use
      },
      {
        test: /\.tsx?$/,
        loader: 'ts-loader'
      }
    ]  //-rules
  },  //-module

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
    new webpack.NamedModulesPlugin(),
  ],
}

module.exports = merge.smart(devConfig, baseConfig)

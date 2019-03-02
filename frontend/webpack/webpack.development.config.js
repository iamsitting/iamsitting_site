var path = require("path")
var webpack = require('webpack')
var BundleTracker  = require('webpack-bundle-tracker')
var merge = require('webpack-merge')
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

var baseConfig = require('./webpack.base.config')

var devConfig = {
  mode: 'development',
  entry: {
    main: [
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
    ],
    blog: [
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
    ]
  },  //-entry

  output: {
    publicPath: 'http://localhost:3000/iamsitting_site/static/bundles/',
  },  //-output

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
  },  //-module

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
    new webpack.NamedModulesPlugin(),
    new MiniCssExtractPlugin({
      filename: '[name].css'
    })
  ],
}
module.exports = merge.smart(devConfig, baseConfig)

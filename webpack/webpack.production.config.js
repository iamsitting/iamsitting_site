var path = require("path")
var webpack = require("webpack")
var BundleTracker = require("webpack-bundle-tracker")
var MiniCssExtractPlugin = require("mini-css-extract-plugin")
var merge = require("webpack-merge")
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')

var baseConfig = require("./webpack.base.config")

var prodConfig = {
  mode: 'production',
  module: {
    rules: [
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

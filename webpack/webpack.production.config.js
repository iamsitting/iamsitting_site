var path = require("path")
var webpack = require("webpack")
var BundleTracker = require("webpack-bundle-tracker")
var ExtractTextPlugin = require("extract-text-webpack-plugin")
var merge = require("webpack-merge")

var baseConfig = require("./webpack.base.config")

var prodConfig = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ExtractTextPlugin.extract('css-loader'),
      },
      {
        test: /\.scss$/,
        use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: [
            { loader: 'css-loader', options: { sourceMap: true } },
            { loader: 'resolve-url-loader', options: { sourceMap: true } },
            { loader: 'sass-loader', options: { sourceMap: true } }
          ] // -use
        })  // -use
      }
    ]  // -rules
  },  // -module

  plugins: [
    new webpack.LoaderOptionsPlugin({
      minimize: true,
      debug: false
    }),
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('production')
    }),
    new webpack.optimize.UglifyJsPlugin({
      beautify: false,
      mangle: {
        screw_ie8: true,
        keep_fnames: true
      },
      compress: {
        screw_ie8: true
      },
      output: {
        "ascii_only": true
      },
      comments: false
    }),
    new ExtractTextPlugin({
      filename: '[name].css'
    })
  ]  // -plugins
}

module.exports = merge.smart(prodConfig, baseConfig)
